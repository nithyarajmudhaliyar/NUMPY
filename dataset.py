import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "marks": [35, 40, 45, 50, 55, 65, 70, 80]
}

df = pd.DataFrame(data)

print(df)

plt.scatter(df["hours_studied"], df["marks"])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()