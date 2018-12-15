from light import Light
from system import System, LightMapper

class MappingAdapter(LightMapper):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    @staticmethod
    def _grid_objects(descriptor, grid):
        """

        :param descriptor: 1 for lights, -1 for obstacles
        :grid: System's map
        :return:
        """

        return [(j, i) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == descriptor]


    def lighten(self, map):
        dim = (len(map[0]), len(map))
        self.adaptee.set_dim(dim)

        self.adaptee.set_lights(self._grid_objects(1, map))
        self.adaptee.set_obstacles(self._grid_objects(-1, map))

        return self.adaptee.generate_lights()


if __name__ == '__main__':
    system = System()
    lights = Light((0, 0))
    adapter = MappingAdapter(lights)
    system.get_lightening(adapter)
