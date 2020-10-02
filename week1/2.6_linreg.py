import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
pop = pd.read_excel('gapminder_population.xlsx', index_col=0)
pop = pop.sum()
pop.index = pop.index.astype(int)
logpop = np.log(pop)
logpop.dropna(inplace=True)
X = logpop.index.values.reshape(-1, 1)
y = logpop.values
m = LinearRegression()
m.fit(X, y)
ypred = m.predict(X)
print("slope    : ", m.coef_[0])
print("intercept: ", m.intercept_)
print("R-squared: ", m.score(X, y))
xfuture = [[2020], [2030], [2040], [2050], [2100]]
yfuture = m.predict(xfuture)
yfuture = np.exp(yfuture) / 1000_000_000
for year, forecast in zip(xfuture, yfuture):
    print(f"population forecast for {year}: {forecast:5.1f} bln")

plt.plot(X, y)
plt.plot(X, ypred)
plt.savefig('linearreg.png')
plt.show()