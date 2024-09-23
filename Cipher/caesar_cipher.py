alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','r','p','q','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encode and 'decode' to decode").lower()
text= input("Type your message:\n").lower()
shift=int(input("Type the shift number"))

def encrypt(original_text, shift_amount):
    cipher_text=""
    for letter in original_text:
        if letter in alphabet:
            shifted=alphabet.index(letter)+shift_amount
            shifted%=len(alphabet)
            cipher_text+= alphabet[shifted]
    else:
        cipher_text+=letter
    print(f"here is the encoded result :{cipher_text}")


def decrypt(cipher_text,key):
    original_text=""
    for letter in cipher_text:
        if letter in alphabet:
            back=alphabet.index(letter)-key
            back%=len(alphabet)
            original_text+=alphabet[back]
        else:
            original_text+=letter
    print(f"The original text was {original_text}")

if (direction=="encode"):
    encrypt(original_text=text,shift_amount=shift)
elif(direction=="decode"):
    decrypt(cipher_text=text,key=shift)
else:
    print("Invalid")