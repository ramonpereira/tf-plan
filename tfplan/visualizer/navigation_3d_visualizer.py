# This file is part of tf-rddlsim.

# tf-rddlsim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# tf-rddlsim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with tf-rddlsim. If not, see <http://www.gnu.org/licenses/>.


from tfrddlsim.viz.abstract_visualizer import Visualizer
from rddl2tf.compiler import Compiler

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from typing import Sequence, Optional, Tuple, Union
Value = Union[bool, int, float, np.array]
NonFluents = Sequence[Tuple[str, Value]]
Fluents = Sequence[Tuple[str, np.array]]


class Navigation3DVisualizer(Visualizer):
    '''Visualizer for the Navigation domain (adapted from Thiago Bueno).

    It uses Matplotlib.pyplot to render a graphical representation
    of the navigation paths, and the initial and goal positions.

    Args:
        compiler (:obj:`rddl2tf.compiler.Compiler`): RDDL2TensorFlow compiler
        verbose (bool): Verbosity flag
    '''

    def __init__(self, compiler: Compiler, verbose: bool) -> None:
        super().__init__(compiler, verbose)

    def render(self,
            trajectories: Tuple[NonFluents, Fluents, Fluents, Fluents, np.array],
            batch: Optional[int] = None) -> None:
        '''Render the simulated state-action `trajectories` for Navigation domain.

        Args:
            stats: Performance statistics.
            trajectories: NonFluents, states, actions, interms and rewards.
            batch: Number of batches to render.
        '''

        non_fluents, initial_state, states, actions, interms, rewards = trajectories

        non_fluents = dict(non_fluents)
        states  = dict((name, fluent[0]) for name, fluent in states)
        actions = dict((name, fluent[0]) for name, fluent in actions)
        rewards = rewards[0]

        idx = self._compiler.state_fluent_ordering.index('location/1')

        start = initial_state[idx][0]
        g = non_fluents['GOAL/1']
        path = states['location/1']
        deltas = actions['move/1']

        center_is_defined = False
        decay_is_defined = False
        centers = None
        decays = None
        zones = None
        fig = plt.figure()
        self.ax = fig.gca(projection='3d')
        self._render_state_space()
        self._render_start_and_goal_positions(start, g)
        
        self._render_state_action_trajectory(start, path, deltas)

        plt.title('Navigation', fontweight='bold')
        plt.legend(loc='lower right')
        plt.show()

    def _render_state_space(self):
        self.ax.set_aspect("equal")
        self.ax.set_xlabel("x coordinate")
        self.ax.set_ylabel("y coordinate")
        self.ax.set_zlabel("z coordinate")
        self.ax.grid()

    def _render_start_and_goal_positions(self, start, goal):
        self.ax.scatter([start[0]], [start[1]], [start[2]], marker='^', color='limegreen', label='initial')
        self.ax.scatter([goal[0]], [goal[1]], [goal[2]], marker='x', color='crimson', label='goal')

    def _render_state_action_trajectory(self, start, path, deltas):
        xpath = [ p[0] for p in path ]
        ypath = [ p[1] for p in path ]
        zpath = [ p[2] for p in path ]

        xpath.insert(0, start[0])
        ypath.insert(0, start[1])
        zpath.insert(0, start[2])        
        self.ax.plot(xpath, ypath, zpath)

        x0, y0, z0 = start
        xdeltas = [ d[0] for d in deltas ]
        ydeltas = [ d[1] for d in deltas ]
        zdeltas = [ d[2] for d in deltas ]
        # self.ax.quiver([x0] + xpath[:-1], [y0] + ypath[:-1], [z0] + zpath[:-1], xdeltas, ydeltas, zdeltas, length=0.15, normalize=True)