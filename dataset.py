import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Define the dataset as a dictionary
data = {
    "hours_studied":,
    "marks": [35, 40, 45, 50, 55, 65, 70, 80]
}

# 2. Convert the dictionary into a pandas DataFrame for structured data manipulation
df = pd.DataFrame(data)

# 3. Print the DataFrame to the console to verify the data structure
print(df)

# 4. Initialize a scatter plot using the defined X (hours) and Y (marks) variables
plt.scatter(df["hours_studied"], df["marks"])

# 5. Add descriptive labels to the horizontal and vertical axes
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

# 6. Display the generated plot in a window
plt.show()
