# Lazy Admin

* IP = 10.10.212.24

## Enumeration & Scanning

* Nmap scan to discover open ports:
`nmap -sC -sV -vv $IP`
* **Nmap Scan Results:**
```bash
PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 49:7c:f7:41:10:43:73:da:2c:e6:38:95:86:f8:e0:f0 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCo0a0DBybd2oCUPGjhXN1BQrAhbKKJhN/PW2OCccDm6KB/+sH/2UWHy3kE1XDgWO2W3EEHVd6vf7SdrCt7sWhJSno/q1ICO6ZnHBCjyWcRMxojBvVtS4kOlzungcirIpPDxiDChZoy+ZdlC3hgnzS5ih/RstPbIy0uG7QI/K7wFzW7dqMlYw62CupjNHt/O16DlokjkzSdq9eyYwzef/CDRb5QnpkTX5iQcxyKiPzZVdX/W8pfP3VfLyd/cxBqvbtQcl3iT1n+QwL8+QArh01boMgWs6oIDxvPxvXoJ0Ts0pEQ2BFC9u7CgdvQz1p+VtuxdH6mu9YztRymXmXPKJfB
|   256 2f:d7:c4:4c:e8:1b:5a:90:44:df:c0:63:8c:72:ae:55 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC8TzxsGQ1Xtyg+XwisNmDmdsHKumQYqiUbxqVd+E0E0TdRaeIkSGov/GKoXY00EX2izJSImiJtn0j988XBOTFE=
|   256 61:84:62:27:c6:c3:29:17:dd:27:45:9e:29:cb:90:5e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILe/TbqqjC/bQMfBM29kV2xApQbhUXLFwFJPU14Y9/Nm
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
* Basic Apache index page, enumerating with gobuster using `common` list of routes.

* Used `gobuster` to scan to find any other hidden directories on the website:
* **Gobuster Scan Results:**
```
/.htaccess (Status: 403)
/.hta (Status: 403)
/.htpasswd (Status: 403)
2023/07/21 20:47:26 [!] Get "http://10.10.212.24/connections": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
2023/07/21 20:47:26 [!] Get "http://10.10.212.24/connector": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
2023/07/21 20:47:26 [!] Get "http://10.10.212.24/connectors": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
2023/07/21 20:47:26 [!] Get "http://10.10.212.24/console": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
/content (Status: 301)
/index.html (Status: 200)
/server-status (Status: 403)
=====================================================
2023/07/21 20:50:51 Finished
=====================================================
```
* `content` route contains sweet-rice CMS
* `content` route gobuster scan:
```
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/_themes (Status: 301)
/as (Status: 301)
/attachment (Status: 301)
/images (Status: 301)
/inc (Status: 301)
/index.php (Status: 200)
/js (Status: 301)
=====================================================
2023/07/21 20:57:50 Finished
=====================================================
```
* Admin User: `manager`
* Admin Pass Hash: `42f749ade7f9e195bf475f37a44cafcb` (md5)
* Admin pass: `Password123`

## Exploitation & Gaining Access

```bash
/usr/bin/script -qc /bin/bash /dev/null
```

## Post Exploitation

```perl
#!/usr/bin/perl

system("sh", "/etc/copy.sh");
```
`rice:randompass`


## Privilege Escalation

## Questions

1. User Flag:

**Ans-THM{63e5bce9271952aad1113b6f1ac28a07}**

1. Root Flag:

**Ans-THM{6637f41d0177b6f37cb20d775124699f}**