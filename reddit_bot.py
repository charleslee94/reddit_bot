import praw
import codecs
import re
import os
import random
import steam_wishlist
from datetime import datetime



def find_game_sale():
    user_agent = ("Dark Souls 2 sale finder")
    r = praw.Reddit(user_agent = user_agent)
    subreddit = r.get_subreddit("gamedeals")
    output = codecs.open('game_sales.txt', 'w', 'utf-8')
    games =  steam_wishlist.get_steam_wishlist('charlesleesr')
    for submission in subreddit.get_hot(limit=20):
        for game in games:
            if re.findall('''Dark\s?Souls\s?(2|two)?''', submission.title, re.I) or re.findall(game, submission.title, re.I):
                if re.findall('''Scholar\s?of\s?the\s?first\s?sin''', submission.title, re.I):
                    output.write (" This is the DLC, THIS IS WHAT YOU WANT")
                output.write("Title: %s \n" % submission.title)
                output.write("Url: %s \n" % submission.url)
                output.write("-------------------------------------------------\n")
    if os.stat("game_sales.txt").st_size == 0:
       output.write("No steam wishlist sales found in the hottest 20 submission on r/gamedeals on  %s \n" % datetime.today())
       ds3_threshold = random.randrange(1,10)
       if ds3_threshold >= 5:
           output.write("Forget ds2, you should just get ds3 instead \n")
       else:
           output.write("Keep trying!\n")
       output.write("This script will run again at 10 am tomorrow")


find_game_sale()
