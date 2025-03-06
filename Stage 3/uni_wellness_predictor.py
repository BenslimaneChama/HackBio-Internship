import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.feature_selection import RFE

# Load and preprocess data
df = pd.read_csv('http://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Student%20Depression%20Dataset.csv')
df = df.dropna().drop(columns=['id'])
df = df[(df['Job Satisfaction'] == 0.0) & (df['Work Pressure'] == 0.0)]
df = df[df['Profession'] == 'Student'].drop(columns=['Profession', 'Job Satisfaction', 'Work Pressure'])

valid_cities = ['Visakhapatnam', 'Bangalore', 'Srinagar', 'Varanasi', 'Jaipur', 'Pune', 'Thane',
                'Chennai', 'Nagpur', 'Nashik', 'Vadodara', 'Kalyan', 'Rajkot', 'Ahmedabad',
                'Kolkata', 'Mumbai', 'Lucknow', 'Indore', 'Surat', 'Ludhiana', 'Bhopal',
                'Meerut', 'Agra', 'Ghaziabad', 'Hyderabad', 'Vasai-Virar', 'Kanpur', 'Patna',
                'Faridabad', 'Delhi']

df = df[df['City'].isin(valid_cities)]
le_city = LabelEncoder()
df['City'] = le_city.fit_transform(df['City'])
city_mapping = dict(zip(le_city.classes_, le_city.transform(le_city.classes_)))

categorical_cols = ['Gender', 'Dietary Habits', 'Degree', 
                   'Have you ever had suicidal thoughts ?', 'Family History of Mental Illness']
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = dict(zip(le.classes_, le.transform(le.classes_)))

sleep_mapping = {'Less than 5 hours': 4, '5-6 hours': 5.5, 'Others': 6.5,
                '7-8 hours': 7.5, 'More than 8 hours': 9}
df['Sleep Duration'] = df['Sleep Duration'].map(sleep_mapping)

# Prepare data for modeling
X = df.drop(columns=['Depression'])
Y = df['Depression']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train Logistic Regression
log_reg = LogisticRegression(max_iter=1000, random_state=123)
log_reg.fit(X_train, Y_train)

# Train XGBoost with RFE
rfe_6 = RFE(estimator=XGBClassifier(eval_metric='logloss', random_state=123), n_features_to_select=6)
X_rfe_6 = rfe_6.fit_transform(X, Y)
selected_features_6 = X.columns[rfe_6.support_]
X_train_rfe6, X_test_rfe6, y_train, y_test = train_test_split(X_rfe_6, Y, test_size=0.2, random_state=123)
xgb_rfe6 = XGBClassifier(eval_metric='logloss', random_state=123)
xgb_rfe6.fit(X_train_rfe6, y_train)

# User interaction
def get_xgboost_input():
    print("\nPlease provide the following information (XGBoost model):")
    age = float(input("Age: "))
    academic_pressure = float(input("Academic Pressure (0-5 scale): "))
    study_satisfaction = float(input("Study Satisfaction (0-5 scale): "))
    
    diet = input("Dietary Habits (Healthy/Moderate/Others/Unhealthy): ")
    while diet not in label_encoders['Dietary Habits']:
        diet = input("Invalid input. Please enter from (Healthy/Moderate/Others/Unhealthy): ")
    
    suicidal = input("Ever had suicidal thoughts? (Yes/No): ")
    while suicidal not in label_encoders['Have you ever had suicidal thoughts ?']:
        suicidal = input("Invalid input. Please enter Yes/No: ")
    
    financial_stress = float(input("Financial Stress (0-5 scale): "))
    
    return {
        'Age': age,
        'Academic Pressure': academic_pressure,
        'Study Satisfaction': study_satisfaction,
        'Dietary Habits': label_encoders['Dietary Habits'][diet],
        'Have you ever had suicidal thoughts ?': label_encoders['Have you ever had suicidal thoughts ?'][suicidal],
        'Financial Stress': financial_stress
    }

def get_logistic_input():
    print("\nPlease provide the following information (Logistic Regression model):")
    inputs = {}
    
    inputs['Gender'] = label_encoders['Gender'][input("Gender (Male/Female): ")]
    inputs['Age'] = float(input("Age: "))
    
    city = input(f"City ({', '.join(city_mapping.keys())}): ")
    while city not in city_mapping:
        city = input("Invalid city. Please enter from the valid cities list: ")
    inputs['City'] = city_mapping[city]
    
    inputs['Academic Pressure'] = float(input("Academic Pressure (0-5 scale): "))
    inputs['CGPA'] = float(input("CGPA: "))
    inputs['Study Satisfaction'] = float(input("Study Satisfaction (0-5 scale): "))
    
    sleep = input("Sleep Duration (Less than 5 hours/5-6 hours/7-8 hours/More than 8 hours/Others): ")
    while sleep not in sleep_mapping:
        sleep = input("Invalid input. Please enter valid sleep duration: ")
    inputs['Sleep Duration'] = sleep_mapping[sleep]
    
    diet = input("Dietary Habits (Healthy/Moderate/Others/Unhealthy): ")
    while diet not in label_encoders['Dietary Habits']:
        diet = input("Invalid input. Please enter from (Healthy/Moderate/Others/Unhealthy): ")
    inputs['Dietary Habits'] = label_encoders['Dietary Habits'][diet]
    
    inputs['Degree'] = label_encoders['Degree'][input("Degree: ")]
    
    suicidal = input("Ever had suicidal thoughts? (Yes/No): ")
    while suicidal not in label_encoders['Have you ever had suicidal thoughts ?']:
        suicidal = input("Invalid input. Please enter Yes/No: ")
    inputs['Have you ever had suicidal thoughts ?'] = label_encoders['Have you ever had suicidal thoughts ?'][suicidal]
    
    inputs['Work/Study Hours'] = float(input("Work/Study Hours: "))
    inputs['Financial Stress'] = float(input("Financial Stress (0-5 scale): "))
    
    family = input("Family History of Mental Illness (Yes/No): ")
    while family not in label_encoders['Family History of Mental Illness']:
        family = input("Invalid input. Please enter Yes/No: ")
    inputs['Family History of Mental Illness'] = label_encoders['Family History of Mental Illness'][family]
    
    return inputs

# Main interaction loop
print("University Student Depression Prediction System")
model_choice = input("Choose model [Enter for XGBoost (6 features) or 'LR' for Logistic Regression (full features)]: ").strip().upper()

if model_choice == 'LR':
    model = log_reg
    model_name = 'Logistic Regression'
    user_input = get_logistic_input()
    input_df = pd.DataFrame([user_input], columns=X.columns)
else:
    model = xgb_rfe6
    model_name = 'XGBoost'
    user_input = get_xgboost_input()
    input_df = pd.DataFrame([user_input], columns=selected_features_6)

print(f"\nUsing model: {model_name}")

if model_name == 'XGBoost':
    input_data = input_df.values
else:
    input_data = input_df

pred = model.predict(input_data)[0]
prob = model.predict_proba(input_data)[0][1]

result = "Likely depressed" if pred == 1 else "Not likely depressed"
print(f"\nPrediction Result: {result}")
print(f"Probability of depression: {prob:.2%}")