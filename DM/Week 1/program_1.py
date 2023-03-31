"""Create multidimensional arrays and find its shape and dimension."""


import numpy as np
def main():
    """Main Function"""
    a = np.array([[[1, 2, 3],[1,2,3]],[[1, 2, 3],[1,2,3]],[[1, 2, 3],[1,2,3]],[[1, 2, 3],[1,2,3]]])
    a_shape=a.shape
    a_dimensions=a.ndim
    matrix_of_zeroes=np.zeros((2,2))
    matrix_of_ones=np.ones((2,2))
    reshaped_a=a.reshape(6,4)
    flattened_a=a.flatten()
    print('Initial Array:',a,sep='\n')
    print('Shape: ',a_shape,sep='\n')
    print('Dimensions: ',a_dimensions,sep='\n')
    print('Matrix of Zeroes: ',matrix_of_zeroes,sep='\n')
    print('Matrix of Ones: ',matrix_of_ones,sep='\n')
    print('Shape of a after reshaping: ',reshaped_a.shape,'Array after reshaping',reshaped_a,sep='\n')
    print('Shape of a after flattening: ',flattened_a.shape,'Array after flattening',flattened_a,sep='\n')
    sx=np.zeros((2,2))
    y=np.ones((2,2))
    # vertical=np.vstack((x,y))
    # horizontal=np.hstack((x,y))
    # print('Vertical: ',vertical,sep='\n')
    # print('Horizontal: ',horizontal,sep='\n')
main()
