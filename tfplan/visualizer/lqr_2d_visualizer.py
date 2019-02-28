import matplotlib.pyplot as plt

class LQR2DVisualizer():

    def __init__(self):
        super().__init__()

    def render(self, step_states, t_states, vx_states, vy_states, x_states, y_states):
        # Trajectory
        plt.figure(1)
        plt.xlabel('x')
        plt.ylabel('y')

        plt.plot(x_states, y_states)

        plt.title('LQR 2D Nav (Trajectory)', fontweight='bold')
        plt.grid(True)

        # State Variables
        plt.figure(2)
        plt.xlabel('time')
        plt.ylabel('variable')        

        plt.plot(step_states, t_states, label='t')
        plt.plot(step_states, vx_states, label='vx')
        plt.plot(step_states, vy_states, label='vy')
        plt.plot(step_states, x_states, label='x')
        plt.plot(step_states, y_states, label='y')

        plt.title('LQR 2D Nav (State Variables)', fontweight='bold')
        plt.legend(loc="best")

        plt.show()        