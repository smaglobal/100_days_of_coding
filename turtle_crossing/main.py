from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from score_board import Scoreboard

screen = Screen()
screen.bgcolor("skyBlue")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    # Detect successful crossing
    if player.is_at_finished_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()