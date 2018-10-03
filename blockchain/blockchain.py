#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : blockchain.py
# @Author: Zhangyiqi
# @Date  : 2018/9/21

# {
#     "index": 0,
#     "timestamp": "",
#     "transactions": [
#         {
#             "sender": "",
#             "recipient": "",
#             "amount": 5,
#         }
#     ],
#     "proof": "",
#     "previous_hash": "",
# }

import hashlib
import json
from time import time

class Blockchain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(proof=100, previous_hash=1)  #创世纪区块

    def new_block(self, proof, previous_hash = None):

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block)
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount) -> int:
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):

        return self.chain(-1)
