import pandas as pd
import kagglehub
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder  


dataset_path = kagglehub.dataset_download("yasserh/housing-prices-dataset")

csv_file_path = f"{dataset_path}/Housing.csv"  

house_data = pd.read_csv(csv_file_path)
print(house_data.head())

y = house_data.price
all_features = house_data.columns
print(all_features)

features = input("\nEnter the features you want, separated by commas.:" ).replace(" ", "").split(",")
special_features = house_data[features]
print(special_features)

categorical_columns = special_features.select_dtypes(include=['object']).columns
le = LabelEncoder()

for col in categorical_columns:
    special_features[col] = le.fit_transform(special_features[col])

special_features = pd.get_dummies(special_features)
print(special_features)

train_special_features, val_special_features, train_y, val_y = train_test_split(special_features, y, random_state=0)
house_model = DecisionTreeRegressor()
house_model.fit(train_special_features, train_y)

prediction = house_model.predict(val_special_features)
val_mae = mean_absolute_error(val_y, prediction)
print(val_mae)

