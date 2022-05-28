#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"D:\Data Science-Browsejobs\Myfiles\udemy_courses.csv",parse_dates=["published_timestamp"])

data.dtypes


# In[5]:


# 1. Display Top 10 Rows of The Dataset

data.head(10)


# In[6]:


# 2. Check Last 5 Rows of The Dataset

data.tail(5)


# In[8]:


# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)

data.shape


# In[10]:


print("No of rows", data.shape[0])

print("No of columns", data.shape[1])


# In[12]:


#4. Getting Information About Our Dataset Like Total Number Rows, 
#Total Number of Columns, Datatypes of Each Column And Memory Requirement

data.info()


# In[16]:


# 5. Check Null Values In The Dataset

# data.isnull().sum()

print("Any Missing Values?", data.isnull().values.any())

sns.heatmap(data.isnull())


# In[19]:


# 6. Check For Duplicate Data and Drop Them

data.duplicated().any()


# In[18]:


data = data.drop_duplicates()


# In[20]:


# 7. Find Out Number of Courses Per Subjects

data.columns


# In[24]:


data["subject"].value_counts()


# In[30]:


sns.countplot(data["subject"])
plt.xlabel("Subjects", fontsize = 13)
plt.ylabel("No of Courses",fontsize = 13)
plt.xticks(rotation=40)
plt.show()  
    


# In[31]:


# 8. For Which Levels, Udemy Courses Providing The Courses

data.columns


# In[32]:


data.head(1)


# In[34]:


data["level"].value_counts()


# In[35]:


sns.countplot(data["level"])
plt.xlabel("Subjects", fontsize = 13)
plt.ylabel("No of Courses",fontsize = 13)
plt.xticks(rotation=40)
plt.show()  


# In[36]:


# 9. Display The Count of Paid and Free Courses 

data.columns


# In[37]:


data.head()


# In[38]:


data.columns


# In[39]:


data["is_paid"].value_counts()


# In[40]:


sns.countplot(data["is_paid"])
plt.xlabel("Subjects", fontsize = 13)
plt.ylabel("No of Courses",fontsize = 13)
plt.xticks(rotation=40)
plt.show()  


# In[2]:


# 10. Which Course Has More Lectures (Free or Paid)?

data.columns


# In[6]:


data.groupby(['is_paid']).mean()


# In[7]:


# 11. Which Courses Have A Higher Number of Subscribers Free or Paid?

sns.barplot(x="is_paid", y="num_subscribers", data = data)


# In[8]:


# 12. Which Level Has The Highest Number of Subscribers?

data.columns


# In[9]:


sns.barplot(x="level", y="num_subscribers", data=data)


# In[10]:


# 13. Find Most Popular Course Title

data.columns


# In[15]:


data[data["num_subscribers"].max()==data["num_subscribers"]]["course_title"]


# In[16]:


# 14. Display 10 Most Popular Courses As Per Number of Subscribers

data.columns


# In[19]:


top_10=data.sort_values(by="num_subscribers", ascending = False).head(10)


# In[22]:


sns.barplot(x="num_subscribers",y="course_title", data = top_10)


# In[23]:


# 15. Find The Course Which Is Having The Highest Number of Reviews

data.columns


# In[30]:


data["num_reviews"].max()


# In[2]:


data[data["num_reviews"].max()==data["num_reviews"]]["course_title"]


# In[5]:


sns.barplot(x='subject', y='num_reviews', data = data)
plt.xticks(rotation=40)
plt.show()  


# In[6]:


# 16. Does Price Affect the Number of Reviews?
data.columns


# In[7]:


sns.scatterplot(x="price",y="num_reviews", data=data)


# In[8]:


# 17. Find Total Number of Courses Related To Python

data.columns


# In[16]:


len(data[data['course_title'].str.contains("Python", case=False)])


# In[20]:


# 18. Display 10 Most Popular Python Courses As Per Number of Subscribers

pyhton=data[data['course_title'].str.contains("Python", case=False)].sort_values(by="num_subscribers",ascending=False).head(10 )


# In[25]:


sns.barplot(x='num_subscribers',y='course_title', data=pyhton)
plt.xticks(rotation=40)
plt.show()


# In[26]:


# 19. In Which Year The Highest Number of Courses Were Posted?

data.columns


# In[31]:


data.dtypes["published_timestamp"]


# In[32]:


data["Year"]=data["published_timestamp"].dt.year


# In[34]:


data.head(1)


# In[35]:


sns.countplot('Year',data=data)


# In[37]:


data["Year"].value_counts()


# In[38]:


# 20. Display Category-Wise Count of Posted Subjects [Year Wise]

data.columns


# In[39]:


data.groupby("Year")["subject"].value_counts()


# In[ ]:




