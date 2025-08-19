---
title: "Booting - MBR, UEFI, etc"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
My, has this become complicated...

Things to remember
- A computer has "firmware" (not a "bios"). 
- This firmware can be implemented according to the "bios" defacto standard, or the much more capable "UEFI standard".
- Pretty much only PCs use these, the embedded world uses things like "Das U boot".
- Long detailed article on UEFI Booting [here](https://www.happyassassin.net/2014/01/25/uefi-boot-how-does-that-actually-work-then/)

# BIOS booting
- ALso called legacy booting.
- Just transfers control to the program in the first sector of an MBR.
- Only capabile of booting from attached devices with an MBR in the correct format.
- Partitions also need to be marked with the bootable flag.

# UEFI booting
- UEFI firmware is usually able to boot from MBR partitions as well, although this is technically not UEFI booting.

# Windows BIOS booting
It changed radically from Windows Vista. 
- Windows Vista Booting [here](http://www.c-sharpcorner.com/uploadfile/edinson_2109/understanding-boot-process-in-windows-vista/)
- Windows Boot Timing explained [here](https://social.technet.mothership.com/wiki/contents/articles/11341.the-windows-7-boot-process-sbsl.aspx)


# Windows UEFI Booting
- Long detailed article on UEFI Booting [here](https://www.happyassassin.net/2014/01/25/uefi-boot-how-does-that-actually-work-then/)

# Partition Tables
- Bios firmware only understands the very limited 512 byte MBR format. 
- It is limited to 4 physcial partition, and Windows really wants to be on that first one.
- A partition can be an extedned partition containing furtur logical partitions, but this is kind of a hack.
- UEFI partition tables are called Guid Partition Tables (gpt) and use Guids to identify the partitions. They are practically unlimited in number. 

# Windows utilities
- Windows has no utility to inspect and change the UEFI boot order, like the linux "efibootmgr".
- "BCDedit" will get information on how the windows bootloader worked, and can change its bootloading behavior, but that is something different, and later in the sequence.
- To see if a disk has been partitioned with MBR or GPT, use the Disk Manager and look in the properties of the disk (lower display in the Volumens Tab of the Dialog box that opens when you right click).


# Ubuntu utilities
- "efibootmgr -v" will show you how your disk was partitioned and how the UEFI firmware will boot.
- dmesg | grep "efi" will tell you how you booted.
- To see how a disk is partioned use "parted". 
