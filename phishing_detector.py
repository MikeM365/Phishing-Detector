from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

train_emails = [
    "Congratulations! You have won a $1000 Walmart gift card. Click here to claim now.",
    "Alert: Your account has been compromised. Log in to verify your identity.",
    "Dear customer, your order has shipped and will arrive soon.",
    "Let's have lunch tomorrow at our usual place?",
    "Please see attached report for the project update.",
    "You've been selected for a limited-time offer, act now!",
    "Can you send me the quarterly financials by end of day?",    
]
labels = [1, 1, 0, 0, 0, 1, 0]  # 1 = Phishing, 0 = Legitimate

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(train_emails)

model = MultinomialNB()
model.fit(X, labels)

test_emails = [
    "Dear user, your account has been selected for a prize! Click this link to claim.",
    "Hi team, please find the attached project update document for review.", 
    "URGENT: Your bank account is locked. Login now to verify your information http://fakebank.com",
    "Lunch at noon in the kitchen. See you there!", 
]

test_X = vectorizer.transform(test_emails)
predictions = model.predict(test_X)

for email, prediction in zip(test_emails, predictions):
  print("Email:", email)
  print("Prediction:", "Phishing" if prediction == 1 else "Legitimate")
  print("-" * 60)