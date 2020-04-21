from agent import Qlearning
import matplotlib.pylab as plt

from game import Game
from teacher import Teacher


def plot_agent_reward(rewards):
    names = ['wins', 'draws', 'loses']
    values = [rewards.count(1), rewards.count(0), rewards.count(-1)]
    plt.bar(names, values)
    plt.show()


class GameLearning:
    """
    A class that holds the state of the learning process. Learning
    agents are created/loaded here, and a count is kept of the
    games that have been played.
    """

    def __init__(self, alpha=0.5, gamma=0.9, epsilon=0.1):
        self.games_played = 0
        self.agent = Qlearning(alpha, gamma, epsilon)
        self.rewards = []

    def beginPlaying(self):
        """ Loop through game iterations with a human player. """
        game = Game(self.agent)
        self.rewards.append(game.start())
        self.games_played += 1
        return self.rewards

    def beginTeaching(self, episodes):
        teacher = Teacher(level=0.9)
        for i in range(episodes):
            game = Game(self.agent, teacher)
            self.rewards.append(game.start())
            self.games_played += 1
        return self.rewards


if __name__ == "__main__":
    game_learning = GameLearning()
    number_episodes = 10000
    plot_agent_reward(game_learning.beginTeaching(number_episodes))
    # tester l'agent sinon arreter le programme
    game_learning.beginPlaying()
