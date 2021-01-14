#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 


# In[2]:

st.title('Netflix Movies and TV Shows')
from PIL import Image
image = Image.open('netflix.jpg')
st.image(image,use_column_width=True)        

st.sidebar.markdown(' **Netflix Dataset Analysis Dashboard**  ')
st.sidebar.markdown(''' Use Netflix Movies and TV Shows dataset from Kaggle and perform following operations :''')
st.sidebar.markdown('''1. Make a visualization showing the total number of movies
watched by children
2. Make a visualization showing the total number of standup
comedies
3. Make a visualization showing most watched shows.
4. Make a visualization showing highest rated show.
5. Make a dashboard (DASHBOARD A) containing all of these above visualizations. ''')

st.sidebar.markdown(''' Designed by: **Mihir Kulkarni**  ''')
                    
 



st.header('Dataset')
netflix_df = pd.read_csv("netflix_titles.csv")
netflix_df


# In[3]:


netflix_df.isnull().sum()


# In[4]:


netflix_df.director.fillna("No director",inplace=True)
netflix_df.cast.fillna("No cast",inplace=True)
netflix_df.country.fillna("Country N.A",inplace=True)
netflix_df.dropna(subset=["date_added", "rating"], inplace=True)


# In[5]:


netflix_df.isnull().sum()


# In[6]:


#netflix_df.columns


# # 1. Make a visualization showing the total number of movies watched by children

# In[34]:

with st.echo():
    filtered_genres = netflix_df.set_index('title').listed_in.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);


# In[72]:


#netflix_df.shape


# In[41]:

st.header('Filtered Genres')
st.write(filtered_genres.value_counts())


# In[79]:


children = [("Kids' TV", 325),("Children & Family Movies", 378)]
children = dict(children)
for_kids = children["Children & Family Movies"] + children["Kids' TV"]
print("Movies + TV shows for children : ",for_kids)
total = 6214
print("Total content : ",total)
ovr_percent = (for_kids/total)*100
print("Percentage of children's content : ",ovr_percent)
y = children["Children & Family Movies"]
print("Movies for children",y)
z = (netflix_df.type == "Movie").sum()
print("Total Movies : ",z)
p = (y/z)*100
print("Percentage of children's movies : ",p)
print("Percentage of movies not for children : ",100-p)


# In[99]:

st.header('Total number of movies watched by children')
fig, ax = plt.subplots()

labels = ['Chilren','Others'] 
             

percentages = [8.879492600422834, 91.12050739957716]
plt.rcParams['font.size']=12
explode=(0.1,0)
ax.pie(percentages, explode=explode, labels=labels, autopct='%1.0f%%', shadow=False, startangle=0, pctdistance=1.2,labeldistance=1.4)   
ax.axis('equal')
#ax.set_title("Total number of movies watched by children")
ax.legend(frameon=False, bbox_to_anchor=(1.5,0.8))
    
st.pyplot(fig)


# In[63]:


#netflix_df.query('listed_in == "Children & Family Movies"').listed_in.count()


# In[64]:


#(netflix_df.listed_in == "Kids' TV").sum()


# In[65]:


#def return_counter(data_frame, column_name, limit):
#    from collections import Counter    
#    print(dict(Counter(data_frame[column_name].values).most_common(limit)))


# In[66]:


#return_counter(netflix_df, 'listed_in', 10)


# # 2. Make a visualization showing the total number of standup comedies

# In[84]:


StandUpComedy = 281
StandUpComedy_TalkShows = 42
total_standup = 323
print("Stand-up Comedies ; ",total_standup)
total_shows = (netflix_df.type == "TV Show").sum()
print("Total TV Shows : ",total_shows)
percent_standup = (total_standup/total_shows)*100
print("Percentage of Stand-up Comedies : ",percent_standup)
print("Percentage of non Stand-up Comedies : ",100-percent_standup)


# In[98]:

st.header('Total number of Standup Comedies')
#col1, col2 = st.beta_columns(2)
#with col1:
#    fig, ax = plt.subplots()

#    labels = ['Stand-up Comedies', 'Others'] 


#    percentages = [16.50485436893204, 83.49514563106796]
#    plt.rcParams['font.size']=12
#    explode=(0.1,0)
#    ax.pie(percentages, explode=explode, labels=labels, autopct='%1.0f%%', shadow=False, startangle=-60, pctdistance=1.2,labeldistance=1.4)   
#    ax.axis('equal')
    #ax.set_title("Total number of Stand-up Comedies")
#    ax.legend(frameon=False, bbox_to_anchor=(1.5,0.8))

#    st.pyplot(fig)

# In[120]:

fig, ax1 = plt.subplots()

labels = ['Stand-up Comedies', 'Others']
sizes = [16.50485436893204, 83.49514563106796]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']#colors
explode = (0.05,0.05)#explsion
plt.rcParams['font.size']=9
plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=-60, pctdistance=0.85, explode = explode)#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
    #fig = plt.gcf()
fig.gca().add_artist(centre_circle)# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
    #ax1.set(title='Total number of Stand-up Comedies')
ax1.legend(frameon=False, bbox_to_anchor=(1.5,0.8))
plt.tight_layout()

plt.show()

st.pyplot(fig)


# # 3. Make a visualization showing most watched shows.

# In[21]:

st.header('Most watched shows')
filtered_genres = netflix_df.set_index('title').listed_in.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
plt.figure(figsize=(10,10))
fig, ax = plt.subplots()
ax = sns.countplot(y = filtered_genres, order=filtered_genres.value_counts().index[:20])
plt.title('Top 20 Genres on Netflix')
plt.xlabel('Titles')
plt.ylabel('Genres')
plt.show()
st.pyplot(fig)


# # 4. Make a visualization showing highest rated show

# In[20]:
st.header('Highest rated shows')
fig, ax = plt.subplots()
ax = sns.countplot(netflix_df["rating"])
plt.xticks(rotation=90)
plt.title("Rating Count in Netflix")
st.pyplot(fig)

# In[ ]:
st.balloons()



