TheFloridaMoon
==============

Twitter bot that posts what the status of the sky is going to be for Moon viewing from Central Florida for the night

Can be found live [here](https://twitter.com/TheFloridaMoon "TheFloridaMoon's twitter")!

APIs Used
=========
<ul>
	<li><a href="https://github.com/tweepy/tweepy">Tweepy</a> to interact with Twitter.</li>
	<li><a href="https://forecast.io/">Forecast.io</a> to get weather data.</li>
</ul>


Installation
============

Set up a `.env` file with your keys in it:

## .env Example ##
```sh
CONSUMER_KEY=yourtwitterconsumerkey
CONSUMER_SECRET=yourtwitterconsumersecret
ACCESS_KEY=yourtwitteraccesskey
ACCESS_SECRET=yourtwitteraccesssecret
FORECASTIO_API=yourforecastioapikey
LATITUDE=yourlatitude
LONGITUDE=yourlongitude
```