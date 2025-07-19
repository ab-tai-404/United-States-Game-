from turtle import Turtle ,Screen
import pandas as pd

screen = Screen()
screen.bgpic("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
states  = []

for name_states in data.state :
    states.append(name_states)


timy = Turtle()
timy.penup()
timy.ht()

is_on = True
print(states)
while is_on :
    answer= screen.textinput("NIM", "Name of first player:")

    if answer in states :
        x = int(data[data.state == answer].x.iloc[0])
        y = int(data[data.state == answer].y.iloc[0])
        timy.goto(x, y)
        timy.write(f"{answer}", align='left', font=('Arial', 8, 'normal'))

    elif answer == "off" :
        is_on = False

screen.exitonclick()

