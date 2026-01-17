# ai_single_detection.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# -----------------------------
# Training data
# -----------------------------
phrases = [
    "Ay clean my pc for me dont you?",
    "Clean my computer now",
    "I need you to clean my PC",
    "Do nothing",
    "Turn off the lights",
    "Play some music"
]

labels = [
    "clean_pc",
    "clean_pc",
    "clean_pc",
    "no_action",
    "no_action",
    "no_action"
]
# -----------------------------
# Text to numbers
# -----------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(phrases)

# -----------------------------
# Train model
# -----------------------------
model = MultinomialNB()
model.fit(X, labels)

# -----------------------------
# Action function
# -----------------------------
def clean_pc():
    print("Cleaning PC... Done!")

# -----------------------------
# Test AI
# -----------------------------
test_commands = [
    "Could you clean the PC?",
    "Clean my comp ASAP",
    "i dont know do nothing"
]

for cmd in test_commands:
    X_test = vectorizer.transform([cmd])
    prediction = model.predict(X_test)[0]

    print(f"\nInput: {cmd}")
    if prediction == "clean_pc":
        clean_pc()
    else:
        print("No action detected.")