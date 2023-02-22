import random
import pickle
import os
import json

print("version_name = a0.3_1602 | Time worked on : 8h \n")

# Get the absolute path of the current Python script
python_file_dir = os.path.dirname(os.path.abspath(__file__))

# Create a relative file path to the pickle file
pickle_count_path = os.path.join(python_file_dir, "Data/count.pickle")
pickle_random_int_path = os.path.join(python_file_dir, "Data/random_int.pickle")
proposition_input_path = os.path.join(python_file_dir, "Data/proposition_input.pickle")

class StartGame():

    def __init__(self, proposition, X, Y):
        self.proposition = proposition
        self.X = X
        self.Y = Y
        #générer le nombre a trouver entre X et Y
        try:
            random_int = random.randint(X, Y)
            self.random_int = random_int
        except ValueError:
            pass
        except TypeError:
            pass

    #check is les paramètres de StartGame() sont des ints positifs et si proposition est entre X et Y
    def Debug_game_var(self):

        #si allow_game = True, alors Game() pourra s'executer
        allow_game = True

        #faire en sorte que Y soit uniquement un INT
        if type(self.proposition) != int:
            print("Please make your proposition a integrer")
            allow_game = False

        #faire en sorte que Y soit uniquement un INT
        if type(self.X) != int:
            print("Please make X a integrer")
            allow_game = False

        #faire en sorte que Y soit uniquement un INT
        if type(self.Y) != int:
            print("Please make Y a integrer")
            allow_game = False

        #faire en sorte que X doit toujours être en dessous de Y
        if type(self.X) == int:
            if type(self.Y) == int:
                if self.X > self.Y:
                    print("Please make X inferior to Y")
                    allow_game = False

        #faire en sorte que X ne doit pas être égal à Y
        if self.X == self.Y:
            print("Please make X a different value from Y")
            allow_game = False

        #faire en sorte que la proposition soit entre X et Y
        try:
            if self.proposition not in range(self.X, self.Y + 1):
                print(f"{self.proposition} is not between X and Y")
                allow_game = False
        except TypeError:
            pass
        except ValueError:
            pass

        #faire en sorte que les paramètres de la variable d'instance game_var soient tous positifs
        try:
            for i in [self.proposition, self.X, self.Y]:
                if i > 0:
                    continue
                else:
                    print(f"Please make {i} a positive number")
                    allow_game = False
        except TypeError:
            pass
        
        #actualisation finale de la variable d'instance allow_game
        self.allow_game = allow_game

    def Game(self):
        #on load le fichier pickle
        try:
            with open(pickle_random_int_path, "rb") as f:
                pickle_random = pickle.load(f)

                #comparer le nombre a trouver avec celui exporté par pickle
                if self.proposition == pickle_random:

                    #si il correspond, print résultat positif et reset du int dans le pickle
                    print(f"Congratulations, you found the right number, {pickle_random} !")
                    print("The guessing number will be re-generated next time!")
                    self.win = True

                    #reset du random int dans le pickle
                    with open(pickle_random_int_path, "wb") as f:
                        pickle.dump(self.random_int, f)

                #else print résultat negatif
                else:
                    print(f"# Your guess is {self.proposition}                        #\n# Sadly, you didn't found it...          #\n#                                        #")
                    self.win = False

        #si le fichier pickle n'existe pas, alors on le créee.
        except FileNotFoundError:

            with open(pickle_random_int_path, "wb") as f:
                pickle.dump(game_var.random_int, f)
                print(f"The setup has finished, please restart one time")

    #Debug auto si changement de X ou Y ou si pickle ne correspond pas a range(X, Y + 1)
    def Debug_pickle(self):
        try:
            with open(pickle_random_int_path, "rb") as f:
                pickle_random = pickle.load(f)


                if pickle_random not in range(self.X, self.Y + 1, 1):
                    if pickle_random != self.random_int:

                        print(f"The number to guess is not between {self.X} and {self.Y}, resetting...")
                        with open(pickle_random_int_path, "wb") as f:
                            pickle.dump(game_var.random_int, f)

                if pickle_random == self.random_int:

                    with open(pickle_random_int_path, "wb") as f:
                        pickle.dump(game_var.random_int, f)

        except FileNotFoundError:
            pass

    #Pour pouvoir output le int random de random et celui stocké dans pickle
    def Cheat(self, activate=False):
        if activate == True:

            print(f"DEBUG : random_int = {self.random_int}")
            try:
                with open(pickle_random_int_path, "rb") as f:
                    pickle_random = pickle.load(f)
                    print(f"DEBUG: pickle_random = {pickle_random}")
            except FileNotFoundError:
                print("DEBUG: La variable pickle pickle_random n'existe pas")

        if activate not in [True, False]:
            print(f"{activate} is not egal to True or False, please correct the input argument of Cheat()")
        else:
            pass
        
    #rendre impossible le fait de générer deux même nombres aléatoire de suite
    def Cant_be_the_same(self, activate=True):
        if activate == True:

            try:          
                with open(pickle_random_int_path, "rb") as f:
                    pickle_random = pickle.load(f)
                    while pickle_random == self.random_int:
                        self.random_int = random.randint(self.X, self.Y)
            except FileNotFoundError:
                pass

    #mettre en place un système d'indice : f - proposition dans un read pickle -------------------
    def Hint(self):
        pass

    #mise en place du compteur d'essais
    def Count(self):                

        #load le count ou créer le self.dict_count si il n'existe pas, dans le fichier pickle
        try: 
            with open(pickle_count_path, "rb") as f:
                self.dict_count = pickle.load(f)
        except FileNotFoundError:
            self.dict_count = {}
            self.dict_count["count"] = -1

        #update le dict du count
        self.dict_count["count"] += 1

        #save le dict dans le fichier pickle
        with open(pickle_count_path, "wb") as f:
            pickle.dump(self.dict_count, f)

        #correction de l'erreur lors du premier lancement
        try:
            
            #f-strings count au singulier/pluriel
            if self.win == False:
                if self.dict_count['count'] in range(2):
                    print(f"# Your total number of attempt is {self.dict_count['count']}     #")
                else:
                    print(f"# Your total number of attempt is {self.dict_count['count']}     #")

            if self.win == True:
                #reset du count
                self.dict_count['count'] = 0
                with open(pickle_count_path, "wb") as f:
                    pickle.dump(self.dict_count, f)
        
        except AttributeError:
            pass

    #sauvegarder le guess_int dans pickle
    def Save_proposition_input(self):

            with open(proposition_input_path, "wb") as f:
                pickle.dump(self.proposition, f)

