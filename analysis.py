import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_data.csv")

# Calculate average score
df["average"] = df[["math score","reading score","writing score"]].mean(axis=1)

# Top 3 students
top_students = df.sort_values(by="average", ascending=False).head(3)

# Subject averages
subject_avg = df[["math score","reading score","writing score"]].mean()

# Weakest subject
weakest_subject = subject_avg.idxmin()

print("Top Students:\n", top_students)
print("\nSubject Averages:\n", subject_avg)
print("\nWeakest Subject:", weakest_subject)

# Visualization
subject_avg.plot(kind="bar")
plt.title("Average Scores per Subject")
plt.savefig("performance.png")
plt.show()
