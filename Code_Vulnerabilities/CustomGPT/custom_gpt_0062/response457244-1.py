
from PyKCS11 import PyKCS11Lib

# Initialize the PKCS#11 library
pkcs11 = PyKCS11Lib()
pkcs11.load('/path/to/your/pkcs11/library.so')  # Update with the correct library path

# Open a session with the smart card
slot = pkcs11.getSlotList()[0]  # Select the first available slot
session = pkcs11.openSession(slot)

# Login to the token (smart card) with a PIN
session.login('your_pin_here')

# Generating a key pair (for illustration)
keypair = session.generateKeyPair(2048)

private_key = keypair[0]  # This is your private key
public_key = keypair[1]    # This is your public key

# Here, we write the private key to the card
# (assuming the smart card supports this operation)
session.setAttributeValue(private_key, {
    'CKA_LABEL': 'MyPrivateKey',
    'CKA_VALUE': b'your_private_key_bytes_here'  # Replace with actual key bytes
})

# Logout and close the session
session.logout()
session.closeSession()
