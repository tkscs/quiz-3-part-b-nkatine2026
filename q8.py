#4 letter palindrome checker
def palindrome():
    pal = "miim"
    y = pal[0]
    x = pal[1]
    w = pal[2]
    z = pal[3]
    if y == z:
        if x == w:
            print("palindrome!")
            return True
        else:
            return False
    else:
        return False
palindrome() 

     