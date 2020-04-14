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


