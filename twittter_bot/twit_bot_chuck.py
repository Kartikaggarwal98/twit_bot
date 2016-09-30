import tweepy,sys,time

Consumer_Key ='YQKk8BVbrK0hTne6RqqPbhrjy'
Consumer_Secret='QLDRTUoC0GT7y3z3hbkUd46uyHlh4XQOMnR3sQ6fEbJ3WE69lJ'
Access_Token='401187814-nYmgn2UOmywfhJDIuWBG6EbdyTsOzEXAkJzYLaXZ'
Access_Token_Secret	= 'o6N8dtxUnUKnwAMgIWEJYj8ouozaPUKT5Mg485ZT94B9q'

def twit_bot():
	auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
	auth.set_access_token(Access_Token, Access_Token_Secret)
	api = tweepy.API(auth)
	output_text="hello bot"
	api.update_status(status=output_text)

twit_bot()
print "done"