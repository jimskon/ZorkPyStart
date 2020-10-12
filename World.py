import xml.etree.ElementTree as ET
from Border import Border
from Room import Room

class World:
  '''
  A class for the whole world
  '''
  def __init__(self, node):
    '''
    Load rooms into room dict indexed by room name
    '''
    self.rooms={}
    self.location=""
    self.inventory=[]
    for child in node:
      if child.tag=="room":
        r=Room(child)
        self.rooms[r.name]=r
        # The first room we find is the room where we start
        if self.location=="":
          self.location = r.name
