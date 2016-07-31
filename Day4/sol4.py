import hashlib
text = "yzbqklnj"
no_zeros = 6 # or 6 in part 2
i=1

while True:
    is_code = text + str(i)
    # peform the MD5 hash
    m = hashlib.md5(is_code.encode('utf-8'))
    check = m.hexdigest()
    # check if 5 leading zeros
    check_string = str(0)*no_zeros
    if check[0:no_zeros] == check_string:
        break
    else:
        i += 1

print("Lowest Number:",i)