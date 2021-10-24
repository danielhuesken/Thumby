# Tic Tac Toe.

# Written by Daniel Huesken (https://danielhuesken.de) for thumbly.
# Last edited 10/23/2021

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import thumby
import random
import machine

playField = []
dificulty = 7 # 10 = high; 0 = easy Computer
currentPlayer = ''
winnsX = 0
winnsO = 0
draws = 0

def newGame():
    global playField, currentPlayer
    
    playField = ['','','','','','','','','']
    if not currentPlayer:
        currentPlayer = random.choice(['o','x'])
    boxBorederSize = int(round(thumby.DISPLAY_H/3))
    boxCenter = int(round((thumby.DISPLAY_W-thumby.DISPLAY_H)/2))
    thumby.display.fill(0)
    thumby.display.drawLine(boxCenter+boxBorederSize, 0, boxCenter+boxBorederSize, thumby.DISPLAY_H)
    thumby.display.drawLine(boxCenter+boxBorederSize*2, 0, boxCenter+boxBorederSize*2, thumby.DISPLAY_H)
    thumby.display.drawLine(boxCenter,boxBorederSize, boxCenter+thumby.DISPLAY_H, boxBorederSize)
    thumby.display.drawLine(boxCenter,boxBorederSize*2, boxCenter+thumby.DISPLAY_H, boxBorederSize*2)
    thumby.display.update()

    
def updateField(playerPos = -1):
    global playField
    
    boxBorederSize = int(round(thumby.DISPLAY_H/3))
    boxCenter = int(round((thumby.DISPLAY_W-thumby.DISPLAY_H)/2))
    bitmap0 = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    bitmap1 = (1,2,132,72,48,48,72,132,2,1,2,1,0,0,0,0,0,0,1,2)
    bitmap2 = (48,204,134,2,1,1,2,134,204,48,0,0,1,1,2,2,1,1,0,0)
    posBitmap = (254,253,123,183,207,207,183,123,253,254,1,2,3,3,3,3,3,3,2,1)
    posX = boxCenter+2
    posY = 2
    for i in range(9):
        if (i == playerPos and not playField[i]):
            thumby.display.drawSprite(posBitmap,posX,posY,10,10,False,False,-1)
        elif not playField[i]:
            thumby.display.drawSprite(bitmap0,posX,posY,10,10,False,False,-1)
        elif (playField[i] == 'x'):
            thumby.display.drawSprite(bitmap1,posX,posY,10,10,False,False,-1)
        elif (playField[i] == 'o'):
            thumby.display.drawSprite(bitmap2,posX,posY,10,10,False,False,-1)
        posX = posX+boxBorederSize
        if (i == 2 or i == 5 ):
            posX = boxCenter+2
            posY = posY+boxBorederSize
    thumby.display.update()

