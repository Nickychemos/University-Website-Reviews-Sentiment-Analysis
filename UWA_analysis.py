from textblob import TextBlob

with open('UWAreview.txt', 'r', encoding='utf-8') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)

#The overall sentiment of the whole text is 0.336, indicating a sightly positive sentiment.