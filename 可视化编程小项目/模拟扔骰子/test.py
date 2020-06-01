import pygal
view=pygal.Bar()
view.title='条形图'
view.x_labels=['1','2','3','4','5']
view._x_title='横轴'
view._y_title='纵轴'
y_labels=[10,20,30,40,50]
view.add('D',y_labels)
view.render_to_file('test.svg')