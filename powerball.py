#Rafael Mendez
#Independent Project - PowerBall



#Funtion that will open file and ensure that user is inputting a valid file
def checkFile():
    goodFile = False
    #Will ask user for input of file to search for data
    while goodFile == False:
        try:
            fileName = input('Please enter a file name: ')
            inFile = open(fileName, 'r')
            goodFile = True
        except IOError:
            print("Invalid file name try again...")
    return inFile

#Function to open up CSV file with data and split it into different list
def getData():
    inFile = checkFile()
    #Creating empty lists that will store CSV data from file
    #Each winning number will be stored in different list
    drawDates = []
    winningNum1 = []
    winningNum2 = []
    winningNum3 = []
    winningNum4 = []
    winningNum5 = []
    powerBallNum = []
    powerPlayNum = []

    #Getting Rid of first line in file
    inFile.readline()

    #Loop that will itereate through data file and add data to lists
    for line in inFile:
        line = line.strip()
        date, num1, num2, num3, num4, num5, pbNum, ppNum = line.split(',')
        #Appending data to list
        drawDates.append(str(date))
        winningNum1.append(int(num1))
        winningNum2.append(int(num2))
        winningNum3.append(int(num3))
        winningNum4.append(int(num4))
        winningNum5.append(int(num5))
        powerBallNum.append(int(pbNum))
        powerPlayNum.append(int(ppNum))

    inFile.close()
    return drawDates, winningNum1, winningNum2, winningNum3, winningNum4, winningNum5, powerBallNum, powerPlayNum

#Function that will iterate through each list of winning numbers and give an appearance score
#It will retunr the number with the highest appearance
def appearCount(list):
    highestAppearance = 0
    highestI = 1
    for t in range (len(list)):
        for i in range(1,70):
            placeHold = int(list.count(i))
            if placeHold > highestAppearance:
                highestAppearance = placeHold
                highestI = i
                print(i, 'appears', placeHold, 'times')
    return highestI, placeHold
            
            
        
            
        


def main():
    drawDates, winningNum1, winningNum2, winningNum3, winningNum4, winningNum5, powerBallNum, powerPlayNum = getData()
    winner1,placeHold1 = appearCount(winningNum1)
    winner2,placeHold2 = appearCount(winningNum2)
    winner3,placeHold3 = appearCount(winningNum3)
    winner4,placeHold4 = appearCount(winningNum4)
    winner5, placeHold5 = appearCount(winningNum5)
    winnerPW,placeHoldPW = appearCount(powerBallNum)
    winnerPP,placeHoldPP = appearCount(powerPlayNum)
    print(winner1,winner2,winner3,winner4,winner5,winnerPW,winnerPP)
    print(placeHold1,placeHold2,placeHold3,placeHold4,placeHold5,placeHoldPW,placeHoldPP)
    
    
    
    
