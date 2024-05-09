#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("fifa_data.csv")


# In[3]:


df


# In[14]:


players=df['Nationality'].value_counts().idxmax()


# In[57]:


players


# In[50]:


# 2. Plot a bar chart of 5 top countries with the most number of players
import matplotlib.pyplot as plt
top_countries = df['Nationality'].value_counts().head(5)
plt.bar(top_countries.index, top_countries.values)
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.title('Top 5 Countries with Most Players')
plt.show()


# In[37]:


# 3. Which player has the highest salary?
df['Wage'] = df['Wage'].str.replace('€', '').str.replace('K', '000')
df['Wage'] = df['Wage'].astype(float)
highest_salary_player = df.loc[df['Wage'].idxmax()]['Name']
print("Player with the highest salary:", highest_salary_player)


# In[54]:


# 4. Plot a histogram to get the salary range of the players.
plt.figure(figsize=(10, 6))
plt.hist(df['Wage'], bins=30)
plt.title('Salary Range of Players')
plt.xlabel('Salary')
plt.ylabel('Number of Players')
plt.show()


# In[ ]:





# In[29]:


# 6. Which club has the most number of players
most_players_club = df['Club'].value_counts().idxmax()
print("Club with the most number of players:", most_players_club)


# In[56]:


# 7. Which foot is most preferred by the players? Draw a bar chart for preferred foot
preferred_foot = df['Preferred Foot'].value_counts()
plt.figure(figsize=(10, 5))
preferred_foot.plot(kind='bar', color='green')
plt.title('Preferred Foot of Players')
plt.xlabel('Preferred Foot')
plt.ylabel('Number of Players')
plt.xticks(rotation=0)
plt.show()


# In[2]:


# Data story
# Most number of players in country
# According to dataset,England has most number of players.This indicates the popularity of football in England.
# 5 top countries with the most number of players.
# According to the dataset, the top 5 countries with the most number of players in FIFA are England, Germany, Spain, Argentina,
# and France.
# Player with the highest salary:

# The player with the highest salary in FIFA is L. Messi. This suggests Messi's significant value
# and recognition in the football world, as he is one of the highest-paid athletes globally.

# Salary Range of Players:
    
# Based on histogram,Most players in the dataset have relatively lower salaries, forming a peak towards the lower end of the salary range.
# There is a long tail on the left side of the histogram, indicating a smaller number of players earning higher wages.

# Tallest player in FIFA:

# T. Holý is the tallest player in FIFA based on the dataset. Height can be advantageous in football

# Club with the most number of players:



# In[ ]:


# FC Barcelona has the most number of players in FIFA. 
# This indicates the popularity and extensive squad of FC Barcelona within the game.

# Preferred Foot of Players:

# The bar chart provides a visual representation of the preferred foot among players in FIFA. 
# Most players in the dataset prefer their right foot over their left foot.

