#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os


  
print (configur.get('installation', 'prefix')) 
  
 
print (configur.read(os.path.expanduser('~/.config.ini'))) 
print (configur.get('installation', 'prefix')) 
print (configur.get('installation', 'library')) 
  
print (configur.getboolean('debug', 'log_errors'))


# In[ ]:





# In[ ]:




