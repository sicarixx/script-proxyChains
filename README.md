### Python Script for Proxychains and Tor
#### Python script for Proxychains and Tor by [_Sicarixx_](https://github.com/sicarixx) and [_Wre_](https://github.com/BrendaVlaam)<br>
#### Intructions

1. Give execute permissions to the file `chmod +x proxychains.py`
2. Execute file whit `./proxychains.py`

#### Important information 
1. For the script to work, you must have _Proxychains_ and _Tor_ installed. If they are not installed, the script does it for you.
2. Python3 is required.
3. We are going to replace the "proxychains.conf" file located in the /etc/ folder and the original file name will be replaced by "proxychains.conf.bak".
4. Script for Debian based distributions.

#### Manual installation

Update and upgrade system 
```bash
sudo apt-get update && sudo apt upgrade -y
```
Install Proxychains and Tor
```bash
sudo apt-get install proxychains tor
```
Install Git and Python3
```bash
sudo apt-get install git python3
```
Now follow the [instructions](https://github.com/fineg4n/Proxychains-Script#intructions) to run the script.
##### Enjoy!

> _"The quieter you become, the more you are able to hear"_
