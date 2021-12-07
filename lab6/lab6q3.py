# @author: vinay

import matlab.engine
eng = matlab.engine.start_matlab()
matrix_dimension = int(input('Enter the matrix dimension:'))
eng.lab6q3(matrix_dimension)
eng.quit()