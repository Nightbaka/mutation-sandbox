import numpy as np
import os

import neat
import visualize
import gymnasium
import random


class Game:
    def __init__(self):
        pass

    def eval(self, genomes, config):
        pass


class NEAT_wrap:
    def __init__(self, game: Game, config, reporters) -> None:
        self.game = game
        self.reporters = reporters
        self.config = config

    def run(
        self,
    ):
        # Create the population, which is the top-level object for a NEAT run.
        p = neat.Population(self.config)
        for reporter in self.reporters:
            p.add_reporter(reporter)

        winner = p.run(self.game.eval, 300)
        p.run(self.game.eval, 10)
        return winner


class Cartpole(Game):
    def __init__(self, genome_saver, render_mode):
        self.env = gymnasium.make("CartPole-v1", render_mode=render_mode)
        self.ideal_pos = 0
        self.saver = genome_saver

    def eval(self, genomes, config):
        for genomeid, genome in genomes:
            self.episode(genome, config)

    def episode(self, genome, config):
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        observation, info = self.env.reset()
        self.ideal_pos = 1.2
        observation = np.append(observation, self.ideal_pos)
        for i in range(500):
            if i % 100 == 99:
                self.ideal_pos = -self.ideal_pos
            action = net.activate(observation)
            action = 0 if action[0] < 0.5 else 1

            # save information about game
            if self.saver:
                self.saver.save(genome, action, observation, self.ideal_pos, i)

            observation, reward, done, truncated, info = self.env.step(action)
            distance = abs(observation[0] - self.ideal_pos)
            normalized_distance = distance / 2.4

            genome.fitness += reward * (1 - normalized_distance)
            observation = np.append(observation, self.ideal_pos)
            if done or truncated:
                self.env.close()
                self.genome_saver.end(genome, i, self.ideal_pos, observation)
                break

class ConfigBuilder:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = None

    def get(self):
        self.config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                           neat.DefaultSpeciesSet, neat.DefaultStagnation,
                           self.config_file)
    
    def set(self):
        self.config = config
