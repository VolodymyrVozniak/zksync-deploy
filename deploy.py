import os
import time
import random

from tqdm import tqdm
from web3 import Web3


SLEEP_FROM = 100
SLEEP_TO   = 200

RANDOM_WALLETS = True
RPC = "https://mainnet.era.zksync.io"

WALLETS_PATH   = "data/wallets.txt"
TEMPLATE_PATH  = "templates/template.ts"
DEPLOY_PATH    = "deploy/deploy.ts"

EXPLORER_STRING = "https://explorer.zksync.io/address"


def sleeping(from_sleep: int, to_sleep: int):
    x = random.randint(from_sleep, to_sleep)
    for i in tqdm(range(x), desc='sleep', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)


def get_public_key(private_key: str) -> str:
    web3 = Web3(Web3.HTTPProvider(RPC))
    account = web3.eth.account.from_key(private_key)
    return account.address


if __name__ == "__main__":
    with open(WALLETS_PATH, "r") as f:
        WALLETS = [row.strip() for row in f]

    if RANDOM_WALLETS:
        random.shuffle(WALLETS)

    for private_key in WALLETS:
        public_key = get_public_key(private_key)

        print(f"`{public_key}` is being running...")

        with open(TEMPLATE_PATH, "r") as f:
            deploy = f.read()

        deploy = deploy.replace("<WALLET-PRIVATE-KEY>", private_key)

        with open(DEPLOY_PATH, "w") as f:
            f.write(deploy)

        os.system("npx hardhat deploy-zksync")

        print(f"Check transactions here: {EXPLORER_STRING}/{public_key}", end="\n\n")

        sleeping(SLEEP_FROM, SLEEP_TO)
