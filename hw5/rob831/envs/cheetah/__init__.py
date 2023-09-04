from gym.envs.registration import register

register(
    id='cheetah-rob831-v0',
    entry_point='rob831.envs.cheetah:HalfCheetahEnv',
    max_episode_steps=1000,
)
from rob831.envs.cheetah.cheetah import HalfCheetahEnv
