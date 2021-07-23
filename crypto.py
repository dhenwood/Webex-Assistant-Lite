import base64
import config
from typing import Optional, Sequence
from cryptography import fernet
from cryptography.hazmat.primitives import hashes, hmac, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, padding, rsa


def decrypt(encryptedMsg):
    encrypted_components: Sequence[str] = encryptedMsg.split('.')
    encrypted_temp_key: str = encrypted_components[0]
    encrypted_message: str = '.'.join(encrypted_components[1:])

    with open(config.privateKeyLocation, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
        )

    try:
        decoded_temp_key = base64.b64decode(encrypted_temp_key.encode('utf-8'))
    except binascii.Error as exc:
        raise EncryptionKeyError('Message cannot be decoded') from exc
    pad = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None
    )

    try:
        temp_key: bytes = private_key.decrypt(decoded_temp_key, pad)
    except ValueError as exc:
        raise EncryptionKeyError('Invalid key') from exc

    cipher: fernet.Fernet
    try:
        cipher = fernet.Fernet(temp_key)
    except (binascii.Error, ValueError) as exc:
        raise EncryptionKeyError('Invalid key') from exc
    return cipher.decrypt(encrypted_message.encode('utf-8')).decode('utf-8')

