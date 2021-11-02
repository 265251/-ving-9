# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:33:32 2021

@author: rklei
"""

fila = open("sporsmaalsfil.txt", "r", encoding="UTF8")

class Quiz:
     def __init__(self, sporsmal, rettsvar, svar):
          self.sporsmal= sporsmal
          self.rettsvar = rettsvar
          self.svar = svar
          
          
     def brukersjekk(self, brukersvar):
         if brukersvar == self.rettsvar:
             if brukersvar == True:
                 spillere[{i}] +=1
         else:
             return False
          

     def __str__(self):
         svartekst = ""
         for svar in self.svar:
             svartekst +=svar +"\n"
         return f"{self.sporsmal} \n{svartekst}"
     
    
     
spillere = dict()  
quizspor = []
for line in fila:
    line = line.strip()
    start = line.find("")
    slutt = line.find(":")
    spors = line[start:slutt]       
    start1 = line.find(":")
    slutt1 = line.find(":")
    svar = int(line[start1+2:slutt1+3])
    start2 = line.find("[")
    slutt2 = line.find("]")
    alt = line[start2+1:slutt2]
    alt = alt.split(", ")
    quiz1 = quizspor.append(Quiz(spors,svar,alt))
 
if __name__ == "__main__":
    antall_spillere = int(input("Antall spillere: "))
    for i in range(antall_spillere):
        navn = input(f"Navn til spiller {i+1}:")
        spillere[navn] = 0
    for object in (quizspor):
        for i in range(antall_spillere):
            print(object)
            object.brukersvar = int(input(f"Velg et svaralternativ {i+1}[spillere] :"))
            object.brukersjekk(object.brukersvar)
#        print(f"Korrekt svar var {object.self.svar[object.self.rettsvar]} :")
#        print()                                
    
#    vinnere = list()
#    vinnere.append(spillerne[0])
#    for spiller in spillerne:
#        if spiller == spillerne[0]:
#            continue
#        if spiller.kort.verdi > vinnere[0].kort.verdi:
#            vinnere.clear()
#            vinnere.append(spiller)
#        elif spiller.kort.verdi == vinnere[0].kort.verdi:
#            vinnere.append(spiller)
#    print("Vinnere:")
#    for spiller in vinnere:
#        print(f"{spiller.navn} har {spiller.kort}")
     
#
#b = quiz("Hva er spørsmålet?", ["1. alternativ 1", "2. alternativ 2", "3. alternativ 3"], 3)
#print(a)
#brukersvar = int(input("Hvilket svaralternativ er riktig #1-3?  "))
#a.brukersjekk(brukersvar)
#print(b)
#brukersvarb = int(input("Hvilket svaralternativ er riktig #1-3?  "))
#b.brukersjekk(brukersvarb)
#def run_quiz(sporsmal):
#     score = 0
#     for question in questions:
#          answer = input(question.prompt)
#          if answer == question.answer:
#               score += 1
#     print("Du klarte", score, "av", len(questions))
#
#run_quiz(questions)