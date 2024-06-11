# StayAwake
Python GUI to keep the computer active and awake by pressing the F15 key evert 2 minutes

Note: The F15 key doesn't exist on the keyboad and wont be inputed to any open apps but the system still registers the event.

![App](images/app.png)

## Setup
Install dependencies
```
pip install pipenv
pipenv run install
```

Run app
```
pipenv run start
```

### Note
On Linux (Currently using Rocky 9) python3-tkinter, python3-devel, and scrot need to be installed for as dependences for pyautogui.

Enable EPEL to install scrot
```
sudo dnf config-manager --set-enabled crb
sudo dnf install epel-release
```
Then install the packages
```
sudo dnf install -y python3-tkinter python3-devel scrot
```