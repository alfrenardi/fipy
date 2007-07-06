#!/usr/bin/env python

## 
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "square.py"
 #                                    created: 11/17/03 {10:29:10 AM} 
 #                                last update: 7/5/07 {8:16:59 PM} { 1:23:41 PM}
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental
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
 #  2003-11-17 JEG 1.0 original
 # ###################################################################
 ##

r"""

Here we solve the level set equation in two dimensions for a square. The equation is
given by:

.. raw:: latex

    \begin{alignat*}{2}
    | \nabla \phi | &= 1 &\qquad& \\
    \phi &= 0 && \text{at} \qquad \begin{cases}
	x = \left( L / 3, 2 L / 3 \right) 
	& \text{for $L / 3 \le y \le 2 L / 3$} \\
	y = \left( L / 3, 2 L / 3 \right) 
	& \text{for $L / 3 \le x \le 2 L / 3$}
    \end{cases}
    \end{alignat*}
    

Do the tests:

   >>> def evalCell(phix, phiy, dx, dy):
   ...     aa = dy**2 + dx**2
   ...     bb = -2 * ( phix * dy**2 + phiy * dx**2)
   ...     cc = dy**2 * phix**2 + dx**2 * phiy**2 - dx**2 * dy**2
   ...     sqr = sqrt(bb**2 - 4. * aa * cc)
   ...     return ((-bb - sqr) / 2. / aa,  (-bb + sqr) / 2. / aa)
   >>> val = evalCell(-dy / 2., -dx / 2., dx, dy)[0]
   >>> v1 = evalCell(val, -3. * dx / 2., dx, dy)[0]
   >>> v2 = evalCell(-3. * dy / 2., val, dx, dy)[0]
   >>> v3 = evalCell(v2, v1, dx, dy)[0]
   >>> v4 = dx * dy / sqrt(dx**2 + dy**2) / 2
   >>> arr = array((
   ...     v3           , v2      , -3. * dy / 2.   , v2      , v3,
   ...     v1           , val     , -dy / 2.        , val     , v1           ,
   ...     -3. * dx / 2., -dx / 2., v4              , -dx / 2., -3. * dx / 2.,
   ...     v1           , val     , -dy / 2.        , val     , v1           ,
   ...     v3           , v2      , -3. * dy / 2.   , v2      , v3           ))
   >>> print var.allclose(arr)
   1

"""
__docformat__ = 'restructuredtext'

from fipy import *

dx = 0.5
dy = 2.
nx = 5
ny = 5

Lx = nx * dx
Ly = ny * dy

mesh = Grid2D(dx = dx, dy = dy, nx = nx, ny = ny)

var = DistanceVariable(
    name = 'level set variable',
    mesh = mesh,
    value = -1,
    hasOld = 1
    )

x, y = mesh.getCellCenters()
var.setValue(1, where=((Lx / 3. < x) & (x < 2. * Lx / 3.)) & ((Ly / 3. < y) & (y < 2. * Ly / 3)))

var.calcDistanceFunction()

if __name__ == '__main__':
    import fipy.viewers
    viewer = fipy.viewers.make(vars = var, limits = {'maxval': -5., 'minval': 5.})
    viewer.plot()
    raw_input('finished')
