import json
import oauth2 as oauth
consumer_key = 'Us6kzx1ZXXqT9p6E2LYRc3QMR'
consumer_secret = 'JKsNC1EVKSYUZ0effTS9hpk6BihjlOhCNTNbIqiPWZtQkJgcpg'
access_token = '2430662952-bThO1AQAQ6OfvUTrKHbMuT51lL07joDm842RUY5'
access_token_secret = 'Iv39IR999CQmbwMenkdvndzF2TRIprNjRTZxBvnyhzDCM'
consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access_tok=oauth.Token(key = access_token, secret = access_token_secret)
client = oauth.Client(consumer, access_tok)
url='https://api.twitter.com/1.1/help/languages.json'
response, data = client.request(url)
tweets=json.loads(data)
print tweets
