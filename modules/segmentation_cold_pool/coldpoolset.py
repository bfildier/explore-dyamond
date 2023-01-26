import coldpool
import numpy as np

class ColdPoolSet:

    def __init__(self,
            mask:np.array):

        self.mask = mask
        ind_mask = np.where(mask == -1)
        self.i_mask = ind_mask[0]
        self.j_mask = ind_mask[1]

        ## Go through all points detected and create a ColdPool object with separate label

    ##-- Methods --##

    def shiftMask(self,
        i_values:[],
        j_values:[],
        direction:str):
        """Shift mask in directions horizontal, vertical, diagonal1 and diagonal2."""

        ## Define transformations, return two new lists of indices of shifted points

    def intersectMasks(self,
        direction:str):
        """Intersect mask with its image shifted in directions horizontal, vertical, diagonal1 and diagonal2."""

    