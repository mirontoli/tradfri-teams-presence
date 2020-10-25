# tradfri-teams-presence
Use your raspberry pi to fetch your current presence in Teams and show it with a Trådfri RGB smart light from IKEA.

The corresponding blog post will be linked to shortly.

# Prerequisites
* Raspberry Pi Zero W with Raspberry Pi OS Light Buster (although, other client will work)
* python3 and pip3
* Trådfri Gateway, Remote and an RGB Light
* libcoap-client
* [O365 python module](https://pypi.org/project/O365/)
* Microsoft Graph API and consent to the used app (or your own)
* Teams (where the presence is set)

# Configuration
Install O365: 
```bash  
pip3 install O365
``` 
Copy and update the config.cfg
```bash
cp config-sample.cfg config.cfg
```
# Running the script
Start the `main.py` and keep it running:
```bash
nohup python3 main.py &
```
On the first run it will ask you to paste an URL into your browser and paste the redirect url. After that the tokens are saved in the file `my_token.txt` (listed in the `.gitignore`)

