import numpy as np
import pandas as pd

class Universe(object):
    """Define the universe that this instance operates within.
    This includes the preference space and the choice list.
    """

    def __init__(self, prefSpace=None, choices=None):
        if prefSpace:
            self.prefSpace = prefSpace
        else:
            self.prefSpace = PrefSpace()
        if choices:
            self.choices = choices
        else:
            self.choices = []


class Dem(object):

    def __init__(self, name=None, N=0, vote=None, B=None, universe=None):
        """A dem is the fundamental demographic unit in this model, not individuals!
        N is the number of individuals in this dem
        B is this dem's k-dimensional preference vector (object)
        """
        self.name = name
        self.N = N
        self.vote = vote
        self.B = B
        self.universe = universe

    @property
    def B(self):
        return self._B
    
    @B.setter
    def B(self, B):
        self._B = B

    @property
    def N(self):
        return self._N

    @N.setter
    def N(self, N):
        self._N = max(0, N)


class PrefSpace(object):
    """a PrefSpace is the definition of the k-dimensional preference space.
    Individual PrefVectors live within the space.
    """

    def __init__(self, prefList=None, descList=None, k=None):
        self.prefList = prefList
        self.descList = descList
        # wondering if maybe the prefs and descs should be a dict? to keep them together?
        if k is not None:
            self.kinit(k)

    @property
    def k(self):
        return len(self.prefList)
    
    def kinit(self, k=1):
        """fill out a nominal list of preferences of length k
        """
        self.prefList = []
        self.descList = []
        for i in range(k):
            prefList.append('Issue %d' % i)
            descList.append('Issue %d description placeholder' % i)



class PrefVector(np.ndarray):
    """Subclassing ndarray as per example in
    https://numpy.org/doc/stable/user/basics.subclassing.html
    """

    def __new__(cls, vector=None, prefspace=None, universe=None):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        if vector is not None:
            obj = np.asarray(vector).view(cls)
        else:
        # add the new attribute to the created instance
        obj.universe = universe
        if obj.universe is not None:
            obj.prefSpace = obj.universe.prefSpace
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        if obj is None: return
        self.universe = getattr(obj, 'universe', None)
        
