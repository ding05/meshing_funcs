#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */meshing/input.py
#
# PROGRAMMER: Ding Ning
# DATE CREATED: September 18, 2023
# REVISED DATE: September 20, 2023
##

def input(input_filepath: str) -> list:
    """
    Read the TXT file that contains the arguments for the meshing function.
    :param input_dirpath: the path to the TXT file that contains the arguments
    for the meshing function
    :return: a list of arguments for the meshing functions
    """
    # Open and read the input TXT file.
    with open(input_filepath) as f:
        # Read the items from the TXT file as the items in a list.
        argument_list = f.read().splitlines()

    # Close the input TXT file.
    f.close()

    # Convert the string type into the float type in the list.
    argument_list = [float(i) for i in argument_list]

    return argument_list