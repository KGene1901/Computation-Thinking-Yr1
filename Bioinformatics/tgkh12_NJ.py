# -----------------------------------------------------
# Importing modules -----------------------------------
import sys
import numpy as np

# -----------------------------------------------------

# Initialising functions ------------------------------
'''
@param: array => array with distances
@return: sum => row sum
'''
def rowSum(array):  # calculates row sum for that specific row
    sum = 0
    for i in array:
        sum += float(i)    # adds each value in the array to running total
    return sum

'''
@param: difference => distance value between two objects {d(a,b)}
@param: r => total number of objects/elements being compared (not distance values)
@param: rowsuma => row sum which the first element is in
@param: rowsumb => row sum which the second element is in
@return: q => q score
'''
def qScore(difference, r, rowsuma, rowsumb):    # calculates q score for every comparison in the n x n matrix
    q = (r-1)*difference - rowsuma - rowsumb
    return q

'''
@param: dac => difference between first element and every other element 
@param: dbc => difference between second element and every other element
@param: dab => difference between first element and second element
@return: difference => distance value between two objects {d(a,b)}
'''
def diffScore(dac, dbc, dab):   # calculates distance value between two objects (used to update distance matrix)
    difference = (dac + dbc - dab) / 2
    return difference

'''
@param: matrix => matrix to be updated
@param: pos => position of row/column to be removed
@return: newMatrix => updated matrix after transformation 
'''
def convert(matrix, pos):   # removes one row and one column from the given matrix to shrink it
    newMatrix = np.delete(matrix, pos, 1) # deletes column (axis = 1)
    newMatrix = np.delete(newMatrix, pos, 0) # deletes row (axis = 0)
    newMatrix = newMatrix.astype('f8') # sets data as float
    return newMatrix

'''
@param: matrixA => distance scoring matrix 
@return: matrixB => q-score matrix
'''
def createQMatrix(matrixA): # generates a new q-score matrix
    r = np.size(matrixA, 0) # getting total number of elements
    matrixB = np.copy(matrixA)  # deep copy of distance matrix for intialisation
    for i in range (0, np.size(matrixA, 0)):     # i = row
        rs1 = rowSum(matrixA[i])
        for j in range (0, np.size(matrixA, 0)):  # j = column
            if matrixA[i][j] == 0:
                continue
            rs2 = rowSum(matrixA[j])
            matrixB[i,j] = qScore(matrixA[i,j], r, rs1, rs2)    # populate q-score matrix with the q scores for each comparison
    
    return matrixB

'''
@param: matrix => q-score matrix
@return: i => row position of smallest q value
@return: j => column position of smallest q value
'''
def minFinder(matrix):
    minLoc = np.where(matrix == np.amin(matrix))  # finding coordinates of min Q value
    minLoc = list(zip(minLoc[0], minLoc[1]))    # declaring value to a variable
    i = minLoc[0][0]
    j = minLoc[0][1]

    return i,j

'''
@param: file => text file that contains an n x n distance matrix 
'''
def NJ(file):   # main function to process the given matrix and display step-by-step process of the neighbour joining algorithm until a 2 x 2 matrix has been reached
    matrix = np.loadtxt(file, dtype= str, delimiter = ' ')  # assigning textfile to a variable

    titleRow = matrix[:1, 1:np.size(matrix, 0)] # extracts subarray consisting of the names of elements being compared 
    titleRow = titleRow.flatten()   
    titleRow = titleRow.astype("U30") # allows for 30-character string

    print("\n Original distance matrix and Row sums:")    # displays original distance matrix
    for a in range(0, len(matrix)):   
        if a == 0:
            print(' ', matrix[0])
        else:

            print(' ', matrix[a], '       (', rowSum(matrix[a][1:len(matrix[a])]), ')')

    dMatrix = convert(matrix, 0)    # removes the lettering
    qMatrix = createQMatrix(dMatrix)    # creates first q-score matrix from original distance matrix
    
    print("\n Original Q scores: \n", qMatrix, "\n")    # displays q-score matrix

    while (np.size(dMatrix, 0) != (2)): # loops until matrix is a 2 x 2
        i, j, = minFinder(qMatrix)   # finding the smallest q-score
        delchar = titleRow[i]+titleRow[j]   # merges the two elements whose matching q value is the smallest
        titleRow[j] = delchar   # updates column with new combined element
        titleRow = np.delete(titleRow, i) # delete one column
        
        d2Matrix = convert(dMatrix, i)  # removing one row and one column
        k=0 # determines column in previous distance matrix
        c=0 # determines column in new distance matrix

        while k < np.size(d2Matrix, 0)+1 and c < np.size(d2Matrix, 0): 
            if (d2Matrix[j-1][c] == 0): # skips if distance is 0 as I do not want to compare the same element 
                k+=1
                c+=1
                continue
            elif ((dMatrix[i][c] == 0) or (dMatrix[j][k] == 0)):    # condition is satisfied if one of the two elements is being compared to itself in the original distance matrix
                d2Matrix[j-1][c] = diffScore(dMatrix[i][k+1], dMatrix[j][k+1], dMatrix[i][j])   # the next available score will be used to updated distance score
                k+=2    # skips a column (as the next available score is used rather than the current one)
                c+=1    
            else:
                d2Matrix[j-1][c] = diffScore(dMatrix[i][k], dMatrix[j][k], dMatrix[i][j])   # updates distance value with new distance score
                k+=1
                c+=1

        for l in range (0, np.size(d2Matrix, 0)):
            d2Matrix[l][j - 1] = d2Matrix[j - 1][l] # copies values in new row to the new column

        print("\n Distance matrix and Row sums: \n", ' ', titleRow)   
        for a in range(0, len(d2Matrix)):   
            print(' ', d2Matrix[a], '       (', rowSum(d2Matrix[a]), ')')   # prints rows in new distance matrix with respective row sums

        qMatrix = createQMatrix(d2Matrix)   # generates a new q-score matrix from the new distance matrix
        
        print("\n Q matrix:\n", qMatrix)

        dMatrix = d2Matrix  # old distance matrix is updated 
    
    print("\n Final distance matrix: \n", dMatrix)  # final distance matrix is displayed once more for clarity

# -----------------------------------------------------

# This is used to open the file -----------------------
file1 = open(sys.argv[1], 'r') # recieves file via command line argument

# -----------------------------------------------------

# Main ------------------------------------------------
NJ(file1)

# -----------------------------------------------------