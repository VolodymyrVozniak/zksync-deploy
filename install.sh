# Server Preparation
sudo apt-get update && sudo apt-get install -y
sudo apt install curl -y
curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh
sudo bash /tmp/nodesource_setup.sh
sudo apt-get install -y nodejs

# Preparing for Deploy
npm init -y
npm add -D typescript ts-node @types/node ethers@^5.7.2 zksync-web3@^0.14.3 @ethersproject/hash @ethersproject/web hardhat @matterlabs/hardhat-zksync-solc @matterlabs/hardhat-zksync-deploy
npx hardhat compile