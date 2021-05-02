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

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while(check_proof==False):
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_hash**2).encode()).hexdigest()
            #check that target. Assume target is leading 4 zeroes
            if hash_operation[:4] = '0000':
                check_proof = True
            else:
                new_proof = new_proof+1

    def hash(self, block):
        encoded_block = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()




        




#Mining the block 