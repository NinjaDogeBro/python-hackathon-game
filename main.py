# Final Project
# CS 111, Hayes & Reckinger
# Name: Guillermo Ramirez III UIN: 664042145 Partner: Abdias Kpatcha Date:12/3/2023
#Here we have a game based on the 4th prompt from the WICS org, A day in a CS student's life.
#These are some of the things our game does
# 1)Our project takes into account, user choice and outputs different things based on those choices
# 2)Contains multiple for loops and around 3-4 while loops
# 3)Contains many if-statements
# 4)Contains multiple functions/function calls
# 5)Reads data from a txt file and image files
# 6)Uses multiple built-in functions including range(),print(),etc.
# 7)Contains multiple animations and uses multiple turtles
# 8)Has multiple onclicks and ontimers and onkeys


import turtle
import random
import time
########FUNCTIONS#################
todo_text = turtle.Turtle()
dogThumbsUp = turtle.Turtle()

todo = turtle.Turtle()
sparky = turtle.Turtle()
map_symbol = turtle.Turtle()
stress = turtle.Turtle()
health = turtle.Turtle()
knowledge = turtle.Turtle()
stress_text = turtle.Turtle()
health_text = turtle.Turtle()
kdg_text = turtle.Turtle()
back_btn = turtle.Turtle()
assign_ttl = turtle.Turtle()
t6 = turtle.Turtle()
t5 = turtle.Turtle()
t4 = turtle.Turtle()
scooter = turtle.Turtle()
book = turtle.Turtle()
teacher = turtle.Turtle()
food = turtle.Turtle()
gym = turtle.Turtle()
home = turtle.Turtle() 
lib_text = turtle.Turtle()
math_btn = turtle.Turtle()
cs_btn = turtle.Turtle()
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle() 
click = 0
click1 = 0
click2 = 0
count = 0
count1 = 0
count2 = 0
count3 = 0
answer = turtle.Turtle()
lib_text = turtle.Turtle()
math_text = turtle.Turtle()
answer_text = turtle.Turtle()
chick = turtle.Turtle()
subway =  turtle.Turtle()
panda = turtle.Turtle()
scooter.hideturtle()
book.hideturtle()
gym.hideturtle()
home.hideturtle()
teacher.hideturtle()
food.hideturtle()
day_text = turtle.Turtle()
sandwich = turtle.Turtle()
table = turtle.Turtle()
sandwichEat = turtle.Turtle()
sandwichNom = turtle.Turtle()
subEat = turtle.Turtle()
subNom = turtle.Turtle()
tableEat = turtle.Turtle()
tableNom = turtle.Turtle()
emoji = turtle.Turtle()
sub = turtle.Turtle()
pail = turtle.Turtle()
pailEat = turtle.Turtle()
pailNom = turtle.Turtle()
rest_text = turtle.Turtle()
rest_text.hideturtle()
day_text.hideturtle()
def school_day():
    day_text.showturtle()
    day_text.up()
    math_text.goto(-50,150)
    math_text.down()
    math_text.color("white")
    math_text.write("The school day is now over. Head home",False,"center",("Deja Vu Sans Mono",30,"bold"))
    math_text.goto(0,150)
    math_text.down()
    math_text.color("black")
    math_text.write("The school day is now over. Head home",False,"center",("Deja Vu Sans Mono",30,"bold"))
def load_rules():
    file = open("rules.txt")
    file_list = file.readlines()
    return file_list
rules_list = load_rules()
#######################################################################
def game_over():
    dogThumbsUp.hideturtle()
    todo_text.hideturtle()
    s.bgcolor("red")
    s.bgpic(None)
    text.color("white")
    text.goto(0,100)
    text.write(f"Stress:{count}",False,"center",("Deja Vu Sans Mono",30,"bold"))
    text.goto(0,0)
    text.write(f"Health:{count1}",False,"center",("Deja Vu Sans Mono",30,"bold"))
    text.goto(0,-100)
    text.write(f"Knowledge:{count2}",False,"center",("Deja Vu Sans Mono",30,"bold"))

###########################CLASS#######################################
def goClass():
    back_btn.shape("back.gif")
    back_btn.up()
    back_btn.goto(-450,-200)
    back_btn.down()
    back_btn.showturtle()
    back_btn.onclick(show_map)
    scooter.hideturtle()
    book.hideturtle()
    teacher.hideturtle()
    food.hideturtle()
    gym.hideturtle()
    home.hideturtle()
    sparky.hideturtle()
    back_btn.hideturtle()
    s.bgpic("classroom.gif")
    text.color("white")
    player.goto(-500,300)
    s.ontimer(show_map2,5000)
    text.write("New Assignment",False,"center",("Deja Vu Sans Mono",30,"bold"))
    increase_stress()
    text.clear()


######################################################################
#################################GYM###################################
armCircles = 0
def goGym():
  global armCircles
  scooter.hideturtle()
  book.hideturtle()
  teacher.hideturtle()
  food.hideturtle()
  gym.hideturtle()
  home.hideturtle()
  sparky.hideturtle()
  back_btn.hideturtle()
  s.bgpic("gym.gif")
  text.goto(0, 200)
  text.color("white")
  text.write("Get that pump in! (click on the arm)", move=False, align="center", font=("Deja Vu Sans Mono", 30, "bold"))

  turtle.addshape("armDown.gif")
  turtle.addshape("armMid.gif")
  turtle.addshape("armUp.gif")
  turtle.addshape("armUpRight.gif")
  turtle.addshape("armDownLeft.gif")
  turtle.addshape("armDownRight.gif")
  turtle.addshape("two.gif")
  turtle.addshape("three.gif")
  turtle.addshape("cat.gif")



  armDown = turtle.Turtle()
  armMid = turtle.Turtle()
  armUp = turtle.Turtle()
  armUpRight = turtle.Turtle()
  armDownLeft = turtle.Turtle()
  armDownRight = turtle.Turtle()
  two = turtle.Turtle()
  three = turtle.Turtle()
  cat = turtle.Turtle()

  armMid.hideturtle()
  armUp.hideturtle()
  armUpRight.hideturtle()
  armDownLeft.hideturtle()
  armDownRight.hideturtle()
  two.hideturtle()
  three.hideturtle()
  cat.hideturtle()

  armDown.penup()
  armMid.penup()
  armUp.penup()
  armUpRight.penup()
  armDownLeft.penup()
  armDownRight.penup()
  two.penup()
  three.penup()
  cat.penup()


  armDown.shape("armDown.gif")
  armMid.shape("armMid.gif")
  armUp.shape("armUp.gif")
  armUpRight.shape("armUpRight.gif")
  armDownLeft.shape("armDownLeft.gif")
  armDownRight.shape("armDownRight.gif")
  two.shape("two.gif")
  three.shape("three.gif")
  cat.shape("cat.gif")


  armDown.goto(0,0)
  armMid.goto(0,0)
  armUp.goto(0,0)
  armUpRight.goto(0,0)
  cat.goto(0,0)

  armDownLeft.goto(-50,-230)
  armDownRight.goto(-50,-230)
  two.goto(-200,-200)
  three.goto(-200,-200)

  def mid(x,y):
      global armCircles
      armDown.hideturtle()
      armMid.showturtle()
      armCircles += 1

  def up(x,y):
      global armCircles
      armMid.hideturtle()
      armUp.showturtle()
      armCircles += 1

  def UpRight(x,y):
      global armCircles
      armUp.hideturtle()
      armUpRight.showturtle()
      armCircles += 1
      #Write keep going
      text.penup()
      text.goto(-100, 100)
      text.color("white")
      text.write("Who told you to stop? Keep going for 2 times.", move=False, align="center", font=("Deja Vu Sans Mono", 30, "bold"))

  def DownRight(x,y):
      global armCircles
      armUpRight.hideturtle()
      armDownRight.showturtle()
      armCircles += 1

  def DownLeft(x,y):
      global armCircles
      armDownRight.hideturtle()
      armDownLeft.showturtle()
      armCircles += 1

  def DownStraight(x,y):
      global armCircles
      armDownLeft.hideturtle()
      armDown.showturtle()
      armCircles += 1


  while armCircles != 18:
      armDown.onclick(mid)
      armMid.onclick(up)
      armUp.onclick(UpRight)
      armUpRight.onclick(DownRight)
      armDownRight.onclick(DownLeft)
      armDownLeft.onclick(DownStraight)
      if armCircles == 12:
          two.showturtle()
      if armCircles == 18:
          two.hideturtle()
          three.showturtle()

  armDown.hideturtle()
  three.hideturtle()
  text.clear()
  text.goto(-100, 200)
  text.color("white")
  text.write("Good Job!", move=False, align="center", font=("Deja Vu Sans Mono", 30, "bold"))
  text.clear()
  cat.showturtle()
  back_btn.hideturtle()
  back_btn.shape("back.gif")
  back_btn.up()
  back_btn.goto(-450,-200)
  back_btn.down()
  back_btn.showturtle()
  back_btn.onclick(show_map)
  increase_health()
  decrease_stress()
  cat.hideturtle()


