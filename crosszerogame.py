import turtle as t
screen = t.Screen()
t.pensize(2)
t.color("black")
t.begin_fill()
t.penup()
t.goto(x=-150,y=-150)
t.pendown()
t.speed(0)

def square() -> None:
    i = 0 
    while i < 4:
        t.forward(100)
        t.left(90)
        i += 1
    
y = -150   
b = 0
while b <3:
    t.penup()
    t.goto(x=-150,y=y)
    t.pendown()  
    o = 0
    while o < 3:
        square()
        t.forward(100)
        o += 1
    b += 1
    y += 100

    
def cross(x:float,y:float) -> None:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(x+100,y-100)
    t.penup()
    t.goto(x+100,y)
    t.pendown()
    t.goto(x,y-100)
    
def circle(x:float,y:float) -> None:
    t.penup()
    t.goto(x+50,y-100)
    t.pendown()
    t.circle(50)

coords_y = [150,50,-50]

coords_x = [-150,-50,50]
    
def on_screen_click(x:float,y:float)->None:
    for el in coords_y:
            if el > y > el - 100:
                    for el1 in coords_x:
                        if el1 < x < el1 + 100:
                            print(f"координати {x,y} є в радіусі {el,el1}")
                    

list_x_i_y=[[-150,150],[-50,150],[50,150],
            [-150,50],[-50,50],[50,50]
            ,[-150,-50],[-50,-50],[50,-50]]
list_with_0 = [0,0,0,0,0,0,0,0,0]
    
        
turn = 1
game_over = False
list_of_victoties = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


def check_line(start_index,end_index):
    if end_index - start_index == 2:
        start_x = list_x_i_y[start_index][0]
        start_y = list_x_i_y[start_index][1] - 50
        end_x = list_x_i_y[end_index][0] + 100
        end_y = list_x_i_y[end_index][1] - 50
        t.penup()
        t.goto(start_x,start_y)
        t.pendown()
        t.goto(end_x,end_y)
    elif end_index - start_index == 6:
        start_x = list_x_i_y[start_index][0] + 50
        start_y = list_x_i_y[start_index][1] 
        end_x = list_x_i_y[end_index][0] + 50
        end_y = list_x_i_y[end_index][1] - 100
        t.penup()
        t.goto(start_x,start_y)
        t.pendown()
        t.goto(end_x,end_y)
    elif end_index - start_index == 8:
        start_x = list_x_i_y[start_index][0]
        start_y = list_x_i_y[start_index][1] 
        end_x = list_x_i_y[end_index][0] + 100
        end_y = list_x_i_y[end_index][1] - 100
        t.penup()
        t.goto(start_x,start_y)
        t.pendown()
        t.goto(end_x,end_y)    
    elif end_index - start_index == 4:
        start_x = list_x_i_y[start_index][0] + 100
        start_y = list_x_i_y[start_index][1] 
        end_x = list_x_i_y[end_index][0] 
        end_y = list_x_i_y[end_index][1] - 100
        t.penup()
        t.goto(start_x,start_y)
        t.pendown()
        t.goto(end_x,end_y)


        
def check_draw()-> None:
    global game_over
    draw = True
    for elements in list_with_0:
        if elements == 0:
            draw = False
    if draw == True:
        t.hideturtle()
        t.penup()
        t.goto(0,200)
        t.pendown()
        t.color("orange")
        t.write(arg="Нічия",align="center",font=["Arial",32,"bold"])
        game_over = True

        
def check_victory():
    global game_over
    for elements in list_of_victoties:
        victory = elements
        if list_with_0[victory[0]] == list_with_0[victory[1]] == list_with_0[victory[2]]:
            if list_with_0[victory[0]] != 0:
                game_over = True
                t.hideturtle()
                t.penup()
                t.goto(0,200)
                t.pendown()
                t.pensize(4)
                t.color("green")
                t.write(arg=f"переміг гравець {turn}",align="center",font=["Arial",32,"bold"])
                check_line(start_index=victory[0], end_index=victory[2])                      
    if game_over == False:
        check_draw()


def click_left(x: float, y: float) -> None:
    global turn
    if game_over == False:
        i = 0
        for el in list_x_i_y:
            if el[0] < x < el[0] + 100:
                if el[1] > y > el[1] - 100:
                    if list_with_0[i] == 0:
                        if turn == 1:
                            cross(el[0], el[1])
                            list_with_0[i] = 1
                            check_victory()
                            turn = 2
                        elif turn == 2:
                            circle(el[0], el[1])
                            list_with_0[i] = 2
                            check_victory()
                            turn = 1
            i += 1    

screen.onscreenclick(fun=click_left,btn=1) 

screen.mainloop()