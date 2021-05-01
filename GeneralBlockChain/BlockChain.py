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
        


#Mining the block 