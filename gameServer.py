from Game import Game

import os
from os import path
import sys

global world


def gameServer():
  fifoname="skonpygame" # unique name for fifos
  commandFifoFile = "/home/fifo/"+fifoname+"_commandFifo"
  resultFifoFile = "/home/fifo/"+fifoname+"_resultFifo"

  #Create Fifos is they don't exist
  if not path.exists(commandFifoFile):
    os.mkfifo(commandFifoFile)
    os.chmod(commandFifoFile, 0o777)
  if not path.exists(resultFifoFile):
    os.mkfifo(resultFifoFile)
    os.chmod(resultFifoFile, 0o777)

  # Main loop.  Wait for message, process it, and return result.  Then loop.
  while True:
    print("Waiting for command");
    commandFifo=open(commandFifoFile, "r")
    resultFifo=open(resultFifoFile, "w")

    line = commandFifo.read()
    print("Command Recieved: ",line)
    id,command=line.split("$")

    ## You have to figure out how to use id to manage multiple games with multiple users
    if command=="Start":
        world=Game("game.xml")
        result=world.start()
    else:
        result=world.processCommand(command)

    print("Sending:",result)

    resultFifo.write(result)

    resultFifo.close()
    commandFifo.close()


gameServer()
