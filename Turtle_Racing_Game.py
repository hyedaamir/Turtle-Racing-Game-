import random
import time
from turtle import Screen, Turtle
TRACK_COLOR = "#2e8b57"  # Forest/Grass Green
LANE_LINE_COLOR = "#ffffff"  # White for boundaries
START_LINE_COLOR = "#ffd700"  # Gold start line
FINISH_LINE_COLOR = "#ff4500"  # Orangish-Red finish line
TEXT_COLOR = "#1a1a1a"  # Dark gray for sharp visual contrast

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [140, 80, 20, -40, -100, -160]


def draw_race_track():

    drawer = Turtle()
    drawer.hideturtle()
    drawer.speed("fastest")

    drawer.penup()
    drawer.goto(-280, 200)
    drawer.pendown()
    drawer.color("#1e272e")
    drawer.pensize(5)
    for _ in range(2):
        drawer.forward(560)
        drawer.right(90)
        drawer.forward(400)
        drawer.right(90)

    drawer.pensize(2)
    drawer.color("#dcdde1")
    for y in [110, 50, -10, -70, -130]:
        drawer.penup()
        drawer.goto(-280, y)
        while drawer.xcor() < 280:
            drawer.pendown()
            drawer.forward(15)
            drawer.penup()
            drawer.forward(15)

    drawer.penup()
    drawer.goto(-220, 190)
    drawer.pendown()
    drawer.color(START_LINE_COLOR)
    drawer.pensize(6)
    drawer.goto(-220, -190)

    drawer.penup()
    drawer.goto(-220, 205)
    drawer.write("START", align="center", font=("Century Gothic", 12, "bold"))

    drawer.penup()
    drawer.goto(230, 190)
    drawer.pendown()
    drawer.color(FINISH_LINE_COLOR)
    drawer.pensize(10)
    drawer.goto(230, -190)

    drawer.penup()
    drawer.goto(230, 205)
    drawer.color("red")
    drawer.write("FINISH ", align="center", font=("Century Gothic", 12, "bold"))


def show_bet_popup(screen):

    return screen.textinput(
        title=" PLACE YOUR BET!",
        prompt="Which turtle will win the race?\nChoose a color: Red, Orange, Yellow, Green, Blue, Purple",
    )


def show_game_result(winner_color, user_bet):

    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, 0)

    if winner_color == user_bet:
        writer.color("#2ecc71")  # Bright green for win
        result_text = f" YOU WON! \nThe {winner_color.upper()} turtle is the champion!"
    else:
        writer.color("#e74c3c")  # Red for loss
        result_text = f"Better Luck Next Time! \nThe {winner_color.upper()} turtle won.\n(Your bet: {user_bet.upper()})"

    writer.write(result_text, align="center", font=("Century Gothic", 18, "bold"))


def main():
    screen = Screen()
    screen.setup(width=620, height=520)
    screen.title(" Super Turtle Championship ")
    screen.bgcolor("#f1f2f6")

    user_bet = show_bet_popup(screen)

    if not user_bet:
        print("Bet canceled. Exiting game.")
        screen.bye()
        return

    user_bet = user_bet.lower().strip()

    if user_bet not in COLORS:
        print("Invalid turtle color selected!")
        screen.bye()
        return

    draw_race_track()

    all_turtles = []
    for idx in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(COLORS[idx])
        new_turtle.shapesize(stretch_len=1.4, stretch_wid=1.4)  # Size slightly scaled
        new_turtle.penup()

        new_turtle.goto(x=-240, y=Y_POSITIONS[idx])
        all_turtles.append(new_turtle)

    countdown = Turtle()
    countdown.hideturtle()
    countdown.penup()
    countdown.goto(0, 0)
    countdown.color("#2c3e50")
    for count in ["3...", "2...", "1...", "GO! 🔥"]:
        countdown.write(count, align="center", font=("Impact", 36, "italic"))
        time.sleep(0.6)
        countdown.clear()

    is_race_on = True
    winner_color = None

    while is_race_on:
        for turtle in all_turtles:

            random_distance = random.randint(3, 11)
            turtle.forward(random_distance)

            if turtle.xcor() > 215:
                is_race_on = False
                winner_color = turtle.pencolor()
                break

    show_game_result(winner_color, user_bet)

    screen.exitonclick()

if __name__ == "__main__":
    main()