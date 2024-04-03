#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


movies= pd.read_csv(r'D:\IMDB Movie Rating\movie.csv') #read the movies file


# In[6]:


movies.head(2)


# In[8]:


tags= pd.read_csv(r'D:\IMDB Movie Rating\tag.csv') #read the tags file


# In[10]:


tags.head(2)


# In[11]:


ratings= pd.read_csv(r'D:\IMDB Movie Rating\rating.csv') #read the ratings file


# In[12]:


ratings.head(2)


# In[13]:


del ratings['timestamp'] #deleted the timestamp form bothe the datasets.
del tags['timestamp']


# In[16]:


ratings.head(1)


# In[17]:


tags.head(1)


# # what does loc() and iloc() do?

# * loc[] and iloc[] are indexing methods used in pandas to access rows and columns in a DataFrame.
# 
# * loc[]: This method is primarily label-based, meaning you use the row or column labels to index data. **For example, df.loc[1] would retrieve the row with label "1".**
# 
# * iloc[]: This method is integer-based and is used for positional indexing. It means you use integer indices to access data, similar to how you would use indexing in lists or arrays. **For example, df.iloc[0] would retrieve the first row in the DataFrame regardless of its label. You can also use iloc[] to access specific rows and columns by integer position, such as df.iloc[0, 1] to access the element in the first row and second column.**

# # Data Structures:

# In[18]:


row_0 = tags.iloc[0]
type(row_0)


# In[19]:


print(row_0)


# In[21]:


row_0.index #it displays only 3 index becoz we deleted timestamp.


# In[23]:


row_0['userId']


# In[24]:


'rating' in row_0


# In[25]:


row_0.name


# In[26]:


row_0 = row_0.rename('firstRow')
row_0.name


# # DataFrames:

# In[27]:


tags.head()


# In[31]:


tags.index


# In[32]:


tags.columns


# In[35]:


tags.iloc[[0,11,500]]


# # Descriptive Statistics

# In[36]:


ratings['rating'].describe()


# In[37]:


ratings.describe()


# In[38]:


ratings['rating'].mode()


# In[39]:


ratings.corr()


# In[41]:


filter1=ratings['rating']>10
print(filter1)
filter1.any()


# In[43]:


filter2= ratings['rating']>0
filter2.all()


# # Data Cleaning: Handling Missing Data

# In[45]:


movies.shape


# In[47]:


movies.isnull().sum()


# In[50]:


movies.isnull().any() #No missing values in the data set


# In[51]:


ratings.shape


# In[52]:


ratings.isnull().sum()


# In[54]:


ratings.isnull().any() #No missing values in the data set


# In[56]:


tags.shape


# In[67]:


tags.isnull().any().any() #No missing values in the data set


# In[60]:


tags=tags.dropna() #is used to remove rows from a Dataset where the values in the "tags" column are missing.


# In[63]:


tags.isnull().any().any()


# In[64]:


tags.shape


# # Data Visualization

# In[69]:


get_ipython().run_line_magic('matplotlib', 'inline')

ratings.hist(column='rating', figsize=(10,5))


# In[70]:


ratings.boxplot(column='rating', figsize=(10,5))


# #  Slicing Out Columns

# In[72]:


tags['tag'].head(2)


# In[76]:


movies[['title','genres']].head()


# In[77]:


ratings[-10:]


# In[79]:


tag_counts=tags['tag'].value_counts()
tag_counts[-10:]


# In[80]:


tag_counts[:10].plot(kind='bar', figsize=(10,5))


# # Filters for Selecting Rows

# In[81]:


is_highly_rated = ratings['rating'] >= 5.0
ratings[is_highly_rated][30:50]


# In[82]:


is_action= movies['genres'].str.contains('Action')
movies[is_action][5:15]


# In[83]:


movies[is_action].head(15)


# # Group By and Aggregate

# In[84]:


ratings_count = ratings[['movieId','rating']].groupby('rating').count()
ratings_count


# In[85]:


average_rating = ratings[['movieId','rating']].groupby('movieId').mean()
average_rating.head()


# In[86]:


movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.head()


# In[87]:


movie_count = ratings[['movieId','rating']].groupby('movieId').count()
movie_count.tail()


# # Merge Dataframes

# In[88]:


tags.head()


# In[89]:


movies.head()


# In[90]:


t = movies.merge(tags, on='movieId', how='inner')
t.head()


# # Combine aggreagation, merging, and filters to get useful analytics

# In[91]:


avg_ratings= ratings.groupby('movieId', as_index=False).mean()
del avg_ratings['userId']
avg_ratings.head()


# In[92]:


box_office = movies.merge(avg_ratings, on='movieId', how='inner')
box_office.tail()


# In[93]:


is_highly_rated = box_office['rating'] >= 4.0
box_office[is_highly_rated][-5:]


# In[94]:


is_Adventure = box_office['genres'].str.contains('Adventure')
box_office[is_Adventure][:5]


# In[95]:


box_office[is_Adventure & is_highly_rated][-5:]


# # Vectorized String Operations

# In[96]:


movies.head()


# # Split 'genres' into multiple columns

# In[97]:


movie_genres = movies['genres'].str.split('|', expand=True)
movie_genres[:10]


# # Add a new column for comedy genre flag

# In[98]:


movie_genres['isComedy'] = movies['genres'].str.contains('Comedy')
movie_genres[:10]


# # Extract year from title e.g. (2007)

# In[99]:


movies['year'] = movies['title'].str.extract('.*\((.*)\).*', expand=True)
movies.tail()


# # Parsing Timestamps

# In[102]:


tags = pd.read_csv(r'D:\IMDB Movie Rating\tag.csv', sep=',')
tags.dtypes


# In[103]:


tags.head(5)


# In[114]:


tags['parsed_time'] = pd.to_datetime(tags['timestamp'], unit='s', errors='coerce')


# In[108]:


tags['parsed_time'].dtype


# In[110]:


tags.head(2)


# In[111]:


greater_than_t = tags['parsed_time'] > '2015-02-01'

selected_rows = tags[greater_than_t]

tags.shape, selected_rows.shape


# In[112]:


tags.sort_values(by='parsed_time', ascending=True)[:10]


# # Average Movie Ratings over Time
# Movie ratings related to the year of launch?

# In[115]:


average_rating = ratings[['movieId','rating']].groupby('movieId', as_index=False).mean()
average_rating.tail()


# In[119]:


numeric_columns = joined.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_columns.corr()


# In[124]:


correlation_matrix


# In[ ]:





# In[ ]:





# In[ ]:




