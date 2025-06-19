# KasplexTestnet

Faucet Coin Automation for Kaspa Finance Kasplex Layer 2 Testnet

## Overview

KasplexTestnet is a Python-based project designed to automate claiming faucet coins from Kaspa Finance’s Kasplex testnet. Kasplex is a Layer 2 rollup solution built on the Kaspa network, providing a scalable, EVM-compatible environment for issuing fungible tokens (KRC-20), non-fungible tokens (KRC-721), and other digital assets without causing UTXO bloat.

This repository helps developers, artists, and influencers easily obtain testnet tokens to build and test decentralized applications on Kasplex.

## About Kasplex

Kasplex is an open-source, community-driven infrastructure protocol on Kaspa that enables:

- Efficient data insertion using Pay-to-Script-Hash (P2SH) to avoid UTXO bloat  
- Creation and management of KRC-20 fungible tokens and KRC-721 NFTs  
- A gas fee mechanism supporting sustainable miner incentives  
- An open-source indexer and public APIs for seamless on-chain data retrieval  
- Foundation for Layer 2 solutions and future cross-chain interoperability  

Kasplex leverages Kaspa’s high block rate and decentralized Proof-of-Work Layer 1 to provide scalable, secure, and efficient token issuance and management.

## Features

- Automated faucet coin claiming for Kasplex testnet  
- Python scripts to interact with Kasplex network  
- Supports token minting, transfers, and querying via Kasplex APIs  
- Helps developers build and test Layer 2 dApps on Kaspa  

## Getting Started

### Prerequisites

- Python 3.7 or higher  
- Install dependencies:

```
pip install -r requirements.txt
```

### Installation

1. Clone the repository:

```
git clone https://github.com/piobox2001/KasplexTestnet.git
cd KasplexTestnet
```

2. Install required Python packages as above.

3. Configure your testnet wallet address and private key in the script or configuration files as needed.

### Usage

Run the main faucet claiming or interaction script:

```
python main.py
```

This will automate faucet coin requests and enable basic Kasplex testnet interactions.

## Resources

- [Kasplex Official Documentation](https://docs.kasplex.org)  
- [Kaspa Network](https://kaspa.org) — Fastest Layer 1 blockchain with BlockDAG architecture  
- [Kasplex API Documentation](https://docs.kasplex.org/api)  
- [Kasplex GitHub Repository](https://github.com/piobox2001/KasplexTestnet)  

## Contributing

Contributions are welcome! Please open issues or submit pull requests to enhance the scripts or add new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

