import numpy as np
import itertools
from numpy.core.fromnumeric import reshape
from numpy.core.records import array
from pprint import pprint
from numpy.lib.polynomial import RankWarning

csKey = 0


def caesarCypherEncrypt(text, s):
    result = ""
    ts = s
    for i in text:
        # print(s)
        if i == " ":
            result += " "
            continue
        if ord(i)+s > 122:
            temp = ord(i)
            ts = s
            while ts != -1:
                if temp > 122:
                    temp = 97
                    ts -= 1
                    continue
                temp += 1
                ts -= 1
            result += chr(temp)
        else:
            result += chr(ord(i)+s)
    print("substituted text", result)
    return result


def ceaserCypherDecrypt(text, s):
    result = ""
    ts = s
    for i in text:
        # print(s)
        if i == " ":
            result += " "
            continue
        if ord(i)-s < 97:
            temp = ord(i)
            ts = s
            while ts != -1:
                if temp < 97:
                    temp = 122
                    ts -= 1
                    continue
                temp -= 1
                ts -= 1
            result += chr(temp)
        else:
            result += chr(ord(i)-s)
        # print(result)
    return result


def getAllFactors(n):
    temp = []
    for i in range(1, n):
        if (n % i == 0):
            temp.append(i)
    return(temp)


def getAllCombinations2(n):
    factors = getAllFactors(n)
    l = 0
    r = len(factors)-1
    tl = []
    while l < len(factors):
        tl.append((int(factors[l]), int(factors[r])))
        l += 1
        r -= 1
    # print(tl)
    return(tl)


def getAllCombinations(n):
    i = 1
    while i*csKey < n:
        i += 1
    return (i, csKey)


def transpositon(encpText):
    possibleCombinations = getAllCombinations(len(encpText))
    arrayL = []

    arrayL = np.reshape(list(encpText), possibleCombinations)
    print(possibleCombinations)
    # for i, j in possibleCombinations:
    #     if i == csKey:
    #         keyi, keyj = i, j
    #         break
    # key = "bac"
    # order = [(ord(i) % 26, idx) for idx, i in enumerate(key)]
    # order.sort()
    # order = [i[1] for i in order]
    order = [i for i in range(csKey-1, -1, -1)]
    newEnc = ""
    for i in order:
        for j in arrayL:

            newEnc += (j[i])
    # print(arrayL, "trans")
    print("Transpositon matrix")
    print(arrayL)
    print("Encrypted text")

    print(newEnc)
    DecryptTransformation(newEnc, possibleCombinations)


def DecryptTransformation(enc, possibleCombinations):

    global csKey
    # print(csKey)
    # print(len(enc))
    arrayL = [[i for i in range(possibleCombinations[1])]
              for j in range(possibleCombinations[0])]

    i, j = 0, 0
    for e in enc:
        if(i >= possibleCombinations[0]):
            i = 0
            j += 1
        arrayL[i][j] = e
        i += 1
        # if(j>=possibleCombinations[1]):
        #     j=0

        # arrayL = np.reshape(list(enc), possibleCombinations)
        # arrayL = np.transpose(arrayL)
    # print(arrayL)
    # print(arrayL)
    # possibleCombinations = getAllCombinations(len(enc))

    keyLength = csKey

    newpos = list(itertools.permutations(
        [i for i in range(keyLength)], keyLength))
    # print(newpos)
    print("All the {} possiblities".format(len(newpos)))
    for per in newpos:  # cols order
        FinalTemp = []
        for i in range(len(arrayL)):
            temp = []
            # print(i)
            for idx, j in enumerate(per):

                temp.append(arrayL[i][j])
            FinalTemp.append(temp)
        text = ""
        for i in FinalTemp:
            text += ''.join(i)

        pprint(FinalTemp)
        print(ceaserCypherDecrypt(text, csKey))

    # print(newpos)


def mainFunc():

    global csKey
    encpText = input("Enter string ")
    csKey = int(input("Enter key "))
    while len(encpText) % csKey != 0:
        encpText += " "

    transpositon(caesarCypherEncrypt(encpText, csKey))


mainFunc()
