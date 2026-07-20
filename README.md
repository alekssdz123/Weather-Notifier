# Weather Notifier

A simple Python application that displays the current weather as a desktop notification when your computer starts.

## Preview

![Notification Preview](images/windows_example.gif)

## Features

* Current temperature (°C)
* Feels-like temperature (°C)
* Humidity (%)
* Wind speed (m/s)
* Weather description
* English and Russian language support
* Automatic startup on:
  * Windows
  * Linux (desktop environments with autostart support)
* Automatic configuration creation
* Application uninstall option
* Built-in application updater
* OpenWeatherMap API error handling
* OS-specific setup architecture

---

## Requirements

Before installing, make sure you have:

* Python 3.12 or newer
* OpenWeatherMap account
* OpenWeatherMap API key

Supported operating systems:

* Windows 10/11
* Linux distributions with a graphical desktop environment

macOS support is planned for future releases.

Create an OpenWeatherMap account:

https://home.openweathermap.org/users/sign_in

Download Python:

https://www.python.org/downloads

---

# Installation

## Clone the repository

```bash
git clone https://github.com/alekssdz123/Weather-Notifier.git
cd Weather-Notifier
```

Or download the repository as a ZIP archive:

1. Open the GitHub repository.
2. Click **Code** → **Download ZIP**.
3. Extract the archive to any folder.

---

# Windows Installation

Run:

```bash
python setup.py
```

Select:

```text
1
```

or:

```text
install
```

The installer will:

* Install required Python packages
* Create a Windows startup script
* Create a configuration file

After installation, the application will automatically start when Windows starts.

---

# Linux Installation

Linux currently requires manual dependency installation because package management differs between distributions.

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run setup:

```bash
python3 setup.py
```

Select:

```text
1
```

The installer will:

* Create a Linux autostart `.desktop` file
* Create a configuration file

The application will start automatically after logging into your desktop session.

---

# Configuration

Run setup:

```bash
python setup.py
```

Select:

```text
2
```

or:

```text
setconfig
```

You will be asked to enter:

* City
* Country code (LV, US, GB, etc.)
* Language (EN/RU)
* OpenWeatherMap API key

Example:

```text
City: Riga
Country code: LV
Language: EN
API key: your_api_key_here
```

---

# Updating

Weather Notifier includes a built-in updater.

Run:

```bash
python setup.py
```

Select:

```text
3
```

or:

```text
update
```

The updater will:

* Check the latest GitHub release
* Download the newest version
* Replace application files
* Keep user configuration
* Keep the existing virtual environment

---

# Uninstallation

Run:

```bash
python setup.py
```

Select:

```text
4
```

or:

```text
uninstall
```

The installer will remove:

* Startup configuration
* Application configuration file

---

# Known Issues

* Linux dependency installation is currently manual.
* Linux functionality has been tested only on Ubuntu 24.04.
* macOS is not supported yet.
* Windows console window is still visible during startup (planned improvement).

---

# Technologies

* Python
* Requests
* OpenWeatherMap API
* Desktop Notifier
* GitHub Releases API

---

# License

This project is licensed under the MIT License.