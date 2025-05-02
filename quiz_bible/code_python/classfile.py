import json

import random
import os
from abc import ABC, abstractmethod


class Prototype(ABC):
    
    pass




class Files:
    
    def __init__(self, file_name: str, directory: str):
        
        self.file_name = file_name
        
        self.directory = directory
        
    
    def loading(self):
        
        os.chdir(self.directory)
        
        if os.path.isfile(self.file_name):
            
            with open(self.file_name, "r") as file:
                
                return json.load(file)
            
            return []
    
    
    def saving(self, data):
        
        datastock = self.loading()        

class Livres(Files):

        def __init__(self, file_name, directory):
            
            super().__init__(file_name, directory)
            
            self.__data_livre = str()
              
            self.__livre = str()
              
            self.__auteur = str()
              
            self.__chapitre = int()
              
            self.__resusme = str()
              
            self.__questions = list()
              
              
        def recover(self):
            
            
            self.__data_livre = self.loading()
            
            self.__livre = self.__data_livre.get("livre")
      
            self.__auteur = self.__data_livre.get("auteur")
            
            self.__chapitre = self.__data_livre.get("chapitres")
            
            self.__resusme = self.__data_livre.get("resume")
            
            self.__questions = self.__data_livre.get("questions")

            return self.__questions
        
        
        def show(self):
            
            self.recover()
            
            print()
            
            print(f"Livre: {self.__livre}")
            
            print()
            
            print(f"Auteur: {self.__auteur}")
            
            print()
            
            print(f"Nombre de Chapitres: {self.__chapitre}")
            
            print()
            
            print(f"Resumé: {self.__resusme}")
            
            print()




class Question(Livres):
    
    def __init__(self, file_name, directory):
        super().__init__(file_name, directory)
        
        
        self.__questions = ""
        
        self.__choix = ""
        
        self.__reponse = ""
        
        self.__explication = ""
        
        self.__reference = ""
        
        self.__lenght = 0
        
        self.__conter = 0
        
        self.__index = 0
        
        self.__score = 0
        
    def recover(self):
        
        return super().recover()
        
         

    def show(self):
        return super().show()
    
    
    def blend(self):
        
        self.__questions = self.recover()
        
        random.shuffle(self.__questions)
        

    def start(self):
        
        self.blend()
        
        
        self.__lenght =  len(self.__questions)
        
        
        while  self.__index < self.__lenght:
                
                self.__conter += 1
                        
                print()
                
                print(f"{self.__conter}.{self.__questions[self.__index].get("question")}")
                
                print()
                
                self.__choix = self.__questions[self.__index].get("choix")
                
                self.__reponse = self.__questions[self.__index].get("reponse")
                
                self.__explication = self.__questions[self.__index].get("explication")
                
                self.__reference = self.__questions[self.__index].get("reference")
                
                for choi in self.__choix:
                    
                    print(choi)
                
                print()
                
                try:
                    
                       
                    reponse = int(input("Entrez votre Reponse: "))
                
                except Exception as err:
                    
                    print(err)
                    self.stop()
                
                if reponse == self.__reponse:

                        self.__score += 1
                        
                        print()
                        
                        print("Bravo!, bien joué.\nScore: {}".format(self.__score))
                        
                        print()
                        
                        print(f"Référence: {self.__reference}")
                        
                        print()
                        
                        print(f"Explication: {self.__explication}")
                        
                        print()
                        
                else:
                    
                    print()
                    
                    print("Oups! mauvaise réponse.\nScore: {}".format(self.__score))
                    
                         
                    
                self.__index += 1 
    
    
    def stop(self):
        
        return exit(1) 
     
        
question = Question("genese.json", "/home/joel/Bureau/.projets_perso/GAME/quiz_bible/data")

question.start()

question.stop()