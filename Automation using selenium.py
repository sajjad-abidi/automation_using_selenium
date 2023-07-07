#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
driver.maximize_window()

input = driver.find_element('name', 'q')
input.send_keys('lucknow')
time.sleep(5)


button = driver.find_element('name', 'btnK')
button.click()

time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)

driver.quit()


# In[ ]:




