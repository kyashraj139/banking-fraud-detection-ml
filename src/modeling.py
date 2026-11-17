"""Leakage-safe preprocessing and classifier construction."""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier, HistGradientBoostingClassifier
from sklearn.svm import SVC

NUMERIC=['amount','hour','customer_age','account_age_days','transactions_24h','foreign_transaction','new_device']
CATEGORICAL=['merchant_category','region']
FEATURES=NUMERIC+CATEGORICAL

def make_preprocessor():
    return ColumnTransformer([
      ('numeric',Pipeline([('imputer',SimpleImputer(strategy='median')),('scale',StandardScaler())]),NUMERIC),
      ('categorical',Pipeline([('imputer',SimpleImputer(strategy='most_frequent')),('encode',OneHotEncoder(handle_unknown='ignore',sparse_output=False))]),CATEGORICAL)
    ])

def candidate_models():
    return {
      'Logistic Regression':LogisticRegression(max_iter=1500,class_weight='balanced',random_state=42),
      'Gaussian Naive Bayes':GaussianNB(),
      'KNN':KNeighborsClassifier(n_neighbors=15),
      'Decision Tree':DecisionTreeClassifier(max_depth=6,class_weight='balanced',random_state=42),
      'Random Forest':RandomForestClassifier(n_estimators=100,min_samples_leaf=3,class_weight='balanced',random_state=42,n_jobs=-1),
      'Extra Trees':ExtraTreesClassifier(n_estimators=100,min_samples_leaf=3,class_weight='balanced',random_state=42,n_jobs=-1),
      'Gradient Boosting':GradientBoostingClassifier(random_state=42),
      'Histogram Gradient Boosting':HistGradientBoostingClassifier(max_iter=100,random_state=42),
      'SVM':SVC(kernel='rbf',probability=True,class_weight='balanced',random_state=42)
    }

def make_pipeline(estimator):
    return Pipeline([('preprocess',make_preprocessor()),('model',estimator)])
