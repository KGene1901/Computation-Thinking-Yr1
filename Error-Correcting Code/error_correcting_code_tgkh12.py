def decimalToVector(i,l):
    bit_seq = [0]*l # initialising vector

    if i == 0:
        return bit_seq  # trivial as binary of 0 will always be 0 regardless of how many digits

    else:
        for x in range(0,len(bit_seq)):
            if (i-(2**(l-1)))<0:    # if number is less than 2^(l-1) then move to the next position
                l-=1
            else:
                bit_seq[x]=1    
                i-=(2**(l-1))
                l-=1

    return bit_seq

#function HammingG
#input: a number r
#output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
def hammingGeneratorMatrix(r):
    n = 2**r-1
    
    #construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)

    #construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))

    #construct H'
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))

    #construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))

    #apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    #transpose    
    G = [list(i) for i in zip(*G)]

    return G

def repetitionEncoder(m,n):

    if len(m)!=1:   # input error checking
        return []   
    else:
        return m*n

def repetitionDecoder(v):
    num0 = 0
    num1 = 0

    for i in v:
        if i==0:
            num0+=1 # total number of bit 0s in the vector
        elif i==1:
            num1+=1 # total number of bit 1s in the vector

    if num0>(len(v)/2): # checks if the number of bit 0 are more than bit 1
        return [0]
    
    elif num1>(len(v)/2): # checks if the number of bit 1 are more than bit 0
        return [1]
    else:
        return []

def message(a):
    #initialising variables
    l = len(a)  # length of vector
    r=2 # trying to use the smallest posssible r starting from 2
    k=(2**r)-r-1    # messages of length k can only be encoded for some r>=2

    while k-r<l:    # increase r by one until this is satisfied
        r+=1
        k=(2**r)-r-1

    msg = [0]*r

    m = r   # copy variable values to retain original data values for the initial parameters
    n = l

    for x in range(0,len(msg)): # converts length of vector into binary
            if (n-(2**(m-1)))<0:
                m-=1
            else:
                msg[x]=1
                n-=(2**(m-1))
                m-=1

    msg+=([0]*(k-r))    # concatenate rest of the bits to create message of length k

    for i in range (r, r+l):    # (m[r+1], . . . , m[r+l]) =a
        msg[i]=a[m]
        m+=1

    if k>(l+r): # checking if there are any unused bits
        for j in range (r+l+1, k):  # (m[r+l+1], . . . , m[k]) = (0, . . . ,0)
            msg[j]=0

    return msg

def hammingEncoder(m):
    r = 2
    
    while ((2**r)-r-1)<len(m):  # line 124-130 are input error checking to ensure that the input vector is of length (2**r)-r-1
        r+=1
    else:
        if ((2**r)-r-1)==len(m):
            pass
        else:
            return []

    Gmatrix = hammingGeneratorMatrix(r) # creates generator matrix for calculated r from the error checking
    resultMatrix = [0]*len(Gmatrix[0])  # initialising codework matrix
    pos=0

    for i in range (len(Gmatrix[0])):   # lines 136-145 are for the multiplication of the message with the generator matrix
        total = 0  
        for j in range (len(Gmatrix)):
            
            total = total + ((m[j])*(Gmatrix[j][i]))
            if total>1:
                total=0

        resultMatrix[pos] = total
        pos+=1

    return resultMatrix

def hammingDecoder(v):
    
 ## validating received message length ##
    r = 2
    
    while ((2**r)-1)<len(v):    # line 155-161 are input error checking to ensure that the input vector is of length (2**r)-1
        r+=1
    else:
        if ((2**r)-1)==len(v):
            pass
        else:
            return []               
 ########################################

 ##  Validating message recieved ##
    H_transpose = []

    for i in range(1, (2**r)):
        H_transpose.append(decimalToVector(i,r))    # creates transposed parity check matrix

    result = [0]*len(H_transpose[0])
    
    pos=0
        
    for i in range (len(H_transpose[0])):   # lines 174-183 are for the multiplication of the received message/codeword with the parity check matrix
        total=0   
        for j in range (len(H_transpose)):
            
            total = total + ((v[j])*(H_transpose[j][i]))
            if total>1:
                total=0

        result[pos] = total
        pos+=1
 #####################################

 ## generating the right codeword ##
    binary = int(''.join((map(str, result))))
    i,x = 0,0
    while binary!=0:
        rem = binary % 10
        i += (rem * (2**x))
        binary = binary//10
        x += 1

    if i==0:    # recieved message/codeword is valid
        return v

    e_i_bin = [0]*len(v)    # initialises error vector
    e_i_bin[i-1] = 1
    codeword = []
    total = 0
    
    for j in range (len(e_i_bin)):  # addition of recieved message/codeword with error vector
        total = v[j] + e_i_bin[j]
        if total>1:
            total=0
        codeword.append(total)
        

    return codeword
 ########################################   

def messageFromCodeword(c):
    r = 2
    
    while ((2**r)-1)<len(c):    # line 217-223 are input error checking to ensure that the input vector is of length (2**r)-1
        r+=1
    else:
        if ((2**r)-1)==len(c):
            pass
        else:
            return []

    i = 0
    m = []
    for j in range (len(c)):
        if j+1==(2**i):
            i+=1
        else:
            m.append(c[j])  # picks only the bits which are not in the positions of powers of 2
        
    return m


def dataFromMessage(m):

    k = len(m)
    r = 2
    l_bin = []
    l = 0
    
    while ((2**r)-r-1)<len(m):  # line 243-249 are input error checking to ensure that the input vector is of length (2**r)-r-1
        r+=1
    else:
        if ((2**r)-r-1)==len(m):
            pass
        else:
            return []

    for i in range(r):
        l_bin.append(m[i])  # (m_1, . . . , m_r) represents l in binary

    binary = int(''.join((map(str, l_bin))))
    x = 0
    while binary!=0:
        rem = binary % 10
        l += (rem * (2**x)) # calculates value of l in decimal
        binary = binary//10
        x += 1

    if k-r<l:   # validating k − r = 2r − 2r − 1 ≥ l 
        return []
    
    data = []
    for y in range (r, r+l):    # (m_r+1, . . . , m_r+l) = data initially sent
        data.append(m[y])

    return data
