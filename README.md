# Webex Assistant Lite
The Webex Assistant Lite is a cut down version of the [Mindmeld Webex Assistant](https://github.com/cisco/webex-assistant-sdk). The intent of this is to simplify performing demonstrations of the Webex Assistant capability on Webex devices. Whilst the Mindmeld solution provides a highly scalable solution, it does require significant setup (docker containers, etc).

## Setup
A public/private key needs to be created. The public key is used when setting up the skill on the [Webex Assistant Admin portal](https://skills-admin.intelligence.webex.com/admin). Whilst the private key is referenced in the config.py file and used to decrypt the incoming message.

Generate Public/Private keys (MacOS/Linux)
```sh
$ ssh-keygen -t rsa
```

Update the config.py file to specify the location of your private key. Whilst still in the config.py file, you may also wish to update the logic code to reflect what you would like the assistant to respond with.

Once, compelete, setup the Flask instance such as below. Ensure you set the correct IP address (your own) and port. The destination needs to be reachable from the Webex cloud service (in my case, I used port forwarding on my router, but you may need to use ngrok to get the connection through).
```sh
$ export FLASK_APP=server
$ export FLASK_ENV=development
$ flask run -h 192.168.0.100 -p 7171
```
