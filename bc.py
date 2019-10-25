#!/usr/bin/env python
from time import sleep
import hashlib
from random import randint


from api_funcs import last_proof_, mine_

def valid_proof(last_proof: int, proof: int, difficulty: int) -> bool:
    guess = f'{last_proof}{proof}'.encode()

    guess_hash = hashlib.sha256(guess).hexdigest()

    return guess_hash[:difficulty] == "0" * difficulty

def mine():

    m = last_proof_()
    sleep(m['cooldown'])
    last_proof = m['proof']
    difficulty = m['difficulty']

    proof = 0
    while not valid_proof(last_proof, proof, difficulty):
        proof = randint(0, 2**30)

    return proof

if __name__=='__main__':
    proof = mine()
    m = mine_(proof)
    print(m)
