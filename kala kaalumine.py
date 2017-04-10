def kala_kaal(pikkus,fti): #fti - tüsedusindeks
    kaal = (pikkus**3*fti)/100
    return int(round(kaal,0))
failiNimi = input("Sisesta faili nimi: ")
alamoot = input("Sisesta alamõõt: ")
fti = input("Sisesta Fultoni indeks: ")
with open(failiNimi,"r",encoding="utf-8") as inputfile:
    kaaluList = []
    for line in inputfile.readlines():
        if int(line.strip()) < int(alamoot):
            print ("Kala lasti vette tagasi")
        else:
            kaal = kala_kaal(int(line.strip()),float(fti))
            print ("Püütud kala kaaluga " + str(kaal) + " grammi")
            kaaluList.append(kaal)
    print ("Kõige raskem püütud kala: "+str(round(max(kaaluList)/1000,3)) + " kg")