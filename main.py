import sys
ds = []
h = int(input("nhap so hang cho tau:"))
c = int(input("nhap so cot cho tau:"))
print()
for i in range(h):
    for j in range(c):
        print("_", end = " ")
    print()
s = 1
def dat_cho_ngoi():
    global ds
    h1 = int(input("nhap so hang dat cho:"))
    c1 = int(input("nhap so cot dat cho:"))
    if (h1 > h or c1 > c) or (h1 <= 0 or c1 <= 0):
        print("cho ngoi khong ton tai")
        print("so do cho sau khi dat:")
        print()
    elif (h1 - 1, c1 - 1) in ds:
        print("cho da duoc dat")
        print("so do cho sau khi dat:")
    else:
        ds.append((h1 - 1, c1 - 1))
    for i in range(h):
        for j in range(c):
            if (i, j) in ds:
                print("X", end = " ")
            else:
                print("_", end = " ")
        print()
    print("so cho con lai:" + str(h * c - len(ds)))
    print()

def xem_cho_ngoi():
    for i in range(h):
        for j in range(c):
            if (i, j) in ds:
                print("X", end = " ")
            else:
                print("_", end = " ")
        print()
    print("so cho con lai:" + str(h * c - len(ds)))    

def chon():
    try:
        d = int(input("chon chuc nang:"))
        return(d)
    except ValueError:
        print("khong hop le")
        return(4)
    
def kiem_tra(d):
    match d:
        case 1:
            dat_cho_ngoi()
        case 2:
            xem_cho_ngoi()
        case 3:
            print("cam on ban va tam biet!")
            sys.exit()
        case _:
            print("khong hop le")
            print()


while s == 1:
    print("1.Dat cho ngoi")
    print("2.Xem cho ngoi")
    print("3.Thoat")
    print()
    kiem_tra(chon())
    if s == 1:
        print("1.Dat cho ngoi")
        print("2.Xem cho ngoi")
        print("3.Thoat")
        print()
        kiem_tra(chon())


