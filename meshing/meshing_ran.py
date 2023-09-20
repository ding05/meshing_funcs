#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */meshing/meshing_ran.py
#
# PROGRAMMER: Ding Ning
# DATE CREATED: September 17, 2023
# REVISED DATE: September 20, 2023
# PURPOSE: Create a function meshing_ran that uses the given lengths of the
#          gap, the element on the left end, and the element on the right end,
#          with the least elements of randomly unequal sizes method, to fill
#          the gap between the two side elements. The function returns a list
#          of the length(s) of the filling element(s).
#          Note 1: The least elements of randomly unequal sizes (RAN) method
#          fills the gap with the possible smallest number of elements in
#          random sizes in the range [S1, S2]. The smallest number is the
#          ceiling of the quotient of L and max(S1, S2).
#          For example, if L = 7, S1 = 2, and S2 = 1, the number of filling
#          elements is four and the lengths of the filling elements could be
#          1.95, 1.62, 1.78, and 1.65:
#          [2]...[2]|[1.88][1.43][1.92][1.77]|[1]...[1] (The elements between
#          pipes are filling elements.)
#          Note 2: This method is not suitable for a large gap.
##
# Import the math library for the floor function and the random library for
# the uniform function.
import math
import random

# Define meshing function using the RAN method.
def meshing_ran(len_gap: float, len_s1: float, len_s2: float) -> list:
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
        # Get the number of the first element(s) of random lengths.
        num_filling_elements_less_one = math.floor(len_gap / len_max)

        # Generate "num_filling_elements" lengths that sum up to "len_gap".
        # Continue until a valid list is generated.

        # If the lower bound is len_min, the process is very slow to get a
        # valid list. Instead, a larger lower bound is temporarily used and
        # uncomment either of the following commented lines.
        adjusted_len_min = len_min
        # adjusted_len_min = (len_min + len_max) / 2
        # adjusted_len_min = len_max * 0.98

        # Set a start condition where the last element is not decided.
        filled = False

        while not filled:
            lens_filling_elements = [random.uniform(adjusted_len_min, len_max) for
                                     _ in range(num_filling_elements_less_one)]
            last_len = len_gap - sum(lens_filling_elements)

            # If the last length falls in the range [len_min, len_max], append
            # it to the filling element list; else, continue randomizing the
            # lengths of the first element(s).
            if len_min <= last_len <= len_max:
                lens_filling_elements.append(last_len)
                filled = True

    return lens_filling_elements