import matplotlib.pyplot as plt

class CarParkingVisualizer():

    def __init__(self):
        super().__init__()

    def render(self, step_states, x_states, y_states, theta_states, v_states):
        # Trajectory
        plt.figure(1)
        plt.xlabel('x')
        plt.ylabel('y')        

        plt.plot(x_states, y_states)

        plt.title('CarParking (Trajectory)', fontweight='bold')
        plt.grid(True)

        # State Variables
        plt.figure(2)
        plt.xlabel('time')
        plt.ylabel('variable')        

        plt.plot(step_states, x_states, label='x')
        plt.plot(step_states, y_states, label='y')
        plt.plot(step_states, theta_states, label='theta')
        plt.plot(step_states, v_states, label='v')

        plt.title('CarParking (State Variables)', fontweight='bold')
        plt.legend(loc="best")

        plt.show()        