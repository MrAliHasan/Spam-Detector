from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the dataset
dataset = pd.read_excel('Email_Dataset.xlsx')

# Initialize the vectorizer and fit_transform the data


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(dataset['Message'])

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, dataset['Label'], test_size=0.2, random_state=42)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)


def home(request):
    return render(request, 'home.html')


def predict_spam(request):
    if request.method == 'POST':
        input_text = request.POST['message']

        # Transform the input text
        input_text = [input_text]
        input_features = vectorizer.transform(input_text)

        # Make predictions
        prediction = model.predict(input_features)

        return render(request, 'prediction.html', {'prediction': prediction[0]})
    else:
        return HttpResponse('Invalid request')