#find the proposition between X and Y ! (need to start it 2 times if playing for very first time) ----------------------------------------------------
X = 1
Y = 100
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#essayer de faire en sorte de faire une boucle while qui fait que tant que proposition est pas égale a random alors on continue 
#with open(proposition_input_path, "rb") as f:
#    pickle_P = pickle.load(f)
#    with open(pickle_random_int_path, "rb") as f:
#        pickle_random = pickle.load(f)
#        while pickle_P != pickle_random:

print("##########################################")
print(f"########### X = {X} ##### Y = {Y} ##########")
#recupération input() et le random dans pickle

try:
    with open(proposition_input_path, "rb") as f:
        pickle_P = pickle.load(f)
        with open(pickle_random_int_path, "rb") as f:
            pickle_random = pickle.load(f)

            #print(f"DEBUG: pickle_P = {pickle_P}")
            #print(f"DEBUG: pickle_random = {pickle_random}")
            #si pickle_P est supérieur a pickle_random alors ↑ sinon ↓
            if pickle_P < pickle_random:
                print(f"################ Hint : ↑ ################")
            if pickle_P > pickle_random:
                print(f"################ Hint : ↓ ################")

except FileNotFoundError:
    pass

guess_str = input("> ")

try:
    guess_int = int(guess_str)
except ValueError:
    guess_int = guess_str

game_var = StartGame(
    proposition= guess_int,
    X= X,
    Y= Y
    ) 



#empêche de créer des erreurs d'input utilisateur
game_var.Debug_game_var()
#check si les variables de StartGame() sont OK; si oui, les parties du programme s'executent
# (allow_game est une self.variable de Debug_game_var)
if game_var.allow_game == True:

    #empêche de créer des erreurs lié au fichier pickle
    game_var.Debug_pickle()

    #fait en sorte que le chiffre a trouver ne soit jamais deux fois le même
    game_var.Cant_be_the_same(
    activate=True
    )

    #Debug mode console
    game_var.Cheat(
    activate=False
    )

    #lance le jeu
    game_var.Game()

    #count
    game_var.Count()

    #sauvegarde input utilisateur dans pickle
    game_var.Save_proposition_input()

print("##########################################")

#------------------------ 
#faire le hint (ptetre pas valable en dessous de Y - X = 5 un truc comme ça (et exemple : si tu es a moins de 5 (formule a définir) du chiffre a trouver tu es "chaud" )
#apprendre a executer ce programme en bash avec un input utilisateur pour la proposition
# et peut-être des variables a utiliser pour changer X et Y au lieu de devoir game_var = (X, Y) (sinon pas de soucis, tu gères quand même)

# idée incroyable : imaginer une forme géométrique composé de chiffres un peu a la manière du morpion; autour de chaque chiffre entre X et Y il y a un carré (représentées dans l'ordre)
# il y a plusieurs symboles autour du chiffre proposé, un peu a la manière de minesweeper
#------------------------