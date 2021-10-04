#creates a Ceasar cypher for a string
def encrypt(shift_amount, message):
	'''
	Given a shift amount and a message return
	the encrypted message.
	'''
	pass

#decrypts a Ceasar cipher for a string
def decrypt(shift_amount, encoded_message):
	'''
	Given a shift amount and a message return
	the decrypted message.
	'''
	pass


###########################
## This is the test code ##
##     DO NOT MODIFY     ##
###########################

stringtodecrypt = ("Iq wkh ehjlqqlqj wkh xqlyhuvh zdv fuhdwhg.", 
		"Tklv kdv pdgh d orw rishrsoh yhub dqjub",
		"dqg ehhq zlghob uhjdughg dv d edg pryh.")

decrypted_string = decrypt(5, stringtodecrypt)
print(f'The decrypted string is: {decrypted_string}')


stringtoencrypt = ("galia est omnis divisa in partes tres, "
		"quarum unam incolunt belgae, aliam aquitani, "
		"tertiam qui ipsorum lingua celtae, nostra "
		"galli appellantur.")

encrypted_string = encrypt(3, stringtoencrypt)
print(f'The encrypted string is: {encrypted_string}')

