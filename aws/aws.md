---
title: "AWS"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro

- There are "root users" and "IAM Users"
   - you sign in as a root user using your email
   - Then you can 
- The signin for root can be the email or the user name
- You need to install the aws cli to get things to work


# Permissions model
- You need to configure a user with the approprate rigths in IAM
- You need to set up an `aws_access_key` and a corresponding `aws_secret_access_key` to enable that user to be used locally


# Local account information
- is stored in `~/.aws` in Linux or `%homedrive%%homepath%\.aws` in Windows
- access_key and secret is then found in `credentials`
- region is then found in `config`
- proper way to configure region: `aws configure set region us-west-2`

