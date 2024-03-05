from planetmint_driver import Planetmint
from ipld import marshal, multihash
import utils

plntmnt = Planetmint('https://test.ipdb.io')


def new_keypair():
    alice = utils.generate_keypair()
    print(alice)
    utils.save_keypair(alice)


def load_keypair():
    alice = utils.load_keypair()
    print(alice)


alice = load_keypair()

# asset = [
#     {
#         'data':
#         multihash(marshal({'message': 'Blockchain all the things!'}))
#     }
# ]

# print(asset)

# tx = plntmnt.transactions.prepare(
#     operation='CREATE',
#     signers=alice.public_key,
#     assets=asset
# )

# signed_tx = plntmnt.transactions.fulfill(tx, private_keys=alice.private_key)

# print(plntmnt.transactions.send_commit(signed_tx))
