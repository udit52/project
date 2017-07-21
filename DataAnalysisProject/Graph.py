import pandas as pd
import datetime
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from Validator import Validator

class Graph:
	def __init__(self,dataFile,field_list,isDateTimeSelected,xmin,xmax,ymin,ymax,dates,percent,target):
		v=Validator(dataFile)
		self.dates=dates
		self.df=v.getDataFrame()
		self.ymin=ymin
		self.ymax=ymax
		self.xmin=xmin
		self.xmax=xmax
		self.target=target
		self.percent=percent
		self.field_list=field_list
		self.isDateTimeSelected=isDateTimeSelected
		self.N=len(self.df[self.field_list])
		self.reqLen=int(math.floor(self.N*self.percent/100))
		self.plotDf=self.df.iloc[0:self.reqLen]
		self.x=range(self.reqLen)
		self.width= 1/1.5
		
	'''
	@func- As per the user input, it will call one of the methods to create graph
	@args- graph_type is the type of the graph user selected
	@return- None
	'''
	
	def selectGraph(self,graph_type):
		tgraph= {"bar":self.createBar_2D,
				"line":self.createLine_2D,
				"box":self.createBox_2D,
				"hist":self.createHist_2D,
				"area":self.createArea_2D,
				"scatter":self.createScatter_2D,
				"pie":self.createPie_2D,
				"hexbin":self.createHexbin_2D}
		tgraph.get(graph_type)()
		return
		
	'''
	@func- It will create 2D bar graph
	@args- NONE
	@return- NONE
	'''
	
	def createBar_2D(self):
		fig=plt.figure()
		ax=fig.add_subplot(111)
		fig.subplots_adjust(left=0.15, bottom=0.25)
		ymin= float(self.plotDf[self.field_list].min())
		ymax= float(self.plotDf[self.field_list].max())
		print ymin
		print ymax
		if self.isDateTimeSelected=="yes":
			xdates=pd.to_datetime(self.plotDf[self.dates])
			for field in self.field_list:
				plt.bar(xdates,self.plotDf[field],self.width,label=field,color=np.random.rand(3,1))
		else:
			for field in self.field_list:
				plt.bar(self.x,self.plotDf[field],self.width,label=field,color=np.random.rand(3,1))
		plt.xlabel("X-Axis")
		plt.ylabel("Y-Axis")
		'''
		plt.axis([self.xmin,self.xmax,self.ymin,self.ymax])
		'''
		plt.title("$Bar Chart$")
		plt.legend(bbox_to_anchor=(1.05, 1),loc=2,borderaxespad=0.).draggable()
		plt.grid(True)
		plt.ylim([self.ymin,self.ymax]) #initial Limits
		axcolor = 'lightgoldenrodyellow'
		axmin = fig.add_axes([0.25,0.1,0.65,0.03], axisbg=axcolor)
		axmax = fig.add_axes([0.25,0.15,0.65,0.03], axisbg=axcolor)
		smin= Slider(axmin, 'Min',ymin, ymax,valinit=ymin)
		smax= Slider(axmax, 'Max',ymin,ymax,valinit=ymax)
		
		def update(val):
			plt.subplot(111)
			plt.ylim([smin.val,smax.val])
		smin.on_changed(update)
		smax.on_changed(update)
		plt.savefig("bar.png")
		plt.show()
		return "bar.png"
		
	'''
	@func- It will create 2D line graph
	@args- None
	@return- None
	'''
	
	def createLine_2D(self):
		if self.isDateTimeSelected=="yes":
			xdates=pd.to_datetime(self.plotDf[self.dates])
			for field in self.field_list:
				fig= plt.plot(xdates,self.plotDf[field],label=field,color=np.random.rand(3,1))
		else:
			for field in self.field_list:
				fig=plt.plot(self.x,self.plotDf[field],label=field,color=np.random.rand(3,1))
		plt.xlabel("X Axis")
		plt.ylabel("Y Axis")
		plt.title("Line Chart")
		plt.axis([self.xmin,self.xmax,self.ymin,self.ymax])
		plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.).draggable()
		plt.savefig("line.png")
		plt.show()
		return "line.png"
		
	'''
	@func: It will create box graph
	@args- None
	@return- None
	'''	
	
	def createBox_2D(self):
		for field in self.field_list:
			fig= plt.boxplot(self.plotDf[field])
		plt.xlabel("x axis")
		plt.ylabel("y axis")
		plt.title("Box Chart")
		plt.axis([self.xmin,self.xmax,self.ymin,self.ymax])
		plt.legend(bbox_to_anchor=(1.05,1),loc=2, borderaxespad=0.)
		plt.savefig("box.png")
		plt.show()
		return "box.png"
		
	'''
	@func- It will create histogram
	@args-None
	@return- None
	'''
	
	def createHist_2D(self):
		for field in self.field_list:
			fig=plt.hist(self.plotDf[field],label=field,color=np.random.rand(3,1))
		plt.xlabel("x axis")
		plt.ylabel("y axis")
		plt.axis([self.xmin,self.xmax,self.ymin,self.ymax])
		plt.title("Histogram")
		plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.).draggable()
		plt.savefig("hist.png")
		plt.show()
		return "hist.png"
		
	'''
	@func- It will create area graph
	@args-None
	@return- None
	'''
	def createArea_2D(self):
		if self.isDateTimeSelected=="yes":
			xdates=pd.to_datetime(self.plotDf[self.dates])
			for field in self.field_list:
				fig=plt.fill_between(xdates,self.plotDf[field],label=field,color=np.random.rand(3,1))
		else:
			for field in self.field_list:
				fig=plt.fill_between(self.x,self.plotDf[field],label=field,colo=np.random.rand(3,1))
		plt.xlabel("x axis")
		plt.ylabel("y axis")
		plt.axis([self.xmin,self.xmax,self.ymin,self.ymax])
		plt.title("Area Chart")
		plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
		plt.savefig("area.png")
		plt.show()
		return "area.png"
		
		
	'''
	@func- It will create Scatter Chart
	@args-None
	@return- None
	'''
	
	def createScatter_2D(self):
		for field in self.field_list:
			fig=plt.scatter(self.plotDf[self.target],self.plotDf[field],label=field,color=np.random.rand(3,1))
		plt.xlabel("x axis")
		plt.ylabel("y axis")
		plt.axis([self.xmin,self.xmax,self.ymin,self.ymax])
		plt.title("Scatter Chart")
		plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.).draggable()
		plt.savefig("scatter.png")
		plt.show()
		return "scatter.png"
		
	'''
	@func- It will create Pie chart
	@args-None
	@return- None
	'''
	
	def createPie_2D(self):
		for field in self.field_list:
			fig=plt.pie(self.plotDf[field])
		plt.title("Pie Chart")
		plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
		plt.savefig("pie.png")
		plt.show()
		return "pie.png"
		
	'''
	@func- It will create Hexbin graph of the field selected by the user
	@args-None
	@return- None
	'''
	
	def createHexbin_2D(self):
		for field in self.field_list:
			fig=plt.hexbin(self.x,self.plotDf[field],label=field,color=np.random.rand(3,1))
		plt.xlabel("x axis")
		plt.ylabel("y axis")
		plt.title("Hexagon Binning")
		plt.axis([self.xmin,self.xmax,self.ymin,self.ymax])
		plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
		plt.savefig("hexbin.png")
		plt.show()
		return "hexbin.png"
