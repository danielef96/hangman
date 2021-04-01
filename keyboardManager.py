from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import emoji

class KeyboardManager():
    def __init__(self, *args, **kwargs):
        super(KeyboardManager, self).__init__(*args, **kwargs)
        # variabili globali
        self.keyboard1 = [[KeyboardButton(text="Q"), KeyboardButton(text="W"), KeyboardButton(text="E"),
              KeyboardButton(text="R"), KeyboardButton(text="T"), KeyboardButton(text="Y"),
              KeyboardButton(text="U"), KeyboardButton(text="I"), KeyboardButton(text="O"),
              KeyboardButton(text="P")],
             [KeyboardButton(text="A"), KeyboardButton(text="S"), KeyboardButton(text="D"),
              KeyboardButton(text="F"), KeyboardButton(text="G"), KeyboardButton(text="H"),
              KeyboardButton(text="J"), KeyboardButton(text="K"), KeyboardButton(text="L")],
             [KeyboardButton(text="Z"), KeyboardButton(text="X"), KeyboardButton(text="C"),
              KeyboardButton(text="V"), KeyboardButton(text="B"), KeyboardButton(text="N"),
              KeyboardButton(text="M")]
             ]

        self.keyboard2 = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                     ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
                     ["Z", "X", "C", "V", "B", "N", "M"]]

        self.characters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
                     "A", "S", "D", "F", "G", "H", "J", "K", "L",
                     "Z", "X", "C", "V", "B", "N", "M"]

    def getKeyboard(self, character):
        # Verifica se il carattere è ammesso
        error = False
        if(self.checkCharacter(chosenCharacter=character)):
            # cerca il carattere da sostituire
            a, b = self.searchElement(searchingCharacter=character)
            #  se trova il carattere lo sostituisce, altrimenti restituisce errore
            if a != None :
                self.keyboard1[a][b]= KeyboardButton(text=emoji.emojize(":x:", use_aliases=True))
        # se il carattere è "" allora si è nel caso in cui non si deve sostituire nulla
        elif character != "":
            error = True
        return ReplyKeyboardMarkup(keyboard=self.keyboard1), error

    def reactivateKeyboard(self):
        for i,line in enumerate(self.keyboard2):
            for j,elem in enumerate(line):
                self.keyboard1[i][j] = KeyboardButton(text=elem)
        return ReplyKeyboardMarkup(keyboard=self.keyboard1)

    # Se viene restituita la coppia (None, None), allora la lettera non esiste o è già stata premuta
    def searchElement(self, searchingCharacter):
        for i,line in enumerate(self.keyboard1):
            for j,elem in enumerate(line):
                if elem == KeyboardButton(text=searchingCharacter):
                    return (i, j)
        return (None, None)

    def checkCharacter(self, chosenCharacter):
        return chosenCharacter in self.characters

    def hideKeyboard(self):
        return ReplyKeyboardRemove(remove_keyboard=True)