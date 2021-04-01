from random import randint
#Gestore del file con le parole
import dictionaryOrganizer as dO
import emoji

class WordManager():
    def __init__(self, *args, **kwargs):
        super(WordManager, self).__init__(*args, **kwargs)
        # Variabili globali
        self.fileWords = "word.txt"
        self.hiddenWord = ""
        self.underscoredWord = ""
        self.finished = False

    def newWord(self):
        n = dO.nLines(self.fileWords)
        #Genero un numero casuale che indentifica la parola
        n_word = randint(1, n)
        #Ricavo la parola nascosta
        self.hiddenWord = dO.getWord(self.fileWords, n_word)
        #Genero la stringa con i trattini
        #print(hiddenWord)
        #imposto la variabile con i trattini
        self.underscoredWord = emoji.emojize(':heavy_minus_sign: ') * self.getLen()
        return self.underscoredWord

    def getHiddenWord(self):
        if self.hiddenWord != "":
            return self.hiddenWord
        else:
            self.newWord()
            return self.hiddenWord

    def getUnderscoredWord(self):
        if self.underscoredWord != "":
            return self.underscoredWord
        else:
            return self.newWord()

    def getLen(self):
        return len(self.hiddenWord)-1

    def replace(self, attempt):
        found = False
        new = ""
        # Verifica se è stata individuata la parola
        self.finished = True
        for i, character in enumerate(self.hiddenWord):
            # Elimina gli spazi
            if character != "\n" and self.underscoredWord[i] == " ":
                i += 1
            if character.upper() == attempt:
                new += attempt
                found = True
            # Verifica se il giocatore ha vinto
            elif character != "\n" and self.underscoredWord[i] == emoji.emojize(':heavy_minus_sign:'):
                new += emoji.emojize(":heavy_minus_sign:")
                self.finished = False
            elif character != "\n":
                new += self.underscoredWord[i]
        self.underscoredWord = new
        return found

    def isFinished(self):
        return self.finished