import string

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

encryption_key = 3

encoding = {c:(i+encryption_key)%27 for i, c in letters.items()}

encoded_message = "klcpacqdphclvcfdhvdu"

def caesar(message, encryption_key):
    # return the encoded message as a single string!
    m="" 
    for word in message:
        i = (encoding[word]+ (encryption_key))%27
        print(i)
        m+=(letters[(i+encryption_key)%27])
        
    return m
                

decoded_message = caesar(encoded_message, -3) 
print(decoded_message)  


         

