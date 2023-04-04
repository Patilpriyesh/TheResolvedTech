#!/usr/bin/env python
# coding: utf-8

# # Google stock price prediction using machine learning 

# Import the libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[42]:


from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense,LSTM,Dropout


# load the training dataset

# In[49]:


data = pd.read_csv('D:\drive p\imp folders\TRT internship\Google_train_data.csv')
data.head()


# In[44]:


data.info()


# In[45]:


data["Close"] = pd.to_numeric(data.Close,errors = 'coerce')
data = data.dropna()
trainData = data.iloc[:,4:5].values


# In[46]:


data.info()


# In[48]:


sc = MinMaxScaler(feature_range=(0,1))
trainData = sc.fit_transform(trainData)
trainData.shape


# In[53]:


x_train = []
y_train = []

for i in range (60,1149): #60:timestep //1149 : Length of the data
    x_train.append(trainData[i-60:i,0])
    y_train.append(trainData[i,0])

x_train, y_train = np.array(x_train), np.array(y_train)    


# In[57]:


#adding the batch_size axis
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
x_train.shape


# In[66]:


model = Sequential()

model.add(LSTM(units = 100, return_sequences = True, input_shape = (x_train.shape[1],1)))
model.add(Dropout(0.2))

model.add(LSTM(units = 100, return_sequences = True))
model.add(Dropout(0.2))

model.add(LSTM(units = 100, return_sequences = True))
model.add(Dropout(0.2))

model.add(LSTM(units = 100, return_sequences = False))
model.add(Dropout(0.2))

model.add(Dense(units = 1))
model.compile(optimizer = 'adam', loss = "mean_squared_error")


# In[67]:


hist = model.fit(x_train, y_train, epochs = 20, batch_size = 32, verbose = 2)


# In[68]:


plt.plot(hist.history['loss'])
plt.title('Training model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc = 'upper left')
plt.show()


# In[72]:


testData = pd.read_csv('D:\drive p\imp folders\TRT internship\Google_test_data.csv')
testData["Close"] = pd.to_numeric(testData.Close, errors = 'coerce')
testData = testData.dropna()
testData = testData.iloc[:,4:5]
y_test = testData.iloc[60:,0:].values

#input array for the model

inputClosing = testData.iloc[:,0:].values
inputClosing_scaled = sc.transform(inputClosing)
inputClosing_scaled.shape
x_test = []
length = len(testData)
timestep = 60
for i in range(timestep, length):
    x_test.append(inputClosing_scaled[i-timestep:i,0])
x_test = np.array(x_test)
x_test = np.reshape(x_test,(x_test.shape[0], x_test.shape[1],1))
x_test.shape


# In[73]:


y_pred = model.predict(x_test)
y_pred


# In[74]:


predicted_price = sc.inverse_transform(y_pred)


# # Plotting the actual and predicted prices for google stocks

# In[75]:


plt.plot(y_test, color = 'red', label = 'Actual Stock Price')
plt.plot(predicted_price, color = 'green', label = 'Predicted Stock Price')
plt.title('Google stock price prediction')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()


# As you can see above, the model can predict the trend of the actual stock prices very closely. The accuracy of the model can be enhanced by training with more data and increasing the LSTM layers.

# # Conclusion:

# The stock market plays a remarkable role in our daily lives. It is a significant factor in a country's GDP growth. In this tutorial, you learned the basics of the stock market and how to perform stock price prediction using machine learning. 
