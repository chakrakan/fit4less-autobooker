# fit4less-autobooker

[![Fit4Less-Autobooker](https://circleci.com/gh/chakrakan/fit4less-autobooker.svg?style=svg)](https://circleci.com/gh/chakrakan/fit4less-autobooker)

A Selenium automation script set up on a cron job every midnight to book a time-slot for workouts everyday at the Fit4Less gym.  

## Why?

Fit4Less allows you to book time-slots either daily, one-day ahead, or two-days ahead. Now obviously, the longer you go without booking, the quicker the time-slots fill out. Therefore, in order to guarantee booking time-slots, I wanted to book two days ahead of schedule, and set up this script to run early each day (think midnight, or around that time) so it can book those slots before anyone else in advance.

## How?

1. Fork this repo
2. Set it up as a project on CircleCI
3. Check project settings on CircleCI and configure Environment Variables as following:
```shell script
WEBDRIVER_PATH=/usr/local/bin/chromedriver
DAYS=2
F4L_LOGIN=your email
F4L_PASSWORD=your password
TIME_SLOT=10:00 AM
ENVIRONMENT=prod
```
**Notes** 
> - You can change `DAYS` between 2, 1, 0 (check .env.example)  
> - Please keep `WEBDRIVER_PATH` exactly as shown above since that's the path to driver in the docker container  
> - `TIME_SLOT` doesn't need quotes for the space between the time and AM/PM as opposed to running it locally  
4. Run the build on CircleCI and check the logs under Instal & Run for the build steps


#### Local

1. Clone the repo
2. Follow instructions provided in the .env.example file and add your respective information
3. Run `pip install -r requirements.txt` to install necessary dependencies
3. Run `autobooker.py` script
4. ???
5. Profit!

> Note: You can't book consecutive slots for the same day! One day/one slot is the rule from Fit4Less.
