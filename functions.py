"""
/***************************************************************************
 SOSIexpressions
                                 A QGIS plugin
 Expressions related to SOSI
                              -------------------
        begin                : 2023-11-22
        copyright            : (C) 2023 by Morten Sickel
        email                : morten@sickel.net

 Ideas from  Ian Turton ianturton@astuntechnology.com
***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Morten Sickel'
__date__ = '2023-11-22'
__copyright__ = '(C) 2023 by Morten Sickel'

from qgis.core import (
    QgsExpression
)
from qgis.utils import qgsfunction

groupName = "SOSI"

import math

 

@qgsfunction(args='auto', group='SOSI',usesgeometry = False)
def rotate_from_vector(vectorfield,feature,parent):

    """
    From a field that can be None or a vector given as
    two space separated floating point numbers, return a rotation
    angle

    :param vectorfield: Name of the field containing the vector data
    :return: Rotation in degrees clockwise
    """

    if vectorfield is None:
        return(0)
    (x,y) = vectorfield.split(" ")
    x = float(x)
    y = float(y)
    rotate = math.atan2(y,x) / math.pi *180
    # This rotation is based on 1,0 is 0 degrees, then goes CCW, 
    # We want 0 1 to be 0 degrees and then go CW
    return rotate




def registerFunctions(isRegister=True):
    t_register = (QgsExpression.registerFunction, lambda f: f)
    u_register = (QgsExpression.unregisterFunction, lambda f: f.name())
    (funcReg, funcArg) = t_register if isRegister else u_register
    # g = globals()
    l_func = (g[v] for v in g if hasattr(g[v], 'usesGeometry'))
    for f in l_func:
        funcReg(funcArg(f))

