# Created By: Sanjana Harichandran
# Purpose: Homework 3 - Practice using Graphics library
# Authenticity - I created this program / code on my own - This work is Authentic
# Created At: 09/27/2025
# Last Modified: 09/28/2025


# Import the Graphics library, random library and the time library
from graphics import *
import random
import time 

# Create the window called "Fall Greeting" with dimentions 500x500 and set background to darkblue
win = GraphWin("Fall Greeting", 500, 500)
win.setBackground("blue4")

# Draw a moon for spooky effect in the background 
moon = Circle(Point(70,60),50)
moon.setFill("white")
moon.setOutline("lightyellow")
moon.draw(win)

# Draw out random stars in the background
# Using loop for creating 90 tiny circles 
# Used Random library for random placement of stars
# Used time to allow ste stars to appear every 0.03 seconds
for s in range(90):
    x = random.randint(0,500)
    y = random.randint(0,500)
    stars = Circle(Point(x,y),2)
    stars.setFill("white")
    stars.setOutline("white")
    stars.draw(win)
    time.sleep(0.03)

# Creating a Greeting text
greet = Text(Point(270,160),"!HAPPY HALOWEEN!")
greet.setSize(30)
greet.setFill("darkorange")
greet.setOutline("red3")
greet.setStyle("bold")
greet.draw(win) 

# Creating the Pumpkin body 
# This is made of 3 ovals (pump_right, pump_left, pump_mid)
# Create a stem on top of pumpkin body (stem)
pump_right = Oval(Point(250,230),Point(380,420))
pump_right.setFill("darkorange")
pump_right.setOutline("red4")
pump_right.draw(win)

pump_left = Oval(Point(130,230),Point(260,420))
pump_left.setFill("darkorange")
pump_left.setOutline("red4")
pump_left.draw(win)

stem = Rectangle(Point(240,200),Point(270,250))
stem.setFill("green4")
stem.setOutline("red4")
stem.draw(win)

pump_mid = Oval(Point(170,230),Point(340,430))
pump_mid.setFill("darkorange")
pump_mid.setOutline("red4")
pump_mid.draw(win)

# Now creating the spooky face of the Pumpkin
# This is made od eyes, nose, mouth (left_eye, right_eye, nose, mouth)
left_eye = Polygon(Point(190,300),Point(240,300),Point(220,260))
left_eye.setFill("darkorange")
left_eye.setOutline("red4")
left_eye.draw(win)

right_eye = Polygon(Point(270,300),Point(320,300),Point(290,260))
right_eye.setFill("darkorange")
right_eye.setOutline("red4")
right_eye.draw(win)

nose = Polygon(Point(255,300),Point(230,340),Point(280,340))
nose.setFill("darkorange")
nose.setOutline("red4")
nose.draw(win)

mouth = Polygon(Point(190,350),Point(210,380),
                Point(240,380),Point(255,400),
                Point(270,380),Point(300,380),
                Point(320,350),Point(290,370),
                Point(270,360),Point(255,375),
                Point(240,360),Point(220,370))
mouth.setFill("darkorange")
mouth.setOutline("red4")
mouth.draw(win)

# Now THE LIGHTS!
# Creating the flicker effect using Nested Loop
# Here the range is set to 30 to change the color 30 times
# Using random.randint in color_rgb to randomly selet cours to be flickered in the pumpkin
# Then looped again to fill the randomly selected colors in the face of the pumpkin, text and the moon
# Lastly used the time library to set the flicker time to every 0.3 seconds 
for l in range(30):
    moon_color = color_rgb(255,random.randint(200,255),random.randint(100,180))
    color = color_rgb(random.randint(210,255),random.randint(150,255),random.randint(0,100))
    for flick in (greet,pump_left,pump_right,left_eye,right_eye,nose,mouth):
        flick.setFill(color)
    for flik in(moon,stars):
        flik.setFill(moon_color)
    time.sleep(0.3)
    
# At the end, Display the messase "Click anywhere" so that user clicks anywhere to close the program
end_msg = Text(Point(260,460),"Click anywhere to Close")
end_msg.setOutline("white")
end_msg.setSize(15)
end_msg.draw(win)

# getMouse() to click to close the program
win.getMouse()
win.close()