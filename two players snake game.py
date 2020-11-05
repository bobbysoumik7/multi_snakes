import turtle
import time
import random

delay=0.1

#score
score=0
playerB=0

#set up the screen
wn=turtle.Screen()
wn.title("snake game by soumik")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)#turn off the screen updates

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(100,0)
head.direction="stop"
#snake head2
head2=turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("white")
head2.penup()
head2.goto(-100,0)
head2.direction="stop"



#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]
segs=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0  playerB: 0",align="center", font=("courier",24,"normal"))

#functions
def go_up():
   if head.direction !="down":
      head.direction="up"
def go_down():
   if head.direction !="up":
      head.direction="down"
def go_left():
   if head.direction !="right":
      head.direction="left"
def go_right():
   if head.direction !="left":
      head.direction="right"
#functions
def go_upa():
   if head2.direction !="down":
      head2.direction="up"
def go_downa():
   if head2.direction !="up":
      head2.direction="down"
def go_lefta():
   if head2.direction !="right":
      head2.direction="left"
def go_righta():
   if head2.direction !="left":
      head2.direction="right"




def move():
   if head.direction=="up":
      y=head.ycor()
      head.sety(y+20)
   if head.direction=="down":
      y=head.ycor()
      head.sety(y-20)
   if head.direction=="left":
      x=head.xcor()
      head.setx(x-20)
   if head.direction=="right":
      x=head.xcor()
      head.setx(x+20)
def move2():
   if head2.direction=="up":
      y=head2.ycor()
      head2.sety(y+20)
   if head2.direction=="down":
      y=head2.ycor()
      head2.sety(y-20)
   if head2.direction=="left":
      x=head2.xcor()
      head2.setx(x-20)
   if head2.direction=="right":
      x=head2.xcor()
      head2.setx(x+20)


#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
#keyboard bindings
wn.listen()
wn.onkeypress(go_upa,"w")
wn.onkeypress(go_downa,"s")
wn.onkeypress(go_lefta,"a")
wn.onkeypress(go_righta,"d")

#main game loop
while True:
   wn.update()

   #check for collision wiht the border
   if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
      time.sleep(1)
      head.direction="stop"
   if head2.xcor()>290 or head2.xcor()<-290 or head2.ycor()>290 or head2.ycor()<-290:
      time.sleep(1)
      head2.direction="stop"

      #hide the segments
      for segment in segments:
          segment.goto(1000,1000)
      for seg in segs:
             seg.goto(1000,1000)

      #clear the segments list
      segments.clear()
      segs.clear()
      #reset the score
      score=0

      #reset the delay
      delay=0.1

      pen.clear()
      pen.write("score:{} high score: {}".format(score, playerB),align="center",font=("courier",24,"normal"))  
   
   #check for colission with the food
   if head.distance(food)<19:
      x=random.randint(-290,290)
      y=random.randint(-290,290)
      food.goto(x,y)
   #check for colission with the food
   if head2.distance(food)<19:
      x=random.randint(-290,290)
      y=random.randint(-290,290)
      food.goto(x,y)
      

      #add a segment
      new_segment=turtle.Turtle()
      new_segment.speed(0)
      new_segment.shape("square")
      new_segment.color("black")
      new_segment.penup()
      segments.append(new_segment)
      #add a seg
      new_seg=turtle.Turtle()
      new_seg.speed(0)
      new_seg.shape("square")
      new_seg.color("white")
      new_seg.penup()
      segs.append(new_seg)


      #shorten the display
      delay-=0.001

      #increase the score
      score+=1

      if score>playerB:
         playerB=score
      pen.clear()
      pen.write("score:{} high score: {}".format(score, playerB),align="center",font=("courier",24,"normal"))

   #move the end segments first in reverse order
   for index in range(len(segments)-1,0,-1):
      x=segments[index-1].xcor()
      y=segments[index-1].ycor()
      segments[index].goto(x,y)
   #move2 the end segs first in reverse order
   for index in range(len(segs)-1,0,-1):
      x=segs[index-1].xcor()
      y=segs[index-1].ycor()
      segs[index].goto(x,y)


   #move segment 0 to where the head is
   if len(segments)>0:
      x=head.xcor()
      y=head.ycor()
      segments[0].goto(x,y)
   move()
   #move2 seg 0 to where the head2 is
   if len(segs)>0:
      x=head2.xcor()
      y=head2.ycor()
      segs[0].goto(x,y)
   move2()

   #move2 the end segs first in reverse order
   for index in range(len(segs)-1,0,-1):
      x=segs[index-1].xcor()
      y=segs[index-1].ycor()
      segs[index].goto(x,y)
   #move2 the end segs first in reverse order
   for index in range(len(segs)-1,0,-1):
      x=segs[index-1].xcor()
      y=segs[index-1].ycor()
      segs[index].goto(x,y)


   #check for head colission
   for segment in segments:
      if segment.distance(head)<20:
         time.sleep(1)
         head.goto(0,0)
         head.direction="stop"
   #check for head2 colission
   for seg in segs:
      if seg.distance(head2)<20:
         time.sleep(1)
         head2.goto(0,0)
         head2.direction="stop"



         #hide the segments
         for segment in segments:
             segment.goto(1000,1000)
         #hide the segs
         for seg in segs:
             seg.goto(1000,1000)
             
         #clear the segments list
         segments.clear()
         segs.clear()

         #reset the score
         score=0
         #reset the delay
         delay=0.1
         #update the score display
         pen.clear()
         pen.write("score:{} high score: {}".format(score, playerB),align="center",font=("courier",24,"normal"))
   
   time.sleep(delay)

wn.mainloop()

