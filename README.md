# SparseMatrix Operations

## project name

-Sparse-Matrix

## Overview

This project provides a Python implementation for performing operations on large sparse matrices. Sparse matrices are matrices in which most elements are zero. This implementation optimizes both memory and runtime efficiency by storing only non-zero elements. The supported operations are addition, subtraction, and multiplication.

## Features

- Load sparse matrices from a file.
- Perform matrix addition, subtraction, and multiplication.
- Save the resulting matrix to a file.
- Custom implementation without using built-in libraries such as regex or standard matrix manipulation libraries.

## File Format

The input files for sparse matrices should be in the following format:

```
rows=<number_of_rows>
cols=<number_of_columns>
(row, col, value)
(row, col, value)
...
```

Example:

```
rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)
(0, 639, 857)
(0, 165, -933)
(0, 1350, -89)
```

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Gakwaya011/-Sparse-Matrix.git
   cd -Sparse-Matrix
   ```

2. No additional packages are required.

### Usage

1. Prepare your input files for the two sparse matrices you want to operate on.

2. Run the script:

   ```bash
   python operation_matrices.py
   ```

3. Follow the prompts to select the matrix operation (addition, subtraction, or multiplication).

4. The result will be saved in `result_matrix.txt` in the same directory.

### Example

If you have two input files, `matrix1.txt` and `matrix2.txt`, with the following content:

`matrix1.txt`:

```
rows=2
cols=2
(0, 0, 1)
(1, 1, 2)
```

`matrix2.txt`:

```
rows=2
cols=2
(0, 0, 3)
(1, 0, 4)
```

Running the script and choosing addition will produce a `result_matrix.txt` with:

```
rows=2
cols=2
(0, 0, 4)
(1, 0, 4)
(1, 1, 2)
```

## Code Structure

- `SparseMatrix` class:

  - `__init__(self, numRows=None, numCols=None, filePath=None)`: Initializes the sparse matrix.
  - `_load_from_file(self, filePath)`: Loads matrix data from a file.
  - `getElement(self, currRow, currCol)`: Gets the value of the matrix at the specified row and column.
  - `setElement(self, currRow, currCol, value)`: Sets the value of the matrix at the specified row and column.
  - `__add__(self, other)`: Adds two matrices.
  - `__sub__(self, other)`: Subtracts two matrices.
  - `__mul__(self, other)`: Multiplies two matrices.
  - `save_to_file(self, filePath)`: Saves the matrix data to a file.
  - `__str__(self)`: Returns a string representation of the matrix.

- `main()`: The main function to run the script, handle user input, and perform the selected matrix operation.

## Error Handling

- The code checks for the correct format of input files and raises `ValueError` if the format is incorrect.
- Dimension mismatches for addition, subtraction, and multiplication operations are handled with appropriate error messages.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or suggestions, please contact c.gakwaya@alueducation.com
