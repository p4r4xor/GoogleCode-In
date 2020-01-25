# DVWA Installation in Fedora 31

This is for a task for Fedora Project in the GCI. I've ran as a liveuser as I didn't have much space left on my system.

### Setup and Installation:

These steps are explained with screenshots for an easy understanding.

* We'll be firing up the Terminal of the Fedora 31.
* Running the following command `sudo yum -y install httpd` gives us the following.

![2](https://user-images.githubusercontent.com/59013403/71284368-9301ea00-2330-11ea-90f4-d3c7bb63d381.png)
* To check if the installed dependency works, use `apachectl start` and navigate to `127.0.0.1` in your browser.

![1](https://user-images.githubusercontent.com/59013403/71284341-854c6480-2330-11ea-9079-c7ae7cd890e2.png)
* Next, we install `mysql-server`. This is done by `sudo yum install mysql-server`.

![3](https://user-images.githubusercontent.com/59013403/71284734-6b5f5180-2331-11ea-9973-a14a6e77deb4.png)
* We have installed the following, next we clone the DVWA repo from GitHub. This is done by `git clone https://github.com/ethicalhack3r/DVWA.git`

![4](https://user-images.githubusercontent.com/59013403/71285163-81b9dd00-2332-11ea-9aa9-8f470400eb03.png)
* Next is changing the file config. The below screenshot helps.

![5](https://user-images.githubusercontent.com/59013403/71285278-c6de0f00-2332-11ea-93a1-4a0c822890e4.png)
* Now use `vi config.inc.php` to open and edit the file, change the username and password to user and pass respectively. (press i to enter insert/edit mode, hit `esc` first and `:wq` next to save the file and quit)

![6](https://user-images.githubusercontent.com/59013403/71285390-0efd3180-2333-11ea-9561-b98a0d52eed1.png)
* Now open mariadb and hit the exact stuff given in the screenshot.

![7](https://user-images.githubusercontent.com/59013403/71285639-acf0fc00-2333-11ea-9a62-930511a2050c.png)
* If you have php already installed, skip this step. Otherwise install the dependencies with `sudo yum install php php-pear`

![8](https://user-images.githubusercontent.com/59013403/71285742-f0e40100-2333-11ea-89e0-47c7c5b3e9b4.png)
* And you're done.

### Usage
* Type `127.0.0.1/DVWA` after typing `apachectl start` on your terminal.

![DVWA1](https://user-images.githubusercontent.com/59013403/71285886-3ef90480-2334-11ea-9690-4743c992b426.png)
* The credentials are `admin` and `password` respectively.
* You'll be shown the given after entering them.

![DVWA2](https://user-images.githubusercontent.com/59013403/71285958-6bad1c00-2334-11ea-97e7-e74753ad5e94.png)
* Hit the clear/reset database button and you'll be sent back to the login screen. Enter the credentials again and you're good to go.

![DVWA3](https://user-images.githubusercontent.com/59013403/71286056-a8791300-2334-11ea-92ea-852b72ccc4c1.png)
* Click the `DVWA Security` button and update the security level to `Low` and click submit.

![DVWA4](https://user-images.githubusercontent.com/59013403/71286149-e8d89100-2334-11ea-9a9c-8ef0d21e0f56.png)
* And it's done! :)


