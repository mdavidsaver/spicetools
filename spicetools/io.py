# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
_log = logging.getLogger(__name__)

import os.path, weakref

import numpy
import h5py

from . import raw2hdf

__all__ = [
    'loadspice',
    'readhdf5',
]

# Operations on numpy vectors (ndarray.dtype.kind)
_dataops = {
    'i':{
        'no-op':lambda x:x,
    },
    'u':{
        'no-op':lambda x:x,
    },
    'f':{
        'no-op':lambda x:x,
    },
    'c':{
        'amplitude':numpy.abs,
        'phase':lambda z:numpy.angle(z, deg=1),
        'real':numpy.real,
        'imag':numpy.imag,
    }
}

class File(dict):
    def __init__(self, name, vdict):
        super(File, self).__init__(vdict)
        self.name = name

class VectorSet(dict):
    def __init__(self, data, labels, adict):
        self.ops = _dataops[data.dtype.kind]
        self.data, self.labels, self.attrs = data, labels, adict
        self.tmap = dict([(N,i) for i,N in enumerate(labels)])
        super(VectorSet, self).__init__([(N,data[:,i]) for N,i in self.tmap.iteritems()])

        if len(data.shape)!=2 or data.shape[0]==0 or data.shape[1]==0:
            raise ValueError('Data shape not supported %s'%data.shape)
        elif len(labels)!=data.shape[1]:
            raise ValueError('length of variables list (%d) does not '%len(labels)
                             +'match number of data columns (%d)'%data.shape[1])

    def value(self, col, op):
        op = self.ops[op]
        return op(self[col])

def loadspice(fname):
    """Read a spice raw file or HDF5
    
    Input is a string describing a spice raw or HDF5 file.
    """
    if fname.find(':')!=-1 and not os.path.isfile(fname):
        # an HDF5 file with group specifier
        fname, _, grp = fname.partition(':')
        F = h5py.File(fname)
        return readhdf5(F.require_group(grp))

    # magic detection of HDF5
    with open(fname,'rb') as F:
        fid = F.read(4)
        if fid!='\x89HDF':
            F.seek(0)
            return readspice(F)

    return readhdf5(fname)

def _autoclose(F):
    F().close()

def readhdf5(fname):
    """Process an HDF5 file and return a vectorset File
    
    Input is either a string naming an HDF5 w/ optional group
    (eg. "file.h5:/grp"), or an already opened Group object.
    """
    _log.debug("Reading: %s", fname)
    if isinstance(fname, h5py.Group):
        F = fname
    else:
        fname, _, grp = fname.partition(':')
        F = h5py.File(fname,'r')
        if grp:
            F = F.require_group(grp)

    grps=[]
    def collect(name, obj, grps=grps):
        if not isinstance(obj, h5py.Group):
            return
        _log.debug("Visit group %s (%s)", obj, obj.attrs)
        if obj.attrs.get('formatid')=='spice2hdf-1.0':
            grps.append(obj)
    F.visititems(collect)

    if len(grps)==0:
        raise ValueError('No data found in "%s"'%fname)

    vectors = {}
    for grp in grps:
        V = VectorSet(grp['data'], grp.attrs['columns'],
                      dict(grp.attrs))
        vectors[grp.name] = V

    R = File(F.file.filename, vectors)
    R._autoclose = weakref.ref(F.file, _autoclose)
    return R

def readspice(fname):
    """Process an spice raw file and return a vectorset File

    Input is either a string naming an file, or an
    already opened file object.
    """
    if hasattr(fname, 'read'):
        data, header = raw2hdf.loadspice(fname)
    else:
        with open(fname, 'rb') as F:
            data, header = raw2hdf.loadspice(F)
    labels = [V[0] for V in header['variables']]

    V = VectorSet(data, labels, header)
    return File(fname, {'default':V})
