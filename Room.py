import xml.etree.ElementTree as ET
from Border import Border

class Room:
  def __init__(self, node):
    '''
    Load a room object from the XML
    A room contains lists of items and borders
    '''
    self.name=node.find("name").text
    if node.find("action")!=None:
      self.action=node.find("action").text
    else:
      self.action=None
    self.description=node.find("description").text
    self.items=[]
    # Get items list
    for i in node.findall("./item"):
      self.items.append(i.text+"\n")
    # get borders
    self.borders=[]
    for i in node.findall("./border"):
      b=Border(i)
      self.borders.append(b)

  def enter(self):
    '''
    Enter a room
    '''
    message=self.describe()
    if self.action == "exit":
      message+="The game is over!\n"
    return message

  def describe(self):
    '''
    Describe the room, and list the contents
    '''
    message=self.name+"\n"
    message+=self.description+"\n"
    # Should only do the following if there is light!
    message+="You see:"+"\n"
    if len(self.items)>0:
      for i in self.items:
        message+=i+" "
    else:
      message+="Nothing is in the room"+"\n"
    return message

  def checkBorder(self,command):
    '''
    Look around the boarders.  if the command given matches
    a border, return that name of that room
    '''
    for b in self.borders:
      if b.direction==command:
        return b.name
    return None

  def lookAround(self):
    '''
     Look around and give the directions and ajacent rooms
    '''
    message=""
    for b in self.borders:
      message+="If you go "+b.direction+" you will go to "+b.name+".\n"
    return message
