#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "levelSetEquation.py"
 #                                    created: 11/12/03 {10:39:23 AM} 
 #                                last update: 4/2/04 {4:02:15 PM} 
 #  Author: Jonathan Guyer
 #  E-mail: guyer@nist.gov
 #  Author: Daniel Wheeler
 #  E-mail: daniel.wheeler@nist.gov
 #    mail: NIST
 #     www: http://ctcms.nist.gov
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  PFM is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2003-11-12 JEG 1.0 original
 # ###################################################################
 ##

import Numeric
import MA
from fipy.meshes.numMesh.mesh import MAtake
from fipy.equations.equation import Equation

class LevelSetEquation(Equation):
    """
    Level set equation is implicit.
    """    
    def __init__(self, var):
        
        self.mesh = var.getMesh()
	
	Equation.__init__(
            self,
            var = var,
            terms = (),
            solver = None)

    def solve(self):
        ## Return an array for each cell where each entry has an array
        ## over the neigbouring cells. The entry is 1 where the nieghbour
        ## has the opposite sign.
        self.zeroNeighbours = self.getZeroNeighbors()
        ## Return an array over cells where each entry is the number of
        ## adjacent cells with opposite sign.
        self.numberOfZeroNeighbors = self.getNumberOfZeroNeighbors()
        ## Return an array of the index of the cells with adjacent cell
        ## values of opposite sign.
        self.zeroCellIDs = self.getZeroCellIDs()
        ## Evaluate the initial bounding cell values.
        self.zeroValues = self.getZeroValues()
        ## Find the IDs of cells next to the zero values
        self.trialInitialCellIDs = self.getInitialTrialCellIDs()
        

    def getZeroNeighbors(self):
        values = self.var.getNumericValue()
        tmp = MAtake(values, self.mesh.getCellToCellIDs())* values[:,Numeric.NewAxis]
        return MA.where(tmp < 0, Numeric.ones(tmp.shape), Numeric.zeros(tmp.shape))

    def getNumberOfZeroNeighbors(self):
        return MA.sum(self.zeroNeighbours, 1)

    def getZeroCellIDs(self):
        return Numeric.nonzero(self.numberOfZeroNeighbors)

    def getZeroValues(self):
        self.varOld = self.var.copy()
        values = self.varOld.getNumericValue()
        cellToCellDistances = MAtake(self.mesh.getCellDistances(), self.mesh.getCellFaceIDs())
        adjacentValues = MAtake(values, self.mesh.getCellToCellIDs())
        d = MA.absolute(values[:,Numeric.NewAxis] * self.zeroNeighbours * cellToCellDistances / (values[:,Numeric.NewAxis] - adjacentValues))
        d = MA.sort(d, axis = 1)[:,0]
        sign = values / MA.absolute(values)
        return MA.where(d.mask(), values, sign * d)
        
    def getInitialTrialCellIDs(self):
        zeroCellToCellIDs = MA.take(self.mesh.getCellToCellIDs(), self.zeroCellIDs)
        trialAndZeroCellFlag = Numeric.zeros(self.mesh.getNumberOfCells())
        Numeric.put(trialAndZeroCellFlag, zeroCellToCellIDs, Numeric.ones(zeroCellToCellIDs.shape))
        trialFlag = Numeric.logical_and(Numeric.logical_not(self.numberOfZeroNeighbors), trialAndZeroCellFlag)
        return Numeric.nonzero(trialFlag)

    def getTrialCellValues(self):
        pass
        
    def getLowestTrialValue(self):
        pass
