import turtle
turtle.speed(1) 
turtle.delay(0) 
r=330 
size=10  
colors=["#ff0000","#ff7f00","#ffff00","#00ff00","#00ffff","#0000ff","#8b00ff"] 
for i in range(7): 
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(r,-50) 
    turtle.pendown()
    turtle.pencolor(colors[i]) 
    turtle.pensize(size)     
    turtle.circle(r,180)       
    r=r-size+1
