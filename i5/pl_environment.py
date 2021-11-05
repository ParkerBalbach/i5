#!/usr/bin/env python
""" generated source for module Environment """
#  (C) 2013 Jim Buffenbarger
#  All rights reserved.
from pl_evalexception import EvalException

class Environment(object):
    """ generated source for class Environment """

    def __init__(self):
        """ generated source for method __init__ """
        self.map = {}
        self.funcMap = {}


    def put(self, var, val):
        """ generated source for method put """
        self.map[var] = val
        return val

    def get(self, pos, var):
        """ generated source for method get """
        if var in self.map:
            return self.map[var]
        raise EvalException(pos, "undefined variable: " + var)

    def putF(self, _id, val):

        self.funcMap[_id] = val
        return val

    def getF(self, pos, _id):
        if _id in self.funcMap:
            return self.funcMap[_id]
        raise EvalException(pos, "undefined variable: " + _id)


    def copy(self):
        copyEnv = Environment()
        copyEnv.map = dict(self.map)
        copyEnv.funcMap = dict(self.funcMap)
        return copyEnv
