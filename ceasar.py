def encrypt(shift_amount, message):
    '''
    Given a shift amount and a message return
    the encrypted message.
    '''
    pass

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

stringtodecrypt = (
        "lq wkh ehjlqqlqj wkh xqlyhuvh zdv fuhdwhg."
        "wklv kdv pdgh d orw rishrsoh yhub dqjub dqg"
        "ehhq zlghob uhjdughg dv d edg pryh."
        )

# This should decrypt a string and print out a sensible 
# English sentence.
decrypted_string = decrypt(3, stringtodecrypt)
print(f'The decrypted string is: {decrypted_string}')


stringtoencrypt = ("galia est omnis divisa in partes tres, "
        "quarum unam incolunt belgae, aliam aquitani, "
        "tertiam qui ipsorum lingua celtae, nostra "
        "galli appellantur.")

# This should encrypt the intro to Ceasar's "Commentarii de Bello Gallico"
encrypted_string = encrypt(5, stringtoencrypt)
print(f'The encrypted string is: {encrypted_string}')

