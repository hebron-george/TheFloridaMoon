#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from datetime import datetime
import tweepy, time, json, requests

json_data=open('data.json')
data = json.load(json_data)
json_data.close()
 
# Twitter info
CONSUMER_KEY    = data['keys'][0]['CONSUMER_KEY']
CONSUMER_SECRET = data['keys'][0]['CONSUMER_SECRET']
ACCESS_KEY      = data['keys'][0]['ACCESS_KEY']
ACCESS_SECRET   = data['keys'][0]['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
api_key   = data['keys'][0]['FORECASTIO_API']
latitude  = data['location'][0]['lat']
longitude = data['location'][0]['long']

# Forecast.io API call
r = requests.get('https://api.forecast.io/forecast/' + api_key + '/' + latitude + ',' + longitude)
weather_data = r.json()

# Get tonight's moon phase and cloud cover
moonPhase  = weather_data['daily']['data'][0]['moonPhase']
cloudCover = weather_data['currently']['cloudCover']

tweet = '' # the string that eventually gets tweeted

if moonPhase == 0:
	tweet = tweet + 'New Moon '
elif moonPhase > 0 and moonPhase < 0.25:
	tweet = tweet + 'Waxing Crescent Moon '
elif moonPhase == 0.25:
	tweet = tweet + 'First Quarter Moon '
elif moonPhase > 0.25 and moonPhase < 0.5:
	tweet = tweet + 'Waxing Gibbous Moon '
elif moonPhase == 0.5:
	tweet = tweet + 'Full Moon '
elif moonPhase > 0.5 and moonPhase < 0.75:
	tweet = tweet + 'Waning Gibbous Moon '
elif moonPhase == 0.75:
	tweet = tweet + 'Last Quarter Moon '
elif moonPhase > 0.75 and moonPhase < 1:
	tweet = tweet + 'Waning Crescent Moon '
else:
	print 'Weird value for moonPhase: ' + str(moonPhase) + ' at: ' + str(datetime.now().date()) + str(datetime.now().time())

if cloudCover == 0:
	tweet = tweet + 'with clear skies tonight!'
elif cloudCover > 0 and cloudCover < 0.4:
	tweet = tweet + 'with partly scattered clouds tonight!'
elif cloudCover == 0.4:
	tweet = tweet + 'with scattered clouds tonight!'
elif cloudCover > 0.4 and cloudCover < 0.75:
	tweet = tweet + 'with partly broken cloud cover tonight!'
elif cloudCover == 0.75:
	tweet = tweet + 'with broken cloud cover tonight!'
elif cloudCover > 0.75 and cloudCover < 1:
	tweet = tweet + 'with mostly overcast skies tonight!'
elif cloudCover == 1:
	tweet = tweet + 'with completely overcast skies tonight!'
else:
	print 'Weird value for cloudCover: ' + str(cloudCover) + ' at: ' + str(datetime.now().date()) + str(datetime.now().time())

tags  = " #florida #moon #space #stars #astronomy #science #orlando #centralflorida"
tweet = tweet + tags

# Post Tweet
try:
	api.update_status(tweet)
except tweepy.error.TweepError:
	print '[' + str(datetime.now()) + ']'
	print '======= Tweet Too Long ======='
	print '=== tweepy.error.TweepError ==='
except e:
	print '[' + str(datetime.now()) + ']'
	print  e