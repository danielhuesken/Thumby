# Tic Tac Toe game for thumby.
# Written by Daniel Huesken (https://danielhuesken.de) for thumbly.


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
playerSymbol = 'x' 
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
    bitmapEmpty = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    bitmapX = (1,2,132,72,48,48,72,132,2,1,2,1,0,0,0,0,0,0,1,2)
    bitmapO = (48,204,134,2,1,1,2,134,204,48,0,0,1,1,2,2,1,1,0,0)
    bitmapCursor =  (0,0,190,126,254,62,206,242,0,0, 0,0,1,1,0,1,1,1,0,0)
    posX = boxCenter+2
    posY = 2
    for i in range(9):
        if (i == playerPos and not playField[i]):
            thumby.display.drawSprite(bitmapCursor,posX,posY,10,10,False,False,-1)
        elif not playField[i]:
            thumby.display.drawSprite(bitmapEmpty,posX,posY,10,10,False,False,-1)
        elif (playField[i] == 'x'):
            thumby.display.drawSprite(bitmapX,posX,posY,10,10,False,False,-1)
        elif (playField[i] == 'o'):
            thumby.display.drawSprite(bitmapO,posX,posY,10,10,False,False,-1)
        posX = posX+boxBorederSize
        if (i == 2 or i == 5 ):
            posX = boxCenter+2
            posY = posY+boxBorederSize
    thumby.display.update()

def playerMove():
    global playField, currentPlayer, playerSymbol
    
    if (playerSymbol == 'x'):
        currentPlayer = 'o'
    else:
        currentPlayer = 'x'
    postion = 0
    while(playField[postion]):
        postion = postion + 1
    updateField(postion)
    while (True):
        if thumby.buttonA.justPressed():
            playField[postion] = playerSymbol
            updateField()
            break
        if thumby.buttonB.justPressed():
            pass
        if thumby.buttonU.justPressed():
            if postion < 3:
                if not playField[postion + 6]:
                    postion = postion + 6
                elif not playField[postion + 3]:
                    postion = postion + 3
            elif postion < 6:
                if not playField[postion - 3]:
                    postion = postion - 3
                elif not playField[postion + 3]:
                    postion = postion + 3
            elif postion < 9: 
                if not playField[postion - 3]:
                    postion = postion - 3
                elif not playField[postion - 6]:
                    postion = postion - 6
        if thumby.buttonD.justPressed():
            if postion < 3:
                if not playField[postion + 3]:
                    postion = postion + 3
                elif not playField[postion + 6]:
                    postion = postion + 6
            elif postion < 6:
                if not playField[postion + 3]:
                    postion = postion + 3
                elif not playField[postion - 3]:
                    postion = postion - 3
            elif postion < 9: 
                if not playField[postion - 6]:
                    postion = postion - 6
                elif not playField[postion - 3]:
                    postion = postion - 3
        if thumby.buttonL.justPressed():
            if (postion == 0):
                postion = 8
            else:
                postion = postion - 1
            while(playField[postion]):
                postion = postion - 1
                if (postion<0):
                    postion = 8
        if thumby.buttonR.justPressed():
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
    global playField, dificulty, currentPlayer, playerSymbol
    
    setPosition = -1
    if (playerSymbol == 'x'):
        currentPlayer = 'x'
        playerIds = ['o','x']
    else:
        currentPlayer = 'o'
        playerIds = ['x','o']
    
    for palyer in playerIds:
        if (setPosition == -1 and random.randint(0,10) <= dificulty):
            if (playField[0] == palyer and playField[1] == palyer and not playField[2]):
                setPosition = 2
            elif (playField[0] == palyer and not playField[1] and playField[2] == palyer):
                setPosition = 1
            elif (not playField[0] and playField[1] == palyer and playField[2] == palyer):
                setPosition = 0
            elif (playField[3] == palyer and playField[4] == palyer and not playField[5]):
                setPosition = 5
            elif (playField[3] == palyer and not playField[4] and playField[5] == palyer):
                setPosition = 4
            elif (not playField[3] and playField[4] == palyer and playField[5] == palyer):
                setPosition = 3
            elif (playField[6] == palyer and playField[7] == palyer and not playField[8]):
                setPosition = 8
            elif (playField[6] == palyer and not playField[7] and playField[8] == palyer):
                setPosition = 7
            elif (not playField[6] and playField[7] == palyer and playField[8] == palyer):
                setPosition = 6
            elif (not playField[0] and playField[3] == palyer and playField[6] == palyer):
                setPosition = 0
            elif (playField[0] == palyer and not playField[3] and playField[6] == palyer):
                setPosition = 3
            elif (playField[0] == palyer and playField[3] == palyer and not playField[6]):
                setPosition = 6
            elif (not playField[1] and playField[4] == palyer and playField[7] == palyer):
                setPosition = 1
            elif (playField[1] == palyer and not playField[4] and playField[7] == palyer):
                setPosition = 4
            elif (playField[1] == palyer and playField[4] == palyer and not playField[7]):
                setPosition = 7
            elif (not playField[2] and playField[5] == palyer and playField == palyer):
                setPosition = 2
            elif (playField[2] == palyer and not playField[5] and playField[8] == palyer):
               setPosition = 5
            elif (playField[2] == palyer and playField[5] == palyer and not playField[8]):
                setPosition = 8
            elif (playField[0] == palyer and playField[4] == palyer and not playField[8]):
                setPosition = 8
            elif (playField[0] == palyer and not playField[4] and playField[8] == palyer):
                setPosition = 4
            elif (not playField[0] and playField[4] == palyer and playField[8] == palyer):
                setPosition = 0
            elif (not playField[2] and playField[4] == palyer and playField[6] == palyer):
                setPosition = 2
            elif (playField[2] == palyer and not playField[4] and playField[6] == palyer):
                setPosition = 4
            elif (playField[2] == palyer and playField[4] == palyer and not playField[6]):
                setPosition = 6

    if (not playField[4] and setPosition == -1 and random.randint(0,10) <= dificulty):
       setPosition = 4

    if (setPosition == -1):
        postion = random.randint(0,8)
        while(playField[postion]):
            postion = random.randint(0,8)
        setPosition = postion
     
    if (playerSymbol == 'x'):  
        playField[setPosition] = 'o'
    else: 
        playField[setPosition] = 'x'
    updateField()
    
