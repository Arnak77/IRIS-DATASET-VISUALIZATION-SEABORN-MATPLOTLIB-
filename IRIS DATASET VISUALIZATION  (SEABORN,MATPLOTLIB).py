#!/usr/bin/env python
# coding: utf-8

# #### IRIS DATASET VISUALIZATION(SEABORN,MATPLOTLIB)

# ##### Importing pandas and Seaborn module

# In[247]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[248]:


import warnings
warnings.filterwarnings("ignore")


# # Importing Iris data set 

# In[249]:


iris=pd.read_csv(r"D:\NIT\27_28NOV\IRIS DATASET _ ADVANCE VISUALIZATION _ EDA 2\Iris.csv")


# In[250]:


iris


# # Displaying data

# In[5]:


iris.head()


# In[6]:


iris.drop('Id',axis=1,inplace=True)


# In[7]:


iris.head()


# In[292]:


iris.describe()


# ## Checking if there are any missing values

# In[8]:


iris.info()


# In[9]:


iris.Species=iris.Species.astype('category')        


# In[10]:


iris.dtypes


# In[11]:


iris['Species'].value_counts()


# ### This data set has three varities of Iris plant.

# # Bar Plot

# In[12]:


c=sns.countplot(data=iris,x='Species')


# In[13]:


iris.head()


# # jointplo()

# In[14]:


j=sns.jointplot(data=iris,x="SepalLengthCm",y="SepalWidthCm")


# In[15]:


j=sns.jointplot(data=iris,x="SepalLengthCm",y="SepalWidthCm",kind='reg')


# In[16]:


j=sns.jointplot(data=iris,x="PetalLengthCm",y="PetalWidthCm")


# In[17]:


j=sns.jointplot(data=iris,x="PetalLengthCm",y="PetalWidthCm")


# In[18]:


fig=sns.jointplot(x='SepalLengthCm',y='SepalWidthCm',kind='hex',data=iris)


# In[19]:


j=sns.jointplot(data=iris,x="PetalLengthCm",y="PetalWidthCm",kind='hex')


# # FacetGrid Plot

# In[20]:


sns.FacetGrid(iris)


# In[49]:


s=sns.FacetGrid(iris,hue='Species',height=5)
s1=s.map(plt.scatter,"SepalLengthCm","SepalWidthCm")
s2=s1.add_legend()



# In[54]:


s3=sns.FacetGrid(iris,hue='Species',height=4)
s4=s3.map(sns.scatterplot,"PetalLengthCm","PetalWidthCm")
s5=s4.add_legend()


# # Boxplot()

# In[55]:


iris.head()


# In[56]:


b=sns.boxplot(data=iris,x="Species",y="PetalLengthCm")


# In[69]:


b=sns.boxplot(data=iris,x="Species",y="PetalLengthCm",order=["Iris-versicolor","Iris-setosa","Iris-virginica"],linewidth=2.5,orient='v',dodge=False)


# In[71]:


b1=sns.boxplot(data=iris,x="Species",y="PetalWidthCm",order=["Iris-versicolor","Iris-setosa","Iris-virginica"],linewidth=2.5,orient='v',dodge=False)


# In[74]:


b2=sns.boxplot(data=iris,x="Species",y="SepalWidthCm",order=["Iris-versicolor","Iris-setosa","Iris-virginica"],linewidth=2.5,orient='v',dodge=False)


# In[75]:


b3=sns.boxplot(data=iris,x="Species",y="SepalLengthCm",order=["Iris-versicolor","Iris-setosa","Iris-virginica"],linewidth=2.5,orient='v',dodge=False)


# In[82]:


iris.boxplot(by="Species", figsize=(12, 10))


# # Strip plot

# In[141]:


s1=sns.stripplot(data=iris,x="Species",y="SepalLengthCm")


# In[65]:


s1=sns.stripplot(data=iris,x="Species",y="SepalLengthCm",jitter=True,palette='winter',size=8,orient='v')


# In[66]:


s2=plt.gcf()
s2.set_size_inches(8,7)
s2=sns.stripplot(data=iris,x="Species",y="SepalWidthCm",jitter=True,palette='Set2',size=8,orient='v')


# In[67]:


s3=plt.gcf()
s3.set_size_inches(10,7)
s3=sns.stripplot(data=iris,x="Species",y="PetalWidthCm",jitter=True,palette='dark',size=8,orient='v')


# In[68]:


s4=plt.gcf()
s4.set_size_inches(10,7)
s4=sns.stripplot(data=iris,x="Species",y="PetalLengthCm",jitter=True,palette='deep',size=8,orient='v')


# # Combining Box and Strip Plots

# In[71]:


iris.Species.cat.categories


# In[90]:


f=plt.gcf()
f.set_size_inches(10,7)
f=sns.boxplot(data=iris,x="Species",y="SepalLengthCm")
f=sns.stripplot(data=iris,x="Species",y="SepalLengthCm",jitter=False,edgecolor='gray')


# In[92]:


f=plt.gcf()
f.set_size_inches(10,7)
f=sns.boxplot(data=iris,x="Species",y="SepalWidthCm")
f=sns.stripplot(data=iris,x="Species",y="SepalWidthCm",jitter=True,edgecolor='gray')


# In[93]:


