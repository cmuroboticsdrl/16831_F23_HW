from gym.envs.registration import register

register(
    id='pointmass-rob831-v0',
    entry_point='rob831.envs.pointmass:Pointmass',
    max_episode_steps=1000,
)
from rob831.envs.pointmass.pointmass import Pointmass
