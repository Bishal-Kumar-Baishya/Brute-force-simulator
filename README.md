# Brute Force Simulator
A brute force simulator is made with python

## How to run
- Start the server first:- python target_app.py
- In another terminal, run:- python brute_force.py --url http://127.0.0.1:5000/login --username light --wordlist wordlist.txt --delay 0.5

## CLI Arguments
- `--url` - targets login url
- `--username` - username to use for all attempts
- `--wordlist` - path to the wordlist .txt file
- `--delay` - float value for each delay between brute force attempts


## About the tool
This tool performs repeated login attempts in a flask server trying every possible passwords from a wordlist file for a username. Added `--delay` to avoid rate limiter, and for each failed attempts it logs in a file with info like IP, username, password.


## Built with
- Python 3
- flask module
- argparse module
- requests module
- logging module
- time module

## Purpose
This tool demonstrates understanding of authentication attacks from defensive perspective - can show how to detect and mitigate them. It teaches about HTTP requests, wordlist iteration, rate limiting and how defenders can spot this pattern.