#Create a blockChain

import datetime
import hashlib
import json
from flask import Flask, jsonify 

#Building the blockchain

class BlockChain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1,previous_hash='0')
    
    def create_block(self,proof,previous_hash):
        block = {'index': len(self.chain)+1,
                'TimeStamp': datetime.datetime.now(),
                'proof': proof, 
                'previous_hash': previous_hash,
                'data':"Dummy data"
            }
        self.chain.append(block)
        return block

    def get_previousblock(self):
        return self.chain[-1]




#Mining the block 