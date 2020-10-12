import xml.etree.ElementTree as ET
from Border import Border
from Room import Room
from World import World

class Game:
    '''
    A text advanture game class
    '''
    def __init__(self,xmlfile):
      '''
      Load the world and return the world object
      '''
      tree = ET.parse(xmlfile)
      root = tree.getroot()
      self.world=World(root)

    def start(self):
      '''
      call at start to get things going
      '''
      return(self.world.rooms[self.world.location].enter())

    def processCommand(self,command):
      c=command.lower().split( )
      nextRoom=None
      message=""
      # Look around
      if c[0] == "look":
        message+=self.world.rooms[self.world.location].lookAround()
      # Go someplace
      elif c[0] == "go":
        if len(c)<2:
          message+="Go where?\n"
        else:
          nextRoom=self.world.rooms[self.world.location].checkBorder(c[1])
          if (nextRoom!=None and nextRoom != self.world.location):
            self.world.location=nextRoom
          else:
            message+="Can't go "+c[1]+"\n"
      elif c[0] == "inventory" or c[0] == "i":
        message+="Inventory ot yet implemented\n"
      elif c[0] == "take":
        message+="Take not yet implemented\n"
      else:
        message+="Not a command.\n"
        message+="Commands: look go inventory take\n"
      message+=self.world.rooms[self.world.location].enter()+"\n"
      return message