#######################################################################
#############################HOUSE#####################################

def house():
  s.bgpic("bedroom.gif")
  scooter.hideturtle()
  book.hideturtle()
  teacher.hideturtle()
  food.hideturtle()
  gym.hideturtle()
  home.hideturtle()

  turtle.addshape("sleepButton.gif")
  turtle.addshape("gameButton.gif")
  turtle.addshape("dogThumbsUp.gif")
  turtle.addshape("cookie.gif")


  sleep = turtle.Turtle()
  game = turtle.Turtle()
  cookie = turtle.Turtle()


  cookie.hideturtle()
  dogThumbsUp.hideturtle()


  dogThumbsUp.penup()
  sleep.penup()
  game.penup()
  cookie.penup()


  sleep.shape("sleepButton.gif")
  game.shape("gameButton.gif")
  dogThumbsUp.shape("dogThumbsUp.gif")
  cookie.shape("cookie.gif")


  game.goto(-200, 0)
  sleep.goto(200,0)
  dogThumbsUp.goto(0,-100)
  cookie.goto(0,0)


  def goSleep(x,y):
      player.penup()
      sleep.hideturtle()
      game.hideturtle()
      player.goto(200, -100)
      player.showturtle()
      text.penup()
      text.speed(1)
      text.color("white")
      text.goto(-200, 200)
      text.write("Z", move=False, align="center", font=("Deja Vu Sans Mono", 50, "normal"))
      text.setheading(0)
      text.forward(100)
      text.write("Z", move=False, align="center", font=("Deja Vu Sans Mono", 50, "normal"))
      text.forward(100)
      text.write("Z", move=False, align="center", font=("Deja Vu Sans Mono", 50, "normal"))
      text.forward(100)
      text.write("Z", move=False, align="center", font=("Deja Vu Sans Mono", 50, "normal"))
      text.forward(100)
      text.write("Z", move=False, align="center", font=("Deja Vu Sans Mono", 50, "normal"))
      text.speed(20)
      text.clear()
      player.hideturtle()
      text.goto(0,200)
      text.write("Good job", move=False, align="center", font=("Deja Vu Sans Mono", 30, "normal"))
      dogThumbsUp.showturtle()
      increase_health()
      decrease_stress()
      game_over()




  def goPlay(x,y):
      s.bgpic("screen.gif")
      sleep.hideturtle()
      game.hideturtle()
      text.color("Brown")
      text.penup()
      text.goto(-200, 200)
      text.write("Tap the cookie", move=False, align="center", font=("Deja Vu Sans Mono", 30, "normal"))
      cookie.showturtle()


  def cookieTap(x,y):
      text.clear()
      cookie.hideturtle()
      text.write("Good job", move=False, align="center", font=("Deja Vu Sans Mono", 30, "normal"))
      dogThumbsUp.showturtle()
      back_btn.hideturtle()
      back_btn.shape("back.gif")
      back_btn.up()
      back_btn.goto(-450,-200)
      back_btn.down()
      back_btn.showturtle()
      back_btn.onclick(show_map)
      decrease_stress()





  sleep.onclick(goSleep)
  game.onclick(goPlay)
  cookie.onclick(cookieTap)

#######################################################################

