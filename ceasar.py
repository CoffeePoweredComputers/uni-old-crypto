#creates a Ceasar cypher for a string
def encrypt(shift_amount, message):
	'''
	'''
	pass

#decrypts a Ceasar cipher for a string
def decrypt(shift_amount, encoded_message):
	'''
	'''
	pass


###########################
## This is the test code ##
##     DO NOT MODIFY     ##
###########################

stringtodecrypt = ("Iq wkh ehjlqqlqj wkh xqlyhuvh zdv fuhdwhg.", 
		"Tklv kdv pdgh d orw rishrsoh yhub dqjub",
		"dqg ehhq zlghob uhjdughg dv d edg pryh.")


encrypted_string = encrypt(3, string)
print(f'The encrypted string is: {encrypted_string}')


stringtoencrypt = ("galia est omnis divisa in partes tres, "
		"quarum unam incolunt belgae, aliam aquitani, "
		"tertiam qui ipsorum lingua celtae, nostra "
		"galli appellantur.")

decrypted_string = decrypt(5, encrypted_string)
print(f'The decrypted string is: {decrypted_string}')
