import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

try:
    data = pd.read_csv('bamboo_reviewsss.csv')
except FileNotFoundError:
    print("Omo! File not found!")


def sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'


data['sentiment'] = data['content'].apply(sentiment)

sentiment_summary = data['sentiment'].value_counts()
print(f'Sentiment Summary:{sentiment_summary}')

text = ' '.join(data['content'].dropna().tolist())

stopwords = set(STOPWORDS)
stopwords.update(['app', 'game', 'play', 'will'])

wordcloud =WordCloud(
    width = 800,
    height = 400,
    background_color='white',
    stopwords=stopwords,
    min_font_size=10
).generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud for Bamboo Reviews")
plt.show()
