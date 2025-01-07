# -*- coding: utf-8 -*-
"""COSC 5367 - Homework03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LXGEFEIPO7FLB0hHBB_MgA5C6IVw0eyl
"""

pip install pycryptodome

#Kayla Bell
#COSC 5367.060
#November 1,2024


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

#Encryption Function

def encrypt(plaintext,key):
  #Convert plaintext to bytes
  plaintext = plaintext.encode('ascii')
  #Generate a random nonce for CTR mode
  nonce = os.urandom(8)
  #Create a new AES cipher object in CTR mode
  cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
  #Encrypt the plaintext
  ciphertext = cipher.encrypt(plaintext)
  #Return ciphertext and nonce
  return (ciphertext,nonce)




def decrypt(ciphertext,key,nonce):
  #Create a new AES cipher object in CTR mode
  cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
  #Decrypt the ciphertext
  plaintext_bytes = cipher.decrypt(ciphertext)
  #Convert plaintext to string
  plaintext = plaintext_bytes.decode('ascii')
  #Return plaintext
  return plaintext