# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import numpy
import h5py

import spice2hdf

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
    with open(fname,'rb') as F:
        fid = F.read(4)
    if fid=='\x89HDF':
        return readhdf5(fname)
    else:
        return readspice(fname)

def readhdf5(fname):
    F = h5py.File(fname,'r')
    grps=[]
    def collect(name, obj, grps=grps):
        if not isinstance(obj, h5py.Group):
            return
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

    return File(fname, vectors)

def readspice(fname):
    with open(fname, 'rb') as F:
        data, header = spice2hdf.loadspice(F)
    labels = [V[0] for V in header['variables']]

    V = VectorSet(data, labels, header)
    return File(fname, {'default':V})
