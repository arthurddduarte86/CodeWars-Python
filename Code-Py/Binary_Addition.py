<<<<<<< HEAD
'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
'''
#
#
#
def add_binary(a,b):
    return bin(a+b)[2:]
# bin() convert integer to binary and after [2:] is reponsible to
# remove the first 2 chars from '0b10'
=======
'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
'''
#
#
#
def add_binary(a,b):
    return bin(a+b)[2:]
# bin() convert integer to binary and after [2:] is reponsible to
# remove the first 2 chars from '0b10'
>>>>>>> refs/remotes/origin/main
