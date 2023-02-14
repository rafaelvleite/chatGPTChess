# -*- coding: utf-8 -*-
import chess     # pip install chess
import pyperclip # pip install pyperclip

# Method to pass the board and get moves played and legal moves to pass to chatGPT
def getChatGPTText(board):
    ply = 0
    moveNumber = 1
    playedMovesList = []
    for playedMove in board.move_stack:
        if ply%2 == 0:
            playedMovesList.append(str(moveNumber) + "." + playedMove.uci())
            moveNumber += 1
        else:
            playedMovesList.append(" " + playedMove.uci() + " ")
        ply += 1

    legalMovesList = []
    for move in board.legal_moves:
        legalMovesList.append(move.uci())

    stringToPrint = "The following moves have been played: " + ''.join(playedMovesList) + \
        " and now it is your turn. You have to choose between one of the legal moves below: \n" +  \
            '\n'.join(legalMovesList)
    
    stringToPrint += "\nWhick move do you choose?"
    return stringToPrint

# Starts a new game
board = chess.Board()

# board.pop() #if you need to undo a move

# Make a move
board.push_san("e4")

# Call the method and send do Clipboard
pyperclip.copy(getChatGPTText(board))


