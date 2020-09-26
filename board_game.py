import random

class Board:
  def __init__(self):
    self.grid = self.getRandBoard()
    self.width = 6
    self.height = 6
    self.numplayers = 0
    self.killedplayers = 0

  def __str__(self):
    return('\n'.join([' '.join(['{:4}'.format(str(self.grid[j][i])) for i in range(self.width)]) for j in range (self.height)]))

  def getRandBoard(self):
    numBoards = 4

    board1 = [[0, 0, 0, 0, 0, 0],
              [0, "X", 0, 0, 0, 0],
              [0, "X", 0, 0, "X", 0],
              [0, "X", 0, 0, "X", 0],
              [0, 0, 0, 0, "X", 0],
              [0, 0, 0, 0, 0, 0]]
    
    board2 = [[0, 0, "X", 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, "X"],
              ["X", 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, "X", 0, 0]]
    
    board3 = [["X", 0, 0, 0, 0, "X"],
              [0, 0, 0, 0, 0, 0],
              [0, 0, "X", "X", 0, 0],
              [0, 0, "X", "X", 0, 0],
              [0, 0, 0, 0, 0, 0],
              ["X", 0, 0, 0, 0, "X"]]
    
    board4 = [[0, 0, 0, 0, 0, 0],
              [0, "X", "X", 0, 0, 0],
              [0, "X", 0, 0, 0, 0],
              [0, 0, 0, 0, "X", 0],
              [0, 0, 0, "X", "X", 0],
              [0, 0, 0, 0, 0, 0]]

    boardList = [board1, board2, board3, board4]
    num = random.randint(0, numBoards-1)
    return (boardList[num])

  def generate(self):
    placed = False
    while (not placed):
      x = random.randint(0, self.width-1)
      y = random.randint(0, self.height-1)
      if (self.grid[y][x] == 0):
        self.grid[y][x] = "F"
        placed = True
        print(f"flag placed at {x},{y}")
      print(placed)

  def placePlayer(self, player):
    placed = False
    while (not placed):
      x = random.randint(0, self.width-1)
      y = random.randint(0, self.height-1)
      if (self.grid[y][x] == 0):
        self.grid[y][x] = player
        placed = True
        print(f"{str(player)} placed at {x},{y}")
        player.set_coord(x,y)
        self.numplayers += 1
      print(placed)
  #direction is string

  def moveNorth(self, player):
      print("move", player)
      x,y = player.coord
      if y - 1 >= 0:
        if self.grid[y-1][x] == 0:
          self.grid[y-1][x] = player
          self.grid[y][x] = 0
          player.set_coord(x,y-1)
        elif self.grid[y-1][x] == "F":
          print("TODO: end game")
        else:
          print("TODO: play bump sound for client")
      else:
        print("TODO: play bump sound for client")
        
  def moveSouth(self, player):
      print("move", player)
      x,y = player.coord
      if y + 1 <= 5: 
        if self.grid[y+1][x] == 0:
          self.grid[y+1][x] = player
          self.grid[y][x] = 0
          player.set_coord(x,y+1)
        elif self.grid[y+1][x] == "F":
          print("TODO: end game")
        else:
          print("TODO: play bump sound for client")
      else:
        print("TODO: play bump sound for client")

  def moveWest(self, player):
      print("move", player)
      x,y = player.coord
      if x - 1 >= 0: 
        if self.grid[y][x-1] == 0:
          self.grid[y][x-1] = player
          self.grid[y][x] = 0
          player.set_coord(x-1,y)
        elif self.grid[y][x-1] == "F":
          print("TODO: end game")
        else:
          print("TODO: play bump sound for client")
      else:
        print("TODO: play bump sound for client")  

  def moveEast(self, player):
    print("move", player)
    x,y = player.coord
    if x + 1 <= 5: 
      if self.grid[y][x+1] == 0:
        self.grid[y][x+1] = player
        self.grid[y][x] = 0
        player.set_coord(x+1,y)
      elif self.grid[y][x+1] == "F":
        print("TODO: end game")
      else:
        print("TODO: play bump sound for client")
    else:
      print("TODO: play bump sound for client")    

  def fireNorth(self, player): 
    x,y = player.coord
    if y-1 >= 0:
      print("TODO: play fire sound")
      for ycoord in range(y-1, -1, -1):
        print(x, ycoord)
        if self.grid[ycoord][x] == "X" or self.grid[ycoord][x] == "F":
          break
        elif self.grid[ycoord][x] == "Player":
          print(self.grid[ycoord][x])
          print("TODO: killed players, give point to killer")
          self.killedplayers += 1
          self.grid[ycoord][x] = 0 
    
  def fireSouth(self, player):
    x,y = player.coord
    if y+1 <= 5:
      print("TODO: play fire sound")
      for ycoord in range(y+1, 6):
        if self.grid[ycoord][x] == "X" or self.grid[ycoord][x] == "F":
          break
        elif self.grid[ycoord][x] == "Player":
          print("TODO: killed players, give point to killer")
          self.killedplayers += 1
          self.grid[ycoord][x] = 0 
  

  def fireWest(self, player): 
    x,y = player.coord
    if x-1 >= 0:
      print("TODO: play fire sound")
      for xcoord in range(x-1, -1, -1):
        if self.grid[y][xcoord] == "X" or self.grid[y][xcoord] == "F":
          break
        elif self.grid[y][xcoord] == "Player":
          print("TODO: killed players, give point to killer")
          self.killedplayers += 1
          self.grid[y][xcoord] = 0 
    
  def fireEast(self, player):
    x,y = player.coord
    if x+1 <= 5:
      print("TODO: play fire sound")
      for xcoord in range(x+1, 6):
        if self.grid[y][xcoord] == "X" or self.grid[y][xcoord] == "F":
          break
        elif self.grid[y][xcoord] == "Player":
          print("TODO: killed players, give point to killer")
          self.killedplayers += 1
          self.grid[y][xcoord] = 0 


  def echoNorth(self, player): 
    x,y = player.coord
    soundPlayed = False
    if y-1 >= 0:
      for ycoord in range(y-1, -1, -1):
        #print(x, ycoord)
        if self.grid[ycoord][x] == "X":
          soundPlayed = True
          print("play obstacle echo sound")
          break
        elif self.grid[ycoord][x] == "F":
          soundPlayed = True
          print("play flag echo sound")
          break
        elif self.grid[ycoord][x] == "Player":
          soundPlayed = True
          print("play player echo sound")
          break
    if not soundPlayed:
      print("play empty row echo sound")


  def echoSouth(self, player): 
    x,y = player.coord
    soundPlayed = False
    if y+1 <= 5:
      for ycoord in range(y+1, 6, -1):
        #print(x, ycoord)
        if self.grid[ycoord][x] == "X":
          soundPlayed = True
          print("play obstacle echo sound")
          break
        elif self.grid[ycoord][x] == "F":
          soundPlayed = True
          print("play flag echo sound")
          break
        elif self.grid[ycoord][x] == "Player":
          soundPlayed = True
          print("play player echo sound")
          break
    if not soundPlayed:
      print("play empty row echo sound")


  def echoWest(self, player): 
      x,y = player.coord
      soundPlayed = False
      if x-1 >= 0:
        for xcoord in range(x-1, -1, -1):
          #print(x, ycoord)
          if self.grid[y][xcoord] == "X":
            soundPlayed = True
            print("play obstacle echo sound")
            break
          elif self.grid[y][xcoord] == "F":
            soundPlayed = True
            print("play flag echo sound")
            break
          elif self.grid[y][xcoord] == "Player":
            soundPlayed = True
            print("play player echo sound")
            break
      if not soundPlayed:
        print("play empty row echo sound")

  def echoEast(self, player): 
    x,y = player.coord
    soundPlayed = False
    if y+1 <= 5:
      for xcoord in range(x+1, 6, -1):
        #print(x, ycoord)
        if self.grid[y][xcoord] == "X":
          soundPlayed = True
          print("play obstacle echo sound")
          break
        elif self.grid[y][xcoord] == "F":
          soundPlayed = True
          print("play flag echo sound")
          break
        elif self.grid[y][xcoord] == "Player":
          soundPlayed = True
          print("play player echo sound")
          break
    if not soundPlayed:
      print("play empty row echo sound")
  
class Player:
  def __init__(self, playernum):
    self.playerNumber = playernum
    self.score = 0
    self.isDead = False
    self.coord = None

  def set_coord(self, x,y):
    self.coord = (x,y)
  def __str__(self):
    return "P{}".format(self.playerNumber)
      
  def __eq__(self, other):
      return other == "Player"






if __name__ == "__main__":
  test_player = Player(0)
  test_player2 = Player(1)
  board = Board()
  print(board)
  board.generate()
  board.placePlayer(test_player)
  board.placePlayer(test_player2)
  print(board)
  print(test_player.coord)
  #board.moveWest(test_player.coord[0], test_player.coord[1])
  board.moveNorth(test_player)
  print(test_player.coord)
  board.echoWest(test_player)
  print(board)
  

  print(test_player == "Player")