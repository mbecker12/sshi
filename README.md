# sshi
SSHI should help interfacing

Broadcast the most important keys to xdotool on a raspberry pi (or other linux computers).

The project was created because remote desktops were too slow and causing trouble, since there was a monitor and a mouse available, but no keyboard, a workaround to send keystrokes was necessary.

We plan to extend the project for mouse support and more sufficient keyboard inputs.

## Install

###### Host
tested on python 3.7 and 3.8

```
pip install pexpect
pip install pynput
```

###### Guest
login with ssh

```
sudo apt-get install xdotool libxdo-dev
nano .bashrc
```
add line
```
export DISPLAY=:0
```
activate changes
```
source .bashrc
```

## Usage
```
python ssh_interface.py
```
Options:
```
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Set port specification. Will be parsed as
                        192.168.1.<port>
  -n NAME, --name NAME  Username of the Raspberry Pi
  -w PW, --pw PW        Password of the Raspberry Pi User
```

