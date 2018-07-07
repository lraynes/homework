
# NewsMood

* CNN has a mix of both positive and negative tweets, resulting in a compound score very close to zero (neutral).
* CBS is the most positive news outlet of the five and rarely tweets negative content.
* BBC and the New York Times have a very similar mix of positive and negative tweets, with their compound scores being nearly identical.


```python
import tweepy
import json
import pandas as pd
import numpy as np
from config import (consumer_key, consumer_secret, access_token, access_token_secret)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
import matplotlib.pyplot as plt

analyzer = SentimentIntensityAnalyzer()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
master_list = []
news_orgs = ["BBC", "CBS", "CNN", "FOXTV", "nytimes"]

for user in news_orgs:
    
    #Loop through 5 pages of tweets (total 100 tweets)
    for x in range(1, 6):

        #Get all tweets from home feed
        public_tweets = api.user_timeline(user, page=x)

        #Loop through all tweets
        for tweet in public_tweets:

            #Vader analysis
            results = analyzer.polarity_scores(tweet["text"])
            
            #Timestamp conversion
            time = tweet["created_at"]
            converted_time = datetime.strptime(time, "%a %b %d %H:%M:%S %z %Y").replace(tzinfo=None)
            
            #Add all data to dictionary
            master_list.append({
                "User": user,
                "Time": converted_time,
                "Tweet Text": tweet["text"],
                "Compound": results["compound"],
                "Positive": results["pos"],
                "Neutral": results["neu"],
                "Negative": results["neg"],
            })
```


```python
#Convert list of dictionaries to dataframe
data_frame = pd.DataFrame(master_list)

#Export to CSV
data_frame.to_excel("sentiment_news_tweets.xlsx", index=False)
```


```python
#Creating user-specific dataframes
bbc = data_frame[data_frame["User"] == "BBC"]
cbs = data_frame[data_frame["User"] == "CBS"]
cnn = data_frame[data_frame["User"] == "CNN"]
fox = data_frame[data_frame["User"] == "FOXTV"]
nyt = data_frame[data_frame["User"] == "nytimes"]
```


```python
plt.figure()

#Different handles for each news outlet
bbc_handle = plt.scatter(bbc.index, bbc["Compound"], marker="o", c="yellow", edgecolors="black", alpha = .70, label = "BBC")
cbs_handle = plt.scatter(bbc.index, cbs["Compound"], marker="o", c="darkorchid", edgecolors="black", alpha = .70, label = "CBS")
cnn_handle = plt.scatter(bbc.index, cnn["Compound"], marker="o", c="lawngreen", edgecolors="black", alpha = .70, label = "CNN")
fox_handle = plt.scatter(bbc.index, fox["Compound"], marker="o", c="orangered", edgecolors="black", alpha = .70, label = "FOX")
nyt_handle = plt.scatter(bbc.index, nyt["Compound"], marker="o", c="dodgerblue", edgecolors="black", alpha = .70, label = "NYT")

plt.title("Sentiment Analysis of Media Tweets (6/13/2018)")
plt.xlabel("Number of Tweets Ago")
plt.ylabel("Sentiment")

lgnd = plt.legend(loc="upper left", fancybox=True, shadow=True, bbox_to_anchor=(1, 0.5), title="News Outlets")
lgnd.legendHandles[0]
lgnd.legendHandles[1]
lgnd.legendHandles[2]
lgnd.legendHandles[3]
lgnd.legendHandles[4]

#Export to PNG
plt.savefig("sentiment_scatter.png",dpi="figure",bbox_inches="tight")

plt.show()
```


![png](output_5_0.png)



```python
group = data_frame.groupby(["User"])
thing = group.mean()
thing
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
    </tr>
    <tr>
      <th>User</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BBC</th>
      <td>0.030947</td>
      <td>0.08134</td>
      <td>0.82310</td>
      <td>0.09554</td>
    </tr>
    <tr>
      <th>CBS</th>
      <td>0.348066</td>
      <td>0.01397</td>
      <td>0.79497</td>
      <td>0.19107</td>
    </tr>
    <tr>
      <th>CNN</th>
      <td>-0.008282</td>
      <td>0.07788</td>
      <td>0.84625</td>
      <td>0.07581</td>
    </tr>
    <tr>
      <th>FOXTV</th>
      <td>0.213607</td>
      <td>0.02243</td>
      <td>0.82977</td>
      <td>0.14781</td>
    </tr>
    <tr>
      <th>nytimes</th>
      <td>0.037706</td>
      <td>0.06964</td>
      <td>0.84861</td>
      <td>0.08178</td>
    </tr>
  </tbody>
</table>
</div>




```python
barlist = plt.bar(news_orgs, thing["Compound"])

#Assigning corresponding colors to each bar
barlist[0].set_color('yellow')
barlist[1].set_color('darkorchid')
barlist[2].set_color('lawngreen')
barlist[3].set_color('orangered')
barlist[4].set_color('dodgerblue')

plt.title("Sentiment Analysis of Media Tweets (6/13/2018)")
plt.xlabel("News Outlets")
plt.ylabel("Sentiment")

#Export to PNG
plt.savefig("sentiment_bar.png")

plt.show()
```


![png](output_7_0.png)

