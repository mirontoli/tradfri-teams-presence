# tradfri-teams-presence
Use your raspberry pi to fetch your current presence in Teams and show it with a Trådfri RGB smart light from IKEA.

More details in my blog post:
* [DIY: Integrating Trådfri lights with Teams presence](https://chuvash.eu/2020/10/27/diy-integrating-tradfri-lights-with-teams-presence/)

# Prerequisites
* Raspberry Pi Zero W with Raspberry Pi OS Light Buster (although, other client will work)
* python3 and pip3
* Trådfri Gateway, Remote and an RGB Light
* [libcoap-client](https://gist.github.com/mirontoli/b71d94ea4da162b1136d8d1d3da853cc#file-alert-step3-install-libcoap-sh)
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

# Stopping the script
Find the process id and kill it:
```bash
ps -aux | grep main.py #e.g. 10380
kill 10380
```

