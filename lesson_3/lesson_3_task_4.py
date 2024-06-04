from turtle import *

cat = Turtle()
cat.speed(10)
cat.screen.setup(1200, 800)
cat.ht()

# Head
cat.circle(50)

# Left Eye
cat.penup()
cat.goto(-23,56)
cat.pendown()
cat.begin_fill()
cat.circle(5)
cat.end_fill()

# Winking Right Eye
cat.penup()
cat.goto(22,56)
cat.setheading(90)
cat.pendown()
cat.circle(5, 180)

# Nose
cat.penup()
cat.goto(4.5,41)
cat.setheading(180)
cat.pendown()
cat.begin_fill()
cat.forward(10)
cat.left(120)
cat.forward(10)
# print(cat.xcor())
# print(cat.ycor())
cat.left(120)
cat.forward(10)
cat.end_fill()

# Mouth
cat.penup()
cat.goto(-0.5000000000000178,32.339745962155625)
cat.setheading(-90)
cat.pendown()
cat.circle(5, 180)
cat.penup()
cat.goto(-0.5000000000000178,32.339745962155625)
cat.setheading(90)
cat.pendown()
cat.circle(5, -180)

# Right Ear
cat.penup()  
cat.goto(35,85)  # Position the cat to draw the right ear
cat.setheading(90)  
cat.pendown()  
cat.forward(25)  # Draw the base of the triangle
cat.left(120)  # Turn left for the first side
cat.forward(25)  # Draw the first side of the triangle

# Left Ear
cat.penup()  
cat.goto(-20,95)  # Position the cat to draw the left ear
cat.setheading(155)  
cat.pendown()  
cat.forward(25)  # Draw the base of the triangle
cat.left(120)  # Turn left for the first side
cat.forward(25)  # Draw the first side of the triangle

cat.screen.exitonclick()
cat.screen.mainloop()