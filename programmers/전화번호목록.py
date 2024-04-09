def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
        #     return False
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

def solution2(phone_book):
    hash_table = {}
    
    for phone_num in phone_book:
        hash_table[phone_num] = 1
    
    for phone_num in phone_book:
        temp = ""
        for num in phone_num:
            temp += num
            if temp in hash_table and temp != phone_num:
                return False
            
    return True
