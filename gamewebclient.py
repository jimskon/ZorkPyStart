#!/usr/bin/env python3
# nameclient.py - Program to receive web name lookup command
# This CGI program used the python nameserver to lookup names
# And retuen result to web page
# James Skon, 2019
#!/usr/bin/env python
import os
from os import path
import sys

import cgi;
import cgitb
cgitb.enable()

fifoname="skonpygame"  # Unique name for fifos
commandFifoFile = "/home/fifo/"+fifoname+"_commandFifo"
resultFifoFile = "/home/fifo/"+fifoname+"_resultFifo"
def print_header():
    print ("""Content-type: text/html\n""")

def callGameServer(id,command):
    #Create Fifos if they don't exist
    if not path.exists(commandFifoFile):
        os.mkfifo(commandFifoFile)
        os.chmod(commandFifoFile, 0o777)
    if not path.exists(resultFifoFile):
        os.mkfifo(resultFifoFile)
        os.chmod(resultFifoFile, 0o777)

    commandFifo=open(commandFifoFile, "w")
    resultFifo=open(resultFifoFile, "r")

    commandFifo.write(id+"$"+command)
    commandFifo.close()

    result=""
    for line in resultFifo:
        result+=line
    resultFifo.close()
    return(result)

def main():
    print_header()
    form = cgi.FieldStorage()
    if (form.getvalue("command") and form.getvalue("id")):
        id=form.getvalue("id").upper()
        command=form.getvalue("command").replace("+", " ")
        result=callGameServer(id,command)
        result=result.replace("\n", "<br/>")
        # Send back to webpage
        print(result)
    else:
        print("Error in submission")

main()
