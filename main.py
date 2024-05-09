import random
ladderCoordinates = [-154, -200],[30, -200],[-200,-155],[]
'''
def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name
'''
import turtle
import time
import random as rd

def playerChoose ():
  t = input("Player turn. Please select a number between 1 and 4 : ")
  if t == "1":
    return d1
  elif t == "2":
    return d2
  elif t == "3":
    return n
  elif t == "4":
    return m

def computerChoose ():
  t = input("Players turn. Please select a number between 1 and 4 : ")
  if t == "1":
    return d1
  elif t == "2":
    return d2
  elif t == "3":
    return n
  elif t == "4":
    return m


#For computers turn  
'''
def getRandom ():
 r = rd.randint(2,12)
 return r

computerDice = getRandom ()
print(computerDice)
'''

def makeMove(steps):
  global x
  global y
  global cell, row

  
  print("Initial : ",x,y)
  i = 0
  while(i < steps):
    row = cell//10 # we use // to avoid getting decimal point
    if(row == 0 or row == 2 or row == 4 or row == 6 or row ==8):
      cell += 1
      x += 46
      
      tr.goto(x,y)
      time.sleep(1)
      print("a : ",x,y, "cell : ",cell, "row : ", row)
      i += 1
    
    if (row == 0 or row == 2 or row == 4 or row == 6 or row ==8) and (cell == 10 or cell == 30 or cell == 50 or cell == 70 or cell == 90):
      cell += 1
      y += 45
      
      tr.goto(x,y)
      time.sleep(1)
      print("b : ",x,y, "cell : ",cell, "row : ", row)
      i += 1

    if ((row == 1 or row == 3 or row == 5 or row == 7 or row == 9) and cell != 20):
      cell += 1
      x -= 46
      
      tr.goto(x,y)
      time.sleep(1)
      print("c : ",x,y, "cell : ",cell, "row : ", row)
      i += 1

    if ((row == 1 or row == 3 or row == 5 or row == 7 or row == 9) and (cell == 20 or cell == 40 or cell == 60 or cell == 80)):
      cell += 1
      y += 45
      
      tr.goto(x,y)
      time.sleep(2)
      print("up: ",x,y, "cell : ",cell, "row : ", row)
      i += 1


  if (x, y) == (-154, -200):
    tr.goto(-108,-110)
    row = 2
    cell = 23
    (x, y) = (-108,-110)
    
  elif (x, y) == (30, -200):
    tr.goto(-16,-20)
    row = 4
    cell = 45
    (x, y) = (-16,-20)

  elif (x, y) == (-200, -155):
    tr.goto(-154, 70)
    row = 5
    cell = 59
    (x, y) = (-154, 70)

  elif (x, y) == (168,25):
    tr.goto(168,115)
    row = 7
    cell = 72
    (x, y) = (168,115)

  elif (x, y) == (-62,-25):
    tr.goto(-16,205)
    row = 9
    cell = 96
    (x, y) = (-16,205)

  if (x, y) == (-108,-20):
    tr.goto(-62,-155)
    row = 1
    cell = 17
    (x, y) = (-62,-155)

  elif (x, y) == (214,-20):
    tr.goto(-16,-200)
    row = 0
    cell = 5
    (x, y) = (-16, -200)
  
  elif (x, y) == (-16,25):
    tr.goto(122,-200)
    row = 0
    cell = 8
    (x, y) = (122,-200)

  elif (x, y) == (122,115):
    tr.goto(30,-155)
    row = 1
    cell = 15
    (x, y) = (-16,205)

  elif (x, y) == (-62,160):
    tr.goto(-108-70)
    row = 6
    cell = 63
    (x, y) = (-108,70)

  elif (x, y) == (76,160):
    tr.goto(168,-20)
    row = 4
    cell = 949
    (x, y) = (168,20)

  elif (x, y) == (-108,205):
    tr.goto(-200,-65)
    row = 4
    cell = 41
    (x, y) = (-16,205)

def playersTurn():
 tr.clear()
 player = playerChoose()
 print("Player has chosen : ",player)
 makeMove(player)
 tr.dot(30)
 time.sleep(1)  

def computerTurn():
   cm.clear()
   computer = computerChoose()
   print("Computer has chosen : ",computer)
   makeMove(computer)
   cm.dot(30,"red")
   time.sleep(1)

#def computerTurn():


#Above section is the function area
############################################
#Below is the main program
print("Welcome, to play the game you should which option you choose and press Enter!!!")

tr = turtle.Turtle()
tr.up()#to remove the line

wn = turtle.Screen()
wn.setup(width=450,height=450)
wn.bgpic("SnakeAndLadders.gif")

d1 = random.randint(1,6)
d2 = random.randint(1,6)
n = d1 + d2
m = d1 - d2
if m < 0:
  m = m*-1

y = -200
x = -200


cell = 1
row = 0
tr.goto(x,y) #get the turtle to the default place
tr.begin_fill()
tr.color('blue')
while 1:
  
  print()
  print("Option 1 is (First dice)  :",d1)
  print("Option 2 is  (Second dice):",d2)
  print("Option 3 is  (Total):",n)
  print("Option 4 is  (Difference):",m)
  playersTurn()
  
  

  d1 = random.randint(1,6)
  d2 = random.randint(1,6)
  n = d1 + d2
  m = d1 - d2
  if m < 0:
    m = m*-1


  tr.dot(30)
  time.sleep(1)


  tr.end_fill()






'''
cm = turtle.Turtle
cm.up()


y = -200
x = -200
cell = 1
row = 0
cm.goto(x,y) #get the turtle to the default place
cm.begin_fill()



cm.dot(30)3

time.sleep(1)
cm.end_fill()

wn.mainloop()
'''
'''
if tr
'''

