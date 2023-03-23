import pandas
import turtle


def get_mouse_click_coor(x, y):
    print(x,y)

def states_to_learn(states, guessed_states):
    for state in guessed_states:
        states.remove(state)
    
    
    df = pandas.DataFrame(states)
    df.to_csv("states_to_learn.csv")    

if __name__ == "__main__":
    states = pandas.read_csv("50_states.csv")
    correct_states = 0
    amount_of_states = len(states)
    correct_list = []
    
    screen = turtle.Screen()
    screen.title("50 US States")
    us_map = "blank_states_img.gif"
    screen.addshape(us_map)
    
    turtle.shape(us_map)
    #turtle.onscreenclick(get_mouse_click_coor)
    #turtle.mainloop()
    while len(correct_list) < 50:
        answer_state = screen.textinput(title=f"{correct_states}/{amount_of_states} States Correct", \
            prompt="What's another state's name?").title()
        state_list = states.state.to_list()
        
        if answer_state == "Exit":
            states_to_learn(state_list, correct_list)
            break
        
        if answer_state in state_list and answer_state not in correct_list:
            correct_list.append(answer_state)
            correct_states += 1
            
            correct_turtle = turtle.Turtle()
            correct_turtle.hideturtle()
            correct_turtle.penup()
            state_data = states[states.state == answer_state]
            correct_turtle.goto(int(state_data.x), int(state_data.y))
            correct_turtle.write(state_data.state.item())
    
    
    
    screen.exitonclick()
    