[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
# Webex Assistant Lite
The Webex Assistant Lite is a cut down version of the [Mindmeld Webex Assistant](https://github.com/cisco/webex-assistant-sdk). The intent of this is to simplify performing demonstrations of the Webex Assistant capability on Webex devices. Whilst the Mindmeld solution provides a highly scalable solution, it does require [significant setup](https://skills-admin.intelligence.webex.com/walkthrough).

## Setup
A public/private key needs to be created. 

Generate Public/Private keys (MacOS/Linux)
```sh
$ ssh-keygen -m PEM -t rsa -b 4096
```

Login to the [Webex Assistant Admin portal](https://skills-admin.intelligence.webex.com/admin) and "Register a new Skill". The "Public Key" field is populated with the contents of the public key just created (ensure you include the _ssh-rsa_ at the start). Also ensure your target URL address finshes with /parse (ie, https://mywebserver.com/parse).

Back where you are running the python code, update the config.py file to specify the location of your private key. Whilst still in the config.py file, you may also wish to update the logic code to reflect what you would like the assistant to respond with.

Once, compelete, setup the Flask instance such as below. Ensure you set the correct IP address (your own) and port. The destination needs to be reachable from the Webex cloud service (in my case, I used port forwarding on my router, but you may need to use ngrok to get the connection through).
```sh
$ export FLASK_APP=server
$ export FLASK_ENV=development
$ flask run -h 192.168.0.100 -p 7171
```

## Result
Webex Assistant Query
![Webex Assistant Query](https://github.com/dhenwood/Webex-Assistant-Lite/blob/main/webexAssistantQuery.png)

Webex Assistant Response
![Webex Assistant Response](https://github.com/dhenwood/Webex-Assistant-Lite/blob/main/webexAssitantResponse.png)
