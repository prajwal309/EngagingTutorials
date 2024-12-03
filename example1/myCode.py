import sys
import numpy as np
import time
#
def invert_matrix(size):
    try:
        # Generate a random matrix of the given size
        matrix = np.random.rand(size, size)
    
        # Invert the matrix
        inverse_matrix = np.linalg.inv(matrix)
      
        
    except np.linalg.LinAlgError:
        print("Matrix is singular and cannot be inverted.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python myCode.py <matrix_size>")
    else:

        startTime = time.time()
        try:
            size = int(sys.argv[1])
            invert_matrix(size)
        except ValueError:
            print("Please provide a valid integer for matrix size.")
        endTime = time.time()
        print("Matrix Size: ", size, " Execution time: ", endTime - startTime, " seconds.")