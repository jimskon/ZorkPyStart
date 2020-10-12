# A rogram to test the nameserver program
import os
from os import path
import sys
fifoname="skonpygame"  # Unique name for fifos

commandFifoFile = "/home/fifo/"+fifoname+"_commandFifo"
resultFifoFile = "/home/fifo/"+fifoname+"_resultFifo"

#Create Fifos if they don't exist
if not path.exists(commandFifoFile):
        os.mkfifo(commandFifoFile)
        os.chmod(commandFifoFile, 0o777)
if not path.exists(resultFifoFile):
        os.mkfifo(resultFifoFile)
        os.chmod(resultFifoFile, 0o777)

id = input("Enter a unique game ID: ")
#start a new Game
commandFifo=open(commandFifoFile, "w")
resultFifo=open(resultFifoFile, "r")
commandFifo.write(id+"$Start")
commandFifo.close()

for line in resultFifo:
    print(line)

while True:
    com=input(">>> ")
    commandFifo=open(commandFifoFile, "w")
    resultFifo=open(resultFifoFile, "r")

    commandFifo.write(id+"$"+com)
    commandFifo.close()
    for line in resultFifo:
        print(line,end="")

    resultFifo.close()

print("Done!")

from Game import Game
