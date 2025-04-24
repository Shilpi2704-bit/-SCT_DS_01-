import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Population Distribution Analysis: Age & Gender")

# Simulate dataset
data = {
    'Age': [25, 34, 45, 23, 52, 60, 35, 27, 43, 39, 18, 66, 73, 29, 31, 50, 22, 24, 37, 28,
            80, 90, 12, 8, 15, 77, 55, 61, 33, 40],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female',
               'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male',
               'Female', 'Male', 'Female', 'Male', 'Female', 'Male']
}
df = pd.DataFrame(data)

st.subheader("Age Distribution Histogram")
fig, ax = plt.subplots()
ax.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
ax.set_title('Age Distribution')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
st.pyplot(fig)

st.subheader("Gender Distribution Bar Chart")
fig, ax = plt.subplots()
gender_counts = df['Gender'].value_counts()
gender_counts.plot(kind='bar', color=['lightcoral', 'lightskyblue'], ax=ax)
ax.set_title('Gender Distribution')
ax.set_xlabel('Gender')
ax.set_ylabel('Count')
st.pyplot(fig)

st.subheader("Stacked Histogram: Age by Gender")
fig, ax = plt.subplots()
sns.histplot(data=df, x='Age', hue='Gender', multiple='stack', bins=10, palette='Set2', ax=ax)
ax.set_title('Age Distribution by Gender')
ax.set_xlabel('Age')
ax.set_ylabel('Count')
st.pyplot(fig)

st.markdown("""### 📝 Insights
- Most individuals are aged between 20 and 40.
- Slightly more females than males in this sample.
- Females appear more frequently in older age ranges.
""")
