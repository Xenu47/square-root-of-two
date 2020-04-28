import math
def getNumbers():
    numberOne = ""
    numberTwo = ""
    for i in range(0,9):
        numberOne+=str(i+1)
        numberTwo+=str(9-i)
    return int(numberOne), int(numberTwo)
def getTwo():
    approxEight = getNumbers()[1]/getNumbers()[0]
    eight = math.floor(approxEight)
    two = eight**(1/3)
    return two
def squareRootOfTwo():
    result = math.sqrt(getTwo())
    return "fuck you", result

print(squareRootOfTwo()[1])
