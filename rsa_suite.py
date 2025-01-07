#Kayla Bell
#COSC 5367.060
#November 24, 2024

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

#Generate Keys Function
def generate_keys (private_key_filename, public_key_filename, size=2048):
  #Generate RSA key
  key = RSA.generate(size)

  #Public and Private Keys Export
  private_key = key.export_key()
  public_key = key.publickey().export_key()

  #Save the Private Key
  with open(private_key_filename, 'wb') as private_f:
    private_f.write(private_key)
  #Save the Public Key
  with open(public_key_filename, 'wb') as public_f:
    public_f.write(public_key)

#Encryption Function
def encrypt_message(plaintext_filename, ciphertext_filename, public_key_filename):
  #Import Public Key File
  with open(public_key_filename, 'rb') as public_f:
    public_key = RSA.import_key(public_f.read())
  #Read plainbtext from the file
  with open(plaintext_filename, 'rb') as plaintext_f:
    plaintext = plaintext_f.read()
  #Generate random byte session key
  session_key = get_random_bytes(16)
  #Encrypt the session key
  rsa_cipher =   PKCS1_OAEP.new(public_key)
  encrypted_session_key = rsa_cipher.encrypt(session_key)
  #Encrypt the message
  ciper_aes = AES.new(session_key, AES.MODE_EAX)
  ciphertext, tag = ciper_aes.encrypt_and_digest(plaintext)
  #Write the encrypted session key
  with open(ciphertext_filename, 'wb') as ciphertext_f:
    ciphertext_f.write(encrypted_session_key)
    ciphertext_f.write(ciper_aes.nonce)
    ciphertext_f.write(tag)
    ciphertext_f.write(ciphertext)

#Decryption Function
def decrypt_message(ciphertext_filename, private_key_filename):
  #Load Private Key
  with open(private_key_filename, 'rb') as private_f:
    private_key = RSA.import_key(private_f.read())
  #Read the session key, nonce, tag, and ciphertext
  with open(ciphertext_filename, 'rb') as ciphertext_f:
    # Access size_in_bytes as an attribute, ensuring it's an integer
    encrypted_session_key = ciphertext_f.read(private_key.size_in_bytes())
    nonce = ciphertext_f.read(16)
    tag = ciphertext_f.read(16)
    ciphertext = ciphertext_f.read()
  #Decrypt the session key
  rsa_cipher = PKCS1_OAEP.new(private_key)
  session_key = rsa_cipher.decrypt(encrypted_session_key)
  #Decrypt the message
  cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
  plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)
  return plaintext.decode('utf-8')

#Main Function
if __name__ == "__main__":
  # Generate RSA keys
  generate_keys('rsa_private.pem', 'rsa_public.pem', 2048)
  # Write a plaintext message to a file
  with open('plaintext.txt', 'w') as f:
    f.write("This is a secret message for testing.")
  # Encrypt the message
    encrypt_message('plaintext.txt', 'encrypted_data.bin', 'rsa_public.pem')
  # Decrypt the message
    decrypted_message = decrypt_message('encrypted_data.bin', 'rsa_private.pem')
  # Output the result
  if decrypted_message:
    print("Decrypted Message:", decrypted_message)