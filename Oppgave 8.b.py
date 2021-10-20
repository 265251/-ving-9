# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:33:32 2021

@author: rklei
"""

class quiz:
     def __init__(self, sporsmal, svar, rettsvar):
          self.sporsmal= sporsmal
          self.svar = svar
          self.rettsvar = rettsvar
          
          
     def brukersjekk(self, brukersvar):
         if brukersvar == self.rettsvar:
            print("Du svarte riktig")
         else:
            print("Svaret var ikke riktig")
          

     def __str__(self):
         svartekst = ""
         for svar in self.svar:
             svartekst +=svar +"\n"
         return f"{self.sporsmal} \n{svartekst}"

a = quiz("Hva er UIS forkortelsen for?", ["1. Ullrigg", "2. Universitetet i Stavanger", "3. Ullanhaug"], 2)
b = quiz("Hva er spørsmålet?", ["1. alternativ 1", "2. alternativ 2", "3. alternativ 3"], 3)
print(a)
brukersvar = int(input("Hvilket svaralternativ er riktig #1-3?  "))
a.brukersjekk(brukersvar)
print(b)
brukersvarb = int(input("Hvilket svaralternativ er riktig #1-3?  "))
b.brukersjekk(brukersvarb)
#def run_quiz(sporsmal):
#     score = 0
#     for question in questions:
#          answer = input(question.prompt)
#          if answer == question.answer:
#               score += 1
#     print("Du klarte", score, "av", len(questions))

#run_quiz(questions)