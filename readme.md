Link to project overview video: https://youtu.be/w6OMMBi8gGo

Some difficulties I overcame:
I wanted to create many monster (turtle) objects but I didn't want to create their names manually so I learned about accessing the list of
global variables. I found a way to add a string into the global variables list as a variable name, and I learned how to
access those global variables that I had created within my functions. (  for example,  globals()[monster_name] = turtle.Turtle()   ).

I found myself actually applying math concepts that I never thought I would use, for example, I wrote an absolute value function that would
outline where the monsters would be placed across the canvas.

I also found ways to optimize my code to prevent lag. For example, originally I created a new turtle each time I wanted to indicate "shoot" or "move"
to the player. After seeing that creating all these turtles lagged the game, I redesigned my code to use one turtle that would change it's shape
to display a different image ("shoot" or "move").

I learned the power of dictionaries, because one of my most used variables in this code is a dictionary that stores all the string names
of the monster turtles, and a boolean telling me if that monster is dead. This helped me keep track of the monsters as well as iterate through them.