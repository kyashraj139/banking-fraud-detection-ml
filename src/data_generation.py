"""Synthetic fraud data: demonstration only, not representative of real fraud."""
from pathlib import Path
import numpy as np
import pandas as pd

def generate_transactions(n=6000, seed=42):
    rng = np.random.default_rng(seed)
    amount = np.clip(rng.lognormal(3.7, 1.05, n), 1, 15000)
    hour = rng.integers(0, 24, n)
    age = rng.integers(18, 81, n)
    account_age_days = rng.integers(5, 3600, n)
    txn_24h = rng.poisson(3, n) + 1
    foreign = rng.binomial(1, 0.12, n)
    new_device = rng.binomial(1, 0.18, n)
    merchant = rng.choice(['grocery','travel','electronics','fuel','online'], n)
    region = rng.choice(['north','south','east','west'], n)
    risk = (-5.5 + .00022*amount + .85*foreign + .9*new_device
            + .12*txn_24h + .65*(hour<5) + .5*(merchant=='electronics')
            - .0002*account_age_days)
    probability = 1/(1+np.exp(-np.clip(risk,-30,30)))
    fraud = rng.binomial(1, probability)
    df = pd.DataFrame({'transaction_id':[f'T{i:07d}' for i in range(n)],
       'amount':np.round(amount,2),'hour':hour,'customer_age':age,
       'account_age_days':account_age_days,'transactions_24h':txn_24h,
       'foreign_transaction':foreign,'new_device':new_device,
       'merchant_category':merchant,'region':region,'fraud_flag':fraud})
    return df

def save_dataset(path='data/raw/banking_transactions.csv', n=6000, seed=42):
    output=Path(path); output.parent.mkdir(parents=True, exist_ok=True)
    df=generate_transactions(n,seed); df.to_csv(output,index=False); return df

if __name__=='__main__':
    print(save_dataset().shape)
