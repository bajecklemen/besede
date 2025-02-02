import random

def preberi_besede(ime_datoteke):
    besede = []
    with open(ime_datoteke, 'r', encoding='utf-8') as f:
        for vrstica in f:
            angleška, prevod = vrstica.strip().split(',')
            besede.append((angleška.strip(), prevod.strip()))
            besede.append((prevod.strip(), angleška.strip()))
    return besede

def kviz(besede, N):
    random.shuffle(besede)
    pravilni_odgovori = {}
    stevilo_pravilnih = 0
    skupno_vprasanj = 0
    
    while besede:
        beseda, prevod = random.choice(besede)
        
        odgovor = input(f"Kako se prevede --- {beseda}  ").strip().lower()
        pravilen_odgovor = prevod.lower()
        
        skupno_vprasanj += 1
        
        if odgovor == pravilen_odgovor:
            pravilni_odgovori[(beseda, prevod)] = pravilni_odgovori.get((beseda, prevod), 0) + 1
            stevilo_pravilnih += 1
            if pravilni_odgovori[(beseda, prevod)] >= N:
                besede.remove((beseda, prevod))
        else:
            print(f"Napačno!___________ {pravilen_odgovor}")
    procent = round(stevilo_pravilnih/skupno_vprasanj * 100,0)
    print(f"Kviz zaključen! Pravilni odgovori: {stevilo_pravilnih}/{skupno_vprasanj} - {procent}%")

if __name__ == "__main__":
    ime_datoteke = "besede.txt"  # Datoteka z besedami
    N = 1                   #Kolikokrat pravilno na vsaki besedi 
    besede = preberi_besede(ime_datoteke)
    kviz(besede, N)
    input('ZAPRI ... Enter')    
   
