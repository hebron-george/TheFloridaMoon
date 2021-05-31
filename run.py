#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from datetime import datetime
import tweepy, time, json, requests, os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_twitter_client():
	CONSUMER_KEY    = os.environ.get('CONSUMER_KEY')
	CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
	ACCESS_KEY      = os.environ.get('ACCESS_KEY')
	ACCESS_SECRET   = os.environ.get('ACCESS_SECRET')

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

	return tweepy.API(auth)

def get_weather_data(): 
	api_key   = os.environ.get('FORECASTIO_API')
	latitude  = os.environ.get('LATITUDE')
	longitude = os.environ.get('LONGITUDE')

	# Forecast.io API call
	r = requests.get('https://api.forecast.io/forecast/' + api_key + '/' + latitude + ',' + longitude)
	return r.json()

def build_tweet(moonPhase, cloudCover):
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

	return tweet

def post_to_twitter(tweet):
	try:
		get_twitter_client().update_status(tweet)
	except tweepy.error.TweepError:
		print '[' + str(datetime.now()) + ']'
		print '======= Tweet Too Long ======='
		print '=== tweepy.error.TweepError ==='
	except e:
		print '[' + str(datetime.now()) + ']'
		print  e

def run_bot():
	# Get tonight's moon phase and cloud cover
	weather_data = get_weather_data()
	moonPhase    = weather_data['daily']['data'][0]['moonPhase']
	cloudCover   = weather_data['currently']['cloudCover']
	tweet = build_tweet(moonPhase, cloudCover)
	post_to_twitter(tweet)

run_bot()
