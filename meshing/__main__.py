#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */meshing/__main__.py
#
# PROGRAMMER: Ding Ning
# DATE CREATED: September 17, 2023
# REVISED DATE: September 20, 2023
##
# Import the parser libraries and the processing files module.
from pathlib import Path
import argparse
from meshing.process_files import *

# Argument parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('input_filepath', type=str, help='Input File Pathname')
arg_parser.add_argument('output_filepath', type=str, help='Output File Pathname')
arg_parser.add_argument('meshing_method', type=str, help='Meshing Method')
args = arg_parser.parse_args()

input_filepath = Path(args.input_filepath)
output_filepath = Path(args.output_filepath)
meshing_method = Path(args.meshing_method)

# Use the provided input and output TXT file paths.
# Read the input, process the input, and write the output.
process_files(input_filepath, output_filepath, meshing_method)