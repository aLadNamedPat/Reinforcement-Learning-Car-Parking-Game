import gym
from gym import spaces
import numpy as np
from gym_game.envs.pygame_2d import PyGame2D

class CustomEnv(gym.Env):
    #metadata = {'render.modes' : ['human']}
    def __init__(self):
        self.pygame = PyGame2D()
        self.action_space = spaces.Discrete(9)

        self.observation_space = gym.spaces.Box(
            low=0.,
            high=1.,
            shape=(11,),
            dtype=np.float32)

    def reset(self):
        del self.pygame
        self.pygame = PyGame2D()
        obs = self.pygame.observe()
        return obs

    def step(self, action):
        self.pygame.action(action)
        obs = self.pygame.observe()
        reward = self.pygame.evaluate()
        done = self.pygame.is_done()
        return obs, reward, done, {}

    def render(self, mode="human", close=False):
        self.pygame.view()
