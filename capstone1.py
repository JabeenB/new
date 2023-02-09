import snscrape.modules.twitter as sntwitter
import pandas as pd

tweet_list1=[]#created to append the tweet data

#using twitterSearch Scraper
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:vistara').get_items()):
    if i>1000:
        break
    tweet_list1.append([tweet.id,tweet.date,tweet.content,tweet.user.username])

#creating DataFrame
df=pd.DataFrame(tweet_list1,columns=["datetime","username","Tweetid","text"])
print('DataFrame:\n', df)
scraped_tweets=(df.to_csv("scraped_tweets.csv",index=False))

#using streamlit

import streamlit as st
import numpy as np
import pandas as pd

st.title("Capstone project-1")
st.header("Twitter Scrapping")
#creating a dataframe

st.dataframe(df)
@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

st.download_button('Download CSV','text/csv')