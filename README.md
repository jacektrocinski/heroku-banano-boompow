# Heroku BoomPow Client

Deploy BANANO's super official Proof of Work system (BoomPoW) on Heroku to earn free BAN.

## Requirements

1. A free [Heroku account](https://signup.heroku.com/signup/dc).

## Prepare the app

Clone this repository so that you have a local version of the code that you can then deploy to Heroku, execute the following commands in your local command shell or terminal:

```shell
git clone https://github.com/jacektrocinski/heroku-banano-boompow.git
cd heroku-banano-boompow
```

## Deploy the app

Before continuing, make sure Heroku CLI is installed.

```shell
heroku apps:create banano-boompow
heroku buildpacks:add heroku/python --app banano-boompow
heroku buildpacks:add --index 1 heroku-community/apt --app banano-boompow
```

Replace `YOUR_BANANO_ADDRESS` in `start.sh` with your BAN address.

Deploy the code.

```shell
git push heroku main
heroku ps:scale worker=1 --app banano-boompow
```

## Useful commands

Run Bash inside a Heroku dyno.

```shell
heroku run bash --app banano-boompow
```

Deploy from a branch besides `main`.

```shell
git push heroku dev:main
```

### Installation

- Download the [latest version](https://github.com/bbedward/boompow/releases) and extract it.
- On Linux, open a terminal and cd to the bpow-client directory.
- On Windows, shift + right-click in the bpow-client directory and click "Open Powershell window here".
- On MacOS, in Finder right click on the bpow-client directory and click "New Terminal at bpow-client"
- `pip3 install --user -r requirements.txt`

### Linux

1. Install required library

```bash
sudo apt install ocl-icd-libopencl1
```

2. Check `./bin/linux/nano-work-server --help` for information on how to select your GPU (or CPU).
3. Run the work server:

```bash
./bin/linux/nano-work-server --gpu 0:0 -l 127.0.0.1:7000
```

4. Check the client configuration options with `python3 bpow_client.py --help`
5. Run the client:

```bash
python3 bpow_client.py --payout YOUR_BANANO_ADDRESS --work {ondemand,precache,any}
```
