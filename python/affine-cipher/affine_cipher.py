from math import gcd

alphabet = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26
}

def encode(plain_text, a, b):
    if not gcd(a, len(alphabet)) == 1:
        raise ValueError("a and m must be coprime.")

    numeric_letters = []
    
    for char in plain_text.lower():
        if char.isalpha():
            numeric_letters.append((a * (alphabet[char] - 1) + b) % len(alphabet))
    
    output = "".join([letter for i in range(len(numeric_letters)) for letter, numeric_value in alphabet.items() if (numeric_value - 1) == numeric_letters[i]])

    return ' '.join(output[i:i+5] for i in range(0,len(output),5))

    
        


def decode(ciphered_text, a, b):
    pass

#print(encode('abcdefghjklmnopqrstuvwxyz', 5, 7))