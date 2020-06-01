from random import choice
class RandomWalk():
    def __init__(self,num_points=5000):     #随机漫步的次数
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_direction=choice([1,-1])
            y_direction=choice([1,-1])
            x_step=choice([0,1,2,3,4])
            y_step=choice([0,1,2,3,4])
            x_value=self.x_values[-1]+x_direction*x_step
            y_value=self.y_values[-1]+y_direction*y_step
            if x_value==0 and y_value==0:
                continue
            self.x_values.append(x_value)
            self.y_values.append(y_value)

