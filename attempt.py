from tkinter import *
from random import random as rnd, choice, randint
from time import sleep

# renaming tkinter to root
root = Tk()

# renaming canvas and setting background color
canv = Canvas(root, bg='khaki')

# creating game constants
width = 800
height = 600
basic_vel = 15
total_lifetime = 100
ball_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'tomato', 'cornflower blue', 'hot pink']

# visual borders of the field
canv.create_line(0, 0, width, 0)
canv.create_line(0, 0, 0, height)
canv.create_line(0, height, width, height)
canv.create_line(width, height, width, 0)

# some technical things
root.geometry(str(width) + 'x' + str(height))
canv.pack(fill=BOTH, expand=1)


class Game:
    """
    This class is responsible
    for leading the score of the game,
    for adding and removing balls
    (actually it calls the functions from Balls class rather than creates them).
    """
    def __init__(self, max_amount_of_balls):
        """
        Creates a list of currently existing balls,
        sets counters.
        """
        self.balls = []
        self.cnt = 0
        self.n = max_amount_of_balls
        self.score = 0
        self.missed = 0

    def add_ball(self):
        """ Adds a ball to the list of balls. """
        number = self.n * self.score + self.cnt + self.missed
        ball = Ball(number)
        self.cnt += 1
        self.balls.append(ball)

    def delete_ball(self, num):
        """
        Deletes the clicked ball from the list,
        adds a new one,
        corrects the score.
        """
        ball = self.balls[num]
        ball.clear()
        self.balls.pop(num)
        self.missed += 1
        self.cnt -= 1
        self.add_ball()

    def click(self, event):
        """
        Reads the coords of the click point,
        calls a function that checks if the click point is inside of the ball.
        If inside, deletes the ball from the list and corrects the score.
        """
        point = [event.x, event.y]
        for j in range(len(self.balls)):
            if j >= len(self.balls):
                break
            ball = self.balls[j]
            if ball.click(point):
                self.balls.pop(j)
                self.cnt -= 1
                self.score += 1
            while self.cnt < self.n:
                self.add_ball()

    def show_score(self):
        """ Outputs a widget with score. """
        canv.delete('text')
        canv.create_rectangle(40, 80, 160, 120, fill="cyan")
        canv.create_text(100, 100, text=('Score: ' + str(self.score) + ' / ' + str(self.score + self.missed)),
                         justify=CENTER, font="Impact 16", tag='text')


class Ball:
    """
    This class is responsible
    for creating the parameters of a ball
    for describing the draw and clear functions
    for describing the conditions of removing the ball.
    """
    def __init__(self, number):
        """
        sets random coords, velocity and color of a ball
        :param number: index of the ball in the list of balls
        """
        self.x = randint(100, width - 100)
        self.y = randint(100, height - 100)
        self.r = randint(30, 50)
        self.tag = 'ball' + str(number)
        self.horizontal_velocity = rnd() * basic_vel
        self.vertical_velocity = rnd() * basic_vel
        self.color = choice(ball_colors)
        self.lifetime = 0

    def draw(self):
        canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                         fill=self.color, width=0, tag=self.tag)

    def clear(self):
        canv.delete(self.tag)

    def move(self):
        """
        Sets the rules of movement.
        If the ball touches the wall, its normal velocity is reversed.
        After the ball makes a step, it gets repainted.
        """
        self.lifetime += 1
        self.x += self.horizontal_velocity
        self.y += self.vertical_velocity
        if (self.x >= (width - self.r)) or (self.x <= self.r):
            self.x -= self.horizontal_velocity
            self.horizontal_velocity *= -1
        if (self.y >= (height - self.r)) or (self.y <= self.r):
            self.y -= self.vertical_velocity
            self.vertical_velocity *= -1
        self.clear()
        self.draw()

    def is_in(self, point):
        """
        Checks whether the click point is inside of the ball.
        :param point: click point
        """
        x, y = point[0], point[1]
        if self.r ** 2 >= (x - self.x) ** 2 + (y - self.y) ** 2:
            return True
        return False

    def click(self, point):
        """
        Removes the ball if the click point is inside it.
        :param point: click point
        """
        if self.is_in(point):
            self.clear()
            return True
        return False


# Creating the game with two balls on the field.
def start_game(number_of_balls):
    global the_game
    the_game = Game(number_of_balls)
    for c in range(number_of_balls):
        the_game.add_ball()


start_game(2)


def click(event):
    the_game.click(event)


# making the program read the clicks
canv.bind('<Button-1>', click)


# setting list of the balls that are to be deleted
# (you will see the sense of it later)
to_delete = []


while True:
    """ 
    Checking the lifetime of every ball from the list of balls. 
    If any ball lives for more than total_lifetime, it is added to the to_delete list and is deleted
    """
    for i in range(len(the_game.balls)):
        this_ball = the_game.balls[i]
        if this_ball.lifetime < total_lifetime:
            this_ball.move()
        else:
            to_delete.append(i)
    for k in to_delete:
        the_game.delete_ball(k)

    """updating the to_delete list"""
    to_delete = []
    the_game.show_score()

    sleep(0.03)
    root.update()
