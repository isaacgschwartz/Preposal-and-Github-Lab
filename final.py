import turtle
import random
screen_width = 800
screen_height = 800
craft = turtle.Turtle()
screen = turtle.Screen()
indicator = turtle.Turtle()
lose_indicator = turtle.Turtle()
boss = turtle.Turtle()
shoot_next = False
monsters_and_dead = {}
for i in range(7):
    monster_name = "monster_" + str(i)
    globals()[monster_name] = turtle.Turtle()
    monsters_and_dead[monster_name] = False
monsters_and_dead["boss"] = False

def create_monsters():
    global monsters_and_dead
    monsters_and_dead_no_boss = monsters_and_dead.copy()
    monsters_and_dead_no_boss.pop("boss")
    monster_width = 100
    for i, monster in enumerate(monsters_and_dead_no_boss):
        x = (600/6) * i + 100
        y = -1 * abs(0.5 * x - 200) + 200
        current_turtle = globals()[monster]
        current_turtle.hideturtle()
        current_turtle.penup()
        current_turtle.shape("monster.gif")
        current_turtle.showturtle()
        current_turtle.setpos(x,y)
    

def setup():
    #setting up window and coordinates system
    turtle.setup(screen_width, screen_height, 0, 0)
    turtle.setworldcoordinates(0,screen_width,screen_height,0)
    
    #putting craft in position
    craft.penup()
    craft.speed(0)
    craft.setpos(screen_width/2, screen_height - 200)
    craft.right(90)
    #setting background color
    screen.bgcolor("black")
    #registering shapes to be used throughout program
    screen.register_shape("craft.gif")
    screen.register_shape("shoot.gif")
    screen.register_shape("move.gif")
    screen.register_shape("monster.gif")
    screen.register_shape("boss_monster.gif")
    screen.register_shape("you_lose.gif")
    screen.register_shape("you_win.gif")
    #setting craft shape, speed
    craft.shape("craft.gif")
    craft.speed(5)
    #setting up indicator position and heading
    indicator.setpos(screen_width/2,760)
    indicator.left(90)
    indicator.speed(5)
    #create monsters
    create_monsters()
    #setting up boss
    boss.hideturtle()
    boss.penup()
    boss.speed(0)
    boss.shape("boss_monster.gif")
    boss.setpos(screen_width/2, -40)
    boss.showturtle()
    boss.speed(1)
    boss.setpos(screen_width/2,60)
    return (craft, screen)

def reset():
    global monsters_and_dead
    craft.showturtle()
    for monster in monsters_and_dead:
        monsters_and_dead[monster] = False
        current_turtle = globals()[monster]
        current_turtle.showturtle()

def you_lose(outcome):
    lose_indicator.hideturtle()
    if outcome == True:
        lose_indicator.shape("you_lose.gif")
    else:
        lose_indicator.shape("you_win.gif")
    lose_indicator.speed(0)
    lose_indicator.setpos(0 - screen_width,screen_height/2)
    lose_indicator.showturtle()
    lose_indicator.speed(2)
    lose_indicator.penup()
    lose_indicator.setpos(screen_width*2,screen_height/2)

def enemy_fire():
    global monsters_and_dead
    possible_shooters = []
    for monster in monsters_and_dead:
        if monsters_and_dead[monster] == False:
            possible_shooters.append(monster)
    shooter = random.choice(possible_shooters)
    bullet = turtle.Turtle()
    bullet.hideturtle()
    bullet.speed(0)
    bullet.penup()
    bullet.color("light blue")
    bullet.shape("circle")
    bullet.turtlesize(0.5)
    shooter_turtle = globals()[shooter]
    x = shooter_turtle.xcor()
    y = shooter_turtle.ycor()
    bullet.setpos(x,y)
    bullet.speed(4)
    bullet.showturtle()
    bullet.setpos(x,y+800)

    #checking for player hit
    if craft.xcor() - 50 < x < craft.xcor() + 50:
        craft.hideturtle()
        you_lose(True)
        reset()
    

def check_for_kill():
    global monsters_and_dead
    location = craft.xcor()
    for i in range(7):
        min_value = (600/6) * i + 50
        max_value = (600/6) * i + 150
        if max_value > location > min_value:
            globals()[list(monsters_and_dead)[i]].hideturtle()
            if i == 0:
                monsters_and_dead['monster_0'] = True
            elif i == 1:
                monsters_and_dead['monster_1'] = True
            elif i == 2:
                if monsters_and_dead['monster_2'] == True:
                    boss.hideturtle()
                    monsters_and_dead['boss'] = True
                else:
                    monsters_and_dead['monster_2'] = True
            elif i == 3:
                if monsters_and_dead['monster_3'] == True:
                    boss.hideturtle()
                    monsters_and_dead['boss'] = True
                else:
                    monsters_and_dead['monster_3'] = True
            elif i == 4:
                if monsters_and_dead['monster_4'] == True:
                    boss.hideturtle()
                    monsters_and_dead['boss'] = True
                else:
                    monsters_and_dead['monster_4'] = True
            elif i == 5:
                monsters_and_dead['monster_5'] = True
            elif i == 6:
                monsters_and_dead['monster_6'] = True
    if False not in monsters_and_dead.values():
        you_lose(False)
        reset()    

def indicate_move(): #indicator moves out of screen, displays "move" and reappears
    indicator.forward(100)
    indicator.shape("move.gif")
    indicator.back(100)
    
def indicate_shoot(): ##indicator moves out of screen, displays "shoot" and reappears
    indicator.forward(100)
    indicator.shape("shoot.gif")
    indicator.back(100)
    

def move(x,y): #disables movement on click, moves craft, enables shooting ability, changes indicator
    global shoot_next
    screen.onclick(dont_move)
    shoot_next = True
    craft.setpos(x,y)
    enemy_fire()
    screen.onkeypress(shoot, key="space")
    indicate_shoot()

def shoot(): #disables shooting, shoots, enables movement, changes indicator, checks for kills
    global shoot_next
    screen.onkeypress(dont_shoot, key="space")
    shoot_next = False
    bullet = turtle.Turtle()
    bullet.speed(0)
    bullet.hideturtle()
    bullet.penup()
    bullet.color("light blue")
    bullet.shape("circle")
    bullet.turtlesize(0.5)
    bullet.setpos(craft.xcor(),craft.ycor() -30)
    bullet.right(90)
    bullet.showturtle()
    bullet.speed(7)
    bullet.forward(1000)
    check_for_kill()
    screen.onclick(move)
    indicate_move()
    

def dont_shoot(): #disabling function
    pass
def dont_move(x,y): #disabling function
    pass
    

def main():
    (craft, screen) = setup()
    screen.onclick(move)
    screen.onkeypress(shoot, key="space")
    screen.listen()

main()

