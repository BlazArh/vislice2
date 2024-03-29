import random


STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'


class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke    #spreminjamo tudi seznam iz 'zunanjega' sveta


    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        vse_crke = True
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                pass
            else:
                vse_crke = False
                break
        return vse_crke and STEVILO_DOVOLJENIH_NAPAK >= self.stevilo_napak()

    # na kratko: vse crke = all[crka in self.crke for crka in self.geslo]
    # all nam da True takrat ko so True vsi 

    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK < self.stevilo_napak()

    def pravilni_del_gesla(self):
        rezultat = ''
        ugibanje = [crka.upper() for crka in self.crke]
        for crka in self.geslo:
            if crka.upper() in ugibanje:
                rezultat += crka + ' '
            else:
                rezultat += '_ '
        return rezultat.strip()       # strip se znebi zadnega presledka


    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

            
with open('Vislice/besede.txt', 'r', encoding='UTF-8') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]




def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])


# testno_geslo = 'DEŽUJE'
# testne_crke = ['A', 'I', 'O', 'U', 'D', 'J','K']
# igra = Igra(testno_geslo, testne_crke)

    




