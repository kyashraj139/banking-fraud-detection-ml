# GitHub Upload Guide — Beginner Walkthrough

## 1. Install Git and create a GitHub account
Install Git for Windows from https://git-scm.com/download/win and create/sign in to https://github.com. In PowerShell or Anaconda Prompt run `git --version`.

## 2. Unzip the project
Extract `banking_fraud_detection.zip` into `C:\Data Science\banking_fraud_detection` (or another location). Open a terminal in that folder. Confirm `README.md`, `requirements.txt`, `src`, `tests`, `notebooks`, and `docs` are present.

## 3. Create environment and test locally
```powershell
cd "C:\Data Science\banking_fraud_detection"
conda create -n banking-fraud python=3.11 -y
conda activate banking-fraud
python -m pip install -r requirements.txt
python -m pytest -q
jupyter lab
```
Choose notebook kernel matching the environment (register with `python -m ipykernel install --user --name banking-fraud --display-name "Python (banking-fraud)"` if needed), then run notebook cells from top to bottom. `ipykernel` is installed as a dependency of JupyterLab.

## 4. Create an EMPTY GitHub repository
GitHub → `+` → **New repository** → name `banking-fraud-detection-ml` → Public or Private → **do not initialize with README, .gitignore, or license** (they already exist locally) → Create repository. The repository is separate from GitHub **Projects** boards: the repository stores code; a Projects board tracks tasks.

## 5. Configure Git identity (one-time)
```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
Use your own name/email; GitHub supports a private no-reply email.

## 6. Initialize, stage, inspect and commit
```powershell
git init
git branch -M main
git status
git add README.md requirements.txt .gitignore LICENSE notebooks src tests docs data models reports
git status
git commit -m "Initial banking fraud ML project"
```
Before committing, inspect `git status` and verify that CSV files, model binaries, passwords, keys, `.env`, and large datasets are not staged. `.gitignore` excludes generated artifacts but does not untrack previously committed files; use `git rm --cached <path>` if necessary.

## 7. Connect to GitHub and push
Copy your own repository URL from GitHub (HTTPS example below). Do **not** copy a placeholder URL literally.
```powershell
git remote add origin https://github.com/YOUR_USERNAME/banking-fraud-detection-ml.git
git push -u origin main
```
Authenticate using the Git Credential Manager/browser sign-in or a suitable personal access token when requested. GitHub account passwords are not used for HTTPS Git pushes. Never embed credentials in URLs or files.

## 8. Confirm on GitHub
Refresh the repository page. Check the README renders, notebook opens, and the `src/`, `tests/`, and `docs/` folders exist. Generated model binaries should not be visible.

## 9. Optional: create a GitHub Projects board
On GitHub open your profile/organization → **Projects** → **New project** → Board. Add issues: (1) data generation, (2) statistical EDA, (3) model comparison, (4) evaluation, (5) documentation. Link repository issues to the board and move cards through Todo → In Progress → Done. A Projects board is optional; it does not replace the repository.

## 10. Future changes
```powershell
git status
git add .
git commit -m "Improve fraud evaluation"
git push
```
Check `git status` before every push. If a remote already exists, inspect `git remote -v` and use `git remote set-url origin <your-url>` rather than adding a duplicate.

## Troubleshooting
- `git not recognized`: reinstall Git for Windows and reopen terminal.
- `ModuleNotFoundError`: install requirements into the same Python environment as the notebook kernel.
- `fatal: not a git repository`: `cd` into the extracted project folder.
- `remote origin already exists`: use `git remote -v` then `git remote set-url origin ...`.
- Authentication failed: use browser-based Git Credential Manager or a correctly scoped token; never paste secrets into notebooks.
- Push rejected: verify repository is empty and branch is `main`; do not force-push without understanding the remote changes.
- `FileNotFoundError`: run notebook from repo root or `notebooks/` and keep `src/` alongside it.
