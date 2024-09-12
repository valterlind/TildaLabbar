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

def remove_chars(str_in):
    '''Tar bort tecken från given sträng'''
    kar_att_ta_bort = ",\"'.!"
    översättningstabell = str.maketrans("", "", kar_att_ta_bort)
    str_ut = str_in.translate(översättningstabell)
    return str_ut


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