def playerMove():
    global playField, currentPlayer
    
    currentPlayer = 'o'
    postion = 0
    while(playField[postion]):
        postion = postion + 1
    updateField(postion)
    while (True):
        if (thumby.buttonA.justPressed() == True):
            playField[postion] = 'x'
            updateField()
            break
        if (thumby.buttonB.justPressed() == True):
            pass
        if (thumby.buttonU.justPressed() == True):
            if (postion == 0):
                if not playField[6]:
                    postion = 6
                elif not playField[3]:
                    postion = 3
            elif (postion == 6):
                if not playField[3]:
                    postion = 3
                elif not playField[0]:
                    postion = 0
            elif (postion == 3):
                if not playField[0]:
                    postion = 0
                elif not playField[6]:
                    postion = 6
            elif (postion == 1):
                if not playField[7]:
                    postion = 7
                elif not playField[4]:
                    postion = 4
            elif (postion == 7):
                if not playField[4]:
                    postion = 4
                elif not playField[1]:
                    postion = 1
            elif (postion == 4):
                if not playField[1]:
                    postion = 1
                elif not playField[7]:
                    postion = 7
            elif (postion == 2):
                if not playField[8]:
                    postion = 8
                elif not playField[5]:
                    postion = 5
            elif (postion == 8):
                if not playField[5]:
                    postion = 5
                elif not playField[2]:
                    postion = 2
            elif (postion == 5):
                if not playField[2]:
                    postion = 2
                elif not playField[8]:
                    postion = 8
        if (thumby.buttonD.justPressed() == True):
            if (postion == 0):
                if not playField[3]:
                    postion = 3
                elif not playField[6]:
                    postion = 6
            elif (postion == 3):
                if not playField[6]:
                    postion = 6
                elif not playField[0]:
                    postion = 0
            elif (postion == 6):
                if not playField[0]:
                    postion = 0
                elif not playField[3]:
                    postion = 3
            elif (postion == 1):
                if not playField[4]:
                    postion = 4
                elif not playField[7]:
                    postion = 7
            elif (postion == 4):
                if not playField[7]:
                    postion = 7
                elif not playField[1]:
                    postion = 1
            elif (postion == 7):
                if not playField[1]:
                    postion = 1
                elif not playField[4]:
                    postion = 4
            elif (postion == 2):
                if not playField[5]:
                    postion = 5
                elif not playField[8]:
                    postion = 8
            elif (postion == 5):
                if not playField[8]:
                    postion = 8
                elif not playField[2]:
                    postion = 2
            elif (postion == 8):
                if not playField[2]:
                    postion = 2
                elif not playField[5]:
                    postion = 5
        if (thumby.buttonL.justPressed() == True):
            if (postion == 0):
                postion = 8
            else:
                postion = postion - 1
            while(playField[postion]):
                postion = postion - 1
                if (postion<0):
                    postion = 8
        if (thumby.buttonR.justPressed() == True):
            if (postion == 8):
                postion = 0
            else:
                postion = postion + 1
            while(playField[postion]):
                postion = postion + 1
                if (postion>8):
                    postion = 0
        updateField(postion)
        
def computerMove():
    global playField, dificulty, currentPlayer
    
    currentPlayer = 'x'
    setPosition = -1
    
    for palyerId in ['o','x']:
        if (setPosition == -1 and random.randint(0,10) <= dificulty):
            if (playField[0] == palyerId and playField[1] == palyerId and not playField[2]):
                setPosition = 2
            elif (playField[0] == palyerId and not playField[1] and playField[2] == palyerId):
                setPosition = 1
            elif (not playField[0] and playField[1] == palyerId and playField[2] == palyerId):
                setPosition = 0
            elif (playField[3] == palyerId and playField[4] == palyerId and not playField[5]):
                setPosition = 5
            elif (playField[3] == palyerId and not playField[4] and playField[5] == palyerId):
                setPosition = 4
            elif (not playField[3] and playField[4] == palyerId and playField[5] == palyerId):
                setPosition = 3
            elif (playField[6] == palyerId and playField[7] == palyerId and not playField[8]):
                setPosition = 8
            elif (playField[6] == palyerId and not playField[7] and playField[8] == palyerId):
                setPosition = 7
            elif (not playField[6] and playField[7] == palyerId and playField[8] == palyerId):
                setPosition = 6
            elif (not playField[0] and playField[3] == palyerId and playField[6] == palyerId):
                setPosition = 0
            elif (playField[0] == palyerId and not playField[3] and playField[6] == palyerId):
                setPosition = 3
            elif (playField[0] == palyerId and playField[3] == palyerId and not playField[6]):
                setPosition = 6
            elif (not playField[1] and playField[4] == palyerId and playField[7] == palyerId):
                setPosition = 1
            elif (playField[1] == palyerId and not playField[4] and playField[7] == palyerId):
                setPosition = 4
            elif (playField[1] == palyerId and playField[4] == palyerId and not playField[7]):
                setPosition = 7
            elif (not playField[2] and playField[5] == palyerId and playField == palyerId):
                setPosition = 2
            elif (playField[2] == palyerId and not playField[5] and playField[8] == palyerId):
               setPosition = 5
            elif (playField[2] == palyerId and playField[5] == palyerId and not playField[8]):
                setPosition = 8
            elif (playField[0] == palyerId and playField[4] == palyerId and not playField[8]):
                setPosition = 8
            elif (playField[0] == palyerId and not playField[4] and playField[8] == palyerId):
                setPosition = 4
            elif (not playField[0] and playField[4] == palyerId and playField[8] == palyerId):
                setPosition = 0
            elif (not playField[2] and playField[4] == palyerId and playField[6] == palyerId):
                setPosition = 2
            elif (playField[2] == palyerId and not playField[4] and playField[6] == palyerId):
                setPosition = 4
            elif (playField[2] == palyerId and playField[4] == palyerId and not playField[6]):
                setPosition = 6

    if (not playField[4] and setPosition == -1 and random.randint(0,10) <= dificulty):
       setPosition = 4

    if (setPosition == -1):
        postion = random.randint(0,8)
        while(playField[postion]):
            postion = random.randint(0,8)
        setPosition = postion
        
    playField[setPosition] = 'o'
    updateField()
    
