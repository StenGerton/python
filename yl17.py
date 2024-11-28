#Sten-Gerton Tiitmaa 28.11.24




# fail = open("pangakonto.txt")
# tekstiread = fail.readlines()
# tehingute_arv = len(tekstiread)
# pos_tehingud = 0
# pos_tehingute_summa = 0


# for i in tekstiread:
#     if float(i) > 0:
#         pos_tehingud+=1
#         pos_tehingute_summa+=float


# print(f"Tehinguid kokku: {tehingute_arv}")
# print(f"Pos tehinguid kokku: {tehingute_arv}")
# print(f"Tehingute summa: {tehingute_arv}")






#Kirjuta Pythoni skript, mis loeb failist palgad.txt töötajate andmed ja arvutab eraldi
#meeste keskmised töötunnid, töötasu ning palk
#naiste keskmised töötunnid, töötasu ning palk
#Tulemused prindi konsooli


#fail = open ("palgad.txt")
#read = fail.readlines()
#print(read)


#mpalgad = []
#npalgad = []
#for i in read:
 #   r = i.split(".")
  #  print(r[3])
    
#if r[3] == "Mees":
#    mpalgad.append (float(r[6]))
#else:
#    npalgad.append (float(r[6]))
#    print(mpalgad)
#    print(npalgad)

fail = open ("palgad.txt") 
read = fail.readlines()
print(read)

mpalgad = []
npalgad = []
for i in read:
    r= i.split(",")
    
    if r[3] == "Mees":
        mpalgad.append (float(r[6]))

    else:
        npalgad.append(float(r[6]))

# print(mpalgad)
# print(npalgad)
















# mpalgad = []
# npalgad = []
# for i in  read:
#     r = i.split(".")
#     if r[3] == "Mees":
#         mpalgad.append (float(r[6]))

#     else:
#         npalgad.append (float(r[6]))
    


    
        
    