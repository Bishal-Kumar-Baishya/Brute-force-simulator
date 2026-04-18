# Brute Force Simulator
A brute force simulator is made with python

## How to run
- Start the server first:- python target_app.py
- In another terminal, run:- python brute_force.py --url http://127.0.0.1:5000/login --username light --wordlist wordlist.txt

## CLI Arguments
- `--url` - targets login url
- `--username` - username to use for all attempts
- `--wordlist` - path to the wordlist .txt file


## About the tool
This tool performs repeated login attempts in a flask server trying every possible passwords from a wordlist file for a username.


## Built with
- Python 3
- flask module
- argparse module
- requests module

## Purpose
This tool demonstrates understanding of authentication attacks from defensive perspective - can show how to detect and mitigate them. It teaches about HTTP requests, wordlist iteration etc.