import pandas as pd

data = pd.read_csv("data.csv")

# print(data)
# print(data.info())
# print(data.describe())
# best = data.loc[data['sales'].idxmax()] # print a record index 2
# print(best)
# avg_price = data['price'].mean()
# avg_sales = data['sales'].mean()
# print("Average price:", avg_price)
# print("Average sales:", avg_sales)
# top_product = data.loc[data['sales'].idxmax()]['product']
# print("Top selling product:", top_product)

print("Dataset:")
print(data)

print("\nStatistics:")
print(data.describe())

best = data.loc[data['sales'].idxmax()]
print("\nBest selling product:")
print(best['product'])

avg_price = data['price'].mean()

print("\nAverage price:", avg_price)