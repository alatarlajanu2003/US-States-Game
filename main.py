import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

data = pandas.read_csv("50_states.csv")
cities = data.state.tolist()

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name? ").title()
    if answer_state == "Exit":
        break
    if answer_state in cities:
        score += 1
        cities.remove(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        tim.write(answer_state)

df = pandas.DataFrame(cities)
df.to_csv("states_to_learn.csv")
