import pandas as pd
import random

data = []

for i in range(100):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = a + b

    data.append([a, b, c])

df = pd.DataFrame(data, columns=["a", "b", "c"])

for i in random.sample(range(100), 10):
    df.loc[i, "c"] = df.loc[i, "c"] + random.randint(-10, 10)

print(df)

df.to_csv("dataset.csv", index=False)
import matplotlib.pyplot as plt

plt.scatter(df["a"] + df["b"], df["c"])

plt.title("Actual Sum vs Dataset Value")
plt.xlabel("a + b")
plt.ylabel("c")

plt.show()