f=plt.gcf()
f.set_size_inches(10,7)
f=sns.boxplot(data=iris,x="Species",y="PetalLengthCm")
f=sns.stripplot(data=iris,x="Species",y="PetalLengthCm",jitter=True,edgecolor='gray')


# In[94]:


f=plt.gcf()
f.set_size_inches(10,7)
f=sns.boxplot(data=iris,x="Species",y="PetalWidthCm")
f=sns.stripplot(data=iris,x="Species",y="PetalWidthCm",jitter=True,edgecolor='gray')


# # Violin Plot

# In[107]:


v=plt.gcf()
v.set_size_inches(10,7)
v=sns.violinplot(data=iris,x="Species",y="SepalLengthCm")


# In[136]:


plt.figure(figsize=(15,8))
plt.subplot(2,2,1)
sns.violinplot(x='Species',y='PetalLengthCm',data=iris)
plt.subplot(2,2,2)
sns.violinplot(x='Species',y='PetalWidthCm',data=iris)
plt.subplot(2,2,4)
sns.violinplot(x='Species',y='SepalLengthCm',data=iris)
plt.subplot(2,2,3)
sns.violinplot(x='Species',y='SepalWidthCm',data=iris)


# # Pair Plot

# In[137]:


sns.pairplot(data=iris)


# In[143]:


s1=sns.pairplot(iris,hue="Species")


# # Heat map

# In[154]:


h=plt.gcf()
h.set_size_inches(10,7)
h=sns.heatmap(iris.corr())


# In[192]:


h=plt.gcf()
h.set_size_inches(10,7)
h=sns.heatmap(iris.corr(),annot=True)


# In[168]:


h=plt.gcf()
h.set_size_inches(10,7)
h=sns.heatmap(iris.corr(),annot=True,cmap="viridis",linewidths=2,linecolor='k')


# In[191]:


h=plt.gcf()
h.set_size_inches(10,7)
h=sns.heatmap(iris.corr(),annot=True,cmap="viridis",linewidths=2,linecolor='k',mask=False,vmin=-1,vmax=1,cbar=True,cbar_kws = {"orientation": "horizontal"})


# In[194]:


fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.heatmap(iris.corr(),annot=True,cmap='cubehelix',linewidths=1,linecolor='k',square=True,mask=False, vmin=-1, vmax=1,cbar_kws={"orientation": "vertical"},cbar=True)


# # Distribution plot

# In[199]:


fig=plt.gcf()
fig.set_size_inches(10,7)
fig=iris.hist(edgecolor='black', linewidth=3)


# # Swarm plot

# In[206]:


sns.set(style="dark")
fig=plt.gcf()
fig.set_size_inches(10,7)
s1=sns.swarmplot(data=iris,x='Species',y='PetalLengthCm')


# In[210]:


sns.set(style="dark")
fig=plt.gcf()
fig.set_size_inches(10,7)
s1=sns.swarmplot(data=iris,x='Species',y='PetalLengthCm',color='white',edgecolor="black")
s1=sns.violinplot(data=iris,x='Species',y='PetalLengthCm')


# In[211]:


sns.set(style="dark")
fig=plt.gcf()
fig.set_size_inches(10,7)
s1=sns.swarmplot(data=iris,x='Species',y='PetalWidthCm',color='white',edgecolor="black")
s1=sns.violinplot(data=iris,x='Species',y='PetalWidthCm')


# # LM PLot

# In[212]:


l=sns.lmplot(data=iris,x='PetalLengthCm',y='PetalWidthCm')


# In[213]:


l1=sns.lmplot(data=iris,x='SepalLengthCm',y='SepalWidthCm')


# # Distplot()

# In[299]:


d=sns.distplot(iris['SepalLengthCm'],bins=15,kde=True)


# In[301]:


d=sns.distplot(iris['SepalWidthCm'],bins=15,kde=False)


# # kdeplot()

# In[218]:


k=plt.gcf()
k.set_size_inches(10,7)
k=sns.kdeplot(iris)


# In[224]:


k=plt.gcf()
k.set_size_inches(10,7)
k=sns.kdeplot(iris,x='SepalLengthCm',y='PetalLengthCm')


# # Boxen Plot()

# In[255]:


b=plt.gcf()
b.set_size_inches(10,7)
b=sns.boxenplot(data=iris,x='Species',y='SepalLengthCm')


# In[258]:


b1=plt.gcf()
b1.set_size_inches(10,8)
b1=sns.boxenplot(data=iris,x='Species',y='SepalWidthCm')


# # Dashboard

# In[278]:


sns.set_style('darkgrid')
plt.figure(figsize=(20,25))
b2=plt.subplot(2,2,1)
b2=sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
b2=plt.subplot(2,2,2)
b2=sns.violinplot(x="Species", y="PetalLengthCm", data=iris)
b2=plt.subplot(2,2,3)
b2=plt.hist( data=iris,x="PetalLengthCm")
b2=plt.subplot(2,2,4)
b2=sns.stripplot(x="Species", y="PetalLengthCm", data=iris)


# In[275]:


iris.dtypes


# In[276]:


iris.Species=iris.Species.astype('category')              


# In[277]:


iris.dtypes


# # Area Plot

# In[288]:


iris.plot.area(y=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'])


# In[291]:


iris.plot.area(y=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'],alpha=0.3,figsize=(12,10))

