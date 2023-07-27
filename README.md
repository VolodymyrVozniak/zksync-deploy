# Overview

This repo will help you to deploy contracts on zkSync Era Mainnet for multiple wallets (2 transactions with a total of ~0.3$ with gas of ~20 Gwei).

Recommended to run this script using a remote server:
* OS: Ubuntu 20.04;
* CPU: 2-cores;
* RAM: 4GB;
* Storage: 30GB.

# Instructions

1. Clone this repo:
```sh
git clone https://github.com/VolodymyrVozniak/zksync-deploy.git
```

2. Go to a directory:
```sh
cd zksync-deploy
```

3. Install the requirements and prepare for deploying:
```sh
source install.sh
```

4. Add your private keys to `data/wallets.txt` (paste private keys, each from the new line, press Ctrl+O, Enter and Ctrl+X):
```sh
nano data/wallets.txt
```

5. Create virtual environment (can skip this step):
```sh
python3 -m venv env
```

6. Activate virtual environment (must run every time you connect to a server):
```sh
source env/bin/activate
```

7. Install python requirements (install only once):
```sh
pip install requirements.txt
```

8. Run the script to deploy contracts:
```sh
python3 deploy.py
```

9. You can modify the range of sleeping in seconds between wallets in `deploy.py` (find `SLEEP_FROM` and `SLEEP_TO` arguments, change their values, press Ctrl+O, Enter and Ctrl+X):
```sh
nano deploy.py
```

-----

</br>
</br>

This repo was created for "STD" group.

Donation: `0x34Ec371BA620e6C67A115a6794D44FED038Cc78C`
