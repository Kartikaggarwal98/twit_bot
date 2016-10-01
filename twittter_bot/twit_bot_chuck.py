import tweepy,sys,time,requests,json
from twit_keys import *

def twit_bot():
	auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
	auth.set_access_token(Access_Token, Access_Token_Secret)
	api = tweepy.API(auth)

	url= "https://api.chucknorris.io/jokes/random"
	i=0
	while(i<3):
		resp= requests.get(url=url).text
		data= json.loads(resp)
		output_text=data['value']
		api.update_status(status=output_text)
		i+=1
		print output_text
		time.sleep(100)
	# public_tweets = api.home_timeline()
	# for tweet in public_tweets:
	#     print tweet.text
	# user1=api.get_user("@FuckFeelings")
	# print user1.screen_name
	# print user1.followers_count
twit_bot()
print "done"