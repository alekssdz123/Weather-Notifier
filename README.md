# Weather script

## What is it?

This weather script shows weather in your city when
you turn on your PC using Windows notifications

## What it shows to me?

Well, it shows:
- 1\. Temperature in °С
- 2\. Feels like temperature in °С
- 3\. Humidity in %
- 4\. Wind speed in km/h
- 5\. Description (thunderstorm, drizzle, etc.)

## How to install it?

### Firstly, you will need to have:

- 1\. Installed Python 3.12
- 2\. Installed *requests* libary
- 3\. Installed *win11toast* libary

[Install Python](https://www.python.org/downloads/)

### To install *requests* and *win11toast* libaries:

1. Open cmd on your PC:
    - 1.1\. win + r, write *cmd* in command line, press *Enter*
2. Write in command line:
    ```sh
    py -m pip install requests
    py -m pip install win11toast
    ```