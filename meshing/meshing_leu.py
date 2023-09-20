#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */meshing/meshing_leu.py
#
# PROGRAMMER: Ding Ning
# DATE CREATED: September 17, 2023
# REVISED DATE: September 20, 2023
# PURPOSE: Create a function meshing_leu that uses the given lengths of the
#          gap, the element on the left end, and the element on the right end,
#          with the least elements of unequal sizes method, to fill the gap
#          between the two side elements. The function returns a list of
#          the length(s) of the filling element(s).
#          Note: The least elements of unequal sizes (LEU) method fills the
#          gap with the possible smallest number of elements, where all the
#          elements are of the largest size besides the last element of a
#          smaller size to fill the remained gap (if any).
#          For example, if L = 7, S1 = 2, and S2 = 1, the lengths of the
#          first three filling elements are 2 and the length of the last
#          element is 1:
#          [2]...[2]|[2][2][2][1]|[1]...[1] (The elements between pipes are
#          filling elements.)
##
# Import the math library for the floor function.
import math

# Define meshing function using the LEU method.
def meshing_leu(len_gap: float, len_s1: float, len_s2: float) -> list:
    """
    :param len_gap: the length of the gab between the elements on two sides
    :param len_s1: the length of the element on the left side
    :param len_s2: the length of the element on the right side
    :return: a list of the length(s) of the filling element(s)
    """
    # Compare the lengths of the two given side elements.
    len_max, len_min = max(len_s1, len_s2), min(len_s1, len_s2)

    # Create an empty list for the filling element(s).
    lens_filling_elements = []

    # If the gap is smaller than the largest side element, fill the gap with
    # an element of the gap length.
    if len_gap <= len_max:
        lens_filling_elements.append(len_gap)

    else:
        # Get the number of the first element(s) of the same length.
        num_filling_elements_less_one = math.floor(len_gap / len_max)

        # Get the length of each filling element, i.e. the length of the
        # largest side element, and save them into the list.
        for _ in range(num_filling_elements_less_one):
            lens_filling_elements.append(len_max)

        # For the last element, if there is gap, fill the gap using the
        # remained gap length; otherwise, no more filling element.
        if len_gap - len_max * num_filling_elements_less_one > 0:
            lens_filling_elements.append(len_gap - len_max *
                                         num_filling_elements_less_one)

    return lens_filling_elements