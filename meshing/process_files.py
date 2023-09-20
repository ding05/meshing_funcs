#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */meshing/process_files.py
#
# PROGRAMMER: Ding Ning
# DATE CREATED: September 18, 2023
# REVISED DATE: September 20, 2023
##
# Import the modules.
from meshing.input import *
from meshing.output import *
from meshing.meshing_lee import *
from meshing.meshing_leu import *
from meshing.meshing_ran import *

def process_files(input_filepath: str, output_filepath: str,
                  meshing_method: str) -> None:
    """
    Read the TXT file that contains the arguments for the meshing function and
    write a TXT file that contains a list of the length(s) of the filling
    element(s).
    :param input_dirpath: the path to the TXT file that contains the arguments
    for the meshing function
    :param output_dirpath: the path to the TXT file that contains the output
    list of the length(s) of the filling element(s)
    :param meshing_method: the selected meshing method
    """
    # Read the TXT file and save the arguments in a list.
    argument_list = input(input_filepath)

    # Save the length arguments respectively.
    len_gap, len_s1, len_s2 = argument_list[0], argument_list[1], \
                              argument_list[2]

    # Print the length arguments.
    print('L:', len_gap, 'S1:', len_s1, 'S2:', len_s2)

    # Convert the type of meshing_method into a string.
    meshing_method = str(meshing_method)

    # Choose the meshing function and get the list of the length(s) of the
    # filling element(s).
    if meshing_method == 'lee':
        lens_filling_elements = meshing_lee(len_gap, len_s1, len_s2)

    elif meshing_method == 'leu':
        lens_filling_elements = meshing_leu(len_gap, len_s1, len_s2)

    else:
        lens_filling_elements = meshing_ran(len_gap, len_s1, len_s2)

    # Each float is rounded up to four digits after the decimal place.
    rounded_lens_filling_elements = [round(num, 4) for num in
                                     lens_filling_elements]

    # Print the list of the length(s) of the filling element(s).
    print("List of filling element(s):", rounded_lens_filling_elements)

    # Write the resulted list in a TXT file.
    output(rounded_lens_filling_elements, output_filepath)