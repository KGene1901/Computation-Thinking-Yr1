#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
'''
@param: s1 => string s1
@param: s2 => string s2
@return: score
'''
def scoring(s1, s2):    # compares pairs of letters of the same position in newS1 and newS2 and scores them accordingly  
    score = 0
    for i in range(len(s1)-1, -1, -1):
        if s1[i] == s2[i]:  # letters match
            if s1[i] == 'A':
                score += 3
            elif s1[i] == 'C':
                score += 2
            elif s1[i] == 'G':
                score += 1
            elif s1[i] == 'T':
                score += 2

        elif ((s1[i] == '-' and s2[i] != '-') or (s2[i] == '-' and s1[i] != '-')):  # letters are matched with a gap
            score -= 4

        else:   # mismatch of letters
            score -= 3

    return score

'''
@param: s1 => string s1
@param: s2 => string s2
@param: newS1 => final sequence for s1
@param: news2 => final sequence for s2
@param: best_result => array containing the best score (format: [best score, best sequence generated from sequence 1, best sequence generated from sequence 2])
@param: sequences => total number of alignments (running total)
'''
def alignSeq(s1, s2, newS1, newS2, best_result, sequences):
    s1a = newS1
    s2a = newS2

    if (len(s1) == 0 and len(s2) == 0): # Base case: if both strings are empty
        bScore = scoring(newS1,newS2)   # calculating score for the two compared sequences 
        sequences[0]+=1 # running total of the number of alignments created from the two given sequences
        if bScore>= best_result[0]: # finding for the best score (is constantly updated if the calculated score is higher than the current score)
            best_result[0] = bScore
            best_result[1] = newS1
            best_result[2] = newS2
       
    elif len(s1) != 0 and len(s2) == 0: # Base case: if s2 is empty
        newS2 = (len(s1)*'-') + newS2
        newS1 = s1 + newS1
        bScore = scoring(newS1,newS2)
        sequences[0]+=1
        if bScore>= best_result[0]:
            best_result[0] = bScore
            best_result[1] = newS1
            best_result[2] = newS2

    elif len(s1) == 0 and len(s2) != 0: # Base case: if s1 is empty
        newS1 = (len(s2)*'-') + newS1
        newS2 = s2 + newS2
        bScore = scoring(newS1,newS2)
        sequences[0]+=1
        if bScore>= best_result[0]:
            best_result[0] = bScore
            best_result[1] = newS1
            best_result[2] = newS2

  
    else:
            s1a = s1[:-1]
            s2a = s2[:-1]
            
            alignSeq(s1a, s2a, s1[-1] + newS1, s2[-1] + newS2, best_result, sequences)  # calls function on pairing two letters together 
            alignSeq(s1a, s2, s1[-1] + newS1, '-' + newS2, best_result, sequences)  # calls function on pairing a letter from S1 with a gap
            alignSeq(s1, s2a, '-' + newS1, s2[-1] + newS2, best_result, sequences)  # calls function on pairing a letter from S2 with a gap

# ------------------------------------------------------------

# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it


def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1), len(string2))):
        if string1[i] == string2[i]:
            string3 = string3+"|"
        else:
            string3 = string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1 = file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2 = file2.read()
file2.close()
start = time.time()

# -------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Call any functions you need here, you can define them above.
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score.
# The number of alignments you have checked should be stored in a variable called num_alignments.

sequences = [0]
best_result = [-10000000000000, '', '']
alignSeq(seq1, seq2, '', '', best_result, sequences)
best_alignment = [best_result[1], best_result[2]]   # extracting the pair with the best alignment
best_score = best_result[0] # extracting the best score
num_alignments = sequences[0]

# -------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This calculates the time taken and will print out useful information
stop = time.time()
time_taken = stop-start

# # Print out the best
print('Alignments generated: '+str(num_alignments))
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

# -------------------------------------------------------------
