# 'str' object handles texual data, called string, which are immutable sequences of unicode code points. Python has no 'char' type to store 1 character, its a str with length 1.

def string_practice():
    s = 'Hello World!'
    print(s)
    print(f'{len(s) = }') # prints length of string
    print(f'{s.removeprefix("Hel") = }') # removes prefix "Hel" from the string
    print(f'{s.removesuffix("ere") = }') # removes suffix "ere" from the string
    print(f'{s.removeprefix("ops") = }') # no "ops" prefix, so nothing removed from the string
    print("================================================================\n")

string_practice()


# encoding and decoding strings, utf-8 strings is mostly used 
def encode_decode():
    s = 'This is unic0de'
    print(f'{type(s) = }') # <class 'str'>
    encoded_s = s.encode('utf-8') 
    print(encoded_s, type(encoded_s)) # <class 'bytes'>
    decoded_s = encoded_s.decode('utf-8')
    print(decoded_s, type(decoded_s))  # <class 'str'>
    bytes_obj = b'A bye object!'
    print(bytes_obj, type(bytes_obj)) # <class 'bytes'>
    print("================================================================\n")


encode_decode()