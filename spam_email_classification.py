
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

print(" Loading dataset...")

data = {
    "text": [
        "Win money now", 
        "Congratulations, you won a free gift card",
        "Free vacation offer for you",
        "Lowest price on medicines",
        "Call me when you reach",
        "Are we meeting today?",
        "Please send the report",
        "Let's have lunch tomorrow",
        "URGENT! Your account is blocked",
        "Schedule a meeting with your boss"
    ],
    "label": [
        1, 1, 1, 1,   # spam = 1
        0, 0, 0, 0, 0, 0   # ham = not spam = 0
    ]
}

df = pd.DataFrame(data)
print(" Dataset loaded successfully!\n")
print("Here are the first 5 rows of the dataset:")
print(df.head(), "\n")
print(" Preprocessing text...")

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text']).toarray()
y = df['label']

print(" Text vectorization complete!\n")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print(" Data split complete!\n")

print(" Training KNN model...")
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print(" Model training complete!\n")

print("Evaluating model...")
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print(" Testing with a sample input...")
sample_email = ["Win a free iPhone now!!!"]

sample_vector = vectorizer.transform(sample_email).toarray()
prediction = model.predict(sample_vector)

if prediction[0] == 1:
    result = "SPAM"
else:
    result = "NOT SPAM"

print("Predicted Category:", result, "\n")

pickle.dump(model, open('spam_knn_model.pkl', 'wb'))
pickle.dump(vectorizer, open('spam_vectorizer.pkl', 'wb'))
print(" Model saved successfully as 'spam_knn_model.pkl'")
print(" Vectorizer saved as 'spam_vectorizer.pkl'")
