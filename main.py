#Kalkulaatori loomine Karl Paju IS22
import math # Mathi importimine

class Kalkulaator: # Kalkulaatori klass
    def __init__(self):  # init meetodi kasutamine
        pass

    def liitmine(self, a, b): # defineeritud funktsioon liitmine klassi sees
        return float(a + b) # väljastab tehte.

    def lahutamine(self, a, b): # defineeritud funktsioon lahutamine klassi sees
        return float(a - b)# väljastab tehte.

    def korrutamine(self, a, b): # defineeritud funktsioon korrutamine klassi sees
        return float(a * b)# väljastab tehte.

    def jagamine(self, a, b): # defineeritud funktsioon jagamine klassi sees
        if b == 0: # if käsk, et näha kas b on võrdne nulliga (tõene)
            print("Ei saa jagada nulliga") #Print käsk mis väljastab "ei saa jagada nulliga" kui tegemist on tehtega, kus jagatakse nulliga.
        return float(a / b)

    def astendamine(self, a,b): # astendab sisestatud arvu
        return float(a ** b) #tagastab astendatud arvu.

    def ymardamine(self,a): #ümardab sisestatud arvu.
        if a == 0: # kui a on väärt 0 läheb kood edasi if-ile ning väljastab veakoodi print käsu abil
            print("Arvu ei ole võimalik ümardada") # print käsi
        return (round(a)) # tagastab ümardatud arvu.

    def ruutjuur(self,a): # leiab sisestatud arvu ruutjuure
        if a == 0: # kui a on väärt 0 läheb kood edasi if-ile ning väljastab veakoodi print käsu abil
            print("Sisestatud arvul ei ole võimalik leida ruutjuurt") # prindib välja veakoodi.
        return(math.sqrt(a)) # tagastab ümardatud arvu

kalk = Kalkulaator() # tegemist on objektiga, mis pärib kõik Kalkulaatori omadused.



