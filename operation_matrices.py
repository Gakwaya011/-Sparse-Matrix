class SparseMatrix:
    def __init__(self, numRows=None, numCols=None, filePath=None):
        # Initialize the SparseMatrix object. Can be initialized with dimensions or from a file.
        if filePath:  # If a file path is provided
            self._load_from_file(filePath)  # Load the matrix from the file
        else:  # Otherwise, initialize with given number of rows and columns
            self.rows = numRows  # Set the number of rows
            self.cols = numCols  # Set the number of columns
            self.elements = {}  # Initialize an empty dictionary to store matrix elements

    def _load_from_file(self, filePath):
        # Load matrix data from a file
        self.elements = {}  # Initialize an empty dictionary to store matrix elements
        try:
            with open(filePath, 'r') as file:  # Open the file for reading
                lines = file.readlines()  # Read all lines from the file
                self.rows = int(lines[0].split('=')[1].strip())  # Parse the number of rows from the first line
                self.cols = int(lines[1].split('=')[1].strip())  # Parse the number of columns from the second line

                for line in lines[2:]:  # Iterate over the remaining lines
                    line = line.strip()  # Strip whitespace from the line
                    if line:  # If the line is not empty
                        if line[0] != '(' or line[-1] != ')':  # Check for valid format
                            raise ValueError("Input file has wrong format")  # Raise an error if format is invalid
                        parts = line[1:-1].split(',')  # Split the line into parts
                        if len(parts) != 3:  # Check if there are exactly 3 parts
                            raise ValueError("Input file has wrong format")  # Raise an error if format is invalid
                        row, col, value = int(parts[0]), int(parts[1]), int(parts[2])  # Parse row, column, and value
                        self.setElement(row, col, value)  # Set the element in the matrix
        except Exception as e:  # Catch any exceptions
            raise ValueError(f"Input file has wrong format: {str(e)}")  # Raise an error with a message

    def getElement(self, currRow, currCol):
        # Get the value of the matrix at the specified row and column
        return self.elements.get((currRow, currCol), 0)  # Return the value or 0 if not found

    def setElement(self, currRow, currCol, value):
        # Set the value of the matrix at the specified row and column
        if value != 0:  # If the value is not zero
            self.elements[(currRow, currCol)] = value  # Set the element in the dictionary
        elif (currRow, currCol) in self.elements:  # If the value is zero and the element exists
            del self.elements[(currRow, currCol)]  # Remove the element from the dictionary

    def __add__(self, other):
        # Add two matrices
        if self.rows != other.rows or self.cols != other.cols:  # Check if dimensions match
            raise ValueError("Matrix dimensions must match for addition.")  # Raise an error if they don't match
        result = SparseMatrix(self.rows, self.cols)  # Create a result matrix with the same dimensions
        for (row, col), value in self.elements.items():  # Iterate over the elements of the first matrix
            result.setElement(row, col, value + other.getElement(row, col))  # Add corresponding elements
        for (row, col), value in other.elements.items():  # Iterate over the elements of the second matrix
            if (row, col) not in self.elements:  # If the element is not in the first matrix
                result.setElement(row, col, value)  # Set the element in the result matrix
        return result  # Return the result matrix

    def __sub__(self, other):
        # Subtract two matrices
        if self.rows != other.rows or self.cols != other.cols:  # Check if dimensions match
            raise ValueError("Matrix dimensions must match for subtraction.")  # Raise an error if they don't match
        result = SparseMatrix(self.rows, self.cols)  # Create a result matrix with the same dimensions
        for (row, col), value in self.elements.items():  # Iterate over the elements of the first matrix
            result.setElement(row, col, value - other.getElement(row, col))  # Subtract corresponding elements
        for (row, col), value in other.elements.items():  # Iterate over the elements of the second matrix
            if (row, col) not in self.elements:  # If the element is not in the first matrix
                result.setElement(row, col, -value)  # Set the negative of the element in the result matrix
        return result  # Return the result matrix

    def __mul__(self, other):
        # Multiply two matrices
        if self.cols != other.rows:  # Check if the number of columns of the first matrix equals the number of rows of the second matrix
            raise ValueError("Number of columns of the first matrix must equal the number of rows of the second matrix.")  # Raise an error if they don't match
        result = SparseMatrix(self.rows, other.cols)  # Create a result matrix with the appropriate dimensions
        for (row, col), value in self.elements.items():  # Iterate over the elements of the first matrix
            for k in range(other.cols):  # Iterate over the columns of the second matrix
                result.setElement(row, k, result.getElement(row, k) + value * other.getElement(col, k))  # Multiply and add the elements
        return result  # Return the result matrix

    def save_to_file(self, filePath):
        # Save the matrix data to a file
        with open(filePath, 'w') as file:  # Open the file for writing
            file.write(f"rows={self.rows}\n")  # Write the number of rows
            file.write(f"cols={self.cols}\n")  # Write the number of columns
            for (row, col), value in self.elements.items():  # Iterate over the elements
                file.write(f"({row}, {col}, {value})\n")  # Write each element

    def __str__(self):
        # Return a string representation of the matrix
        elements_str = [f"({row}, {col}) {value}" for (row, col), value in self.elements.items()]  # Create a list of string representations of the elements
        return "SparseMatrix with elements:\n" + "\n".join(elements_str)  # Join the elements into a single string

def main():
    operations = {  # Dictionary to map user choices to operations
        '1': 'addition',
        '2': 'subtraction',
        '3': 'multiplication'
    }

    print("Select the matrix operation:")  # Prompt user to select an operation
    print("1. Addition")  # Option 1: Addition
    print("2. Subtraction")  # Option 2: Subtraction
    print("3. Multiplication")  # Option 3: Multiplication
    choice = input("Enter the number of the operation you want to perform: ")  # Get the user's choice

    if choice not in operations:  # If the choice is not valid
        print("Invalid choice. Exiting.")  # Print an error message
        return  # Exit the function

    operation = operations[choice]  # Get the operation based on the user's choice
    matrix_file1 = 'sample_input_for_students/sample_input_for_students/easy_sample_01_1.txt'  # File path for the first matrix
    matrix_file2 = 'sample_input_for_students/sample_input_for_students/easy_sample_01_3.txt'  # File path for the second matrix
    result_file = 'results_for_sample_inputs/results_for_sample_inputs/result_matrix.txt'  # File path for the result matrix

    try:
        matrix1 = SparseMatrix(filePath=matrix_file1)  # Load the first matrix from the file
        matrix2 = SparseMatrix(filePath=matrix_file2)  # Load the second matrix from the file

        if operation == 'addition':  # If the selected operation is addition
            result = matrix1 + matrix2  # Perform addition
        elif operation == 'subtraction':  # If the selected operation is subtraction
            result = matrix1 - matrix2  # Perform subtraction
        elif operation == 'multiplication':  # If the selected operation is multiplication
            result = matrix1 * matrix2  # Perform multiplication

        result.save_to_file(result_file)  # Save the result matrix to a file
        print(f"Result of {operation} saved to {result_file}")  # Print a success message

    except ValueError as e:  # Catch any ValueError exceptions
        print(f"Error: {e}")  # Print the error message
    except Exception as e:  # Catch any other exceptions
        print(f"An unexpected error occurred: {e}")  # Print the error message

if __name__ == '__main__':
    main()  # Run the main function if the script is executed directly
