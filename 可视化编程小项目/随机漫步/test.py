import matplotlib.pyplot as plot
from 可视化编程小项目.随机漫步.random_walk import RandomWalk
while True:
    random1=RandomWalk(5000)
    random1.fill_walk()
    plot.xlabel('x_values',fontsize=30)
    plot.ylabel('y_values',fontsize=30)
    num_colors=list(range(len(random1.y_values)))
    plot.scatter(random1.x_values,random1.y_values,c=num_colors,s=1,edgecolors='none',cmap=plot.cm.Blues)
    plot.show()
    keep=input('Do you want another random walk?(y/n)')
    if keep=='n':
        break