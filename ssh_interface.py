"""
Created by Jan Schiffeler at 13.04.20
jan.schiffeler[at]gmail.com

Changed by
marvinbecker[at]mail.de

broadcast the most important keys to xdotool on a raspberry pi

Python 3.8.2 and 3.7.6
Library version:
pip install pexpect
pip install pynput

"""
import argparse
from pexpect import pxssh
from pynput.keyboard import Key, Listener
from constants import key_dict, ERR_CODE
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def on_press(key):
    logger.debug(f'{key} pressed')
    if type(key) == Key:
        if key.name == 'alt_r' or key.name == 'f4':
            s.logout()
            logger.info("Stopping session")
            quit()
        else:
            send = key_dict.get(key.name, ERR_CODE)

    else:
        send = key

    if send != ERR_CODE:
        s.sendline(f'xdotool key {send}')
    else:
        logger.warning(f'{key} pressed but not supported')

def create_argparser():
    parser = argparse.ArgumentParser(description='Connect to a Raspberry Pi and type stuff.\nPress F4 key to quit.')

    parser.add_argument('-p', '--port', required=False, default='4', help='Set port specification. Will be parsed as 192.168.1.<port>')
    parser.add_argument('-n', '--name', required=False, default='pi', help='Username of the Raspberry Pi')
    parser.add_argument('-w', '--pw', required=False, default='Passwort', help='Password of the Raspberry Pi User')

    args = vars(parser.parse_args())
    return args

if __name__ == "__main__":
    s = pxssh.pxssh()

    args = create_argparser()
    port = args['port']
    name = args['name']
    pw = args['pw']
    logger.debug(args)

    logger.info("Setting up SSH connection ...")
    if not s.login(f'192.168.1.{port}', f'{name}', f'{pw}', sync_multiplier=5, auto_prompt_reset=False):
        logger.error("SSH session failed on login.")
        logger.warning(str(s))
    else:
        logger.info("SSH session login successful")

        logger.info("Lets do this!!")

        # Collect events until released
        with Listener(
                on_press=on_press) as listener:
            listener.join()
