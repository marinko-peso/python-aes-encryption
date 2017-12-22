# -*- coding: utf-8 -*-
import sys
import os
import io
from scripts.aes_encryption import decrypt_file, OUTPUT_FILE_DEFAULT_SUFFIX


def main():
	"""
	Validate arguments sent and process the input file or notify the user if required.
	"""
	arguments_sent = sys.argv
	if len(arguments_sent) > 1:
		# Get the filename to decrypt.
		in_filename = arguments_sent[1]
		# Check is file valid/exists before proceeding.
		if not os.path.isfile(in_filename):
			print '%s is not a valid file. Exiting...' % in_filename
			return False

		# Fetch password to use.
		password = ''
		while password == '':
			password = raw_input('Please enter your password: ')
		# Fetch keyphrase to use.
		keyphrase = ''
		while keyphrase == '':
			keyphrase = raw_input('Please enter your keyphrase: ')
		# Fetch output filename. This can be empty and auto generated.
		out_filename = ''
		out_filename = raw_input('Enter your output file name. Leaving blank recommended. If left blank, it will retain its name just without %s: ' % OUTPUT_FILE_DEFAULT_SUFFIX)

		# Decrypt the provided file.
		# In case of error notify the caller of its content.
		print 'Starting decryption process...'
		status = decrypt_file(password, keyphrase, in_filename, out_filename)
		if status.get('status'):
			print 'File successfully decrypted and saved as %s. Exiting...' % status.get('out_filename')
		else:
			print 'Something went wrong. Error message below. Exiting...'
			print status.get('error')


# Standard boilerplate to run main method.
if __name__ == '__main__':
	main()
