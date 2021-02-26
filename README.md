# fit4less-autobooker

[![Fit4Less-Autobooker](https://circleci.com/gh/chakrakan/fit4less-autobooker.svg?style=svg)](https://circleci.com/gh/chakrakan/fit4less-autobooker)

A Selenium automation script set up on a cron job every midnight to book a time-slot for workouts everyday at any Fit4Less gym.  

UPDATE: As of Feb 25, 2021 the script works! If you have trouble setting things up, feel free to reach out to me on discord at kan#0979

> **NOTE**  
> I've temporarily suspended my Fit4Less gym membership due to COVID, and as such, won't be able to maintain/add features for now since I no longer have access to the platform. If the script stops working, please make an issue and also don't be afraid to make forks of this repo and create pull requests if you can fix/work on any of them. Lastly, if this project has helped you, feel free to ⭐️ it!  

## Why?

Fit4Less allows you to book time-slots either daily, one-day ahead, or two-days ahead. Now obviously, the longer you go without booking, the quicker the time-slots fill out. Therefore, in order to guarantee booking time-slots, I wanted to book two days ahead of schedule, and set up this script to run early each day (think midnight, or around that time) so it can book those slots before anyone else in advance.

## How?

#### Cron Setup

1. Fork this repo
2. Set it up as a project on CircleCI
3. Check project settings on CircleCI and configure Environment Variables as following:
   
```shell script
WEBDRIVER_PATH=/usr/local/bin/chromedriver
DAYS=2
F4L_LOGIN=your email
F4L_PASSWORD=your password
F4L_CLUB=your desired club # OPTIONAL
TIME_SLOT=10:00AM
ENVIRONMENT=prod
```

4. Run the build on CircleCI and check the logs under Install & Run for the build steps

**Notes**

> - `F4L_CLUB` is optional and not needed as the script will book time-slots for the default selected club under your account. However, if you want to book time-slots at a different club, please add this field and your desired club name in ALL CAPS, e.g. `"WATERLOO NORTHFIELD"`. For a list of ALL CLUBS check here: [CLUBS](https://github.com/chakrakan/fit4less-autobooker/wiki) 
> - You can change `DAYS` between 2, 1, 0 (check .env.example)  
> - Please keep `WEBDRIVER_PATH` exactly as shown above since that's the path to driver in the docker container
> - there's minimal error handling so it either reserves your slot if it finds the timing, or you'll see an exception thrown, or skipped timings in your CircleCI logs
> - Skipped timings means it didn't find your time slot, Exception means you've already booked max amount of slots!


#### Local

1. Clone the repo
2. Follow instructions provided in the .env.example file and add your respective information to your local `.env` file
3. Create a virtual environment for the project using `python -m venv venv` & activate 
4. Run `pip install -r requirements.txt` to install necessary dependencies
5. Run `autobooker.py` script
6. ???
7. Profit!

> Note: You can't book consecutive slots for the same day! One day/one slot is the rule from Fit4Less.