###############################RESTAURANT#############################
def goChick(x,y):
    print("Chicka")
    chick.hideturtle()
    subway.hideturtle()
    panda.hideturtle()
    rest_text.clear()
    s.bgpic("insideChick.gif")
    rest_text.up()
    rest_text.goto(0,300)
    rest_text.down()
    rest_text.color("white")
    rest_text.write("Eat up buddy",False,"center",("Deja Vu Sans Mono",30,"bold"))
    turtle.addshape("sandwich.gif")
    turtle.addshape("table.gif")
    turtle.addshape("sandwichEat.gif")
    turtle.addshape("sandwichNom.gif")
    turtle.addshape("tableEat.gif")
    turtle.addshape("tableNom.gif")
    turtle.addshape("emoji.gif")
    sandwich.shape("sandwich.gif")
    table.shape("table.gif")
    sandwichEat.hideturtle()
    sandwichEat.shape("sandwichEat.gif")
    sandwichEat.up()
    sandwichEat.goto(0,0)
    sandwichEat.down()
    sandwichNom.hideturtle()
    sandwichNom.shape("sandwichNom.gif")
    sandwichNom.up()
    sandwichNom.goto(0,0)
    sandwichNom.down()
    tableEat.shape("tableEat.gif")
    tableNom.shape("tableNom.gif")
    emoji.shape("emoji.gif")
    sandwich.up()
    sandwich.goto(0,0)
    sandwich.down()
    table.up()
    table.goto(0,-300)
    table.down()
    tableEat.up()
    tableEat.goto(0,-300)
    tableEat.down()
    tableNom.up()
    tableNom.goto(0,-300)
    tableNom.down()


    rest_text.up()
    rest_text.goto(350,0)
    rest_text.down()
    rest_text.color("white")
    rest_text.write("Tap the food to eat",False,"center",("Deja Vu Sans Mono",30,"bold"))
    emoji.hideturtle()
    tableNom.hideturtle()
    tableEat.hideturtle()
    sandwichNom.hideturtle()
    sandwichEat.hideturtle()
    def eat(x,y):
        sandwich.hideturtle()
        sandwichEat.showturtle()
    def nom(x,y):
        sandwichEat.hideturtle()
        sandwichNom.showturtle()
    def done(x,y):
        sandwichNom.hideturtle()
        rest_text.up()
        rest_text.goto(0,100)
        rest_text.down()
        rest_text.color("green")
        rest_text.write("You're not done yet, look at that scrumptious table!",False,"center",("Deja Vu Sans Mono",20,"bold"))

    def tabEat(x,y):
        tableEat.showturtle()
        table.hideturtle()
    def tabNom(x,y):
        tableEat.hideturtle()
        tableNom.showturtle()
    def tabDone(x,y):
        rest_text.clear()
        tableNom.hideturtle()
        rest_text.up()
        rest_text.goto(0,200)
        rest_text.down()
        rest_text.color("white")
        rest_text.write("Great job!",False,"center",("Deja Vu Sans Mono",40,"bold"))
        rest_text.clear()
        emoji.showturtle()
        back_btn.hideturtle()
        back_btn.shape("back.gif")
        back_btn.up()
        back_btn.goto(-450,-200)
        back_btn.down()
        back_btn.showturtle()
        back_btn.onclick(show_map)
        increase_health()
        emoji.hideturtle()

    sandwich.onclick(eat)
    sandwichEat.onclick(nom)
    sandwichNom.onclick(done)
    table.onclick(tabEat)
    tableEat.onclick(tabNom)
    tableNom.onclick(tabDone)

def goSub(x,y):
    print("Subby")
    chick.hideturtle()
    subway.hideturtle()
    panda.hideturtle()
    rest_text.clear()
    s.bgpic("insideSubway.gif")
    rest_text.up()
    rest_text.goto(0,300)
    rest_text.down()
    rest_text.color("white")
    rest_text.write("Eat up buddy",False,"center",("Deja Vu Sans Mono",30,"bold"))
    turtle.addshape("sub.gif")
    turtle.addshape("table.gif")
    turtle.addshape("subEat.gif")
    turtle.addshape("subNom.gif")
    turtle.addshape("tableEat.gif")
    turtle.addshape("tableNom.gif")
    turtle.addshape("emoji.gif")
    sub.shape("sub.gif")
    table.shape("table.gif")
    subEat.hideturtle()
    subEat.shape("subEat.gif")
    subEat.up()
    subEat.goto(0,0)
    subEat.down()
    subNom.hideturtle()
    subNom.shape("subNom.gif")
    subNom.up()
    subNom.goto(0,0)
    subNom.down()
    tableEat.shape("tableEat.gif")
    tableNom.shape("tableNom.gif")
    emoji.shape("emoji.gif")
    sub.up()
    sub.goto(0,0)
    sub.down()
    table.up()
    table.goto(0,-300)
    table.down()
    tableEat.up()
    tableEat.goto(0,-300)
    tableEat.down()
    tableNom.up()
    tableNom.goto(0,-300)
    tableNom.down()


    rest_text.up()
    rest_text.goto(350,0)
    rest_text.down()
    rest_text.color("white")
    rest_text.write("Tap the food to eat",False,"center",("Deja Vu Sans Mono",30,"bold"))

    emoji.hideturtle()
    tableNom.hideturtle()
    tableEat.hideturtle()
    subNom.hideturtle()
    subEat.hideturtle()
    def eat(x,y):
        sub.hideturtle()
        subEat.showturtle()
    def nom(x,y):
        subEat.hideturtle()
        subNom.showturtle()
    def done(x,y):
        subNom.hideturtle()
        rest_text.up()
        rest_text.goto(0,100)
        rest_text.down()
        rest_text.color("green")
        rest_text.write("You're not done yet, look at that scrumptious table!",False,"center",("Deja Vu Sans Mono",20,"bold"))

    def tabEat(x,y):
        tableEat.showturtle()
        table.hideturtle()
    def tabNom(x,y):
        tableEat.hideturtle()
        tableNom.showturtle()
    def tabDone(x,y):
        rest_text.clear()
        tableNom.hideturtle()
        rest_text.up()
        rest_text.goto(0,200)
        rest_text.down()
        rest_text.color("white")
        rest_text.write("Great job!",False,"center",("Deja Vu Sans Mono",40,"bold"))
        rest_text.clear()
        emoji.showturtle()
        back_btn.hideturtle()
        back_btn.shape("back.gif")
        back_btn.up()
        back_btn.goto(-450,-200)
        back_btn.down()
        back_btn.showturtle()
        back_btn.onclick(show_map)
        increase_health()
        emoji.hideturtle()
    sub.onclick(eat)
    subEat.onclick(nom)
    subNom.onclick(done)
    table.onclick(tabEat)
    tableEat.onclick(tabNom)
    tableNom.onclick(tabDone)

def goPanda(x,y):
    print("Subby")
    chick.hideturtle()
    subway.hideturtle()
    panda.hideturtle()
    rest_text.clear()
    emoji.hideturtle()
    tableNom.hideturtle()
    tableEat.hideturtle()
    pailNom.hideturtle()
    pailEat.hideturtle()
    s.bgpic("insidePanda.gif")
    rest_text.up()
    rest_text.goto(0,300)
    rest_text.down()
    rest_text.color("white")
    rest_text.write("Eat up buddy",False,"center",("Deja Vu Sans Mono",30,"bold"))
    turtle.addshape("pail.gif")
    turtle.addshape("table.gif")
    turtle.addshape("pailEat.gif")
    turtle.addshape("pailNom.gif")
    turtle.addshape("tableEat.gif")
    turtle.addshape("tableNom.gif")
    turtle.addshape("emoji.gif")
    pail.shape("pail.gif")
    table.shape("table.gif")
    pailEat.hideturtle()
    pailEat.shape("pailEat.gif")
    pailEat.up()
    pailEat.goto(0,0)
    pailEat.down()
    pailNom.hideturtle()
    pailNom.shape("pailNom.gif")
    pailNom.up()
    pailNom.goto(0,0)
    pailNom.down()
    tableEat.shape("tableEat.gif")
    tableNom.shape("tableNom.gif")
    emoji.shape("emoji.gif")

    pail.up()
    pail.goto(0,0)
    pail.down()
    table.up()
    table.goto(0,-400)
    table.down()
    tableEat.up()
    tableEat.goto(0,-400)
    tableEat.down()
    tableNom.up()
    tableNom.goto(0,-400)
    tableNom.down()


    rest_text.up()
    rest_text.goto(350,0)
    rest_text.down()
    rest_text.color("white")
    rest_text.write("Tap the food to eat",False,"center",("Deja Vu Sans Mono",30,"bold"))


    def eat(x,y):
        pail.hideturtle()
        pailEat.showturtle()
    def nom(x,y):
        pailEat.hideturtle()
        pailNom.showturtle()
    def done(x,y):
        pailNom.hideturtle()
        rest_text.up()
        rest_text.goto(0,100)
        rest_text.down()
        rest_text.color("green")
        rest_text.write("You're not done yet, look at that scrumptious table!",False,"center",("Deja Vu Sans Mono",20,"bold"))

    def tabEat(x,y):
        tableEat.showturtle()
        table.hideturtle()
    def tabNom(x,y):
        tableEat.hideturtle()
        tableNom.showturtle()
    def tabDone(x,y):
        tableNom.hideturtle()
        rest_text.clear()
        rest_text.up()
        rest_text.goto(0,200)
        rest_text.down()
        rest_text.color("white")
        rest_text.write("Great job!",False,"center",("Deja Vu Sans Mono",40,"bold"))
        rest_text.clear()
        emoji.showturtle()
        back_btn.hideturtle()
        back_btn.shape("back.gif")
        back_btn.up()
        back_btn.goto(-450,-200)
        back_btn.down()
        back_btn.showturtle()
        back_btn.onclick(show_map)
        increase_health()
        emoji.hideturtle()
    pail.onclick(eat)
    pailEat.onclick(nom)
    pailNom.onclick(done)
    table.onclick(tabEat)
    tableEat.onclick(tabNom)
    tableNom.onclick(tabDone)


