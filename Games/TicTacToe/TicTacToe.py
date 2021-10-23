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

def newGame():
    playField = [0,0,0,0,0,0,0,0,0]
    inGame = True
    thumby.display.fill(0)
    boxBorederSize = int(round(thumby.DISPLAY_H/3))
    boxCenter = int(round((thumby.DISPLAY_W-thumby.DISPLAY_H)/2))
    thumby.display.drawLine(boxCenter+boxBorederSize, 0, boxCenter+boxBorederSize, thumby.DISPLAY_H)
    thumby.display.drawLine(boxCenter+boxBorederSize*2, 0, boxCenter+boxBorederSize*2, thumby.DISPLAY_H)
    thumby.display.drawLine(boxCenter,boxBorederSize, boxCenter+thumby.DISPLAY_H, boxBorederSize)
    thumby.display.drawLine(boxCenter,boxBorederSize*2, boxCenter+thumby.DISPLAY_H, boxBorederSize*2)
    thumby.display.update()

    
def updateField():
    boxBorederSize = int(round(thumby.DISPLAY_H/3))
    boxCenter = int(round((thumby.DISPLAY_W-thumby.DISPLAY_H)/2))
    bitmap0 = ()
    bitmap1 = (1,2,132,72,48,48,72,132,2,1,2,1,0,0,0,0,0,0,1,2)
    bitmap2 = (48,204,134,2,1,1,2,134,204,48,0,0,1,1,2,2,1,1,0,0)
    posX = boxCenter+2
    posY = 2
    for i in range(9):
        if (playField[i] == 1):
            thumby.display.drawSprite(bitmap1,posX,posY,10,10,False,False,-1)
        if (playField[i] == 2):
            thumby.display.drawSprite(bitmap2,posX,posY,10,10,False,False,-1)
        posX = posX+boxBorederSize
        if (i == 2 or i == 5 ):
            posX = boxCenter+2
            posY = posY+boxBorederSize
    thumby.display.update()

def playerMove():
    pass
    
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
        thumby.display.drawText("X Wins!!", 20, 20)
        thumby.display.update()
        inGame = False
        
    elif ((2 == playField[0] and 2 == playField[1] and 2 == playField[2]) or
    (2 == playField[3] and 2 == playField[4] and 2 == playField[5]) or
    (2 == playField[6] and 2 == playField[7] and 2 == playField[8]) or
    (2 == playField[0] and 2 == playField[2] and 2 == playField[5]) or
    (2 == playField[1] and 2 == playField[4] and 2 == playField[7]) or
    (2 == playField[2] and 2 == playField[5] and 2 == playField[8]) or
    (2 == playField[0] and 2 == playField[4] and 2 == playField[8]) or
    (2 == playField[2] and 2 == playField[4] and 2 == playField[6])):
        thumby.display.fill(0)
        thumby.display.drawText("O Wins!!", 20, 20)
        thumby.display.update()
        inGame = False
        
    elif (0 != playField[0] and 0 != playField[1] and 0 != playField[2] and
    0 != playField[3] and 0 != playField[4] and 0 != playField[5] and
    0 != playField[6] and 0 != playField[7] and 0 != playField[8]):
        thumby.display.fill(0)
        thumby.display.drawText("Draw!!", 20, 20)
        thumby.display.update()
        inGame = False
    
  
newGame()
while(inGame):
    playerMove()
    updateField()
    checkWinner()
