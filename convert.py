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
    quotient = 0
    remainder = 0
    hexValue = ''
    tmpDividend = origin
    
    while True:
        remainder = changeHex(tmpDividend % 16)
        quotient = tmpDividend // 16
        hexValue = remainder + hexValue

        if quotient < 16:	
            hexValue = changeHex(quotient) + hexValue
            break
        else: 
            tmpDividend = quotient

    return hexValue

def changeHex(value):
    changedVal = 0
    if value < 10 : changedVal = str(value)
    if value == 10 : changedVal = 'A'
    if value == 11 : changedVal = 'B'
    if value == 12 : changedVal = 'C'
    if value == 13 : changedVal = 'D'
    if value == 14 : changedVal = 'E'
    if value == 15 : changedVal = 'F'
    return changedVal

def main():
    origin =  getInput()
    hexValue = calHexadecimal(origin)
    print(origin, ' => ', hexValue)
    return

if __name__ == "__main__":
    main()

