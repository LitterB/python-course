from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        # 初始化随机漫步的属性
        self.num_points = num_points
        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # x_direction = choice([1, -1])
            # x_distance = choice([0, 1, 2, 3, 4])
            # x_step = x_direction * x_distance

            # y_direction = choice([1, -1])
            # y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            # y_step = y_direction * y_distance

            # if x_step == 0 and y_step == 0:
            #     continue
            
            #最后一个值加上步长算出下一个点的位置
            next_x = self.x_values[-1] + self.get_step()
            next_y = self.y_values[-1] + self.get_step()

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([1, 2, 3, 4, 5, 6, 7, 8])
        return direction * distance

