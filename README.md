# Banking Fraud Detection — End-to-End ML Portfolio Project

A reproducible, beginner-friendly **synthetic banking fraud** project using statistics, 9 scikit-learn classifiers, leakage-safe pipelines, model evaluation, and GitHub-ready files. **Not for real financial decisions.**

## Repository layout
```text
banking_fraud_detection/
├── notebooks/01_banking_fraud_detection.ipynb
├── src/__init__.py
├── src/data_generation.py
├── src/modeling.py
├── tests/test_project.py
├── data/raw/.gitkeep
├── data/processed/.gitkeep
├── models/.gitkeep
├── reports/figures/.gitkeep
├── docs/GITHUB_UPLOAD_GUIDE.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup (Windows PowerShell, Anaconda Prompt, or terminal)
```powershell
cd C:\Data Science\banking_fraud_detection
conda create -n banking-fraud python=3.11 -y
conda activate banking-fraud
python -m pip install -r requirements.txt
python -m ipykernel install --user --name banking-fraud --display-name "Python (banking-fraud)"
jupyter lab
```
Open `notebooks/01_banking_fraud_detection.ipynb`, choose the **Python (banking-fraud)** kernel, and **Run All**. You may instead use a regular Python 3.11 venv. The project is portable; `C:\Data Science` is an example path.

## What it teaches
- Synthetic data generation, quality checks, descriptive statistics, skewness, kurtosis, Wilson confidence intervals
- Mann–Whitney U, chi-square, Cramer's V, point-biserial correlation, visual EDA
- Train/validation/test splits, class imbalance, preprocessing without leakage
- Logistic Regression, Gaussian Naive Bayes, KNN, Decision Tree, Random Forest, Extra Trees, Gradient Boosting, Histogram Gradient Boosting, SVM
- PR-AUC, ROC-AUC, precision, recall, F1, confusion matrix, stratified CV, optional tuning
- Validation threshold selection, final test, permutation importance, model serialization

## Run tests
```powershell
python -m pytest -q
```

## Outputs
Notebook creates `data/raw/banking_transactions.csv`, `reports/model_comparison.csv`, `reports/figures/evaluation.png`, `models/fraud_pipeline.joblib`, and `models/metadata.json`. Generated data and binary models are ignored by Git. Results vary by environment; no target score is guaranteed.

## Security / limitations
Synthetic data is not representative of actual fraud; no real customer information is included. Do not upload secrets or actual bank data. Production requires chronological and customer-aware validation, robust labeling, model governance, fairness and drift monitoring, threshold economics, and human review.

## GitHub instructions
See [`docs/GITHUB_UPLOAD_GUIDE.md`](docs/GITHUB_UPLOAD_GUIDE.md).

## License
MIT — see `LICENSE`.
