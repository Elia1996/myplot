#!/usr/bin/python3
from excel_extract import *
from plotter import *

plot_style = { 'style' : 'Solarize_Light2', 
				'marker' : '.', 
				'linewidth' : 0.5,
				'color' : '#00a1dc'
			}

obj=excel_extract("../MISURE.xlsx","Foglio2",3)
objp=plotter(40,False,**plot_style)
objp.title_font['size']=18
objp.title_font['fontweight']='bold'
objp.ticksize(12)
objp.x_font['color']='#667B83'
objp.x_font['size']='12'
objp.y_font['size']='12'
objp.y_font['color']='#667B83'
objp.x_font['weight']='bold'
objp.x_font['fontweight']='bold'
objp.y_font['weight']='bold'
objp.y_font['fontweight']='bold'


print(objp.style_av())


# plot P(I)
[xlab, x, ylab, y]=obj.getXY(0,1)
title=obj.getcell("A1")
objp.plotXY(xlab,x,ylab,y, title)

# plot lambda(I)
[xlab, x, ylab, y]=obj.getXY(2,3)
title=obj.getcell("C1")
objp.plotXY(xlab,x,ylab,y, title)

# plot modulazione P(V)
[xlab, x, ylab, y]=obj.getXY(4,5)
title=obj.getcell("E1")
objp.plotXY(xlab,x,ylab,y, title)

# plot V(I)
[xlab, x, ylab, y]=obj.getXY(7,6)
title=obj.getcell("G1")
objp.plotXY(xlab,x,ylab,y, title)

# plot SMSR
[xlab, x, ylab, y]=obj.getXY(8,9)
print(xlab)
print(ylab)
title=obj.getcell("I1")
objp.plotXY(xlab,x,ylab,y, title)


