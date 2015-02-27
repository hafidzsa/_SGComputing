from random import randint

ind_1 = "101010"
ind_2 = "100100"
key   = "".join(str(randint(0,1)) for i in range(len(ind_1)))
tuker = {'0':'1','1':'0'}

def berubah(s,k):
    tmp = []
    for a,b in zip(s,k):
        tmp.append(str(int(a)^int(b)))
    return "".join(tmp)

new_ind_1 = berubah(ind_1,key)
new_ind_2 = berubah(ind_2,key)

print key,new_ind_1,new_ind_2
