## **Task 1: Simple Linear Regression**

### **Problem Statement**
Predict the percentage of a student based on the no. of study. What will be the predicted score if a student studies for 9.25hrs per day?

### **Author: Shivani Rajhance.**

Importing the libraries
"""

# Commented out IPython magic to ensure Python compatibility.

import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
# %matplotlib inline

"""Importing the required Dataset"""

# Reading data from remote link
url = "http://bit.ly/w-data"
s_data = pd.read_csv(url)
print("Data imported successfully")

s_data.head(10)

"""Visualizing the dataset to get better understanding between the two parameters"""

#Plotting of graph to give the relation between hours & percentage
s_data.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours VS Percentage')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')
print("Data Visualized Successful")  
plt.show()

"""Dividing the data into "attributes" (inputs) and "labels" (outputs)."""

x = s_data.iloc[:, :-1].values  #independent values/variables
y = s_data.iloc[:, 1].values  #dependent values/variables

"""Splitting of Data into traing & test datasets"""

from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0) 
print("Splitted the data successfully\n\n")


print('Training Dataset')
print('Hours={} \n Percentage={}'.format(x_train.reshape(1,-1),y_train))
print('\nTesting Dataset')
print('Hours={} \n Percentage={}'.format(x_test.reshape(1,-1),y_test))

"""###**The Algorithm training**
Algorithm is Linear Regression. Training data for training the model & test data for predictions.
"""

from sklearn.linear_model import LinearRegression  
r = LinearRegression()  
r.fit(X_train, y_train) 
print("Coefficients: ",r.coef_)
print("Intercepts: ",r.intercept_)
print("Training complete.")

"""### **Plotting the Regression line using y=mx+c**
y=line required
m=r.coef
x=independent variable(hours)
c=r.intercept

"""

# Plotting the regression line
line = r.coef_*x+r.intercept_

# Plotting for the test data
plt.scatter(x, y)
plt.plot(x, line)
plt.xlabel("Hours")
plt.ylabel("Percentage")
plt.show()

"""### **Score Predictions**
Test Data is used for prediction
"""

#print(x_test)
y_pred = r.predict(x_test) # Predicting the scores

"""Comparison of Actual & Predicted values

"""

# Comparing Actual vs Predicted
pred= pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
pred["Difference"]=pred["Actual"]-pred["Predicted"]
pred

"""Predicting the score if the student studies for 9.25 hours per day"""

# You can also test with your own data
hours = np.array([[9.25]])
own_pred = r.predict(hours)
print("No of Hours = {}".format(hours[0][0]))
print("Predicted Score for 9.25 hours = {}".format(own_pred[0]))

"""### **Evaluating the model**

Checking the accuracy of the model. Mean absolute error, R2 score & Residual sum of squares are calculated.
"""

#Accuracy
from sklearn import metrics  
print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, y_pred))

#R2 Score 
from sklearn.metrics import r2_score
print("The R2 Score: {}".format(r2_score(y_pred,y_test)))

#Residual sum of squares
ss=np.sum(np.square(y_pred-y_test))
print("The Residual Sum of Squares: {}".format(ss))
