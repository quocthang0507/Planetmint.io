from planetmint_driver import Planetmint
from ipld import marshal, multihash
import utils

plntmnt = Planetmint('https://test.ipdb.io')


def new_keypair():
    alice = utils.generate_keypair()
    print(alice)
    utils.save_keypair(alice)


alice = utils.load_keypair()

plain_body = {
    'name': 'Planetmint.io',
            'desc': 'Blockchain all the things!'
}

asset2 = [
    {
        'data': multihash(marshal(plain_body))
    }
]

tx = plntmnt.transactions.prepare(
    operation='CREATE',
    signers=alice.public_key,
    assets=asset2
)

signed_tx = plntmnt.transactions.fulfill(tx, private_keys=alice.private_key)

print(signed_tx)

print(plntmnt.transactions.send_commit(signed_tx))
