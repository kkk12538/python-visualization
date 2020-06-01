import pygal
from 可视化编程小项目.模拟扔骰子 import visual
from 可视化编程小项目.模拟扔骰子 import die
num=eval(input('请输入你要抛掷骰子的数目：'))
view=pygal.Bar()
view.x_labels=[1,2,3,4,5,6]
view._x_title='rolling numbers'
view._y_title='count'
view.title='rolling one D6 '+str(num)+' times'
die1= die.Die(6)
view.add('D6', visual.Visual(die1, num))
view.render_to_file('one_roll_D6.svg')

