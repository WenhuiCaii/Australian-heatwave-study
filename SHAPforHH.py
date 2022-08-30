from sklearn.ensemble import RandomForestRegressor
import shap
import pandas as pd
from sklearn.model_selection import train_test_split
import warnings
from PyALE import ale

# Read data from excel and set x and y
data = pd.read_excel("C:/test.xlsx")
x = data.iloc[:, 1: 36]
y = data.iloc[:, 0]

# Random Forest Model with 20% test size
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)
regr = RandomForestRegressor(n_estimators=1000, random_state=0)
regr.fit(x_train, y_train.values.ravel())

# Make prediction
predictions = regr.predict(x_test)

# Generate importance of variables
importances = list(regr.feature_importances_)

# Show importance
characteristics = x.columns
characteristics_importances = [(characteristic, round(importance, 2)) for characteristic, importance in
                               zip(characteristics, importances)]
characteristics_importances = sorted(characteristics_importances, key=lambda x: x[1], reverse=True)
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in characteristics_importances]

# ignore warnings for SHAP explainer
warnings.filterwarnings('ignore')

# Set SHAP explainer
# Top 5% samples was selected
explainer = shap.KernelExplainer(model=regr.predict, data=x.loc[x.Heatwave >= 35.8843], link="identity")

# Set the index of the specific example to explain
x_idx = 0

# Train SHAP explanation Model
shap_values = explainer.shap_values(X=x.loc[x.Heatwave >= 45], nsamples=100)

# Generate SHAP plot
shap.summary_plot(shap_values=shap_values,
                  features=x.iloc[0:50, :],
                  show=False  # save image to plt figure frame
                  )

# Generate ALE plot
ale_eff = ale(X=x_test, model=regr, feature=["NO2"], grid_size=50, include_CI=True, C=0.95)
