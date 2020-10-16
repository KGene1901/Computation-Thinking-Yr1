#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
'''
@param: len1 => length of string s1
@param: len2 => length of string s2
@param: ele => element to fill matrix with 
@return: seqMatrix => m x n matrix 
'''
def createMatrix (len1,len2, ele):  # creates and returns an m x n matrix based on the length of s1 and s2 
    seqMatrix = ([[ele]*(len1+1) for i in range (len2+1)])
    return seqMatrix    

'''
@param: s1 => string s1
@param: s2 => string s2
@return: score
'''
def scoring(s1, s2):    # compares pairs of letters of the same position in newS1 and newS2 and scores them accordingly 
    score = 0
    
    if s1 == s2:    # letters match
        if s1 == 'A':
            score = 3
        elif s1 == 'C':
            score = 2
        elif s1 == 'G':
            score = 1
        elif s1 == 'T':
            score = 2
    
    else:
        score = -3  # mismatch of letters

    return score

'''
@param: s1 => string s1
@param: s2 => string s2
@return: best_score => the best score found from all the comparisons
@return: matrix2 => backtracking matrix
@return: startPos_i => starting row position for backtracking
@return: startPos_j => starting column position for backtracking
@return: s1 => updated s1
@return: s2 => updated s2
'''
def alignMatrix (s1, s2):
    matrix = createMatrix(len(seq1),len(seq2), 0)   # creates scoring matrix
    matrix2 = createMatrix(len(s1),len(s2), '-')    # creates backtracking/direction matrix
    matrix2[0] = ['end']*(len(s1))  # initialising backtracking matrix 
    for k in range (1,len(s2)+1):
        matrix2[k][0] = 'end'   # trivial that for local alignment, the first row and first columns are all zeroes 

    s1 = '-' + s1
    s2 = '-' + s2
    best_score = 0  # score can not be negative

    for i in range (1,len(s2)): # for each row 
        for j in range (1, len(s1)):    # for each column
            matrix[i][j] = max (                        #from left          #from top
                scoring(s1[j],s2[i])+matrix[i-1][j-1], matrix[i][j-1]-4, matrix[i-1][j]-4, 0 
            )   # compares scores from three instances with zero and assigns the position the largest value
            if matrix[i][j]>best_score: # finds best score by comparing each outcome and constantly updating "best_score"
                best_score = matrix[i][j]
                startPos_i = i  # row
                startPos_j = j  # column

            if matrix[i][j] == 0:   # lines 50-58: fills the backtracking matrix with appropriate directions as each score comes in
                matrix2[i][j] = 'end'
            else:
                if matrix[i][j] == scoring(s1[j],s2[i])+matrix[i-1][j-1]:
                    matrix2[i][j] = 'D'
                if matrix[i][j] == matrix[i][j-1]-4:
                    matrix2[i][j] = 'L'
                if matrix[i][j] == matrix[i-1][j]-4:
                    matrix2[i][j] = 'U'

    return best_score, matrix2, startPos_i, startPos_j, s1, s2

'''
@param: matrix => backtracking matrix
@param: posi => starting row position for backtracking
@param: posj => starting column position for backtracking
@param: s1 => string s1
@param: s2 => string s2
@return: best_alignment => array containing matching sequence newS1 and newS2
'''
def backtrack (matrix, posi, posj, s1, s2):
    best_alignment = []
    newS1 = ''
    newS2 = ''
    while matrix[posi][posj] != 'end':  # halts backtracking process if "end" condition is met and returns best_alignment 
        if matrix[posi][posj] == 'D':   # if condition is met: matches pairs of letters in the same position in both the strings
            newS1 = s1[posj] + newS1
            newS2 = s2[posi] + newS2
            posi -= 1
            posj -= 1

        if matrix[posi][posj] == 'U':   # if condition is met: matches letter in that position of s2 with a gap 
            newS1 = '-' + newS1 
            newS2 = s2[posi] + newS2
            posi -= 1

        if matrix[posi][posj] == 'L':   # if condition is met: matches letter in that position of s1 with a gap 
            newS1 = s1[posj] + newS1 
            newS2 = '-' + newS2
            posj -= 1

    # final alignment of newS1 and newS2 appended to the list "best_alignment"
    best_alignment.append(newS1)
    best_alignment.append(newS2)

    return best_alignment


# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# To work with the printing functions below the best local alignment should be called best_alignment and its score should be called best_score. 

best_score, matrix, startPos_i, startPos_j, s1, s2 = alignMatrix(seq1,seq2) 
best_alignment = backtrack(matrix, startPos_i, startPos_j, s1, s2)

#-------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

