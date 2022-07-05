# Fowsniff CTF

* IP = 10.10.168.203

## Questions/Tasks:

* Starting with basic nmap scanning to discover open ports on the server:
`nmap -sC -sV -v $IP`
### Nmap Scan Results:
```bash
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 90:35:66:f4:c6:d2:95:12:1b:e8:cd:de:aa:4e:03:23 (RSA)
|   256 53:9d:23:67:34:cf:0a:d5:5a:9a:11:74:bd:fd:de:71 (ECDSA)
|_  256 a2:8f:db:ae:9e:3d:c9:e6:a9:ca:03:b1:d7:1b:66:83 (ED25519)
80/tcp  open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 1 disallowed entry
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Fowsniff Corp - Delivering Solutions
110/tcp open  pop3    Dovecot pop3d
|_pop3-capabilities: USER SASL(PLAIN) PIPELINING RESP-CODES AUTH-RESP-CODE UIDL TOP CAPA
143/tcp open  imap    Dovecot imapd
|_imap-capabilities: LOGIN-REFERRALS ID listed post-login AUTH=PLAINA0001 have OK IMAP4rev1 capabilities Pre-login more IDLE SASL-IR ENABLE LITERAL+
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

* Gobuster scan Results:
```
/.hta (Status: 403)
/.hta.txt (Status: 403)
/.hta.html (Status: 403)
/.htaccess (Status: 403)
/.htaccess.txt (Status: 403)
/.htaccess.html (Status: 403)
/.htpasswd (Status: 403)
/.htpasswd.txt (Status: 403)
/.htpasswd.html (Status: 403)
/assets (Status: 301)
/images (Status: 301)
/index.html (Status: 200)
/index.html (Status: 200)
/LICENSE.txt (Status: 200)
/README.txt (Status: 200)
/robots.txt (Status: 200)
/robots.txt (Status: 200)
/security.txt (Status: 200)
/server-status (Status: 403)

```

1. Deploy the machine. On the top right of this you will see a Deploy button. Click on this to deploy the machine into the cloud. Wait a minute for it to become live.

**Ans- No Answers Needed**

2. Using nmap, scan this machine. What ports are open?

**Ans-22/ssh,80/http,110/pop3,143/imap**

3. Using the information from the open ports. Look around. What can you find?

**Ans-mailing services:pop3,imap**

4. Using Google, can you find any public information about them?

`https://pastebin.com/NrAqVeeX`
```
mauer@fowsniff:8a28a94a588a95b80163709ab4313aa4
mustikka@fowsniff:ae1644dac5b77c0cf51e0d26ad6d7e56
tegel@fowsniff:1dc352435fecca338acfd4be10984009
baksteen@fowsniff:19f5af754c31f1e2651edde9250d69bb
seina@fowsniff:90dc16d47114aa13671c697fd506cf26
stone@fowsniff:a92b8a29ef1183192e3d35187e0cfabd
mursten@fowsniff:0e9588cb62f4b6f27e33d449e2ba0b3b
parede@fowsniff:4d6e42f56e127803285a0a7649b5ab11
sciana@fowsniff:f7fd98d380735e859f8b2ffbbede5a7e
```

**Ans- In Twitter @fowsniffcorp**

5. Can you decode these md5 hashes? You can even use sites like hashkiller to decode them.

```
8a28a94a588a95b80163709ab4313aa4	md5	mailcall
ae1644dac5b77c0cf51e0d26ad6d7e56	md5	bilbo101
1dc352435fecca338acfd4be10984009	md5	apples01
19f5af754c31f1e2651edde9250d69bb	md5	skyler22
90dc16d47114aa13671c697fd506cf26	md5	scoobydoo2
a92b8a29ef1183192e3d35187e0cfabd	Unknown	Not found.
0e9588cb62f4b6f27e33d449e2ba0b3b	md5	carp4ever
4d6e42f56e127803285a0a7649b5ab11	md5	orlando12
f7fd98d380735e859f8b2ffbbede5a7e	md5	07011972
```

**Ans-Yes Ofcourse**

6. Using the usernames and passwords you captured, can you use metasploit to brute force the pop3 login?

**Ans-Yes**

7. What was seina's password to the email service?

**Ans-scoobydoo2**

8. Can you connect to the pop3 service with her credentials? What email information can you gather?

```
Return-Path: <stone@fowsniff>
X-Original-To: seina@fowsniff
Delivered-To: seina@fowsniff
Received: by fowsniff (Postfix, from userid 1000)
        id 0FA3916A; Tue, 13 Mar 2018 14:51:07 -0400 (EDT)
To: baksteen@fowsniff, mauer@fowsniff, mursten@fowsniff,
    mustikka@fowsniff, parede@fowsniff, sciana@fowsniff, seina@fowsniff,
    tegel@fowsniff
Subject: URGENT! Security EVENT!
Message-Id: <20180313185107.0FA3916A@fowsniff>
Date: Tue, 13 Mar 2018 14:51:07 -0400 (EDT)
From: stone@fowsniff (stone)

Dear All,

A few days ago, a malicious actor was able to gain entry to
our internal email systems. The attacker was able to exploit
incorrectly filtered escape characters within our SQL database
to access our login credentials. Both the SQL and authentication
system used legacy methods that had not been updated in some time.

We have been instructed to perform a complete internal system
overhaul. While the main systems are "in the shop," we have
moved to this isolated, temporary server that has minimal
functionality.

This server is capable of sending and receiving emails, but only
locally. That means you can only send emails to other users, not
to the world wide web. You can, however, access this system via
the SSH protocol.

The temporary password for SSH is "S1ck3nBluff+secureshell"

You MUST change this password as soon as possible, and you will do so under my
guidance. I saw the leak the attacker posted online, and I must say that your
passwords were not very secure.

Come see me in my office at your earliest convenience and we'll set it up.

Thanks,
A.J Stone.
```

**Ans-baksteen:S1ck3nBluff+secureshell is SSH login**

9. Looking through her emails, what was a temporary password set for her?

**Ans-S1ck3nBluff+secureshell**

10. In the email, who send it? Using the password from the previous question and the senders username, connect to the machine using SSH.

**Ans-baksteen**

11. Once connected, what groups does this user belong to? Are there any interesting files that can be run by that group?

**Ans-groups=100(users),1001(baksteen)**
