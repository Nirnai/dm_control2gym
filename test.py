import gym
import dm_control2gym

env = dm_control2gym.make(domain_name="walker", task_name="run")
env.reset()