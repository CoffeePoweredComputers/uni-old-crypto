# Lab 4 - Ancient Encryption

**Note:** To simplify the tasks at hand you can expect all text to come in the form of all lowercase.


## Substitution Cipher

The general form of the substitution cipher is to:
  1. create a one-to-one mapping between each letter in the alphabet and another letter, selected at random.
  2. replace each letter in the message with the letter is is mapped to
  3. store the message and the "key" so you can decrypt it later

The most famous instance in which a substitution cipher was used was during the imprisonment of Mary, Queen of Scots'. Her systems of substitution were of varying complexity and not only involved the replacement of letters with other letters but also various symbols. Through the analysis of many of Mary's messages, the court spymaster, Thomas Pelippes, was able to decipher several of the messages. This was done by analyzing the documents for repeated characters and looking at correlations between those repeated characters and common words/constructs in the English language. From these simple inferences, Pelippes was able to reconstruct the keys', decrypt many of the messages, and ultimately identify both Mary's part in a conspiracy to overthrow the Crown as well as her coconspirators.


## Ceasar Cipher

The Ceasar cipher is a shift-based substitution cipher. Unlike Mary's usage of a complex and everchanging mapping between letters, Ceasar simply shifted the alphabet over. Please refer to the following example and equations when implementing this program: [https://en.wikipedia.org/wiki/Caesar_cipher#Example](https://en.wikipedia.org/wiki/Caesar_cipher#Example). Though this form of encryption is clearly as susceptible to the same form of attack as Mary's cipher and is, in many ways, less secure given it's more simple mapping mechanism it does has some advantages. The most notable one is the simplicity with which one can reconstruct the key. If a message was communicated to another general, Ceasar would not have to communicate a complex decryption method in the same way Mary would have to. He would simply give a courier the message and tell him the shift amount so the general could read it once the message was received.
