#!/usr/bin/env python3
import requests


url = "http://10.10.164.73:62337/components/user/controller.php?action=authenticate"


def login(password):
    s = requests.Session()
    r = s.post(url, data={
        "username": "john",
        "password": password,
        "theme": "default",
        "language": "en",
    })
    return r


print(login("password").text)
