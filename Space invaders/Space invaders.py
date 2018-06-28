import turtle
import os
import math
import random
import winsound

wn = turtle.Screen()                 # Importing screen
wn.bgcolor("black")                  # Background colour
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")   # This file must be in the same location as the python file

# Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)                  # 0 is draws the fastest
border_pen.color("white")
border_pen.penup()                   # penup to take the pen up
border_pen.setposition(-300, -300)   # center is (0,0)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)              # left to right
    border_pen.lt(90)               # Turn left 90 degrees
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the PLAYER turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)         # Center and down 250
player.setheading(90)

playerspeed = 15



# Create BULLET turtle
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# bullet has multiple states
# 1) Hidden, ready to be fire
# 2) Fired, in the middle of moving
bulletstate = "ready"



# Choose a number of enemies
number_of_enemies = 5
# Create an empty list of enemies
enemies = []
# Add enemies to the list
for i in range(number_of_enemies):
    # Create ENEMY turtles
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2



# Function to move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:                    # boundary checking
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

# Functions for bullets
def fire_bullet():
    # Declar bulletstate as a golbal if state is changed
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("laser", winsound.SND_ASYNC)
        bulletstate = "fire"
        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollsion(t1, t2):
    # Pytheagorean theorem
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False



# Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')
turtle.onkeypress(fire_bullet, "space")

game_on = True

# Main game loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

            # Check for a collision between the bullet and the enemy
        if isCollsion(bullet, enemy):
            # Reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            winsound.PlaySound("explosion", winsound.SND_ASYNC)


        if isCollsion(player, enemy) or enemy.ycor() < -250:
            winsound.PlaySound("explosion", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            game_on = False

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # boundary checking for the bullet
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    if not game_on:
        print("Game over!")
        break

delay = input("Press enter to finish.")            # Delay to keep the screen open