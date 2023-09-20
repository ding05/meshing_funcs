# meshing: Element Size Transition

This program performs meshing using a specified method.

## Programming Language

Python 3.7.5

## Running meshing

1. Make sure Python has been installed on your computer.
2. Navigate to [this](.) directory, which contains the README.md file.
3. Run the program as a module: `python -m meshing -h`. This will print the help message.
4. Run the program as a module with real inputs: `python -m meshing <input_filepath> <output_filepath> <meshing_method>`
   For the input for meshing with , i.e. `python -m meshing resources/input_1.txt resources/output_1_lee.txt lee`

### meshing Usage:

```commandline
usage: python -m meshing [-h] input_filepath output_filepath meshing_method

positional arguments:
  input_filepath             Input File Pathname
  output_filepath            Output File Pathname
  meshing_method             Meshing Method:
                             lee (Least Elements of an Equal Size),
                             leu (Least Elements of Unequal Sizes),
                             ran (Elements of Random Sizes Between S1 and S2)

optional arguments:
  -h, --help  show this help message and exit
```

## Input Requirement

The input text files are expected to contain three lines of floats or integers, which respectively denote the length of the gap (L), the length of the elements on the left (S1), and the length of the elements on the right (S2).