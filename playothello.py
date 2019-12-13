import gym
import random
import numpy as np
env = gym.make('Othello8x8-v0')
env.reset()
for i_episode in range(20):
    env.render()
    observation = env.reset()
    for t in range(100):
        enables = env.possible_actions
        #Human player
        print("Possible moves: ", enables)
        m = input("Enter your move: ")
        action = m
        env.render()
        
        #AI player
        # if nothing to do ,select pass
        if len(enables)==0:
            action = env.board_size**2 + 1
        # random select
        else:
            action = random.choice(enables)
        observation, reward, done, info = env.step(action)
        env.render()
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            black_score = len(np.where(env.state[0,:,:]==1)[0])
            white_score = len(np.where(env.state[1,:,:]==1)[0])
            print("Black pieces: ",black_score)
            print("White pieces: ",white_score)
            break

env.close()
