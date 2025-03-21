import pandas as pd
import re
import pickle
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Step 1: Load Dataset
df = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]]
df.columns = ["label", "message"]
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Step 2: Preprocess Data
def preprocess_text(text):
    text = re.sub(r"\W", " ", text)  # Remove special characters
    text = text.lower().strip()
    return text

df["message"] = df["message"].apply(preprocess_text)

# Step 3: Train Model
X_train, X_test, y_train, y_test = train_test_split(df["message"], df["label"], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Step 4: Save Model & Vectorizer
pickle.dump(model, open("spam_classifier.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# Step 5: Create Flask App
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        message = request.form["message"]
        processed_message = preprocess_text(message)
        message_vector = vectorizer.transform([processed_message])
        prediction = model.predict(message_vector)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
    
    return render_template("index.html", result=result)

# Step 6: Run App
if __name__ == "__main__":
    app.run(debug=True)
