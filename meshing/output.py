#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */meshing/output.py
#
# PROGRAMMER: Ding Ning
# DATE CREATED: September 18, 2023
# REVISED DATE: September 19, 2023
##

def output(lens_filling_elements: list, output_filepath: str) -> None:
    """
    Write a TXT file that contains a list of the length(s) of the filling
    element(s)
    :param lens_filling_elements: a list of the length(s) of the filling element(s)
    :param output_filepath: the path to the TXT file that contains the output
    list of the length(s) of the filling element(s)
    """
    # Open and write the list into the output TXT file.
    with open(output_filepath, 'w') as f:
        for len in lens_filling_elements:
            f.write(str(len))
            f.write('\n')

    # Close the output TXT file.
    f.close()