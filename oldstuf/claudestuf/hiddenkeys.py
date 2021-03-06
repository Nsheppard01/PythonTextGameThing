# this is a prototype game designed to help me figure out how to use inventory items as a part of an environment

# map
#you are in a room. There is no navigation.
# there are 4 keys hidden in the room, and there are 4 locked boxes in the room. 
# The goal of the game is to open the locks, collect the locked away items, and use those items to escape the room.

# Keys
# There are 4 keys in the room. they are each colored differently so that they can easily be told apart.
# 1. key is hidden in a vase of flowers. This key is green. 
# 2. key is blue. it is hidden under a squeeky floorboard. To get this key the player must use another item,
# a crowbar, to pry up the floorboard. 
# 3. key is red. This key is hidden behind a picture frame. 
# 4. key is purple. This key is inside the oven.

# Boxes
# 1. Green key opens up a locked fishtank, which contains a magic wand
# 2. Blue key opens up a locked microwave, which contains a vial of newt's blood
# 3. Red key opens up a safe, which contains purifying incense. The safe is in the cupboards under the sink.
# 4. Purple key opens a locket, which contains a message: the magic word "Evanesco"

# by lighting the incense (using a lit candle in the room already), drinking the newt's blood, holding the wand, and
# reciting the magic word on the message, the player can vanish a wall of the room and escape.

def intro():
  print "You are in a room with no exit, your goal is to escape."
  print "It looks like you are in a sort of kitchen."
  print "There is counterspace and kitchen sink, and an oven."
  print "On the wall above the sink is a portrait of an ugly baby."
  print "Over the oven is a wall mounted microwave."
  print "On the counter are salt and pepper shakers, a locket,"
  print "a fish tank, and a ceramic vase with tulips in it."
  print "The counter sits over cupboards and storage space."
  print "The floor is old fashioned wood planks, you notice"
  print "that one floorboard is squeeky."
  print "In a corner you notice a toolbox."
  print
  print "How will you excape?"
  
def look():
  print "There is counterspace and kitchen sink, and an oven."
  print "On the wall above the sink is a portrait of an ugly baby."
  print "Over the oven is a wall mounted microwave."
  print "On the counter are salt and pepper shakers, a locket,"
  print "a fish tank, and a ceramic vase with tulips in it."
  print "The counter sits over drawers and storage space."
  print "The floor is old fashioned wood planks, you notice"
  print "that one floorboard is squeeky."
  print "In a corner you notice a toolbox."
  
game = True
prompt = ">"

class Crowbar(): # the crowbar
  def __init__(self, floorboard):
    self.floorboard = floorboard
  def use(self.floorboard):
    if self.floorboard == True:
      # description of player prying up floorboard, showing them the blue key
    else:
      # error message, e.g. you can't use the crowbar that way
      
  
class Green():  # the green key
  def __init__(self, fishtank):
    self.fishtank = fishtank
  def use(self.fishtank):
    if self.fishtank == True:   # if the key is used on the fishtank
      # fish tank opens, allowing player to retrieve magic wand
    else:
      # error message, e.g. you can't use the green key that way.
      

      
class Blue():
  def __init__(self, microwave):
    self.microwave = microwave
  def use(self.microwave):
    if self.microwave == True:
      # microwave opens, allowing player to retrieve the vial of newt's blood
    else:
      # error message, e.g. you can't use the blue key that way.
      
class Red():
  def __init__(self, safe):
    self.safe = safe
  def use(self.safe):
    if self.safe == True:
      # use red key to open safe, allowing player to retrieve purifying incense
    else:
      # error message, e.g. you can't use the red key that way.
      
class Purple():
  def __init__(self, locket):
    self.locket = locket
  def use(self.locket):
    if self.locket == True:
      # use purple key to open locket
    else:
      # error message, e.g. you can't use the Purple key that way.

while game == True:
  intro()
  next = raw_input(prompt)
  break
  
