def getInput():
    origin = 0
    while True:
        print('Input the number what you want to convert to Hex')
        origin = input().lower()
        if origin in 'abcdefghijklmnopqrstuvwxyz':
            print('Please, input only number')
        else:
            return int(origin)	

def calHexadecimal(origin):
    tmpQuotient = 0
    remainderArray = []
    remainder = 0
    tmpDividend = origin
    
    while True:
        remainder = changeHex(tmpDividend % 16)
        remainderArray.append(remainder)
        tmpQuotient = tmpDividend // 16

        if tmpQuotient < 16:	
            remainderArray.append(changeHex(tmpQuotient))
            break
        else: 
            tmpDividend = tmpQuotient

    return remainderArray

def changeHex(value):
    changedVal = 0
    if value < 10 : changedVal = value
    if value == 10 : changedVal = 'A'
    if value == 11 : changedVal = 'B'
    if value == 12 : changedVal = 'C'
    if value == 13 : changedVal = 'D'
    if value == 14 : changedVal = 'E'
    if value == 15 : changedVal = 'F'
    return changedVal

def convertHexStr(remainderArray):
    strHexValue = ""
    for i in range(1, len(remainderArray) + 1) :
        strHexValue += str(remainderArray[len(remainderArray) - i])
    return strHexValue

def main():
    origin =  getInput()
    remainderArray = calHexadecimal(origin)
    strHexValue = convertHexStr(remainderArray)
    print(origin, ' => ', strHexValue)
    return

if __name__ == "__main__":
    main()

