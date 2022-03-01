import numpy as np
import pandas as pd
ride_sharing_Data = pd.read_csv(ride_sharing_new.csv)
ride_sharing_Data.head()

# In[2]:


ride_sharing_Data['duration']


# **Let's handle this!**
# 
# **1. First:** remove the text minutes from every value
#    - we will use the function `strip` from the `str` module
#    - and store the new value in a new column: `duration_trim`

# In[3]:


ride_sharing_Data['duration_trim'] = ride_sharing_Data['duration'].str.strip('minutes')
ride_sharing_Data['duration_trim']


# **2. Second:** convert the data type to integer
# - we will apply the `astype` method into `duration_trim`
# - and store the new values in a new column: `duration_time`

# In[4]:


# Convert duration to integer
ride_sharing_Data['duration_time'] = ride_sharing_Data['duration_trim'].astype('int')
ride_sharing_Data['duration_time']


# **3. Check with an assert statement**

# In[5]:


assert ride_sharing_Data['duration_time'].dtype == 'int'


# We can now get insight about the average duration time!

# In[6]:


print("Average Ride Duration:")
print(str(ride_sharing_Data['duration_time'].mean()) + ' minutes')


# **User Type**
# Let's have a look at the user type column by calling the `describe` method

# In[7]:


ride_sharing_Data['user_type'].describe()


# When we called the describe method, it turned out that pandas treates this information as `float`, while its a `categorical` information.
# Errors with regards to **data type constraints** are very common and important to handle in the data cleaning process.
# 
# `user_type` shouldn't be treated as `float`, it is **categorical**
# 
# The `user_type` column contains information on whether a user is taking<br>a free ride and takes on the following values:
# 
#     1 for free riders.
#     2 for pay per ride.
#     3 for monthly subscribers.

# **Let's fix this and convert the data type column to categorical**

# In[8]:


# Convert user_type to category
ride_sharing_Data['user_type_cat'] = ride_sharing_Data['user_type'].astype('category')


# **Let's check with as assert statement**

# In[9]:


# Write an assert statement confirming the change
assert ride_sharing_Data['user_type_cat'].dtype == 'category'


# **Let's double-check manually**

# In[10]:


# Print new summary statistics 
ride_sharing_Data['user_type_cat'].describe()
