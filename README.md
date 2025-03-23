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
- 4\. Registered account in openweathermap

[Create account in openweathermap](https://home.openweathermap.org/users/sign_in)
[Install Python](https://www.python.org/downloads/)

### To install *requests* and *win11toast* libaries:

1. Open cmd on your PC:
    - win + r, write *cmd* in command line, press *Enter*
2. Write in command line:
    ```sh
    py -m pip install requests
    py -m pip install win11toast
    ```

### Secondly, you have to clone python scripts from github 

## Downloading Scripts (Git or ZIP)  
You can download the files in two ways:  

### Method 1: Cloning the Repository (Recommended)  
1. Make sure you have **Git** installed. If not, download it from [git-scm.com](https://git-scm.com/downloads).  
2. Open **Terminal / Command Prompt** (`cmd` or `PowerShell` on Windows, `Terminal` on macOS/Linux).  
3. Run the following command, replacing `USERNAME` and `REPOSITORY` with the correct values:  
   ```sh
   git clone https://github.com/USERNAME/REPOSITORY.git
   ```
4. Navigate to the repository folder:  
   ```sh
   cd REPOSITORY
   ```
5. The scripts are now on your PC.

### Method 2: Downloading a ZIP Archive  
1. Open the repository on GitHub.  
2. Click **Code** → **Download ZIP**.  
3. Extract the downloaded archive to a convenient folder.  
