import this
import leather
"""
data1 = ([5.5, 8], [6, 3], [1.5, 6], [10.5, 4])
chart = leather.Chart('Simple pairs of x-y')
chart.add_dots(data1)

chart = leather.Chart('Visualizing Lines')
chart.add_line(data1)
chart.to_svg()

chart.to_svg('image1.svg')


data1 = ([1.5, 2], [2, 3], [4.5, 6], [7.5, 4])
data2 = [(2, 3), (4, 5), (5, 6), (7, 5)]
chart = leather.Chart('Visualizing Multiple series')
chart.add_dots(data1)
chart.add_dots(data2)


chart = leather.Chart('Visualizing Lines')
chart.add_line(data1)
chart = leather.Chart('Customized Line')
chart.add_line(data1,stroke_color='#0000ff', width=5)
chart.to_svg()
chart.to_svg('image2.svg')
"""

data = [[1, 'A'], [2, 'B'], [3, 'C'], [4, 'D']]
chart = leather.Chart('Visualizing Bars')
chart.add_bars(data)
chart.to_svg()

chart.to_svg('image2.svg')