def checkWinner():
    global winnsO, winnsX, draws, currentPlayer, playerSymbol
    
    winner = ''
    #boxBorederSize = int(round(thumby.DISPLAY_H/3))
    #boxCenter = int(round((thumby.DISPLAY_W-thumby.DISPLAY_H)/2))

    for palyer in ['x','o']:
        if (palyer == playField[0] and palyer == playField[1] and palyer == playField[2]):
            #thumby.display.drawLine(boxCenter, boxBorederSize, boxCenter, boxBorederSize)
            winner = palyer
        elif (palyer == playField[3] and palyer == playField[4] and palyer == playField[5]):
            #thumby.display.drawLine(boxCenter, boxBorederSize+boxBorederSize, boxCenter, boxBorederSize+boxBorederSize)
            winner = palyer
        elif (palyer == playField[6] and palyer == playField[7] and palyer == playField[8]):
            #thumby.display.drawLine(boxCenter, boxBorederSize+boxBorederSize*2, boxCenter, boxBorederSize+boxBorederSize*2)
            winner = palyer
        elif (palyer == playField[0] and palyer == playField[3] and palyer == playField[6]):
            #thumby.display.drawLine(lineStartX, lineStartY, lineStartX, lineStartY)
            winner = palyer
        elif (palyer == playField[1] and palyer == playField[4] and palyer == playField[7]):
            #thumby.display.drawLine(lineStartX+boxBorederSize, lineStartY, lineStartX+boxBorederSize, lineStartY)
            winner = palyer
        elif (palyer == playField[2] and palyer == playField[5] and palyer == playField[8]):
            #thumby.display.drawLine(lineStartX+boxBorederSize*2, lineStartY, lineStartX+boxBorederSize*2, lineStartY)
            winner = palyer
        elif (palyer == playField[0] and palyer == playField[4] and palyer == playField[8]):
            #thumby.display.drawLine(lineEndX, lineEndY, lineStartX, lineStartY)
            winner = palyer
        elif (palyer == playField[2] and palyer == playField[4] and palyer == playField[6]):
            #thumby.display.drawLine(lineStartX, lineStartX, lineEndX, lineEndY)
            winner = palyer
        if (winner == 'x'):
            winnsX = winnsX + 1
            currentPlayer = 'o'
            if (playerSymbol == 'x'):
                thumby.display.fillRect(6, 10, 60, 10, 0)
                thumby.display.drawText("Winner!", 10, 11, 1)
            else:
                thumby.display.fillRect(6, 10, 60, 10, 0)
                thumby.display.drawText("Loser!", 12, 11, 1)
            thumby.display.update()
            return True
        elif (winner == 'o'):
            winnsO = winnsO + 1
            currentPlayer = 'x'
            if (playerSymbol == 'o'):
                thumby.display.fillRect(6, 10, 60, 10, 0)
                thumby.display.drawText("Winner!", 10, 11, 1)
            else:
                thumby.display.fillRect(6, 10, 60, 10, 0)
                thumby.display.drawText("Loser!", 10, 11, 1)
            thumby.display.update()
            return True
    if (playField[0] and playField[1] and playField[2] and
    playField[3] and playField[4] and playField[5] and
    playField[6] and playField[7] and playField[8]):
        currentPlayer = random.choice(['o','x'])
        draws = draws + 1
        thumby.display.fillRect(6, 10, 60, 10, 0)
        thumby.display.drawText("Draw!", 14, 10, 1)
        thumby.display.update()
        return True
    return False
    
  
newGame()
while(True):
    if (currentPlayer != playerSymbol):
        computerMove()
    else:
        playerMove()
    if (checkWinner()):
        break
machine.reset()