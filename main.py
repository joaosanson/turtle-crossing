import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.onkeypress(player.go_up, "W")
screen.onkeypress(player.go_up, "w")

score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.reset()
        car_manager.increase_speed()
        score.points()

    for car in car_manager.all_cars:
        if car.distance(player) < 15:
            game_is_on = False
            score.finished()
            player.finish()
screen.exitonclick()
