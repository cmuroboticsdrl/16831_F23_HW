from gym.envs.registration import register

register(
    id='obstacles-rob831-v0',
    entry_point='rob831.envs.obstacles:Obstacles',
    max_episode_steps=500,
)
from rob831.envs.obstacles.obstacles_env import Obstacles