def checkWinner():
    global winnsO, winnsX, draws, currentPlayer
    
    winner = ''
    #boxBorederSize = int(round(thumby.DISPLAY_H/3))
    #boxCenter = int(round((thumby.DISPLAY_W-thumby.DISPLAY_H)/2))

    for palyerId in ['x','o']:
        if (palyerId == playField[0] and palyerId == playField[1] and palyerId == playField[2]):
            #thumby.display.drawLine(boxCenter, boxBorederSize, boxCenter, boxBorederSize)
            winner = palyerId
        elif (palyerId == playField[3] and palyerId == playField[4] and palyerId == playField[5]):
            #thumby.display.drawLine(boxCenter, boxBorederSize+boxBorederSize, boxCenter, boxBorederSize+boxBorederSize)
            winner = palyerId
        elif (palyerId == playField[6] and palyerId == playField[7] and palyerId == playField[8]):
            #thumby.display.drawLine(boxCenter, boxBorederSize+boxBorederSize*2, boxCenter, boxBorederSize+boxBorederSize*2)
            winner = palyerId
        elif (palyerId == playField[0] and palyerId == playField[3] and palyerId == playField[6]):
            #thumby.display.drawLine(lineStartX, lineStartY, lineStartX, lineStartY)
            winner = palyerId
        elif (palyerId == playField[1] and palyerId == playField[4] and palyerId == playField[7]):
            #thumby.display.drawLine(lineStartX+boxBorederSize, lineStartY, lineStartX+boxBorederSize, lineStartY)
            winner = palyerId
        elif (palyerId == playField[2] and palyerId == playField[5] and palyerId == playField[8]):
            #thumby.display.drawLine(lineStartX+boxBorederSize*2, lineStartY, lineStartX+boxBorederSize*2, lineStartY)
            winner = palyerId
        elif (palyerId == playField[0] and palyerId == playField[4] and palyerId == playField[8]):
            #thumby.display.drawLine(lineEndX, lineEndY, lineStartX, lineStartY)
            winner = palyerId
        elif (palyerId == playField[2] and palyerId == playField[4] and palyerId == playField[6]):
            #thumby.display.drawLine(lineStartX, lineStartX, lineEndX, lineEndY)
            winner = palyerId
        if (winner == 'x'):
            winnsX = winnsX + 1
            currentPlayer = 'o'
            thumby.display.drawText("Winner!", 10, 10)
            thumby.display.update()
            machine.reset()
            return True
        elif (winner == 'o'):
            winnsO = winnsO + 1
            currentPlayer = 'x'
            thumby.display.drawText("Loser!", 12, 10)
            thumby.display.update()
            machine.reset()
            return True
    if (playField[0] and playField[1] and playField[2] and
    playField[3] and playField[4] and playField[5] and
    playField[6] and playField[7] and playField[8]):
        currentPlayer = random.choice(['o','x'])
        draws = draws + 1
        thumby.display.drawText("Draw!", 14, 10)
        thumby.display.update()
        machine.reset()
        return True
    return False
    
  
newGame()
while(True):
    if (currentPlayer == 'o'):
        computerMove()
    else:
        playerMove()
    if (checkWinner()):
        break
