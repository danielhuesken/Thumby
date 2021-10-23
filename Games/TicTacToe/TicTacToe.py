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
import time
import machine

playField = [0,0,0,0,0,0,0,0,0]
inGame = True
postion = 0

def newGame():
    global playField
    
    playField = [2,2,0,0,0,2,0,0,0]
    inGame = True
    thumby.display.fill(0)
    boxBorederSize = int(round(thumby.DISPLAY_H/3))
    boxCenter = int(round((thumby.DISPLAY_W-thumby.DISPLAY_H)/2))
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
        if (i == playerPos and playField[i] == 0):
            thumby.display.drawSprite(posBitmap,posX,posY,10,10,False,False,-1)
        elif (playField[i] == 0):
            thumby.display.drawSprite(bitmap0,posX,posY,10,10,False,False,-1)
        elif (playField[i] == 1):
            thumby.display.drawSprite(bitmap1,posX,posY,10,10,False,False,-1)
        elif (playField[i] == 2):
            thumby.display.drawSprite(bitmap2,posX,posY,10,10,False,False,-1)
        posX = posX+boxBorederSize
        if (i == 2 or i == 5 ):
            posX = boxCenter+2
            posY = posY+boxBorederSize
    thumby.display.update()

def playerMove():
    global postion, playField
    
    while(playField[postion] != 0):
        postion = postion + 1
    updateField(postion)
    while (True):
        if (thumby.buttonA.justPressed() == True):
            playField[postion] = 1
            break
        if (thumby.buttonB.justPressed() == True):
            machine.reset()
            break
        if (thumby.buttonU.justPressed() == True):
            if (postion == 0):
                postion = 6
            elif (postion == 5):
                postion = 3
            elif (postion == 3):
                postion = 0
            elif (postion == 1):
                postion = 7
            elif (postion == 7):
                postion = 4
            elif (postion == 4):
                postion = 1
            elif (postion == 2):
                postion = 8
            elif (postion == 8):
                postion = 5
            elif (postion == 5):
                postion = 2
        if (thumby.buttonD.justPressed() == True):
            if (postion == 0):
                postion = 3
            elif (postion == 3):
                postion = 6
            elif (postion == 6):
                postion = 0
            elif (postion == 1):
                postion = 4
            elif (postion == 4):
                postion = 7
            elif (postion == 7):
                postion = 1
            elif (postion == 2):
                postion = 5
            elif (postion == 5):
                postion = 8
            elif (postion == 8):
                postion = 2
        if (thumby.buttonL.justPressed() == True):
            if (postion == 0):
                postion = 9
            else:
                postion = postion - 1
        if (thumby.buttonR.justPressed() == True):
            if (postion == 8):
                postion = 0
            else:
                postion = postion + 1
        while(playField[postion] != 0):
            postion = postion + 1
        updateField(postion)
    
def checkWinner():
    if ((1 == playField[0] and 1 == playField[1] and 1 == playField[2]) or
    (1 == playField[3] and 1 == playField[4] and 1 == playField[5]) or
    (1 == playField[6] and 1 == playField[7] and 1 == playField[8]) or
    (1 == playField[0] and 1 == playField[2] and 1 == playField[5]) or
    (1 == playField[1] and 1 == playField[4] and 1 == playField[7]) or
    (1 == playField[2] and 1 == playField[5] and 1 == playField[8]) or
    (1 == playField[0] and 1 == playField[4] and 1 == playField[8]) or
    (1 == playField[2] and 1 == playField[4] and 1 == playField[6])):
        thumby.display.fill(0)
        thumby.display.drawText("X Wins!!", 5, 20)
        thumby.display.update()
        return True
    elif ((2 == playField[0] and 2 == playField[1] and 2 == playField[2]) or
    (2 == playField[3] and 2 == playField[4] and 2 == playField[5]) or
    (2 == playField[6] and 2 == playField[7] and 2 == playField[8]) or
    (2 == playField[0] and 2 == playField[2] and 2 == playField[5]) or
    (2 == playField[1] and 2 == playField[4] and 2 == playField[7]) or
    (2 == playField[2] and 2 == playField[5] and 2 == playField[8]) or
    (2 == playField[0] and 2 == playField[4] and 2 == playField[8]) or
    (2 == playField[2] and 2 == playField[4] and 2 == playField[6])):
        thumby.display.fill(0)
        thumby.display.drawText("O Wins!!", 5, 20)
        thumby.display.update()
        return True
    elif (0 != playField[0] and 0 != playField[1] and 0 != playField[2] and
    0 != playField[3] and 0 != playField[4] and 0 != playField[5] and
    0 != playField[6] and 0 != playField[7] and 0 != playField[8]):
        thumby.display.fill(0)
        thumby.display.drawText("Draw!!", 5, 20)
        thumby.display.update()
        return True
    return False
    
  
newGame()
while(True):
    playerMove()
    if (checkWinner()):
        break