def mord(str1, forced_list = false):
    
    if not forced_list and len(str1) == 1:
        raw_id =  ord(str1)
        return raw_id + (raw_id > 129) + (raw_id > 141) + (raw_id > 143) + (raw_id > 144) + (raw_id > 157)
    
    else:
        list1 = []
        for c in str1:
            list1.append(mord(c))
        return list1            


def mchr(uin):
    if uin is int:
        return uin - (uin > 129) - (uin > 141) - (uin > 143) - (uin > 144) - (uin > 157)
    
    else:
        list1 = []
        for i in uin:
            list1.append(mchr(c))
        return list1


def encode_string(input_str, key):
    encoded_str = ''
    for char in input_str:
        encoded_char = chr(((ord(char) + key) ^ key) % 256)
        encoded_str += encoded_char
    return encoded_str


def decode_string(encoded_str, key):
    decoded_str = '' 
    for char in encoded_str:
        decoded_char = chr(((ord(char) ^ key) - key) % 256)
        decoded_str += decoded_char
    return decoded_str


with open("Untitled-1.py", "r") as file:
    print ("wilighili = \"\"\"")
    for line in file:
        print("".join([chr(ord(s) + 2) for s in line]))
    print ("\"\"\"")
    
    
    print("exec(\"\".join([chr(ord(s) - 2) for s in wilighili]))")

Decode("")