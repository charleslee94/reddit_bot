import praw
import codecs
import re
from datetime  import datetime
from threading import Timer


x = datetime.today()
y = x.replace(day = x.day + 1, hour = 10, minute = 0, second = 0, microsecond = 0)
delta_t = y - x
secs = delta_t.seconds + 1

def find_ds2_sale():
    user_agent = ("Dark Souls 2 sale finder")
    r = praw.Reddit(user_agent = user_agent)
    subreddit = r.get_subreddit("gamedeals")
    output = codecs.open('output.txt', 'w', 'utf-8')
    for submission in subreddit.get_hot(limit=20):
        if re.findall('''Dark\s?Souls\s?(2|two)?''', submission.title, re.I):
            output.write("Title: %s \n" % submission.title)
            output.write("Url: %s \n" % submission.url)
            output.write("-------------------------------------------------\n")

t = Timer(secs, find_ds2_sale())
t.start()
