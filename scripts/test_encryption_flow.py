# -*- coding: utf-8 -*-
import unittest
import os

from aes_encryption import encrypt_file, decrypt_file


class TestEncryptionFlow(unittest.TestCase):

	def setUp(self):
		"""
		Create a text file which content will be tested.
		Prepare test data.
		"""
		self.password = 'test'
		self.keyphrase = 'test_phrase'
		self.file_original_name = 'test_text_file.txt'
		self.file_original_content = 'Testing will this text remain.'
		self.file_crypto_name = 'test_text_file.txt.enc'
		self.file_new_name = 'test_text_file_2.txt.enc'

		file = open(self.file_original_name, 'w')
		file.write(self.file_original_content)
		file.close()

	def test_encryption(self):
		"""
		Test flow of things.
		First encrypt, then decrypt, and finally check is the new content same as the original one.
		"""
		# Encrypt the original file.
		encrypt_file(self.password, self.keyphrase, self.file_original_name, out_filename=self.file_crypto_name)
		# Decrypt the file into a new file.
		decrypt_file(self.password, self.keyphrase, self.file_crypto_name, out_filename=self.file_new_name)

		# Open the new generated file and compare its content with the original one.
		new_file = open(self.file_new_name, 'r')
		self.assertEqual(new_file.read(), self.file_original_content)

		# Close the new file.
		new_file.close()

	def tearDown(self):
		"""
		Delete created files.
		"""
		os.remove(self.file_original_name)
		os.remove(self.file_crypto_name)
		os.remove(self.file_new_name)


if __name__ == '__main__':
	unittest.main()
