import matplotlib.pyplot as plt
import numpy as np
import random

class LQR1DGoalRecognitionVisualizer():

    def __init__(self):
        super().__init__()

    def render(self, initial_state, candidate_goals, correct_goal, observations, step_states, goals_ideal_x_states, goals_mirroring_x_states):
        plt.xlabel('step')
        plt.ylabel('x')
        x = initial_state[2]
        plt.plot(x, marker='^', markersize=15, color='black', label='Initial State')

        goal_counter = 0
        for goal in candidate_goals:
            color = np.random.rand(3,)
            x_states = goals_ideal_x_states[goal]
            x_mirroring_states = goals_mirroring_x_states[goal]
            goal_label = 'Candidate Goal '
            if goal == correct_goal:
                goal_label = 'Candidate (Correct Hidden) Goal '
            plt.plot(99, goal, marker='X', markersize=15, c=color, label=goal_label + str(goal_counter))
            plt.plot(x_states, linewidth=2, c=color, label='Ideal Trajectory - Goal ' + str(goal_counter))
            plt.plot(x_mirroring_states, linewidth=2, linestyle=(0, (1, 1)), c=color, label='Mirroring Trajectory - Goal ' + str(goal_counter))

            goal_counter += 1        

        obs_counter = 0
        for obs in observations:
            t = obs[0]
            x = obs[2]
            plt.plot(t, x-1, marker='H', markersize=15, color='gray', label='Observation ' + str(obs_counter))
            obs_counter += 1

        plt.title('LQR 1D Nav (Goal Recognition) - Problem 0', fontweight='bold')
        #plt.legend(loc='upper right')
        plt.legend(loc='lower left')
        plt.grid(True)
        
        plt.show()
        
        # n = random.randint(1,100)
        # plt.savefig('Figure ' + str(n) + ' .png')
        # plt.close()