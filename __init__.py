from agent import Qlearning
from game import Game
from play import GameLearning
from teacher import Teacher

teacher = Teacher()
agent = Qlearning()
game = Game(agent, teacher)
game.playGame(True)
