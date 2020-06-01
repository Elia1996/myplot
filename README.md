# myplot
## plotter
This class simplify the creation of graph, in particular
from matplotlib module some feature are added to 
simplify the creation of a graph. A default initialization
of a graph object is provided by:

	objp = get_default_style(40)

That return a full intialized graph, simply passing 
data to plotXY or semilogxXY create the plot:
	
	objp.plotXY("x_label", [1,2,3,4,5,6,7,8,9], "y_label", [1,5,2,6,3,7,4,8,9], "This is an example graph")
