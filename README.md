# Planetmint.io

## Quickstart

Planetmint is a metadata blockchain. This introduction gives an overview about how to attest data to Planetmint. First, simple transaction creation and sending is shown. Thereafter, an introduction about how to set up a single node or a cluster is given.

### The IPDB Testnet - sending transactions

```{python}
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
print(plntmnt.transactions.send_commit(signed_tx))
```
