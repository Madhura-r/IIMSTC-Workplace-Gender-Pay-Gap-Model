import pandas as pd

# STEP 1: Load CLEANED dataset (not raw)
df = pd.read_csv("cleaned_salary_dataset_v1.csv")

print("Dataset Loaded Successfully")
print("\nColumns:")
print(df.columns)

# STEP 2: Encode Gender
df['gender'] = df['gender'].map({'male': 1, 'female': 0})

print("\nGender after encoding:")
print(df['gender'].unique())

# STEP 3: One-Hot Encode Education Level
# Using drop_first=True to avoid dummy variable trap (multicollinearity)
df = pd.get_dummies(df, columns=['education_level'], drop_first=True)

print("\nEducation encoding completed successfully.")

print("\nColumns after education encoding:")
print(df.columns)

# STEP 4: Save encoded dataset
df.to_csv("final_encoded_dataset.csv", index=False)


print("\nDummy encoding completed successfully!")

