from bintreeFile import Bintree

def svenska():
    svenska = Bintree()
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end = " ") 
            else:
                svenska.put(ordet)             # in i sökträdet
    print("\n")
    return svenska

def character_removal(str_in):
    '''Rensar ingående sträng från oönskade tecken'''
    unwanted_characters = ",\"'.!"
    table = str.maketrans("", "", unwanted_characters)
    str_out = str_in.translate(table)
    return str_out


def engelska(svenska):
    '''Skapar ett träd för de engelska orden, 
    och jämför med givet svenskt träd'''
    engelska = Bintree()
    with open("engelska.txt", "r", encoding = "utf-8") as eng_fil:
        for rad in eng_fil:
            rad_lst = rad.strip().split()
            for ord in rad_lst:
                ordet = remove_chars(ord)
                if ordet in engelska:
                    pass
                else:
                    if ordet in svenska:
                        print(ordet, end= " ")
                    engelska.put(ordet)
    print("\n")
                


if __name__ == "__main__":
    engelska(svenska())
