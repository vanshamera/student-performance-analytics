import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Aman", "Riya", "Vansh", "Rahul"],
    "Math": [85, 90, 78, 88],
    "Science": [80, 85, 75, 95],
    "English": [78, 88, 80, 92]
}

df = pd.DataFrame(data)
df["Average"] = df[["Math","Science","English"]].mean(axis=1)

print(df.sort_values(by="Average", ascending=False))

df.plot(x="Name", y=["Math","Science","English"])
plt.title("Student Performance")
plt.show()
