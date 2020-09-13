# fit4less-autobooker

A Selenium automation script set up on a cron job every midnight to book a time-slot for workouts everyday at the Fit4Less gym.  

## Why?

Fit4Less allows you to book time-slots either daily, one-day ahead, or two-days ahead. Now obviously, the longer you go without booking, the quicker the time-slots fill out. Therefore, in order to guarantee booking time-slots, I wanted to book two days ahead of schedule, and set up this script to run early each day (think midnight, or around that time) so it can book those slots before anyone else in advance.

## How?

You can fork this repo if you want to set-up your own cron job that books time-slots for you everyday, and set up the following environment variables for the project on CircleCI

> ToDo: add instructions

#### Local

1. Clone the repo
2. Follow instructions provided in the .env.example file and add your respective information
3. Run `pip install -r requirements.txt` to install necessary dependencies
3. Run `autobooker.py` script
4. ???
5. Profit!

> NOTE: You can't book consecutive slots for the same day! One day/one slot is the rule from Fit4Less.
