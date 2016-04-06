import praw
import codecs
import re
import os
import random
from datetime import datetime



def find_ds2_sale():
    user_agent = ("Dark Souls 2 sale finder")
    r = praw.Reddit(user_agent = user_agent)
    subreddit = r.get_subreddit("gamedeals")
    output = codecs.open('output.txt', 'w', 'utf-8')
    for submission in subreddit.get_hot(limit=20):
        if re.findall('''Dark\s?Souls\s?(2|two)?''', submission.title, re.I):
            if re.findall('''Scholar\s?of\s?the\s?first\s?sin''', submission.title, re.I):
                output.write (" This is the DLC, THIS IS WHAT YOU WANT")
            output.write("Title: %s \n" % submission.title)
            output.write("Url: %s \n" % submission.url)
            output.write("-------------------------------------------------\n")
    if os.stat("output.txt").st_size == 0:
       output.write("No Dark souls 2 sales found in the hottest 20 submission on r/gamedeals on  %s \n" % datetime.today())
       ds3_threshold = random.randrange(1,10)
       if ds3_threshold >= 5:
           output.write("Forget ds2, you should just get ds3 instead \n")
       else:
           output.write("Keep trying!\n")
    output.write("This script will run again at 10 am tomorrow")


find_ds2_sale()
