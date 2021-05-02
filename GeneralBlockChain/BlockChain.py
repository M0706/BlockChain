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
    
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'data':'dummy data'}
        self.chain.append(block)
        return block

    def get_previousblock(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        current_block_index = 1
        while(current_block_index < len(chain)):
            current_block = chain[current_block_index]
            # check if the hashes match that is chain is connected
            if(block[previous_hash] != self.hash(previous_block)):
                return False
            
            #check if the proofs are valid
            previous_block_proof = previous_block['proof']
            current_block_proof = current_block['proof']
            hash_operation = hashlib.sha256(str(current_block_proof**2 - previous_block_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            
            previous_block = current_block
            current_block_index +=1
        
        return True



#Mining the block 

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
blockchain = BlockChain()

@app.route('/mine_block', methods = ["GET"])

#mining the block
def mine_block():
    previous_block = blockchain.get_previousblock()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    new_block = blockchain.create_block(proof,previous_hash) 
    response = {"message":"Congragulations, You just mined a block" , 
                'index': new_block['index'],
                'timestamp': new_block['timestamp'],
                'proof': new_block['proof'], 
                'previous_hash': new_block['previous_hash'],
                'data':new_block['data']
                }
    
    return jsonify(response), 200


# getting the full blockchain
@app.route('/get_chain', methods = ["GET"])
def get_chain():
    response = {'chain': blockchain.chain,
                'length':len(blockchain.chain)}
    
    return jsonify(response), 200

#Running the app
app.run(host='0.0.0.0' , port=5000)
    
    
