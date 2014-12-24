TheFloridaMoon
==============

Twitter bot that posts what the status of the sky is going to be for Moon viewing from Central Florida for the night

APIs Used
=========
<ul>
	<li><a href="https://github.com/tweepy/tweepy">Tweepy</a> to interact with Twitter.</li>
	<li><a href="https://forecast.io/">Forecast.io</a> to get weather data.</li>
</ul>


Installation
============

There are two key steps for installing your own version of TheFloridaMoon:
1. Create your own data.json file with your API keys in it (See below for example)
2. Set up the proper cron job (See below for example)


## data.json Example ##
```
{
	"keys" : [
		{
		    "CONSUMER_KEY" : "YourKey",
		    "CONSUMER_SECRET" : "YourKey",
		    "ACCESS_KEY" : "YourKey",
		    "ACCESS_SECRET" : "YourKey",
		    "FORECASTIO_API" : "YourKey"
	    }
    ],
    "location" : [
    	{
    		"lat" : "YourLat",
    		"long" : "YourLong"
    	}
    ]
}
```
## Cron Job Example ##
###### This job runs at 5:30 PM every day
```
30 17 * * * cd /root/Projects/TheFloridaSky/ && python /root/Projects/TheFloridaSky/run.py > /root/Projects/TheFloridaSky/logs/logs.txt 2>&1
```