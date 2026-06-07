from textblob import TextBlob

review = "This product is amazing"

analysis = TextBlob(review)

print(analysis.sentiment.polarity)

from textblob import TextBlob

review = "This product is amazing"

polarity = TextBlob(review).sentiment.polarity

if polarity > 0:
    print("Positive")
elif polarity < 0:
    print("Negative")
else:
    print("Neutral")

import pandas as pd
from textblob import TextBlob

reviews = [
    "This product is amazing",
    "Worst product ever",
    "It is okay",
    "Excellent quality",
    "Very bad experience",
    "Good value for money"
]

df = pd.DataFrame(reviews, columns=["Review"])

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review"].apply(get_sentiment)

print(df)


import pandas as pd
from textblob import TextBlob

reviews = [
    "This product is amazing",
    "Worst product ever",
    "It is okay",
    "Excellent quality",
    "Very bad experience",
    "Good value for money"
]

df = pd.DataFrame(reviews, columns=["Review"])

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review"].apply(get_sentiment)

print(df)
        
import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x="Sentiment", data=df)

plt.title("Sentiment Distribution")

plt.savefig("sentiment_distribution.png")

plt.show()