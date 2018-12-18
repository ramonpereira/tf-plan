import matplotlib.pyplot as plt

class LQGVisualizer():

    def __init__(self):
        super().__init__()

    def render(self, step_states, t_states, v_states, x_states):
        # Trajectory
        plt.figure(1)
        plt.xlabel('step')
        plt.ylabel('x')

        plt.plot(step_states, x_states)

        plt.title('LQG 1D Nav (Trajectory)', fontweight='bold')
        plt.grid(True)

        # State Variables
        plt.figure(2)
        plt.xlabel('time')
        plt.ylabel('variable')        

        plt.plot(step_states, t_states, label='t')
        plt.plot(step_states, v_states, label='v')
        plt.plot(step_states, x_states, label='x')

        plt.title('LQG 1D Nav (State Variables)', fontweight='bold')
        plt.legend(loc="best")

        plt.show()        