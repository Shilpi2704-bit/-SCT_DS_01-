
# 📊 Population Distribution Analysis: Age & Gender

# 🧰 Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📥 Step 2: Simulate Dataset (or load a real one)
data = {
    'Age': [25, 34, 45, 23, 52, 60, 35, 27, 43, 39, 18, 66, 73, 29, 31, 50, 22, 24, 37, 28,
            80, 90, 12, 8, 15, 77, 55, 61, 33, 40],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female',
               'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female', 'Male']
}
df = pd.DataFrame(data)

# 🧹 Step 3: Data Cleaning
# No cleaning needed for simulated data

# 📊 Step 4: Visualization

## Age Histogram
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

## Gender Bar Chart
plt.figure(figsize=(6, 4))
gender_counts = df['Gender'].value_counts()
gender_counts.plot(kind='bar', color=['lightcoral', 'lightskyblue'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

## Age Distribution by Gender (Stacked Histogram)
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Age', hue='Gender', multiple='stack', bins=10, palette='Set2')
plt.title('Age Distribution by Gender')
plt.xlabel('Age')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# 📝 Step 5: Conclusion
print("""
Insights:
- Most individuals are aged between 20 and 40.
- Slightly more females than males in this sample.
- Females appear more frequently in older age ranges.
""")
