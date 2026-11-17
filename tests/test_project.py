from src.data_generation import generate_transactions
from src.modeling import make_pipeline, candidate_models, FEATURES
from sklearn.model_selection import train_test_split

def test_generation_reproducible():
    assert generate_transactions(100,42).equals(generate_transactions(100,42))

def test_schema_and_target():
    df=generate_transactions(300)
    assert set(FEATURES+['fraud_flag']).issubset(df.columns)
    assert set(df.fraud_flag.unique()).issubset({0,1})

def test_training_predict():
    df=generate_transactions(600)
    x=df[FEATURES]; y=df.fraud_flag
    assert y.nunique()==2
    p=make_pipeline(candidate_models()['Logistic Regression'])
    p.fit(x,y)
    assert len(p.predict(x.iloc[:4]))==4
