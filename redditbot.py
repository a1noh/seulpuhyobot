import praw
import re
import time

reddit = praw.Reddit(client_id = 'KUJxbihdUqMfqQ', 
	client_secret = '7Nl8DQrKCG59JX9ZbPRKAqph7Ko',
	user_agent = '<console:reddit_bot:0.0.1 (by /u/seulpuhyo)>',
	username = 'seulpuhyo',
	password = 'Shwjdgus1!')

print(reddit.read_only)

subreddits = ['anohsandbox']
pos = 0 #start at 0
title = "I want karma !"
url = "https://www.google.com/"


def post():
	global subreddits 
	global pos # we can access the bariables

	subreddit = reddit.subreddit(subreddits[pos])
	subreddit.submit(title, url = url)

	pos = pos + 1

	if (pos <= len(subreddits) - 1):
		post()
	else: 
		print "Done"

post()