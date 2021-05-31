#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from datetime import datetime
import tweepy, time, json, requests, os, pdb
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

  r = requests.get('https://api.forecast.io/forecast/' + api_key + '/' + latitude + ',' + longitude)
  return r.json()

def moon_phase_literal(moonPhase):
  if moonPhase == 0:                        return 'New Moon '
  if moonPhase > 0 and moonPhase < 0.25:    return 'Waxing Crescent Moon '
  if moonPhase == 0.25:                     return 'First Quarter Moon '
  if moonPhase > 0.25 and moonPhase < 0.5:  return 'Waxing Gibbous Moon '
  if moonPhase == 0.5:                      return 'Full Moon '
  if moonPhase > 0.5 and moonPhase < 0.75:  return 'Waning Gibbous Moon '
  if moonPhase == 0.75:                     return 'Last Quarter Moon '
  if moonPhase > 0.75 and moonPhase < 1:    return 'Waning Crescent Moon '
  
  raise Exception("Weird value for moon phase: {}, expecting a value >= 0 and < 1".format(moonPhase))

def cloud_cover_literal(cloudCover):
  if cloudCover == 0:                         return 'clear skies'
  if cloudCover > 0 and cloudCover < 0.4:     return 'partly scattered clouds'
  if cloudCover == 0.4:                       return 'scattered clouds tonight!'
  if cloudCover > 0.4 and cloudCover < 0.75:  return 'partly broken cloud cover'
  if cloudCover == 0.75:                      return 'broken cloud cover'
  if cloudCover > 0.75 and cloudCover < 1:    return 'mostly overcast skies'
  if cloudCover == 1:                         return 'completely overcast skies'
  
  raise Exception("Weird value for cloud cover: {}, expecting a value >= 0 and <= 1".format(cloudCover))

def build_tweet(moonPhase, cloudCover):
  tweet = ''
  tweet += moon_phase_literal(moonPhase)
  tweet += 'with '
  tweet += cloud_cover_literal(cloudCover)
  tweet += ' tonight!'
  tags  = " #florida #moon #space #stars #astronomy #science #orlando #centralflorida"
  tweet += tags

  return tweet

def run_bot():
  weather_data = get_weather_data()
  moonPhase    = weather_data['daily']['data'][0]['moonPhase']
  cloudCover   = weather_data['currently']['cloudCover']
  tweet        = build_tweet(moonPhase, cloudCover)

  get_twitter_client().update_status(tweet)

run_bot()
