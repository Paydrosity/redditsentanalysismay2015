# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:27:54 2017

@author: Paydrosity
"""

from textblob import TextBlob
import sqlite3
import numpy
import matplotlib.pyplot as plt

# Using textblob to do semantic analysis for all comments in each subreddit, finding 
# comments that are more subjective than objective, and adding them to a list which
# we then calculate the average of to compare against other subreddits...

# Average sentiment analysis of all comments in a given subreddit
def sentianalyze(dbData):
    sentmeans = []
    for body in dbData:
        blob = TextBlob(body)
        if blob.sentiment.subjectivity > 0:
            sentmeans.append(blob.sentiment.polarity)  
    return numpy.mean(sentmeans)
    
sql_conn = sqlite3.connect('C://Users/Paydrosity/Documents/reddit-comments-may-2015 (1)/database.sqlite')
# lamba changes cursor output from an awkward tuple into a manageable list
sql_conn.row_factory = lambda cursor, row: row[0]

c = sql_conn.cursor()
announcementsData = c.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'announcements'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000")
d = sql_conn.cursor()
blogData = d.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'blog'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000") 
e = sql_conn.cursor()
picsData = e.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'pics'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000")
l = sql_conn.cursor()
funnyData = l.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'funny'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000")            
f = sql_conn.cursor()
askredditData = f.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'AskReddit'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000")
g = sql_conn.cursor()
scienceData = g.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'science'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000") 
h = sql_conn.cursor()
wtfData = h.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'WTF'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000") 
i = sql_conn.cursor()
politicsData = i.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'politics'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000")
j = sql_conn.cursor()
worldnewsData = j.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'worldnews'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000") 
k = sql_conn.cursor()
technologyData = k.execute("SELECT body FROM May2015\
                         WHERE subreddit = 'technology'\
                         AND LENGTH(body) > 25\
                         LIMIT 80000") 
# MAKE SURE order of FinalData matches FinalSubs so the plot doesn't get disorganized.

FinalData = sentianalyze(announcementsData.fetchall()), sentianalyze(blogData.fetchall()), sentianalyze(picsData.fetchall()), sentianalyze(funnyData.fetchall()), sentianalyze(askredditData.fetchall()), sentianalyze(scienceData.fetchall()), sentianalyze(wtfData.fetchall()), sentianalyze(politicsData.fetchall()), sentianalyze(worldnewsData.fetchall()), sentianalyze(technologyData.fetchall())
FinalSubs = "announcements", "blog", "pics", "funny", "askreddit", "science", "WTF", "politics", "worldnews", "technology"

sentiCollection = dict(zip(FinalSubs, FinalData))
print "Here is the average sentiment of comments from each subreddit that are more\
    subjective than objective. Comments are rated on a scale from 1 being the most positive,\
    to -1 being the most negative."
print sentiCollection.items()

plt.figure(figsize=(12,9))
plt.title("Average Comment Sentiment From 10 Major Subreddits", fontsize=24)    
plt.bar(range(len(sentiCollection)), sentiCollection.values(), align='center', color = 'c')
plt.xticks(range(len(sentiCollection)), sentiCollection.keys(), fontsize = 10)
plt.xlabel("(Subreddit)", fontsize = 14)
plt.text(0,-.02, "Data source: www.Kaggle.com May2015 Reddit Dataset | "  
         "Author: Pedro Perez", fontsize=10)                      
                





