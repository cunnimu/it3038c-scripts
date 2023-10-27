For this project, I chose the option to display a log file in a web browser. This script will create a web server, read the `var/log/secure` log and return the contents to the web page.

![screencap of secure log display](https://github.com/cunnimu/it3038c-scripts/blob/main/project2/secure%20log%20screencap.png?raw=true)

## How to Use
Copy script to your Centos machine. Open a terminal and use the following command:
```
sudo node project2.js 
```
Note: user must be able to view the log files. Ensure you have permissions by using `sudo` command before running the script. If you receive error messages while running or it crashes, check if you used `sudo`.

Go to web browser and navigate to `http://localhost:3000/log` to see log contents.

## About
I chose this project because it was a good reflection of what the course has covered so far. One of the challenges for me was getting each log entry on a new line. I knew it needed to be replaced with a `<br>` character. This was a good way to bring in the lesson on regexp. I read a lot of [documentation](https://www.w3schools.com/jsref/jsref_regexp_newline.asp) and found out `/\n/g` would search for new lines in the entire document (without the `g` for global, it would stop at the first one).
