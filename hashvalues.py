# -*- coding: utf-8 -*-
"""Hash Values for Files.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ab1mCGL49OtUtYFRUne_VLerJy5gzCq9

# Calculating Hash Values for Values
"""

import hashlib

def calculate_file_hash(file_name):
  try:
    #Open the file
    with open(file_name, 'rb') as file:
      file_contents = file.read()

    #Calculate Hash Values
    md5_hash = hashlib.md5(file_contents).hexdigest()
    sha1_hash = hashlib.sha1(file_contents).hexdigest()
    sha256_hash = hashlib.sha256(file_contents).hexdigest()
    sha3_256_hash = hashlib.sha3_256(file_contents).hexdigest()

    # Display the hash values
    print(f"File to Hash: {file_name}")
    print(f"MD5:       {md5_hash}")
    print(f"SHA-1:     {sha1_hash}")
    print(f"SHA-256:   {sha256_hash}")
    print(f"SHA3-256:  {sha3_256_hash}")
  except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")


def main():
  #Prompt for filename
  file_name = input("Enter the name of the file to hash:")
  calculate_file_hash(file_name)

if __name__ == "__main__":
  main()