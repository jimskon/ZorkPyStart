
import xml.etree.ElementTree as ET

global rooms
global inventory
global location


class World:
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

class Border:
  def __init__(self,node):
    '''
    Load a border.  A border has a direction, a name of the room
    '''
    self.direction=node.find("direction").text
    self.name=node.find("name").text

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
      self.items.append(i.text)
    # get borders
    self.borders=[]
    for i in node.findall("./border"):
      b=Border(i)
      self.borders.append(b)    

  def enter(self):
    '''
    Enter a room
    '''
    self.describe()
    if self.action == "exit":
      print("The game is over!")
      exit()

  def describe(self):
    ''' 
    Describe the room, and list the contents
    '''
    print(self.name)
    print(self.description)
    # Should only do the following if there is light!
    print("You see:")
    if len(self.items)>0:
      for i in self.items:
        print(i)
    else:
      print("Nothing is in the room")

  def checkBorder(self,command):
    '''
    Look around the boarders.  if the command given matches
    a border, return that name of that room 
    '''
    for b in self.borders:
      print(b.direction)
      if b.direction==command:
        return b.name
    return None

  def lookAround(self):
    '''
     Look around and give the directions and ajacent rooms
    '''
    for b in self.borders:
      print("If you go "+b.direction+" you will go to "+b.name+".")

def setupWorld():
  '''
  Load the world and return the world object
  '''
  tree = ET.parse('game.xml')
  root = tree.getroot()
  world=World(root)
  return world

def processCommand(world):
  c=input(">").lower().split( )
  nextRoom=None
  # Look around
  if c[0] == "look":
    world.rooms[world.location].lookAround()
  # Go someplace
  elif c[0] == "go":
    if len(c)<2:
      print("Go where?")
    else:
      nextRoom=world.rooms[world.location].checkBorder(c[1])
      if (nextRoom!=None and nextRoom != world.location):
        world.location=nextRoom
      else:
        print("Can't go "+c[1])
  elif c[0] == "inventory" or c[0] == "i":
    print("Inventory ot yet implemented")
  elif c[0] == "take":
    print("Take not yet implemented")
  else:
    print("Not a command.")  
    print("Commands: look go inventory take")

def simpleGame(world):
  while True:
    world.rooms[world.location].enter()
    processCommand(world)

world=setupWorld()
simpleGame(world)