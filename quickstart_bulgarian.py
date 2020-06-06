# -*- coding: UTF-8 -*-

""" Quickstart script for InstaPy usage """

# imports
import time

from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


def like_tags_and_sleep(tags: [str], amount: int):
    session.like_by_tags(tags, amount=amount)
    print(f"\n\n\n Sleeping for an hour after liking ${amount} posts of tag '${tags}' \n\n\n")
    time.sleep(3900000)
    print(f"\n\n\n Slept for an hour after liking ${amount} posts of tag '${tags}' \n\n\n")


CHROMEDRIVER_PATH = "/Users/stanislav/Documents/personal/code/tochka_bestanden/tools/chromedriver"


print("Please input your Instagram password")
password = input()

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)


session = InstaPy(username="netherblood", password=password, driver_path=, headless_browser=True)

with smart_run(session):
    like_tags_and_sleep(["bulgariangirl"], 268)
    session.like_by_tags(["burgasgirl"], amount=100)
    session.like_by_tags(["vscobg"], amount=200)
