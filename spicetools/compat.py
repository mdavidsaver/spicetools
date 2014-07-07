# -*- coding: utf-8 -*-
"""
.sprj compatibility
"""

__all__ = ['updateDict']

def _updateVars(D):
        before = []
        for V in D.pop('alters',[]):
            before.append("alter %s %s"%(V['name'], V['expr']))
        D['before'] = '\n'.join(before)
        # combine vars into after
        after = []
        for V in D.pop('vars',[]):
            after.append("let %s = %s"%(V['name'], V['expr']))
        D['after'] = '\n'.join(after)

def updateDict(D):
    if D['version']==1:
        # combine alters into before
        _updateVars(D)

        for S in D.get('sims',[]):
            _updateVars(S)

        D['version'] = 2

    return D
