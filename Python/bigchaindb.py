from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb_root_url = 'https://example.com:9984'

tokens = {'app_id': 'your_app_id', 'app_key': 'your_app_key'}

bdb = BigchainDB(bdb_root_url, headers=tokens)