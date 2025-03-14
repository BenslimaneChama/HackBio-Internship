import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import RFE
# Prepare Data
df = pd.read_csv('http://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Student%20Depression%20Dataset.csv')
df=df.dropna()
df = df.drop(columns=['id'])
df = df[(df['Job Satisfaction'] == 0.0) & (df['Work Pressure'] == 0.0)]
df = df[df['Profession'] == 'Student']
df = df.drop(columns=['Profession'])
df = df.drop(columns=['Job Satisfaction'])
df = df.drop(columns=['Work Pressure'])
valid_cities = [
    'Visakhapatnam', 'Bangalore', 'Srinagar', 'Varanasi', 'Jaipur', 'Pune', 'Thane',
    'Chennai', 'Nagpur', 'Nashik', 'Vadodara', 'Kalyan', 'Rajkot', 'Ahmedabad',
    'Kolkata', 'Mumbai', 'Lucknow', 'Indore', 'Surat', 'Ludhiana', 'Bhopal',
    'Meerut', 'Agra', 'Ghaziabad', 'Hyderabad', 'Vasai-Virar', 'Kanpur', 'Patna',
    'Faridabad', 'Delhi'
]


df = df[df['City'].isin(valid_cities)]
le_city = LabelEncoder()
df['City'] = le_city.fit_transform(df['City'])

# Save the mapping of City names to numbers
city_mapping = dict(zip(le_city.classes_, le_city.transform(le_city.classes_)))
categorical_cols = ['Gender', 'Dietary Habits', 'Degree', 'Have you ever had suicidal thoughts ?', 'Family History of Mental Illness']

# Create a dictionary to store mappings
label_encoders = {}

# Encode each categorical column
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    
    # Store the mapping of labels to numbers
    label_encoders[col] = dict(zip(le.classes_, le.transform(le.classes_)))

sleep_mapping = {
    'Less than 5 hours': 4,
    '5-6 hours': 5.5,
    'Others': 6.5,
    '7-8 hours': 7.5,
    'More than 8 hours': 9
}

df['Sleep Duration'] = df['Sleep Duration'].map(sleep_mapping)
df = df[df['Age'] <= 40]
df = df[df['CGPA'] > 0]
df_female = df[df["Gender"] == 0]
df_female = df_female.drop(columns=['Gender'])
df_male = df[df["Gender"] == 1]
df_male = df_male.drop(columns=['Gender'])



# Define feature lists explicitly for each gender
female_features = [
    'Age', 'Academic Pressure', 'CGPA', 'Study Satisfaction', 
    'Sleep Duration', 'Dietary Habits', 'Have you ever had suicidal thoughts ?',
    'Work/Study Hours', 'Financial Stress', 'Family History of Mental Illness'
]

male_features = [
    'Age', 'Academic Pressure', 'Study Satisfaction', 
    'Dietary Habits', 'Have you ever had suicidal thoughts ?',
    'Work/Study Hours', 'Financial Stress', 'Family History of Mental Illness'
]

def train_model(df, feature_list):
    X = df[feature_list]  # Use predefined features
    y = df["Depression"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_scaled, y)
    return model, scaler

# Update input functions to match the predefined features
def female_input():
    print("\nPlease provide the following information (Female Model):")
    inputs = {}
    inputs['Age'] = float(input("Age: "))
    inputs['Academic Pressure'] = float(input("Academic Pressure (0-5 scale): "))
    inputs['CGPA'] = float(input("CGPA: "))
    inputs['Study Satisfaction'] = float(input("Study Satisfaction (0-5 scale): "))
    
    sleep = input("Sleep Duration (Less than 5 hours/5-6 hours/7-8 hours/More than 8 hours/Others): ")
    inputs['Sleep Duration'] = sleep_mapping[sleep]
    
    diet = input("Dietary Habits (Healthy/Moderate/Others/Unhealthy): ")
    inputs['Dietary Habits'] = label_encoders['Dietary Habits'][diet]
    
    suicidal = input("Ever had suicidal thoughts? (Yes/No): ")
    inputs['Have you ever had suicidal thoughts ?'] = label_encoders['Have you ever had suicidal thoughts ?'][suicidal]
    
    inputs['Work/Study Hours'] = float(input("Work/Study Hours: "))
    inputs['Financial Stress'] = float(input("Financial Stress (0-5 scale): "))
    
    family = input("Family History of Mental Illness (Yes/No): ")
    inputs['Family History of Mental Illness'] = label_encoders['Family History of Mental Illness'][family]
    
    return inputs

def male_input():
    print("\nPlease provide the following information (Male Model):")
    inputs = {}
    inputs['Age'] = float(input("Age: "))
    inputs['Academic Pressure'] = float(input("Academic Pressure (0-5 scale): "))
    inputs['Study Satisfaction'] = float(input("Study Satisfaction (0-5 scale): "))
    
    diet = input("Dietary Habits (Healthy/Moderate/Others/Unhealthy): ")
    inputs['Dietary Habits'] = label_encoders['Dietary Habits'][diet]
    
    suicidal = input("Ever had suicidal thoughts? (Yes/No): ")
    inputs['Have you ever had suicidal thoughts ?'] = label_encoders['Have you ever had suicidal thoughts ?'][suicidal]
    
    inputs['Work/Study Hours'] = float(input("Work/Study Hours: "))
    inputs['Financial Stress'] = float(input("Financial Stress (0-5 scale): "))

    family = input("Family History of Mental Illness (Yes/No): ")
    inputs['Family History of Mental Illness'] = label_encoders['Family History of Mental Illness'][family]
    
    return inputs

# Main execution
print("University Student Depression Prediction System")
gender = input("What's your gender? type female or male: ").lower()

if gender == 'female':
    model, scaler = train_model(df_female, female_features)
    user_input = female_input()
    input_df = pd.DataFrame([user_input])[female_features]
elif gender == 'male':
    model, scaler = train_model(df_male, male_features)
    user_input = male_input()
    input_df = pd.DataFrame([user_input])[male_features]

pred = model.predict(input_df)[0]
prob = model.predict_proba(input_df)[0][1]

print(f"\nPrediction Result: {'Likely depressed' if pred == 1 else 'Not likely depressed'}")
print(f"Probability of depression: {prob:.2%}")