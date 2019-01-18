import pandas as pd

lines = open(r'phenylalanine.mol').readlines()
Nlist = [[],[],[]]
Dict = dict()
c = 1

for line in lines:
    if len(line.split()) == 7:
        Nlist[0].append(int(line.split()[0]))
        Nlist[1].append(int(line.split()[1]))
        Nlist[2].append(int(line.split()[2]))
    if len(line.split()) == 16:
        Dict[c] = line.split()[3]
        c += 1

df1 = pd.DataFrame(
        {'Atom1' : Nlist[0],
         'Atom2' :  Nlist[1],
         'Bonds' : Nlist[2],
         }
     )
df2 = pd.DataFrame(
        {'Atom1' : Nlist[1],
         'Atom2' :  Nlist[0],
         'Bonds' : Nlist[2],
         }
     )
     
df = pd.concat([df1, df2])
I = df.groupby(['Atom1']).sum()

while 1 in I.Bonds or 2 in I.Bonds:

    L =list(I.Bonds[I.Bonds == 1].index)
    K =list(I.Bonds[I.Bonds == 2].index)
    for ind in K:
        if Dict[ind] == 'O':
            L.append(ind)
            
    if len(L) == 0:
        break
    for idx in L:
        df = df[df.Atom1 != idx]
        df = df[df.Atom2 != idx]    
    I = df.groupby(['Atom1']).sum()        

if len(I.Bonds) == 0:
    print '\n                 ..: The Compound has no ring :..'
else:
    print '\n                 ..: The Compound has at least one ring :..\nElements  Degree'
for a in I.Bonds.index:
    print '  ', Dict[a],'      ', I.Bonds[a]
