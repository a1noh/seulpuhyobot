import praw
import re
import time

reddit = praw.Reddit(client_id = '5bEFMMpIGQ0AXw', 
	client_secret = 'nTXbDgQp2nSZHjC7NyijLqe3Xbo',
	user_agent = '<console:reddit_bot:0.0.1 (by /u/seulpuhyo)>',
	username = 'anohbot',
	password = 'Shwjdgus1!')

print(reddit.read_only)

subreddits = ['anohsandbox'] # it's suppposed to have multipple subreddits
pos = 0 #start at 0
errors = 0

title = "I want karma !"
url = "https://me.me/i/im-hungry-give-karma-help-a-poor-girl-in-need-41a48eb32ed44a7a9acc4cdfaef4bafc"


def post():
	global subreddits 
	global pos # we can access the bariables
	global errors;
	try:
		subreddit = reddit.subreddit(subreddits[pos]) #will try to iterate through the subreddit list
		subreddit.submit(title, url = url)
		print('Posted to ' + subreddits[pos])

		pos = pos + 1

		if (pos <= len(subreddits) - 1): #recurisve call to post agian, if there are more subreddits
			post()
		else: 
			print "Done"

	except praw.exceptions.APIException as e: # will throw an exception when u spam
		if (e.error_type == "RATELIMIT"):
			delay = re.search("(\d+) minutes?", e.message)

			if delay:
				delay_seconds = float(int(delay.group(1))*60)
				print('delaying...')
				time.sleep(delay_seconds)
				post()
			else:
				delay = re.search("(\d+) seconds", e.message)
				delay_seconds = float(delay.group(1))
				print('delaying...')
				time.sleep(delay_seconds)
				post()
	except:
		errors = error + 1
		if (errors > 5):
			print("Crashed !")
			exit(1)

post()