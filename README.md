# Table of Contents

[*Introduction*](#introduction)  
[*What is a blockchain?*](#what_is_a_blockchain?)  
[*What is a cryptocurrency?*](#what_is_a_cryptocurrency?)  

## Introduction

This is a blockchain project for learning Python using Maximilian Schwarzmüller's *Udemy* course.

## What is a blockchain?

A blockchain is a distributed data storage consisting in containers (blocks) connected to one another. Each block is uniquely identified by a hash. This has reflects the contents of the block in such a way that the data of the block cannot be altered without also changing the hash. Blocks are connected in that each block also contains the hash of the block before it. This countermeasure ensures that the data in the chain is resistant to modification: an individual block in the chain cannot be edited without changing the entire chain. The blockchain is 'distributed' in the sense that its state is broadcast across a network. Each member of the network (node) stores a physical copy of the state of the blockchain.

## What is a cryptocurrency?

A cryptocurrency uses the blockchain technology by storing transactional data in blocks. The entire chain (ledger) consists of blocks added by validating transactions, and transactions are validated via hash generation (mining). The reward for doing the work of mining is a token of cryptocurrency (coin). Transactions occur when nodes (wallets) trade these coins. What people are willing to pay in 'real' currency is what the cryptocurrency coin is worth.