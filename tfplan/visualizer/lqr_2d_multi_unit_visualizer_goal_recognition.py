import matplotlib.pyplot as plt
import numpy as np
import random

class LQR2DMultiUnitGoalRecognitionVisualizer():

    def __init__(self):
        super().__init__()

    def render(self, initial_state, candidate_goals, correct_goal, observations, step_states, goals_ideal_states, goals_mirroring_states):
        plt.xlabel('step')
        plt.ylabel('x')
        v002_x = initial_state[5]
        v001_x = initial_state[6]
        v002_y = initial_state[7]
        v001_y = initial_state[8]
        plt.plot(v002_x, v002_y, marker='^', markersize=15, color='black', label='Initial State (v001)')
        plt.plot(v001_x, v001_y, marker='d', markersize=15, color='black', label='Initial State (v002)')

        goal_counter = 0
        for goal in candidate_goals:
            color = np.random.rand(3,)
            goal_ideal_states = goals_ideal_states[goal]
            mirroring_states = goals_mirroring_states[goal]

            v002_ideal_x = (goal_ideal_states[0] if len(goal_ideal_states[0]) == 100 else [(x[0]) for x in goal_ideal_states])
            v001_ideal_x = (goal_ideal_states[1] if len(goal_ideal_states[2]) == 100 else [(x[2]) for x in goal_ideal_states])
            v002_ideal_y = (goal_ideal_states[2] if len(goal_ideal_states[1]) == 100 else [(y[1]) for y in goal_ideal_states])
            v001_ideal_y = (goal_ideal_states[3] if len(goal_ideal_states[2]) == 100 else [(y[2]) for y in goal_ideal_states])

            v002_m_x = (mirroring_states[0] if len(mirroring_states[0]) == 100 else [(x[0]) for x in mirroring_states])
            v001_m_x = (mirroring_states[1] if len(mirroring_states[2]) == 100 else [(x[2]) for x in mirroring_states])
            v002_m_y = (mirroring_states[2] if len(mirroring_states[1]) == 100 else [(y[1]) for y in mirroring_states])
            v001_m_y = (mirroring_states[3] if len(mirroring_states[2]) == 100 else [(y[2]) for y in mirroring_states])            
            
            goal_label = 'Candidate Goal '
            if goal == correct_goal:
                goal_label = 'Candidate (Correct Hidden) Goal '
            
            plt.plot(goal[0], goal[1], marker='X', markersize=15, c=np.random.rand(3,), label=goal_label + str(goal_counter))
            plt.plot(v001_ideal_x, v001_ideal_y, linewidth=2, c=np.random.rand(3,), label='Ideal Trajectory - Goal (v001): ' + str(goal_counter))
            plt.plot(v002_ideal_x, v002_ideal_y, linewidth=2, c=np.random.rand(3,), label='Ideal Trajectory - Goal (v002): ' + str(goal_counter))
            
            plt.plot(v001_m_x, v001_m_y, linewidth=2, linestyle=(0, (1, 1)), c=np.random.rand(3,), label='Mirroring Trajectory - Goal (v001): ' + str(goal_counter))
            plt.plot(v002_m_x, v002_m_y, linewidth=2, linestyle=(0, (1, 1)), c=np.random.rand(3,), label='Mirroring Trajectory - Goal (v002): ' + str(goal_counter))

            goal_counter += 1        

        obs_counter = 0
        for obs in observations:
            t = obs[0]
            x_v002 = obs[5]
            x_v001 = obs[6]
            y_v002 = obs[7]
            y_v001 = obs[8]
            plt.plot(x_v001, y_v001, marker='H', markersize=15, color='gray', label='Observation (v001): ' + str(obs_counter))
            plt.plot(x_v002, y_v002, marker='D', markersize=15, color='gray', label='Observation (v002): ' + str(obs_counter))
            obs_counter += 1

        plt.title('LQR 2D Nav Multi-Unit (Goal Recognition)', fontweight='bold')
        #plt.legend(loc='upper right')
        #plt.legend(loc='lower left')
        plt.grid(True)
        
        plt.show()        
        # n = random.randint(1,100)
        # plt.savefig('Figure ' + str(n) + ' .png')
        # plt.close()