import os
import time
import random


SLEEP_FROM = 100
SLEEP_TO = 200

RANDOM_WALLETS = True
WALLETS_PATH = "wallets.txt"
TEMPLATE_PATH = "templates/template.ts"
DEPLOY_PATH = "deploy/deploy.ts"


if __name__ == "__main__":
    with open(WALLETS_PATH, "r") as f:
        WALLETS = [row.strip() for row in f]

    if RANDOM_WALLETS:
        random.shuffle(WALLETS)

    for i, private_key in enumerate(WALLETS):
        print(f"{i+1} wallet is being running...")

        with open(TEMPLATE_PATH, "r") as f:
            deploy = f.read()

        deploy = deploy.replace("<WALLET-PRIVATE-KEY>", private_key)

        with open(DEPLOY_PATH, "w") as f:
            f.write(deploy)

        os.system("npx hardhat deploy-zksync")

        sleep = random.randint(SLEEP_FROM, SLEEP_TO)
        print(f"Sleeping for {sleep} seconds...")
        time.sleep(sleep)

        print("=" * 100, end="\n\n")
