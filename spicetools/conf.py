# -*- coding: utf-8 -*-
"""
Copyright (C) 2014 Michael Davidsaver
License is GPL3+, see file LICENSE for details
"""

import logging
_log = logging.getLogger(__name__)

import os

_dft_conf = {
    'editor':'kwrite',
    'editor.cmd':'%(editor)s %%(file)s',
    'gschem':'gschem',
    'gschem.cmd':'%(gschem)s %%(file)s',
    'gnetlist':'gnetlist',
    'gnetlist.cmd':"%(gnetlist)s -g spice-sdb -O include_mode -O nomunge_mode -o %%(net)s %%(sch)s",
    'spice':'ngspice',
    'spice.cmd':'%(spice)s --no-spiceinit --pipe %%(deck)s',
}

def loadConfig(FP=None, section='DEFAULT'):
    from ConfigParser import SafeConfigParser as ConfigParser
    P = ConfigParser(defaults=_dft_conf)
    P.add_section('spicerun')
    P.add_section('simbench')
    P.read([
        '/etc/spicerun.conf',
        os.path.expanduser('~/.config/spicetools/spicetools.conf'),
        'spicerun.conf'
    ])
    if FP:
        P.readfp(FP)

    return dict([(K,P.get(section,K)) for K in _dft_conf.iterkeys()])
