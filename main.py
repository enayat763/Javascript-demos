word={
        1:"0", 2:"0", 3:"0", 4:"0", 5:"0", 6:"0", 7:"0", 8:"0", 9:"0",
    }


x="x"
z="y"
counter=set()
counta=[]
countb=[]
def cal(aa,user):
    for y in word.keys():
        if user=="player1":
            if int(y)==int(aa):
                word.update({y:x})
        elif user=="player2":
            if int(y)==int(aa):
                word.update({y:z})
    print(word[1], "**", word[2], "**" ,word[3])
    print(word[4], "**" ,word[5], "**" ,word[6])
    print(word[7], "**" ,word[8], "**" ,word[9],)

while True:
    ab=(word.get(1),word.get(2),word.get(3))
    ac=(word.get(1),word.get(5),word.get(9))
    ad=(word.get(1),word.get(4),word.get(7))
    ae=(word.get(2),word.get(5),word.get(8))
    af=(word.get(3),word.get(6),word.get(9))
    ag=(word.get(3),word.get(5),word.get(7))
    ah=(word.get(4),word.get(5),word.get(6))
    ai=(word.get(7),word.get(8),word.get(9))
    az=('x','x','x')
    ax=('y','y','y')
    if ab == az or ac==az or ad==az or ae==az or af==az or ag==az or ah==az or ai==az:
        print("player 1 has won")
        break
    else:
        if ab == ax or ac== ax or ad== ax or ae== ax or af== ax or ag== ax or ah== ax or ai== ax:
            print("player 2 has won")
            break
    while True:
        b = int(input("player1, choose a socket (1-9): "))
        if b not in counter:
            counter.add(b)
            cal(aa=b, user="player1")
            print(counter)
            break
        else:
            print("slot has been taken choose another ")
            continue

    while True:
        c = int(input("player2, choose a socket (1-9): "))
        if c not in counter:
            counter.add(c)
            cal(aa=c, user="player2")
            print(counter)
            break
        else:
            print("slot has been taken choose another ")
            continue
    continue


