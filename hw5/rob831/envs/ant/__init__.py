from gym.envs.registration import register

register(
    id='ant-rob831-v0',
    entry_point='rob831.envs.ant:AntEnv',
    max_episode_steps=1000,
)
from rob831.envs.ant.ant import AntEnv
