def hex_str_to_bytes(hex_str):
    """Convert a string of hex characters to a list of numbers representing byte values.
    """
    return [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]

def bytes_to_ascii(byte_list):
    """Convert a list of byte values to an ASCII-encoded string.
    """
    return ''.join([chr(x) for x in byte_list])

def is_alpha(n):
    """Returns whether the inputted number represents an alphabetical character in ASCII.
    """
    return (n >= 65 and n <= 90) or (n >= 97 and n <= 122)
    
def xor(l1, l2):
    """Given two lists of bytes, xor them together elementwise, ignoring trailing bytes
    of the longer list.
    """
    return [l1[i] ^ l2[i] for i in range(min(len(l1), len(l2)))]

