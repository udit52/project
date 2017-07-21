import pandas as pd
import numpy as np
from Validator import Validator
class StatisticAnalyser:
	def __init__(self,dataFile,x=2):
		self.x=x
		v=Validator(dataFile)
		v.check()
		self.df=v.getDataFrame()
		self.DfCol=self.df.columns.values
		self.colDtypeMap={}
		self.continousCol=[]
		self.nominalCol=[]
		self.DataTypes1=[]
		self.DataTypes2=[]

	def Read(self):
		for col in self.DfCol:
			self.colDtypeMap[col]=self.df[col].dtypes

	def ComputeMean(self):
		mea=[]
		for col in self.continousCol:
			if(self.colDtypeMap[col] == int or self.colDtypeMap[col] == float):
				mea.append(np.mean(self.df[col]))
			else:
				mea.append("NaN")
		return mea
	
	def ComputeMode1(self):
		mod=[]
		for col in self.continousCol:
			mod.append(self.df[col].mode().values)
		return mod
		
	def ComputeMode2(self):
		mod1=[]
		for col in self.nominalCol:
			mod1.append(self.df[col].mode().values)
		return mod1
		
	def ComputeCount1(self):
		c=[]
		for col in self.continousCol:
			c.append(self.df[col].count())
		return c
		
	def ComputeCount2(self):
		c1=[]
		for col in self.nominalCol:
			c1.append(self.df[col].count())
		return c1
		
	def ComputeVariance(self):
		v=[]
		for col in self.continousCol:
			if(self.colDtypeMap[col] == int or self.colDtypeMap[col] == float):
				v.append(self.df[col].var())
			else:
				v.append("NA");
		return v
		
	def ComputeStandardDeviation(self):
		sd=[]
		for col in self.continousCol:
			if(self.colDtypeMap[col] == int or self.colDtypeMap[col] == float):
				sd.append(self.df[col].std())
			else:
				sd.append("NA")
		return sd
		
	def Range(self):
		r=[]
		for col in self.continousCol:
			if(self.colDtypeMap[col] == int or self.colDtypeMap[col] == float):
				r.append(str(self.df[col].max())+","+str(self.df[col].min()))
			else:
				r.append("NA")
		return r
		
	def ComputeMedian(self):
		med=[]
		for col in self.continousCol:
			if(self.colDtypeMap[col] == int or self.colDtypeMap[col] == float):
				med.append(np.median(self.df[col]))
			else:
				med.append("NA")
		return med
		
	def ComputeStandardError(self):
		err=[]
		for col in self.continousCol:
			if(self.colDtypeMap[col] == int or self.colDtypeMap[col] == float):
				err.append(self.df[col].std()/np.sqrt([self.df[col].count()]))
			else:
				err.append("NA")
		return err
		
	def ComputeSum(self):
		s=[]
		for col in self.continousCol:
			if(self.colDtypeMap[col] == int or self.colDtypeMap[col] == float):
				s.append(self.df[col].sum())
			else:
				s.append("NA")
		return s
		
	def ComputeMin(self):
		min=[]
		for col in self.continousCol:
			min.append(self.df[col].min())
		return min
		
	def ComputeMax(self):
		max=[]
		for col in self.continousCol:
			max.append(self.df[col].max())
		return max
		
	def MissingCount1(self):
		mc=[]
		for col in self.continousCol:
			mc.append(self.df[col].isnull().sum())
		return mc
		
	def MissingCount2(self):
		mc1=[]
		for col in self.nominalCol:
			mc1.append(self.df[col].isnull().sum())
		return mc1
		
	def UniqueCount1(self):
		uc=[]
		for col in self.continousCol:
			uc.append(self.df[col].nunique())
		return uc
		
	def UniqueCount2(self):
		uc1=[]
		for col in self.nominalCol:
			uc1.append(self.df[col].nunique())
		return uc1
		
	def CheckContinous(self):
		for col in self.DfCol:
			if(self.df[col].nunique()<=self.x):
				self.DataTypes2.append("Categorical")
				self.nominalCol.append(col)
			elif(self.df[col].dtypes==object):
				self.DataTypes2.append(self.df[col].dtypes)
				self.nominalCol.append(col)
		       # elif(self.df[col].dtypes==dt.datetime):
		#		self.DataTypes2.append(self.df[col].dtypes)
		#		self.nominalCol.append(col)
			else:
				self.DataTypes1.append(self.df[col].dtypes)
				self.continousCol.append(col)
				
	def getCategorical(self):
		return self.nominalCol
		
	def getContinous(self):
		return self.continousCol
		
	'''
	@func- It will produce a Continous table with all the statistical fields for Comtinous table
	@param- NIL
	@return- NULL
	'''
	def ContinousTable(self):
		print ""
		print "						STATISTICS TABLE"
		print ""
		print "					THIS IS TABLE FOR CONTINOUS DATA"
		print ""
		Dfc=pd.DataFrame(columns=["Field","Data Type","Mean","Mode","Median","Missing Count","Count","Sum","Minimum","Maximum","Standard Error","Variance","Standard Deviation","Unique Count","Range"])
		Dfc["Data Type"]=self.DataTypes1
		Dfc["Field"]=self.continousCol
		Dfc["Mean"]=self.ComputeMean()
		Dfc["Mode"]=self.ComputeMode1()
		Dfc["Median"]=self.ComputeMedian()
		Dfc["Missing Count"]=self.MissingCount1()
		Dfc["Count"]=self.ComputeCount1()
		Dfc["Sum"]=self.ComputeSum()
		Dfc["Minimum"]=self.ComputeMin()
		Dfc["Maximum"]=self.ComputeMax()
		Dfc["Standard Error"]=self.ComputeStandardError()
		Dfc["Variance"]=self.ComputeVariance()
		Dfc["Standard Deviation"]=self.ComputeStandardDeviation()
		Dfc["Unique Count"]=self.UniqueCount1()
		Dfc["Range"]=self.Range()
		print(Dfc)
		print ""
		print ""
		
	'''
	@func- It will produce a table for Nominal DataType with its static fields
	@param- NIL
	@return- NULL
	'''
	def DiscreteTable(self):
		print ""
		print "						THIS IS TABLE FOR CATEGORICAL DATA"
		Dfd=pd.DataFrame(columns=["Field","Data Type","Mode","Missing Count","Count","Unique Count"])
		print ""
		Dfd["Data Type"]=self.DataTypes2
		Dfd["Field"]=self.nominalCol
		Dfd["Mode"]=self.ComputeMode2()
		Dfd["Missing Count"]=self.MissingCount2()
		Dfd["Count"]=self.ComputeCount2()
		Dfd["Unique Count"]=self.UniqueCount2()
		print(Dfd)
		print ""
