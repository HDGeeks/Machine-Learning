import numpy as np
import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score

# Put the correct absolute path here (same style as your baseline.py)
DATA_PATH = "/Users/hd/Desktop/Machine Learning/ML-Excercises/train.csv"

def clean_text(s: str) -> str:
    if pd.isna(s):
        return ""
    s = str(s).replace("\u200b", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s

tfidf = TfidfVectorizer(
    analyzer="char",
    ngram_range=(3, 5),
    min_df=2,
    max_df=0.95,
    sublinear_tf=True
)

clf = LinearSVC(C=1.0)

runs = 0
f1_total = 0.0
scores = []

for seed in range(100):
    # ✅ always loads correctly
    train = pd.read_csv(DATA_PATH, sep=",")

    if "targets" in train.columns and "label" not in train.columns:
        train = train.rename(columns={"targets": "label"})

    test = train.sample(frac=0.05, random_state=seed)
    train = train.drop(test.index)

    y_train = np.array(train["label"])
    y_test  = np.array(test["label"])

    X_train_raw = train["samples"].map(clean_text)
    X_test_raw  = test["samples"].map(clean_text)

    X_train = tfidf.fit_transform(X_train_raw)
    X_test  = tfidf.transform(X_test_raw)

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    f1 = f1_score(y_test, y_pred, average="macro")
    scores.append(f1)
    f1_total += f1
    runs += 1

scores = np.array(scores)
print(f"Average F1 after {runs} runs: {f1_total/runs:.6f}")
print(f"Std dev: {scores.std():.6f}")
print(f"Min / Max: {scores.min():.6f} / {scores.max():.6f}")