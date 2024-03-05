import os
import re
import planetmint_driver.crypto
from planetmint_driver.crypto import CryptoKeypair

private_key_start_comment = '-----BEGIN PRIVATE KEY-----'
private_key_end_comment = '-----END PRIVATE KEY-----'
public_key_start_comment = '-----BEGIN PUBLIC KEY-----'
public_key_end_comment = '-----END PUBLIC KEY-----'
private_key_file_name = "private.key"
public_key_file_name = "public.key"


def generate_keypair() -> CryptoKeypair:
    """
    Generates an ed25519 keypair
    """
    return planetmint_driver.crypto.generate_keypair()


def save_keypair(keypair: CryptoKeypair) -> None:
    """
    Saves keypair into files
    """
    with open(private_key_file_name, "w", encoding="utf-8") as writer:
        writer.write(private_key_start_comment + '\n')
        writer.write(keypair.private_key + '\n')
        writer.write(private_key_end_comment + '\n')
    with open(public_key_file_name, "w", encoding="utf-8") as writer:
        writer.write(public_key_start_comment + '\n')
        writer.write(keypair.public_key + '\n')
        writer.write(public_key_end_comment + '\n')


def load_keypair(current_dir=None) -> CryptoKeypair:
    """
    Loads keypair from files
    """
    public_key_file_path = ''
    private_key_file_path = ''
    public_key = ''
    private_key = ''
    if current_dir != None and os.path.isdir(current_dir):
        public_key_file_path = os.path.join(current_dir, public_key_file_name)
        private_key_file_path = os.path.join(current_dir, private_key_file_name)
    else:
        public_key_file_path = os.path.join(os.getcwd(), public_key_file_name)
        private_key_file_path = os.path.join(os.getcwd(), private_key_file_name)
    if os.path.isfile(public_key_file_path) and os.path.isfile(private_key_file_path):
        with open(public_key_file_path, 'r') as reader:
            data = reader.read()
            pattern = re.compile(
                f'{public_key_start_comment}(.*?){public_key_end_comment}', re.DOTALL)
            match = pattern.search(data)
            if match:
                public_key = match.group(1).strip()
        with open(private_key_file_path, 'r') as reader:
            data = reader.read()
            pattern = re.compile(
                f'{private_key_start_comment}(.*?){private_key_end_comment}', re.DOTALL)
            match = pattern.search(data)
            if match:
                private_key = match.group(1).strip()
    return CryptoKeypair(*(private_key, public_key))
