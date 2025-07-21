from turtle import Turtle ,Screen
import pandas as pd

screen = Screen()
image = "blank_states_img.gif"
screen.bgpic(image)
screen.title("U.S. States Game")

data = pd.read_csv("50_states.csv")
all_states  = data.state.to_list()


timy = Turtle()
timy.penup()
timy.ht()
correct_answer = []
is_on = 50

while len(correct_answer) < 50 :
    print(all_states)
    answer_state = screen.textinput(f"{len(correct_answer)}/50 States Correct",
                                    "Name of first player:").title()
    answer= answer_state.lower()
    print(answer)
    if answer_state in all_states :
        state_data = data[data.state == answer_state]
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        timy.goto(x, y)
        timy.write(f"{answer_state}", align='left', font=('Arial', 9 , 'normal'))
        correct_answer.append(answer_state)
    elif answer_state == "Exit" :
        state_not_know = [item for item in all_states if item not in correct_answer]
        df = pd.DataFrame(state_not_know)
        df.to_csv("states_to_learn.csv")
        break


screen.exitonclick()
