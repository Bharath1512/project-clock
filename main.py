import time
import turtle

def printWelcomeMessages():
  print("Welcome to Alarm Clock\n")
  print("This is going to be the best alarm clock ever!!!")
  askUser ()

#First step: ask the user how many minutes and seconds they want to sleep for
def askUser():
  minutes = int(input("How many minutes do you want to sleep for?\n"))
  seconds = int(input("How many seconds do you want to sleep for?\n"))
  alarm = input("What would you like me to say to wake you up?\n")
  calculateTime(minutes,seconds,alarm)


#calculate time
def calculateTime (minutes,seconds,alarm):
  totalTime = (minutes*60) + seconds 
  print("OK, you want to sleep for %s seconds.\n" % (totalTime))
  print("Here we go...\n")

#counting time
  for i in range(1, totalTime+1):
   print("zzzzzzzz.......you have been asleep for %s seconds..." % (i))
  time.sleep(1)
  
  wakeUpUser(alarm)

#wake up user
def wakeUpUser(alarm):
  print("%s, TIME TO GET UP!!!!\n" % (alarm))
  print("If you don't wake up, turtle will jump on you!!!!")
  drawTurtle()
  
  
#draw turtle 
def drawTurtle (): 
  turtle.shape("turtle")
  turtle.color("green")
  turtle.speed(10)
  turtle.width(5)
  b = turtle.Screen()
  b.bgcolor("red")

  for j in range(5):
    turtle.forward(50)
    turtle.right(144)
  
  for k in range(40):
    turtle.forward(k*10)
    turtle.right(144)
    
printWelcomeMessages()
  
