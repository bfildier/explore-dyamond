import numpy as np

class ColdPool:

    def __init__(
        self,
        label:str,
        coord:np.array,
    ):
    """Class contructor."""

        self.label = label
        self.coord = coord
        self.first_cp_neighbor = None
        self.last_cp_neighbor = None
        self.previous_cp_neighbor = None
        self.next_cp_neighbor = None

    #-- Methods --#

    def 