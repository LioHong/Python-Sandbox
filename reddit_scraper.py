 shou# -*- coding: utf-8 -*-
"""
Filename: reddit_scraper.py
Date created: Fri Aug 28 23:08:48 2020
@author: Julio Hong
Purpose: Test out Reddit's API
***IMPORTANT***
Create a developer account. Store the IDs in separate files. And be careful when committing to Github.
Steps: 
"""

import praw
import pandas as pd
import datetime as dt

# To adjust the dataframe appearance
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 200)


reddit_personal_use_script = 'jnoq1CaHwBm2CA'
longer_script = 'iuO_T96nlFoYEbxfQdNo5HxNlo8'

reddit = praw.Reddit(client_id=reddit_personal_use_script, \
                     client_secret=longer_script, \
                     user_agent='SailboatoMD', \
                     username='SailboatoMD', \
                     password='captainpotato!9321')
sdc = reddit.subreddit('ShitpostCrusaders')
top_subreddit = sdc.top(limit=500)