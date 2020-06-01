import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import style
from matplotlib import rc

class plotter:
	def __init__(sf, title_maxl, save=False, style="ggplot", grid=True,**kwargs):
		sf.save=save
		sf.title_maxl=title_maxl
		sf.style=style
		sf.grid=grid
		sf.plot_kwargs=kwargs
		sf.title()
		sf.xlabel()
		sf.ylabel()
		sf.title_font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
		sf.x_font= {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 10,
        }
		sf.y_font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 10,
        }
		# per poter usare latex
		rc('text', usetex=True)
		#You'll need to load amsmath into the TeX preamble
		plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

	def style_av(sf):
		return plt.style.available
	def ticksize(sf,num):
		plt.rcParams['xtick.labelsize'] = num
		plt.rcParams['ytick.labelsize'] = num
		

	def title(sf, **kwargs):
		sf.title_kwargs=kwargs
	
	def xlabel(sf, **kwargs):
		sf.xlabel_kwargs=kwargs
	
	def ylabel(sf, **kwargs):
		sf.ylabel_kwargs=kwargs

		
	def plotXY(sf, x_label, x_val, y_label, y_val, title, figname="astitle"):
		fig = plt.figure(facecolor='#FFFDF5')
		#fig=plt.figure()
		with plt.style.context(sf.style):
			plt.plot(x_val, y_val, **sf.plot_kwargs)
			plt.xlabel(x_label, fontdict=sf.x_font, **sf.xlabel_kwargs)
			plt.ylabel(y_label, fontdict=sf.y_font, **sf.ylabel_kwargs)
			plt.grid(sf.grid)
			plt.title(sf.set_newline(title), fontdict=sf.title_font, **sf.title_kwargs)
			plt.tight_layout()
		if sf.save:
			if figname=="astitle":
				figname=title+".png"
			plt.savefig(figname, facecolor=fig.get_facecolor(), transparent=True)
		else:
			plt.show()
	def semilogxXY(sf, x_label, x_val, y_label, y_val, title, figname="astitle"):
		fig = plt.figure(facecolor='#FFFDF5')
		#fig=plt.figure()
		with plt.style.context(sf.style):
			plt.semilogx(x_val, y_val, **sf.plot_kwargs)
			plt.xlabel(x_label, fontdict=sf.x_font, **sf.xlabel_kwargs)
			plt.ylabel(y_label, fontdict=sf.y_font, **sf.ylabel_kwargs)
			plt.grid(sf.grid)
			plt.title(sf.set_newline(title), fontdict=sf.title_font, **sf.title_kwargs)
			plt.tight_layout()
		if sf.save:
			if figname=="astitle":
				figname=title+".png"
			plt.savefig(figname, facecolor=fig.get_facecolor(), transparent=True)
		else:
			plt.show()
	
	def set_newline(sf, stringa):
                """Set correct nealine considering the max length of title
                """
		if len(stringa)<sf.title_maxl:
			return stringa
		offset=0
		newstr=""
		while len(stringa)>sf.title_maxl: 
			while sf.title_maxl+offset<len(stringa) and stringa[sf.title_maxl+offset]!=" " :
				offset=offset+1
			newstr=newstr+stringa[0:sf.title_maxl+offset]+"\n"
			stringa=stringa[sf.title_maxl+offset:]

		newstr=newstr+stringa
		if newstr[len(newstr)-1]=="\n":
			newstr=newstr[0:-1]
		return newstr

           
def get_default_style(title_maxl):
    plot_style = { 'style' : 'Solarize_Light2',
                                'marker' : '.',
                                'linewidth' : 0.5,
                                'color' : '#00a1dc'
                        }

    objp=plotter(title_maxl,False,**plot_style)
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
    return objp
