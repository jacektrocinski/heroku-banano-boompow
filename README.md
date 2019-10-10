# BoomPow Client

These steps will guide you on how to setup a new work client. The nano-work-server provided is based on [nanocurrency/nano-work-server](https://github.com/nanocurrency/nano-work-server). Only this work server is fully supported.

## Setup

### Requirements

1. [Python](https://www.python.org/) 3.6.7 or higher.

### Installation

- Download the [latest version](https://github.com/bbedward/boompow/releases) and extract.
- Open a console under `bpow-client`. On Windows, shift + right-click and "Open Powershell window here".
- `pip3 install --user -r requirements.txt`

## Running

You need to find out what your GPU vendor/device numbers are if you're going to be using a GPU. Usually it will be either `0:0`, `0:1`, or `1:0`, depending on how many you have (including integrated graphics).

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

### Windows

1. Edit the file `run_windows.bat` with your desired configuration (including the work-server GPU config).
2. Double-click the same file, which should eventually open two terminals. You must leave them running in the foreground. You can minimize but not close them (sorry!).

### macOS

1. Install Rust if you don't already have it:
   ```bash
   curl https://sh.rustup.rs -sSf | sh
   ```
2. Configure your current shell:
   ```bash
   source $HOME/.cargo/env
   ```
3. Compile the nano-work-server:
   ```bash
   git clone https://github.com/nanocurrency/nano-work-server.git
   cd nano-work-server
   cargo build --release
   ```
4. Overwrite the `nano-work-server` you downloaded from BoomPow with the one you just compliled. You can drag the binary file from here:
   ```
   nano-work-server/target/release/nano-work-server
   ```
   and drop it in the BoomPow directory you downloaded from the [latest version](https://github.com/bbedward/boompow/releases) above:
   ```
   bpow-client/bin/linux/nano-work-server
   ```
5. Check `./bin/linux/nano-work-server --help` for information on how to select your GPU (or CPU).
6. Run the work server:
   ```bash
   ./bin/linux/nano-work-server --gpu 0:0 -l 127.0.0.1:7000
   ```
6. Open Terminal and run the client:
   ```bash
   python3 bpow_client.py --payout YOUR_BANANO_ADDRESS --work {ondemand,precache,any}
   ```
