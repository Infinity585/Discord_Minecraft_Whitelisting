
# Minecraft Whitelist

A simple Python Discord bot designed to be hosted on the same hardware as a Minecraft server, allowing it to update the `whitelist.json` file. This bot was created for a friend who set up a Minecraft server so that members of their Discord could self-whitelist.


## Deployment

### ⚠️ Prerequisites ⚠️

#### Python Version 3.12 and Virtual Environment:
```bash
sudo apt install python3 python3-venv
```

#### Python3-pip

1. Update Package lists
```bash
sudo apt update
```
2. Upgrade the System (optional but recommended):
```bash
sudo apt upgrade
```
3. Install python3-pip
```bash
sudo apt install python3-pip
```







### 🔧Installation🔧

1. Clone the repository:
```bash
git clone https://github.com/Infinity585/Discord_Minecraft_Whitelisting.git
```
2. Navigate to the repository directory:
Change into the repo directory

```bash
cd Discord_Minecraft_Whitelisting/
```
3. Set up a Python Virtual Environment:
```bash
python3 -m venv env
source env/bin/activate
```

4. Install Python dependencies:
```bash
pip3 install -r requirements.txt
```

5. Configure the .env file:
```bash
nano .env
```

6. Paste in and fill out the fields:
```code
token =  (discord bot toekn)
applicationid = (discord applicationid)
jsonPath = (full path)
logChannel = (discord channel id)

```
#### To save changes and exit in nano:

1. Press to exit
```
ctrl + x
```
2. Save changes (Save modified buffer?)
```
y
```
3. Write to file (File Name to Write: .env)
```
Enter
```


### 🏃Running the program🏃

Run the bot:
```bash
 Python3 main.py
```
#### If using SSH, keep the program running with screen

1. Start a screen session:
``` bash
screen -S minecraftDiscordBot
```
2. Navigate to the repository directory
``` bash
cd Discord_Minecraft_Whitelisting/
```
3. Enter the Virtual Environment
```bash
source env/bin/activate
```
4. Run the program
```bash
python3 main.py
```
The bot should now be running, and the SSH terminal can be safely closed.

To list screen sessions:
```bash
screen -ls
```

To reattach a session:
``` bash
screen -r <id or name>
```
## Discord Commands

`/whitelist <minecraft username>`
