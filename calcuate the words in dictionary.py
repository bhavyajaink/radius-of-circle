s="M i s s i s s i p p i"
dt=dict()
rs=s.rstrip()
sp=rs.split()
for word in sp:
    dt[word]=dt.get(word,0)+1
for k,v in dt.items():
    print(k,"=",v)
