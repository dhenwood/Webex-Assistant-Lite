[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
# Webex Assistant Lite
The Webex Assistant Lite is a cut down version of the [Mindmeld Webex Assistant](https://github.com/cisco/webex-assistant-sdk). The intent of this is to simplify performing demonstrations of the Webex Assistant capability on Webex devices. Whilst the Mindmeld solution provides a highly scalable solution with deep-domain voice interfaces, it does require [a fair amount of setup](https://skills-admin.intelligence.webex.com/walkthrough).

## Setup
Generate a Public/Private key pair (MacOS/Linux)
```sh
//$ ssh-keygen -m PEM -t rsa -b 4096
openssl genrsa -des3 -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem
```

From your browser;
* Login to the [Webex Assistant Admin portal](https://skills-admin.intelligence.webex.com/admin)
* Select "Register a new Skill" (in the top right of the Admin page)
* Specify the Name you wish to use as the main voice trigger
* Optionally, you can set numerious synonyms or other words that will trigger the skill
* Set Language to “English”
* Set the URL to the destination where your code will be running, which is reachable from the Webex cloud service (in my case, I used port forwarding on my router, but you may need to use [ngrok](https://ngrok.com/) to get the connection through). **Ensure the end of the URL includes /parse**
* Set Contact Email
* Set Secret to anything (not used in this integration)
* Paste the Public Key that was generated earlier into the corresponding field (ensure you include the _ssh-rsa_ at the start)
* Click OK to save

Back where you are running the python code, update the **config.py** file to specify the location of your private key. Whilst still in the config.py file, you may also wish to update the logic code to reflect what you would like the assistant to respond with.

Once, compelete, setup the Flask instance such as below. Ensure you set the correct IP address (your own) and port. 
```sh
$ export FLASK_APP=server
$ export FLASK_ENV=development
$ flask run -h 192.168.0.100 -p 7171
```

## Result
In the following example, the name of my Skill is **Galileo**. As such, the full command is "_Ok Webex Ask Galileo how far to Mars_"

Webex Assistant Query
![Webex Assistant Query](https://github.com/dhenwood/Webex-Assistant-Lite/blob/main/webexAssistantQuery.png)

Webex Assistant Response
![Webex Assistant Response](https://github.com/dhenwood/Webex-Assistant-Lite/blob/main/webexAssitantResponse.png)
