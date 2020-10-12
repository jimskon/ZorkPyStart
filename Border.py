import xml.etree.ElementTree as ET


class Border:
  def __init__(self,node):
    '''
    Load a border.  A border has a direction, a name of the room
    '''
    self.direction=node.find("direction").text
    self.name=node.find("name").text
