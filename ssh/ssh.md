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
- `Loglevel` can be cranked to `VERBOSE`
- Messages can be viewed with `tail -f /var/log/auth.log`
- Restart: `sudo systemctl restart sshd`
- Password auth can be runed off in the `sshd_config` file by setting the line `PasswordAuthentication no`
- `sshd_config` described here <https://www.ssh.com/ssh/sshd_config/>
- Inspect successful logins `zgrep -i "Accepted password" /var/log/auth.log*`
- Inspect failed logins `zgrep -i "Failed password" /var/log/auth.log*`
- Count failed logins: `zgrep -i "Failed password" /var/log/auth.log* | wc -l`

# Persistent Terminal Sessions
- Sometimes you need a terminal session to stay around after you log out.<br>
- Also know as  a `terminal multiplexer` link: (https://linuxize.com/post/how-to-use-linux-screen/)

- How to keep processes running after ending ssh session:
  - ssh into your remote box. type `screen` Then start the process you want.
  - Or use `screen -S session_name` to give it a name with which you can refer to it
  - `screen ls` gives you a listing of all the screen sessions
  - Press `Ctrl-A` then `Ctrl-D`. This will detach your screen session but leave your processes running. ...
  - If you want to come back later, log on again and type `screen -r` This will resume your screen session, and you can see the output of your process.

- Background tasks: there is also the option of starting a process with a trailing ampersand `&` which detaches it from your process so it will keep running in the background
   - https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html

# Putty private keys
- Putty has its own private key format. There is a way to convert from the normal ssh keys to Putty format keys.
- If a converted private key does not work, check the format. It is easy to write out the public key by mistake (done this at least twice)

# Putty public keys
- Public keys have to go into the `~/.ssh/authenticated_keys` file
- There are two ways to get the public key into there:
  - Either copy it in from the window that putty_keygen gives you at generation
  - Retrive it from the file saved in text and format it with `sed` as follows
  - Formatting text Putty public keys with `sed`: <https://serverfault.com/questions/797044/openssh-adding-an-ssh-key-from-putty-to-authorized-keys>
- Following is an example of using that `sed` command to add the key to my `.ssh/authorized_keys`, and it worked
```
mike@Abra:~/.ssh$ more key.pub
---- BEGIN SSH2 PUBLIC KEY ----
Comment: "rsa-key-20180312 -mike-on-uxie"
AAAAB3NzaC1yc2EAAAABJQAAAgEA69wCLaTiQp4idsAI3vxHBZSl9/KZaCk2lJqG
5cgGIV+i5Q5Ij0TfR+TB2XJasq9EQgJwtngXNkbkZWj8dbodbbeU4f7O4VmezXBs
aevTYOkbBAvtIojWByT6sd8QMXjC8vZKvlfjGrf+UPQkivW8CBsi+0JppiEE6YxF
         <stuff deleted here>
Hx/Tem97zDAuUERZt/BECHVvBRfov3XblTEuoWeh2XOxgNQqyHIn6mgV5fDHK/p2
3dXGCGkcmFVW1kiJrYg+620lJ8XPu78QPC5hE+1mykCGusWzzHsNyW+vOcl6H9+6
j+y7xoMLwYB3x85Lxmm4loTnIH8kI/577midN13H9w7yrmomFattO3bRMEC4cpM7
sbG5xhUfQ0uqzgH5iAsW2Iz694a1zrA0tPH2aKA51POXMl36KtIGph3+wpocb6eu
5HsV7luWAF6WYD1GSvxqXUV4J7Rk8ZWTK8KVpSsJ8zmviq43jvMxjDhpSJPpQEfw
+VqjVVE=
---- END SSH2 PUBLIC KEY ----

mike@Abra:~/.ssh$ sed key.pub -e 's/---- B.*/ssh-rsa /;/Comment:/d;'|sed ':a;N;$!ba;s/\n//g;s/---.*//' >authorized_keys
```
