def swap_case(s):
    string = ""
    for i in s:
        if i.isupper() == True:
            i = i.lower()
        else:
            i = i.upper()
    return


s = input()
result = swap_case(s)
print(result)