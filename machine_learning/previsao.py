# =========================
# IMPORTS
# =========================
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("C:/Users/dadoa/Downloads/archive (11)/job_salary_prediction_dataset.csv")

# =========================
# FEATURES E TARGET
# =========================
X = df.drop('salary', axis=1)
y = df['salary']

# =========================
# ENCODING (CATEGÓRICAS)
# =========================
X = pd.get_dummies(X, drop_first=True)

# =========================
# TRAIN / TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 1. REGRESSÃO LINEAR
# =========================
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# coeficientes
coef = pd.DataFrame({
    'feature': X_train.columns,
    'coefficient': lr_model.coef_
})

# intercepto
intercept = lr_model.intercept_

print("Intercept:", intercept)
print("\nTop coeficientes:")
print(coef.sort_values(by='coefficient', ascending=False).head(10))

y_pred_lr = lr_model.predict(X_test)

mae_lr = mean_absolute_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print("\n=== LINEAR REGRESSION ===")
print("MAE:", mae_lr)
print("R2:", r2_lr)

top_coef = coef.sort_values(by='coefficient', ascending=False).head(10)

print("\n=== EQUAÇÃO (TOP 10) ===")

equation = f"salary = {intercept:.2f}"

for _, row in top_coef.iterrows():
    equation += f" + ({row['coefficient']:.2f} * {row['feature']})"

print(equation)


# =========================
# 2. RANDOM FOREST
# =========================
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print("\n=== RANDOM FOREST ===")
print("MAE:", mae_rf)
print("R2:", r2_rf)

# =========================
# FEATURE IMPORTANCE
# =========================
importances = rf_model.feature_importances_

feature_importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': importances
}).sort_values(by='importance', ascending=False)

print("\n=== TOP 10 FEATURES MAIS IMPORTANTES ===")
print(feature_importance.head(10))

