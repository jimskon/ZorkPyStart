from Game import Game

world=Game("game.xml")
print(world.start())
while True:
    command=input(">>>")
    print(world.processCommand(command))
