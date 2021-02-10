---
title: "Azcopy"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
- Fast scalable copy utility for Azure
- Can bandwidth limit and restart
- Docs: (https://docs.microsoft.com/en-us/azure/storage/common/storage-ref-azcopy?toc=/azure/storage/blobs/toc.json)
- Note that block level resume (i.e. resuming a file download from where it left off) is not supported (github.com/Azure/azure-storage-azcopy/issues/806). Only directory level (restarting from the begining of a file) is supported - apparently to avoid blob consistency issues


# Login
- Can either do anonomous or logged in
- lots of ways to login:
    - `azcopy login` - (https://docs.microsoft.com/en-us/azure/storage/common/storage-ref-azcopy-login)
- `onmicrosoft.com` login: 
    -  `azcopy login --tenant-id  72f988bf-86f1-41af-91ab-2d7cd011db47`

# Examples
## Copy
```
azcopy.exe copy "https://msftcampusdata.blob.core.windows.net/hhdata8/hh5ab-u8.txt?sv=2019-10-10&se=2021-03-12T08%3A27%3A53Z&sr=c&sp=rl&sig=IuKUOzMUtuGdWFVq0dWfq465DHAOCWWY3OI6n4SReDQ%3D" "H:\msftcampusdata\hhdata8\hh5ab-u8.txt" --overwrite=prompt --check-md5 FailIfDifferent --from-to=BlobLocal --cap-mbps=50 --recursive;
```

## Resume
```
azcopy.exe jobs resume 1a81fd96-c51c-8c4d-430a-26e53e316945 --source-sas="sv=2019-10-10&se=2021-03-12T08%3A27%3A53Z&sr=c&sp=rl&sig=IuKUOzMUtuGdWFVq0dWfq465DHAOCWWY3OI6n4SReDQ%3D" --cap-mbps=50
```