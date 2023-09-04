from gym.envs.registration import register

def register_envs():
    register(
        id='cheetah-rob831-v0',
        entry_point='rob831.envs.cheetah:HalfCheetahEnv',
        max_episode_steps=1000,
    )
    register(
        id='obstacles-rob831-v0',
        entry_point='rob831.envs.obstacles:Obstacles',
        max_episode_steps=500,
    )
    register(
        id='reacher-rob831-v0',
        entry_point='rob831.envs.reacher:Reacher7DOFEnv',
        max_episode_steps=500,
    )
