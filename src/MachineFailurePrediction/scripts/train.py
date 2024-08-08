import pandas as pd #type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from xgboost import XGBClassifier
from joblib import dump #type: ignore

def train_model(df):
    X = df.drop(['Target', 'Failure Type'], axis=1)
    y = df['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = XGBClassifier(n_estimators=100, random_state=42, use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    
    dump(model, 'models/machine_failure_model.joblib')
    return model
