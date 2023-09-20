#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */meshing/meshing_lee.py
#
# PROGRAMMER: Ding Ning
# DATE CREATED: September 17, 2023
# REVISED DATE: September 20, 2023
# PURPOSE: Create a function meshing_lee that uses the given lengths of the
#          gap, the element on the left end, and the element on the right end,
#          with the least elements of an equal size method, to fill the gap
#          between the two side elements. The function returns a list of
#          the length(s) of the filling element(s).
#          Note: The least elements of an equal size (LEE) method fills the
#          gap with the possible smallest number of elements of the same size.
#          For example, if L = 7, S1 = 2, and S2 = 1, the lengths of the
#          four filling elements are all 1.75:
#          [2]...[2]|[1.75][1.75][1.75][1.75]|[1]...[1] (The elements between
#          pipes are filling elements.)
##
# Import the math library for the ceil function.
import math

# Define meshing function using the LEE method.
def meshing_lee(len_gap: float, len_s1: float, len_s2: float) -> list:
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
        # Get the numbers of elements if filling the gap with the element(s) of
        # the length of the larger element.
        num_filling_elements_min = len_gap / len_max

        # Use the ceiling function to get the smallest integer as the number of
        # filling elements.
        num_filling_elements = math.ceil(num_filling_elements_min)

        # Get the length of each filling element and save them into the list.
        for _ in range(num_filling_elements):
            lens_filling_elements.append(len_gap / num_filling_elements)

    return lens_filling_elements