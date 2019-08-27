import praw
from PyDictionary import PyDictionary
import enchant

reddit = praw.Reddit(client_id='KB-ZzZzcUJUaJA',
                     client_secret='QoBRWnqsyb2V4theVQWZkvkwmHw',
                     username='anohbot',
                     password='Password1',
                     user_agent='my user agent')
#my bot will live in mysandbox
subreddit = reddit.subreddit('anohsandbox')
print(reddit.read_only)
# bot will look for this to reply
keyphrase = 'word! '

# creating dictionary object
dictionary = PyDictionary()
d = enchant.Dict("en_US")

def isWord(word):
    return d.check(word)
#look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
        try: 
            if isWord(word):
                words = dictionary.meaning(word)
                reply = [item[0] for item in words.values()]
                comment.reply(word + ': '+ reply[0])
                print('posted')
            else:
                reply = "This is not a word."
                comment.reply(reply)
                print('posted')
        except:
            print('To frequent')