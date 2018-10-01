---
title: "ssh"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
Secure Shell. It has a frigging web site: <https://www.ssh.com/>
- History <https://docstore.mik.ua/orelly/networking_2ndEd/ssh/ch01_05.htm#ch01-87482.html>
- SSH1 vs. SSH2 (1995 vs. 1998) <https://docstore.mik.ua/orelly/networking_2ndEd/ssh/ch01_05.htm#ch01-87482.html>

# Configuration
Config page: <https://www.ssh.com/ssh/config/>

## ssh
- The ssh program on a host receives its configuration from either the command line or from configuration files `~/.ssh/config` and `/etc/ssh/ssh_conf` in that order of precendence. Note this is for configuring `ssh`, not the login daemon `sshd`
- Public keys get added to `authorized_keys` file in your `~/.ssh/` directory
- Multiple keys can be used here, just append them one after the other. This should allow you to logon as the same user with different keys.
- `ssh mike@192.168.25.12` for example, note that user is specified in host address

## sshd
- The server deamon is configured with `/etc/ssh/sshd_config`
- Password auth can be runed off in the `sshd_config` file by setting the line `PasswordAuthentication no`
- `sshd_config` described here <https://www.ssh.com/ssh/sshd_config/>

# Putty
- Putty has its own private key format. There is a way to convert from the normal ssh keys to Putty format keys.
- If a converted private key does not work, check the format. It is easy to write out the public key by mistake (done this at least twice)

