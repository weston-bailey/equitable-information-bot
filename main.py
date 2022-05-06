import praw
from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ)

def main():
    reddit = praw.Reddit(
        user_agent=os.environ["USER_AGENT"],
        client_id=os.environ["CLIENT_ID"],
        client_secret=os.environ["CLIENT_SECRET"],
        username=os.environ["USERNAME"],
        password=os.environ["PASSWORD"],
    )

    subreddit = reddit.subreddit("ma_robo_boi")
    print(subreddit.title) 
    for submission in subreddit.stream.submissions():
        # print([method for method in dir(submission) if method[0] != '_'])  
        if submission.title.find('robo') != -1:
            print('found post with keyword in title')
            print(submission.title)
            print(submission.selftext)
            submission.reply("hello I am robo")

if __name__ == "__main__":
    main()
