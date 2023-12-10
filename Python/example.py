from planetmint_driver import Planetmint
from planetmint_driver.crypto import generate_keypair
from ipld import marshal, multihash

plntmnt = Planetmint('https://test.ipdb.io')

alice = generate_keypair()

tx = plntmnt.transactions.prepare(
    operation='CREATE',
    signers=alice.public_key,
    assets=[
        {'data': 
            multihash(marshal({'message': 'Blockchain all the things!'}))
            }   
    ]
)

signed_tx = plntmnt.transactions.fulfill(tx, private_keys=alice.private_key)

print(alice)
print(plntmnt.transactions.send_commit(signed_tx))