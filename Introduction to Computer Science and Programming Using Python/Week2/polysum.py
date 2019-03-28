# -*- coding: utf-8 -*-
import math

def polysum(n,s):
    '''
    This function should sum the area and square of the perimeter of the regular polygon. 
    The function returns the sum, rounded to 4 decimal places.
    '''

    _poligon_area = (0.25 * n * s**2) / math.tan(math.pi / n)
    _poligon_perimeter = s*n

    return round(_poligon_area + _poligon_perimeter**2,4)
