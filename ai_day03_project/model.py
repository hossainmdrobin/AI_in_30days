import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("sales.csv")

X = data[['price']]
y = data['sales']
# print(X,y)

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[50]])
print("Predicted Sales: " , prediction)

plt.scatter(X,y)
plt.xlabel("Price")
plt.ylabel("Sales")
plt.title("Sales Pridiction model")

plt.show()




