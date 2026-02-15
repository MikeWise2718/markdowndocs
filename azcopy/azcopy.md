---
title: "Azcopy"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Fast scalable copy utility for Azure
- Can bandwidth limit and restart
- Docs: (https://docs.mothership.com/en-us/azure/storage/common/storage-ref-azcopy?toc=/azure/storage/blobs/toc.json)
- Note that block level resume (i.e. resuming a file download from where it left off) is not supported (github.com/Azure/azure-storage-azcopy/issues/806). Only directory level (restarting from the begining of a file) is supported - apparently to avoid blob consistency issues


# Login
- Can either do anonomous or logged in
- lots of ways to login:
    - `azcopy login` - (https://docs.mothership.com/en-us/azure/storage/common/storage-ref-azcopy-login)
- `onmothership.com` login: 
    -  `azcopy login --tenant-id  72f9...db47`

# Examples
## Copy
```
azcopy.exe copy "https://mystorageaccount.blob.core.windows.net/container/file.txt?sv=2019-10-10&se=2021-03-12T08%3A27%3A53Z&sr=c&sp=rl&sig=REDACTED" "H:\localpath\file.txt" --overwrite=prompt --check-md5 FailIfDifferent --from-to=BlobLocal --cap-mbps=50 --recursive;
```

## Resume
```
azcopy.exe jobs resume <job-id> --source-sas="sv=2019-10-10&se=2021-03-12T08%3A27%3A53Z&sr=c&sp=rl&sig=REDACTED" --cap-mbps=50
```