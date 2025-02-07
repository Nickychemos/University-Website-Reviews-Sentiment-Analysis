#importing the necessary Libraries
from textblob import TextBlob

#Reading the scrapped data
with open('TUKreviews.txt', 'r', encoding='utf-8') as f:
    text = f.read()

#Sentiment analysis
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)