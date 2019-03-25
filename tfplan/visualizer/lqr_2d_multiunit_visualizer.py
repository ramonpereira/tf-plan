import matplotlib.pyplot as plt

class LQRMultiUnit2DVisualizer():

    def __init__(self):
        super().__init__()

    def render(self, step_states, t_states, vx_states_unit1, vx_states_unit2, vy_states_unit1, vy_states_unit2, x_states_unit1, x_states_unit2, y_states_unit1, y_states_unit2):
        # Trajectory
        plt.figure(1)
        plt.xlabel('x')
        plt.ylabel('y')

        plt.plot(x_states_unit1, y_states_unit1)
        plt.plot(x_states_unit2, y_states_unit2)

        plt.title('LQR 2D Nav Multi Unit (Trajectory)', fontweight='bold')
        plt.grid(True)

        # State Variables
        plt.figure(2)
        plt.xlabel('time')
        plt.ylabel('variable')

        plt.plot(step_states, t_states, label='t')
        plt.plot(step_states, vx_states_unit1, label='vx (v001)')
        plt.plot(step_states, vx_states_unit2, label='vy (v002)')
        plt.plot(step_states, vy_states_unit1, label='vx (v001)')
        plt.plot(step_states, vy_states_unit2, label='vy (v002)')

        plt.title('LQR 2D Nav Multi Unit (State Variables)', fontweight='bold')
        plt.legend(loc="best")

        plt.show()        