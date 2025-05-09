import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#puting the r to tell program that \ is part of file path
my_data = pd.read_csv(r'C:\Users\OneDrive\Desktop\Learn Python\Linear Regression\advertising.csv')

# creates a 2D array of the inputs and outputs from the dataset
x = my_data[['TV', 'Radio', 'Newspaper']].values
y = my_data['Sales'].values

# Splitting the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Normalizing the data  
#x_train = (x_train - np.mean(x_train, axis=0)) / np.std(x_train, axis=0)
#x_test = (x_test - np.mean(x_train, axis=0)) / np.std(x_train, axis=0)


#train the model using the training set
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)

# Predict the output using the testing set
y_pred = model.predict(x_test)
#print(y_pred)
#compare it to the ytest and see the accuracy of the model, must use MSE see mean squared error
from sklearn.metrics import mean_squared_error, r2_score    
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
# MSE (between 0 and inf) is the average of the squared differences between the predicted and actual values, 0 is perfect fit and inf is no fit
print("Mean Squared Error:", mse)
# r2 (between 0 and 1) explains how much the vaiance is explained by the model, 1 is perfect fit and 0 is no fit
print("R-squared:", r2)
#plot the predicted values against the actual values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
plt.axis('tight')
plt.show()

