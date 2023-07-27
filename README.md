# General

This repo will help you to deploy contracts on zkSync Era Mainnet for multiple wallets (2 transactions with a total of ~0.3$ with gas of ~20 Gwei).

Recommended to run this script using a remote server:
* OS: Ubuntu 20.04;
* CPU: 2-cores;
* RAM: 4GB;
* Storage: 30GB.

# Tutorial

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

4. Add your private keys to `wallets.txt` (paste private keys, each from the new line, press Ctrl+O, Enter and Ctrl+X):
```sh
nano wallets.txt
```

5. Run the script to deploy contracts 
```sh
python3 deploy.py
```

6. You can modify the range of sleeping in seconds between wallets in `deploy.py` (find `SLEEP_FROM` and `SLEEP_TO` arguments, change their values, press Ctrl+O, Enter and Ctrl+X):
```sh
nano deploy.py
```

-----

</br>
</br>

This repo was created for "STD" group.

Donation: `0x34Ec371BA620e6C67A115a6794D44FED038Cc78C`
