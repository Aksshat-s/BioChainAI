import hashlib
import time


class Blockchain:
    def __init__(self):
        self.chain = []
        # Create Genesis block
        self.create_block(user_data={}, ai_summary='Genesis Block', previous_hash='0')


    def create_block(self, user_data, ai_summary, previous_hash=''):
        block = {
            'timestamp': time.time(),
            'user_data': user_data,
            'ai_summary': ai_summary,
            'previous_hash': previous_hash,
            'hash': self.hash_block(user_data, ai_summary, previous_hash)
        }
        self.chain.append(block)
        return block


    def hash_block(self, user_data, ai_summary, previous_hash):
        block_string = f"{user_data}{ai_summary}{previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block['previous_hash'] != previous_block['hash']:
                return False
            if current_block['hash'] != self.hash_block(current_block['user_data'], current_block['ai_summary'], current_block['previous_hash']):
                return False
        return True