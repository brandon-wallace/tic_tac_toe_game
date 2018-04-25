#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


A TIC TAC TOE game.



"""
 

import os
import sys
import time
 

title = "LET'S PLAY...."
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
selection = [1,2,3,4,5,6,7,8,9]
blank = '                          '
top = '       A       B       C     '
div = '    -----------------------'
space = '           |       |       '
marker1 = None
marker2 = None
winner = False
 
def game_intro():
    '''Display a splash screen.'''
    os.system("clear")
    print " "
    for i in title:
        time.sleep(0.1)
        sys.stdout.write(i)
        sys.stdout.flush()
    time.sleep(0.5)
    print " "
    print """
    ████████╗██╗ ██████╗      
    ╚══██╔══╝██║██╔════╝      
       ██║   ██║██║           
       ██║   ██║██║           
       ██║   ██║╚██████╗      
       ╚═╝   ╚═╝ ╚═════╝  
       """
    time.sleep(0.7)
    print """
    ████████╗ █████╗  ██████╗ 
    ╚══██╔══╝██╔══██╗██╔════╝ 
       ██║   ███████║██║      
       ██║   ██╔══██║██║      
       ██║   ██║  ██║╚██████╗ 
       ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
       """
    time.sleep(0.9)
    print """
    ████████╗ ██████╗ ███████╗
    ╚══██╔══╝██╔═══██╗██╔════╝
       ██║   ██║   ██║█████╗  
       ██║   ██║   ██║██╔══╝  
       ██║   ╚██████╔╝███████╗
       ╚═╝    ╚═════╝ ╚══════╝
       """
    raw_input("Press Enter to continue. ")
    
game_intro()
 
def display_board(b):
    '''Display the tic tac toe board.'''
    os.system("clear")
    print blank
    print top
    print space 
    print " 1)    {a}   |   {b}   |   {c}   ".format(a=b[0],b=b[1],c=b[2])
    print space
    print div 
    print space
    print " 2)    {d}   |   {e}   |   {f}   ".format(d=b[3],e=b[4],f=b[5])
    print space
    print div 
    print space
    print " 3)    {g}   |   {h}   |   {i}   ".format(g=b[6],h=b[7],i=b[8])
    print space
    print " "
    print """
    1. 1a
    2. 1b
    3. 1c
    4. 2a
    5. 2b
    6. 2c
    7. 3a
    8. 3b
    9. 3c
    """
    return board
 
def player_input(m1, m2):
    '''Get the player input.'''
    global marker1 
    global marker2
    os.system("clear")
    answer = ""
    while answer != 'x' or answer != 'o':
        answer = raw_input("Player1 select 'x' or 'o' to start game: ")
        if answer == 'x':
            marker1 = 'X'
            marker2 = 'O'
            return marker1, marker2
        elif answer == 'o':
            marker1 = 'O'
            marker2 = 'X'
            return marker1, marker2
        else:
            os.system("clear")
            print("I do not understand your answer.")
            time.sleep(1)
            player_input(marker1, marker2)
            
player_input(marker1, marker2)
 
def calculate_winner(b):
    '''Check to see if there is a winner.'''
    global winner
    if b[0] == b[1] == b[2] == marker1:
        winner = True; print "PLAYER1 WINS!"
    elif b[3] == b[4] == b[5] == marker1:
        winner = True; print "PLAYER1 WINS!"
    elif b[6] == b[7] == b[8] == marker1:
        winner = True; print "PLAYER1 WINS!"
    elif b[0] == b[3] == b[6] == marker1:
        winner = True; print "PLAYER1 WINS!"
    elif b[1] == b[4] == b[7] == marker1:
        winner = True; print "PLAYER1 WINS!"
    elif b[2] == b[5] == b[8] == marker1:
        winner = True; print "PLAYER1 WINS!"
    elif b[2] == b[4] == b[8] == marker1:
        winner = True; print "PLAYER1 WINS!"
    elif b[0] == b[4] == b[8] == marker1:
        winner = True; print "PLAYER1 WINS!"
    elif b[0] == b[1] == b[2] == marker2:
        winner = True; print "PLAYER2 WINS!"
    elif b[3] == b[4] == b[5] == marker2:
        winner = True; print "PLAYER2 WINS!"
    elif b[6] == b[7] == b[8] == marker2:
        winner = True; print "PLAYER2 WINS!"
    elif b[0] == b[3] == b[6] == marker1:
        winner = True; print "PLAYER2 WINS!"
    elif b[1] == b[4] == b[7] == marker2:
        winner = True; print "PLAYER1 WINS!"
    elif b[2] == b[5] == b[8] == marker2:
        winner = True; print "PLAYER2 WINS!"
    elif b[2] == b[4] == b[8] == marker2:
        winner = True; print "PLAYER2 WINS!"
    elif b[0] == b[4] == b[8] == marker2:
        winner = True; print "PLAYER2 WINS!"
    else:
        pass
    return winner
    
def select_position(m1, m2, menu, board):
    '''Let the game players select squares on grid.'''
    global winner
    display_board(board)
    while winner == False:
        try:
            pos = int(raw_input("Player1 Select a number 1-9: "))
            if pos in menu:
                board[(pos -1)] = marker1
                menu.remove(pos)
                display_board(board)
                calculate_winner(board)
                if winner == True:
                    break
            else:
                print "Please select another number."
                if winner == True:
                    break
            pos = int(raw_input("Player2 select a number 1-9: "))
            if pos in menu:
                board[(pos -1)] = marker2
                menu.remove(pos)
                display_board(board)
                calculate_winner(board)
            else:
                print "Please select another number."
                if winner == True:
                    break
        except ValueError as e:
            print "Error: %s" % e
 
select_position(marker1, marker2, selection, board)