def restaurant():
    s.bgpic("innerCircle.gif")
    sparky.hideturtle()
    back_btn.hideturtle()
    food.hideturtle()
    teacher.hideturtle()
    gym.hideturtle()
    home.hideturtle()
    book.hideturtle()
    scooter.hideturtle()
    rest_text.up()
    rest_text.goto(0,200)
    rest_text.down()
    rest_text.color("white")
    rest_text.write("What are you hungry for?",False,"center",("Deja Vu Sans Mono",30,"bold"))        

    turtle.addshape("chick.gif")
    turtle.addshape("subway.gif")
    turtle.addshape("pandaExpress.gif")
    chick.shape("chick.gif")
    subway.shape("subway.gif")
    panda.shape("pandaExpress.gif")
    chick.up()
    chick.goto(-300,0)
    chick.down()
    subway.up()
    subway.goto(300,0)
    subway.down()
    panda.up()
    panda.goto(0,-200)
    panda.down()

    chick.onclick(goChick)
    subway.onclick(goSub)
    panda.onclick(goPanda)


#####################################################################
############################LIBRARY##################################
ans_num = 0
def study_math(x,y):
    s.bgpic("mathdesk.gif")
    math_btn.hideturtle()
    cs_btn.hideturtle()
    lib_text.clear()

    ##################QUESTION1#########################

    math_text.up()
    math_text.goto(0,200)
    math_text.down()
    math_text.color("white")
    math_text.write("What is 9 + 10?",False,"center",("Deja Vu Sans Mono",30,"bold"))

    a.goto(-400,0)
    a.showturtle()
    math_text.up()
    math_text.goto(-400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("300",False,"center",("Deja Vu Sans Mono",30,"bold"))

    b.goto(-150,0)
    b.showturtle()
    math_text.up()
    math_text.goto(-150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("21",False,"center",("Deja Vu Sans Mono",30,"bold"))

    c.goto(150,0)
    c.showturtle()
    math_text.up()
    math_text.goto(150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("11",False,"center",("Deja Vu Sans Mono",30,"bold"))


    d.goto(400,0)
    d.showturtle()
    math_text.up()
    math_text.goto(400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("19",False,"center",("Deja Vu Sans Mono",30,"bold"))

    answer_text.up()
    answer_text.goto(0,-250)
    answer_text.down()


    def clicka1(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Wrong",False,"center",("Deja Vu Sans Mono",30,"bold"))
    def clickb1(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Nuh uh",False,"center",("Deja Vu Sans Mono",30,"bold"))
    def clickc1(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Nope",False,"center",("Deja Vu Sans Mono",30,"bold"))
    def clickd1(x,y):
        global ans_num
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Correct",False,"center",("Deja Vu Sans Mono",30,"bold"))
        increase_knowledge()
        ans_num+=1


    while ans_num == 0:
        a.onclick(clicka1)
        b.onclick(clickb1)
        c.onclick(clickc1)
        d.onclick(clickd1)
    answer_text.clear()
    math_text.clear()
    ################################################################
    ############################QUESTION2############################

    math_text.up()
    math_text.goto(0,200)
    math_text.down()
    math_text.color("white")
    math_text.write("What is 2 * 11?",False,"center",("Deja Vu Sans Mono",30,"bold"))

    a.goto(-400,0)
    a.showturtle()
    math_text.up()
    math_text.goto(-400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("211",False,"center",("Deja Vu Sans Mono",30,"bold"))

    b.goto(-150,0)
    b.showturtle()
    math_text.up()
    math_text.goto(-150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("3.14",False,"center",("Deja Vu Sans Mono",30,"bold"))

    c.goto(150,0)
    c.showturtle()
    math_text.up()
    math_text.goto(150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("22",False,"center",("Deja Vu Sans Mono",30,"bold"))


    d.goto(400,0)
    d.showturtle()
    math_text.up()
    math_text.goto(400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("0.22",False,"center",("Deja Vu Sans Mono",30,"bold"))

    answer_text.up()
    answer_text.goto(0,-250)
    answer_text.down()

    def clicka2(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Hold up, let them cook",False,"center",("Deja Vu Sans Mono",30,"bold"))
    def clickb2(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Chat, is this real?",False,"center",("Deja Vu Sans Mono",30,"bold"))

    def clickc2(x,y):
        global ans_num
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Correct",False,"center",("Deja Vu Sans Mono",30,"bold"))
        ans_num+=1
        increase_knowledge()

    def clickd2(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Stop the cap",False,"center",("Deja Vu Sans Mono",30,"bold"))

    # ans_num = 0

    while ans_num == 1:
        a.onclick(clicka2)
        b.onclick(clickb2)
        c.onclick(clickc2)
        d.onclick(clickd2)
    answer_text.clear()
    math_text.clear()
    #################################################################
    ##########################QUESTION3##############################

    math_text.up()
    math_text.goto(0,200)
    math_text.down()
    math_text.color("white")
    math_text.write("What is 10 / 2?",False,"center",("Deja Vu Sans Mono",30,"bold"))

    a.goto(-400,0)
    a.showturtle()
    math_text.up()
    math_text.goto(-400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("5",False,"center",("Deja Vu Sans Mono",30,"bold"))

    b.goto(-150,0)
    b.showturtle()
    math_text.up()
    math_text.goto(-150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("102",False,"center",("Deja Vu Sans Mono",30,"bold"))

    c.goto(150,0)
    c.showturtle()
    math_text.up()
    math_text.goto(150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("42",False,"center",("Deja Vu Sans Mono",30,"bold"))


    d.goto(400,0)
    d.showturtle()
    math_text.up()
    math_text.goto(400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("9000",False,"center",("Deja Vu Sans Mono",30,"bold"))

    answer_text.up()
    answer_text.goto(0,-250)
    answer_text.down()

    def clicka3(x,y):
        global ans_num
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Correct",False,"center",("Deja Vu Sans Mono",30,"bold"))
        increase_knowledge()
        ans_num+=1
    def clickb3(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Close",False,"center",("Deja Vu Sans Mono",30,"bold"))


    def clickc3(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Not even close",False,"center",("Deja Vu Sans Mono",30,"bold"))

    def clickd3(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("IT'S OVER 9,000!!!",False,"center",("Deja Vu Sans Mono",30,"bold"))



    # ans_num = 0
    while ans_num == 2:
        a.onclick(clicka3)
        b.onclick(clickb3)
        c.onclick(clickc3)
        d.onclick(clickd3)
    answer_text.clear()
    math_text.clear()
    #################################################################
    #########################QUESTION4###############################

    math_text.up()
    math_text.goto(0,200)
    math_text.down()
    math_text.color("white")
    math_text.write("What goes in here? Δ v = u ln ( ____ )",False,"center",("Deja Vu Sans Mono",30,"bold"))

    a.goto(-400,0)
    a.showturtle()
    math_text.up()
    math_text.goto(-400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("idk",False,"center",("Deja Vu Sans Mono",30,"bold"))

    b.goto(-150,0)
    b.showturtle()
    math_text.up()
    math_text.goto(-150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("m i m",False,"center",("Deja Vu Sans Mono",30,"bold"))

    c.goto(150,0)
    c.showturtle()
    math_text.up()
    math_text.goto(150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("C6H12O6+6O2",False,"center",("Deja Vu Sans Mono",30,"bold"))


    d.goto(400,0)
    d.showturtle()
    math_text.up()
    math_text.goto(400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("ඞ",False,"center",("Deja Vu Sans Mono",30,"bold"))

    answer_text.up()
    answer_text.goto(0,-250)
    answer_text.down()

    def clicka4(x,y):
        answer_text.color("white")
        answer_text.write("Too bad",False,"center",("Deja Vu Sans Mono",30,"bold"))
        answer_text.clear()

    def clickb4(x,y):
        global ans_num
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("You guessed that but correct",False,"center",("Deja Vu Sans Mono",30,"bold"))
        ans_num+=1
        back_btn.hideturtle()
        back_btn.shape("back.gif")
        back_btn.up()
        back_btn.goto(-450,-200)
        back_btn.down()
        back_btn.showturtle()
        back_btn.onclick(show_map)
        increase_knowledge()
        a.hideturtle()
        b.hideturtle()
        c.hideturtle()
        d.hideturtle()

    def clickc4(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Bro did not just pick photosynthesis 💀",False,"center",("Deja Vu Sans Mono",30,"bold"))

    def clickd4(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Imposter,sus",False,"center",("Deja Vu Sans Mono",30,"bold"))

    # ans_num = 0

    while ans_num == 3:
        a.onclick(clicka4)
        b.onclick(clickb4)
        c.onclick(clickc4)
        d.onclick(clickd4)
    answer_text.clear()
    math_text.clear()



    #################################################################
ans_num2 = 0
def study_cs(x,y):
    s.bgpic("csdesk.gif")
    math_btn.hideturtle()
    cs_btn.hideturtle()
    lib_text.clear()

    ##################QUESTION1#########################

    math_text.up()
    math_text.goto(0,200)
    math_text.down()
    math_text.color("white")
    math_text.write("What is this output? print('cheese')",False,"center",("Deja Vu Sans Mono",30,"bold"))

    a.goto(-400,0)
    a.showturtle()
    math_text.up()
    math_text.goto(-400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("Mouse",False,"center",("Deja Vu Sans Mono",30,"bold"))

    b.goto(-150,0)
    b.showturtle()
    math_text.up()
    math_text.goto(-150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("Queso",False,"center",("Deja Vu Sans Mono",30,"bold"))

    c.goto(150,0)
    c.showturtle()
    math_text.up()
    math_text.goto(150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("eseehc",False,"center",("Deja Vu Sans Mono",30,"bold"))


    d.goto(400,0)
    d.showturtle()
    math_text.up()
    math_text.goto(400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("cheese",False,"center",("Deja Vu Sans Mono",30,"bold"))

    answer_text.up()
    answer_text.goto(0,-250)
    answer_text.down()

    def clicka1(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Wrong",False,"center",("Deja Vu Sans Mono",30,"bold"))
    def clickb1(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Nuh uh",False,"center",("Deja Vu Sans Mono",30,"bold"))
    def clickc1(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Nope",False,"center",("Deja Vu Sans Mono",30,"bold"))
    def clickd1(x,y):
        global ans_num2
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Correct",False,"center",("Deja Vu Sans Mono",30,"bold"))
        increase_knowledge()
        ans_num2+=1

    while ans_num2 == 0:
        a.onclick(clicka1)
        b.onclick(clickb1)
        c.onclick(clickc1)
        d.onclick(clickd1)

    ################################################################
    ############################QUESTION2############################

    math_text.up()
    math_text.goto(0,200)
    math_text.down()
    math_text.color("white")
    math_text.write("What is the variable A? A = moose",False,"center",("Deja Vu Sans Mono",30,"bold"))

    a.goto(-400,0)
    a.showturtle()
    math_text.up()
    math_text.goto(-400,-150)
    math_text.down()
    math_text.color("moo")
    math_text.write("211",False,"center",("Deja Vu Sans Mono",30,"bold"))

    b.goto(-150,0)
    b.showturtle()
    math_text.up()
    math_text.goto(-150,-150)
    math_text.down()
    math_text.color("polar bear")
    math_text.write("3.14",False,"center",("Deja Vu Sans Mono",30,"bold"))

    c.goto(150,0)
    c.showturtle()
    math_text.up()
    math_text.goto(150,-150)
    math_text.down()
    math_text.color("moose")
    math_text.write("22",False,"center",("Deja Vu Sans Mono",30,"bold"))


    d.goto(400,0)
    d.showturtle()
    math_text.up()
    math_text.goto(400,-150)
    math_text.down()
    math_text.color("A")
    math_text.write("0.22",False,"center",("Deja Vu Sans Mono",30,"bold"))

    answer_text.up()
    answer_text.goto(0,-250)
    answer_text.down()

    def clicka2(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("WHERE DO YOU SEE MOO?????",False,"center",("Deja Vu Sans Mono",30,"bold"))

    def clickb2(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Wrong animal",False,"center",("Deja Vu Sans Mono",30,"bold"))


    def clickc2(x,y):
        global ans_num2
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Correct",False,"center",("Deja Vu Sans Mono",30,"bold"))
        ans_num2+=1
        increase_knowledge()
    def clickd2(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Bro, that's not even close",False,"center",("Deja Vu Sans Mono",30,"bold"))



    while ans_num2 == 1:
        a.onclick(clicka2)
        b.onclick(clickb2)
        c.onclick(clickc2)
        d.onclick(clickd2)
    answer_text.clear()
    math_text.clear()
    #################################################################
    ##########################QUESTION3##############################

    math_text.up()
    math_text.goto(0,200)
    math_text.down()
    math_text.color("white")
    math_text.write("What is the list name? Pookie = ['bear','Tohru','Kyo']",False,"center",("Deja Vu Sans Mono",30,"bold"))

    a.goto(-400,0)
    a.showturtle()
    math_text.up()
    math_text.goto(-400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("Pookie",False,"center",("Deja Vu Sans Mono",30,"bold"))

    b.goto(-150,0)
    b.showturtle()
    math_text.up()
    math_text.goto(-150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("Pookie Bear",False,"center",("Deja Vu Sans Mono",30,"bold"))

    c.goto(150,0)
    c.showturtle()
    math_text.up()
    math_text.goto(150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("Tohru",False,"center",("Deja Vu Sans Mono",30,"bold"))


    d.goto(400,0)
    d.showturtle()
    math_text.up()
    math_text.goto(400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("list",False,"center",("Deja Vu Sans Mono",30,"bold"))

    answer_text.up()
    answer_text.goto(0,-250)
    answer_text.down()

    def clicka3(x,y):
        global ans_num2
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Correct",False,"center",("Deja Vu Sans Mono",30,"bold"))
        increase_knowledge()
        ans_num2+=1
    def clickb3(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("OwO",False,"center",("Deja Vu Sans Mono",30,"bold"))


    def clickc3(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("That is in the list",False,"center",("Deja Vu Sans Mono",30,"bold"))

    def clickd3(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("no.",False,"center",("Deja Vu Sans Mono",30,"bold"))



    while ans_num2 == 0:
        a.onclick(clicka3)
        b.onclick(clickb3)
        c.onclick(clickc3)
        d.onclick(clickd3)
    answer_text.clear()
    math_text.clear()
    #################################################################
    #########################QUESTION4###############################

    math_text.up()
    math_text.goto(0,200)
    math_text.down()
    math_text.color("white")
    math_text.write("How many hours of sleep do you get?",False,"center",("Deja Vu Sans Mono",30,"bold"))

    a.goto(-400,0)
    a.showturtle()
    math_text.up()
    math_text.goto(-400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("9",False,"center",("Deja Vu Sans Mono",30,"bold"))

    b.goto(-150,0)
    b.showturtle()
    math_text.up()
    math_text.goto(-150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("What's sleep?",False,"center",("Deja Vu Sans Mono",30,"bold"))

    c.goto(150,0)
    c.showturtle()
    math_text.up()
    math_text.goto(150,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("5",False,"center",("Deja Vu Sans Mono",30,"bold"))


    d.goto(400,0)
    d.showturtle()
    math_text.up()
    math_text.goto(400,-150)
    math_text.down()
    math_text.color("white")
    math_text.write("30 minutes",False,"center",("Deja Vu Sans Mono",30,"bold"))

    answer_text.up()
    answer_text.goto(0,-250)
    answer_text.down()

    def clicka4(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Cap",False,"center",("Deja Vu Sans Mono",30,"bold"))

    def clickb4(x,y):
        global ans_num2
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Correct, welcome to the club",False,"center",("Deja Vu Sans Mono",30,"bold"))
        ans_num2+=1
        back_btn.hideturtle()
        back_btn.shape("back.gif")
        back_btn.up()
        back_btn.goto(-450,-200)
        back_btn.down()
        back_btn.showturtle()
        back_btn.onclick(show_map)
        increase_knowledge()
        a.hideturtle()
        b.hideturtle()
        c.hideturtle()
        d.hideturtle()

    def clickc4(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("That's a LOT of sleep, but wrong",False,"center",("Deja Vu Sans Mono",30,"bold"))

    def clickd4(x,y):
        answer_text.clear()
        answer_text.color("white")
        answer_text.write("Imposter,sus",False,"center",("Deja Vu Sans Mono",30,"bold"))



    while ans_num2 == 0:
        a.onclick(clicka4)
        b.onclick(clickb4)
        c.onclick(clickc4)
        d.onclick(clickd4)
    answer_text.clear()
    math_text.clear()



    #################################################################
    #################################################################
def library():
    s.bgpic("library.gif")
    lib_text.up()
    lib_text.goto(0,200)
    lib_text.down()
    lib_text.color("white")
    lib_text.write("Pick your poison, What do you want to study?",False,"center",("Deja Vu Sans Mono",30,"bold"))
    turtle.addshape("mathbutton.gif")
    turtle.addshape("csbutton.gif")
    turtle.addshape("c.gif")
    turtle.addshape("b.gif")
    turtle.addshape("a.gif")
    turtle.addshape("d.gif")

    math_btn.shape("mathbutton.gif")
    cs_btn.shape("csbutton.gif")
    a.shape("a.gif")
    b.shape("b.gif")
    c.shape("c.gif")
    d.shape("d.gif")

    answer.hideturtle()
    a.hideturtle()
    b.hideturtle()
    c.hideturtle()
    d.hideturtle()
    sparky.hideturtle()
    back_btn.hideturtle()
    food.hideturtle()
    teacher.hideturtle()
    gym.hideturtle()
    home.hideturtle()
    book.hideturtle()
    scooter.hideturtle()

    math_btn.up()
    math_btn.goto(-300,0)
    math_btn.down()

    cs_btn.up()
    cs_btn.goto(300,0)
    cs_btn.down()

    math_btn.onclick(study_math)
    cs_btn.onclick(study_cs)

def check(scooter):
    checkLibrary = 0
    checkFood = 0
    checkGym = 0
    checkHome = 0
    checkClass = 0
    if (scooter.distance(book.xcor(),book.ycor())<30):
        print("Library")
        checkLibrary+=1
    elif (scooter.distance(teacher.xcor(),teacher.ycor())<30):
        print("Class")
        checkClass+=1
    elif (scooter.distance(food.xcor(),food.ycor())<30):
        print("Restaurant")
        checkFood+=1
    elif (scooter.distance(gym.xcor(),gym.ycor())<30):
        print("Gym")
        checkGym+=1
    elif (scooter.distance(home.xcor(),home.ycor())<30):
        print("Home")
        checkHome+=1
    if checkLibrary >= 1:
        library()
    if checkFood >= 1:
        restaurant()
    if checkGym >= 1:
        goGym()
    if checkHome >= 1:
        house()
    if checkClass >= 1:
        goClass()
def up():
    global scooter
    scooter.setheading(90)
    scooter.forward(10)
    check(scooter)  
def down():
    global scooter
    scooter.setheading(270)
    scooter.forward(10)
    check(scooter)  
def left():
    global scooter
    scooter.setheading(180)
    scooter.forward(10)
    check(scooter)  
def right():
    global scooter
    scooter.setheading(0)
    scooter.forward(10)
    check(scooter)  


def show_map2():
    global map_symbol
    global todo_text
    global stress
    global health 
    global knowledge
    global stress_text
    global health_text
    global kdg_text
    global back_btn
    s.bgpic("uicmap.gif")
    map_symbol.hideturtle()





    turtle.addshape("back.gif")
    turtle.addshape("miniscoot.gif")
    turtle.addshape("book.gif")
    turtle.addshape("dumbbell.gif")
    turtle.addshape("home.gif")
    turtle.addshape("teacher.gif")
    turtle.addshape("food.gif")

    scooter.shape("miniscoot.gif")
    teacher.shape("teacher.gif")
    food.shape("food.gif")
    gym.shape("dumbbell.gif")
    home.shape("home.gif")
    book.shape("book.gif")
    book.showturtle()
    gym.showturtle()
    teacher.showturtle()
    food.showturtle()
    scooter.showturtle()
    home.showturtle()
    food.up()
    food.goto(100,200)
    food.down()

    gym.up()
    gym.goto(300,300)
    gym.down()

    book.up()
    book.goto(-250,200)
    book.down()

    home.up()
    home.goto(-400,-100)
    home.down()

    teacher.up()
    teacher.goto(50,-300)
    teacher.down()

    scooter.penup()
    scooter.goto(0,0)


    check(scooter)

    back_btn.hideturtle()
    back_btn.shape("back.gif")
    back_btn.up()
    back_btn.goto(-450,-250)
    back_btn.down()
    back_btn.showturtle()

    back_btn.onclick(hide_map)
def show_map(x,y):
    global map_symbol
    global todo_text
    global stress
    global health 
    global knowledge
    global stress_text
    global health_text
    global kdg_text
    global back_btn
    s.bgpic("uicmap.gif")
    map_symbol.hideturtle()





    turtle.addshape("back.gif")
    turtle.addshape("miniscoot.gif")
    turtle.addshape("book.gif")
    turtle.addshape("dumbbell.gif")
    turtle.addshape("home.gif")
    turtle.addshape("teacher.gif")
    turtle.addshape("food.gif")

    scooter.shape("miniscoot.gif")
    teacher.shape("teacher.gif")
    food.shape("food.gif")
    gym.shape("dumbbell.gif")
    home.shape("home.gif")
    book.shape("book.gif")
    book.showturtle()
    gym.showturtle()
    teacher.showturtle()
    food.showturtle()
    scooter.showturtle()
    home.showturtle()
    food.up()
    food.goto(100,200)
    food.down()

    gym.up()
    gym.goto(300,300)
    gym.down()

    book.up()
    book.goto(-250,200)
    book.down()

    home.up()
    home.goto(-400,-100)
    home.down()

    teacher.up()
    teacher.goto(50,-300)
    teacher.down()

    scooter.penup()
    scooter.goto(0,0)


    check(scooter)

    back_btn.hideturtle()
    back_btn.shape("back.gif")
    back_btn.up()
    back_btn.goto(-450,-250)
    back_btn.down()
    back_btn.showturtle()

    back_btn.onclick(hide_map)


def assignment():
    assign_list=["Exam","Homework"] 
    global assign_ttl
    global count3
    x = random.randint(0,1)
    asgn_choice = assign_list[x]
    assign_ttl.hideturtle()
    assign_ttl.up()
    assign_ttl.goto(count3,0)
    assign_ttl.down()
    assign_ttl.write(asgn_choice,False,align="center",font=("Helvetica",15,"normal"))
    count3-=100
###################################MAP#######################################
def load_map():
    global map_symbol
    turtle.addshape("mapsymbol.gif")
    map_symbol.shape("mapsymbol.gif")
    map_symbol.up()
    map_symbol.goto(500,-180)
    map_symbol.down()
    map_symbol.showturtle()

def hide_map(x,y):
    global map_symbol
    global todo_text
    global stress
    global health 
    global knowledge
    global stress_text
    global health_text
    global kdg_text
    global back_btn
    s.bgpic("quad.gif")
    map_symbol.showturtle()
    todo_text.showturtle()
    stress.showturtle()
    health.showturtle()
    knowledge.showturtle()
    stress_text.showturtle()
    health_text.showturtle()
    kdg_text.showturtle()
    back_btn.hideturtle()
    book.hideturtle()
    gym.hideturtle()
    teacher.hideturtle()
    food.hideturtle()
    scooter.hideturtle()
    home.hideturtle()

########################################################
########################TODO-LIST#######################
def show_todo(x,y):
    global todo
    global todo_text
    global map_symbol
    turtle.addshape("todolist.gif")
    todo.shape("todolist.gif")
    todo.up()
    todo.goto(0,0)
    todo.down()
    todo_text.hideturtle()
    todo.showturtle()
    map_symbol.hideturtle()
    assignment()
def hide_todo(x,y):
    global todo
    global todo_text
    global map_symbol
    global assign_ttl
    assign_ttl.clear()
    todo.hideturtle()
    todo_text.showturtle()
    map_symbol.showturtle()
def todo_list():
    global todo_text
    todo_text.hideturtle()
    turtle.addshape("todosymbol.gif")
    todo_text.shape("todosymbol.gif")
    todo_text.up()
    todo_text.goto(500,10)
    todo_text.down()
    todo_text.showturtle()

    return todo_text
#######################################################
######################HEALTHBARS#######################
def increase_stress():
    global t4
    xcor = 240
    global click
    global count
    t4.hideturtle()
    t4.pencolor("red")
    t4.up()
    t4.goto(xcor+(click*50),200) 
    t4.down()
    t4.fillcolor("red")
    t4.begin_fill()
    t4.forward(50)
    t4.left(90)
    t4.forward(25)
    t4.left(90)
    t4.forward(50)
    t4.left(90)
    t4.forward(25)
    t4.left(90)
    t4.forward(50)
    click += 1
    count += 10
    t4.end_fill()
def increase_health():
    global click1
    global count1
    global t5
    xcor = 240
    t5.hideturtle()

    t5.pencolor("blue")
    t5.up()
    t5.goto(xcor + (click1*50),150) 
    t5.down()
    t5.fillcolor("blue")
    t5.begin_fill()
    t5.forward(50)
    t5.left(90)
    t5.forward(25)
    t5.left(90)
    t5.forward(50)
    t5.left(90)
    t5.forward(25)
    t5.left(90)
    t5.forward(50)
    click1 += 1
    count1 += 10
    t5.end_fill()
def increase_knowledge():
    global t6
    global click2
    global count2
    for i in range(1):
        t6.pencolor("green")
        t6.up()
        t6.goto(240 + (click2 * 50),100) 
        t6.down()
        t6.fillcolor("green")
        t6.begin_fill()
        t6.forward(50)
        t6.left(90)
        t6.forward(25)
        t6.left(90)
        t6.forward(50)
        t6.left(90)
        t6.forward(25)
        t6.left(90)
        t6.forward(50)
        t6.end_fill()
    click2 += 1
    count2 += 10

def decrease_knowledge():
    global t6
    for i in range(8):
        t6.undo()
def decrease_stress():
    global t4
    for i in range(8):
        t4.undo()
def decrease_health():
    global t5
    for i in range(8):
        t5.undo()
def healthbar():
    global stress
    global health 
    global knowledge
    global stress_text
    global health_text
    global kdg_text
    turtle.addshape("healthbar.gif")



    stress_text.hideturtle()
    health_text.hideturtle()
    kdg_text.hideturtle()
    stress.hideturtle()
    health.hideturtle()
    knowledge.hideturtle()

    stress.shape("healthbar.gif")
    health.shape("healthbar.gif")
    knowledge.shape("healthbar.gif")

    stress.up()
    stress.goto(400,200)
    stress.down()
    health.up()
    health.goto(400,150)
    health.down()
    knowledge.up()
    knowledge.goto(400,100)
    knowledge.down()
    stress.showturtle()
    health.showturtle()
    knowledge.showturtle()
    stress_text.up()
    stress_text.goto(400,200)
    stress_text.down()
    stress_text.write("STRESS",False,align="center",font=("Helvetica",15,"italic"))
    health_text.up()
    health_text.goto(400,150)
    health_text.down()
    health_text.write("HEALTH",False,align="center",font=("Helvetica",15,"italic"))
    kdg_text.up()
    kdg_text.goto(400,100)
    kdg_text.down()
    kdg_text.write("KNOWLEDGE",False,align="center",font=("Helvetica",15,"italic"))
#####################################################################################
def rules():
    t.hideturtle()
    turtle.addshape("sparky.gif")
    sparky.shape("sparky.gif")
    sparky.up()
    sparky.goto(-500,50)
    sparky.down()


    text = turtle.Turtle()
    text.up()
    text.goto(0,0)
    text.down()
    text.hideturtle()


    for line in rules_list[:5]:
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()
    turtle.ontimer(healthbar,1)


    for line in rules_list[5:7]:
        text.up()
        text.goto(0,0)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()
    for line in rules_list[7:8]:
        text.up()
        text.goto(100,180)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()
    for line in rules_list[8:9]:
        text.up()
        text.goto(80,130)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()
    for line in rules_list[9:10]:
        text.up()
        text.goto(100,80)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()
    for line in rules_list[10:12]:
        text.up()
        text.goto(0,0)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()
    todo_list()
    todo_text.onclick(show_todo)

    for line in rules_list[12:14]:
        text.up()
        text.goto(0,0)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()



    for line in rules_list[14:15]:
        text.up()
        text.goto(0,0)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()



    for line in rules_list[15:18]:
        text.up()
        text.goto(100,0)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()
    todo.onclick(hide_todo)
    load_map()
    for line in rules_list[18:20]:
        text.up()
        text.goto(100,0)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()
    map_symbol.onclick(show_map)
    back_btn.onclick(hide_map)
    for line in rules_list[20:24]:
        text.up()
        text.goto(100,0)
        text.down()
        text.pencolor("white")
        text.write(line,False,align="center",font=("Theinhardt",15,"bold"))
        time.sleep(2)
        text.clear()


###################################################################
###############SCREEN 1/CHARACTERS#################################

s = turtle.getscreen()
s.title("Game")

t = turtle.Turtle()



s = turtle.getscreen()
s.bgpic("front_uic.gif")
s.setup(width=1162 + 10, height= 773 + 10)


turtle.addshape("steve.gif")
turtle.addshape("girl.gif")
turtle.addshape("dog.gif")
turtle.addshape("amongus.gif")


boy = turtle.Turtle()
girl = turtle.Turtle()
dog = turtle.Turtle()
sus = turtle.Turtle()
text = turtle.Turtle()

t2 = turtle.Turtle()
t3 = turtle.Turtle()

text.shape("turtle")

boy.up()
girl.up()
dog.up()
sus.up()
boy.goto(-400,0)
girl.goto(-150,0)
dog.goto(200,0)
sus.goto(400,0)
boy.down()
girl.down()
dog.down()
sus.down()

text.speed(20)
text.width(5)
text.goto(0, 200)
text.color("white")
text.write("Choose your Character!", move=False, align="center", font=("Deja Vu Sans Mono", 30, "bold"))
nextScreen = 0

player = turtle.Turtle()
boy.shape("steve.gif")
girl.shape("girl.gif")
dog.shape("dog.gif")
sus.shape("amongus.gif")

def chosen_boy_character(x,y):
    global player
    global nextScreen

    nextScreen += 1
    player.shape("steve.gif")
    s.bgpic("quad.gif")
    girl.hideturtle()
    dog.hideturtle()
    sus.hideturtle()
    boy.hideturtle()
    player.up()
    player.goto(-450,270)
    player.down()
    text.clear()
    rules()

def chosen_girl_character(x,y):
    global player
    global nextScreen

    nextScreen += 1
    player.shape("girl.gif")
    s.bgpic("quad.gif")
    girl.hideturtle()
    dog.hideturtle()
    sus.hideturtle()
    boy.hideturtle()
    player.up()
    player.goto(-450,200)
    player.down()
    text.clear()
    rules()

def chosen_dog_character(x,y):
    global player
    global nextScreen

    nextScreen += 1
    player.shape("dog.gif")
    s.bgpic("quad.gif")
    girl.hideturtle()
    dog.hideturtle()
    sus.hideturtle()
    boy.hideturtle()
    player.up()
    player.goto(-450,270)
    player.down()
    text.clear()
    rules()

def chosen_sus_character(x,y):
    global player
    global nextScreen

    nextScreen += 1
    player.shape("amongus.gif")
    s.bgpic("quad.gif")
    girl.hideturtle()
    dog.hideturtle()
    sus.hideturtle()
    boy.hideturtle()
    player.up()
    player.goto(-450,270)
    player.down()
    text.clear()
    rules()


while nextScreen == 0:
    boy.onclick(chosen_boy_character)
    girl.onclick(chosen_girl_character)
    dog.onclick(chosen_dog_character)
    sus.onclick(chosen_sus_character)

s.listen()
s.onkey(up,"Up")
s.onkey(down,"Down")
s.onkey(left,"Left")
s.onkey(right,"Right")

s.ontimer(school_day,600000)
s.mainloop()


#######################SCREEN2######################################

turtle.addshape("miniscoot.gif")
turtle.addshape("book.gif")
turtle.addshape("teacher.gif")
turtle.addshape("food.gif")
turtle.addshape("dumbbell.gif")

scooter.shape("miniscoot.gif")
book.shape("book.gif")
teacher.shape("teacher.gif")
food.shape("food.gif")
gym.shape("dumbbell.gif")

##########################################################