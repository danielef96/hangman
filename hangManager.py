import emoji

class HangManager():
    def __init__(self, *args, **kwargs):
        super(HangManager, self).__init__(*args, **kwargs)
        # Variabili Globali
        self.nErrors = 0
        # Parti del disegno dell'impiccato
        self.base = "|_____\n|_____\ "
        self.error1 = "____\n"
        self.error2 = "|    |\n"
        self.error3 = "|    :sweat_smile: \n"
        self.error4 = "|       \ \n"
        self.error5 = "|    / \ \n"
        self.error6 = "|    /|\ \n"
        self.error7 = "|     \n"
        self.error8 = "|    :skull: \n"

    # Inizializza a zero il numero di errori
    def initError(self):
        # Permette di considerare da qui in poi la variable globale nErrors
        self.nErrors = 0

    # Disegna l'impiccato
    def draw(self):
        # Il disegno è diviso in due parti per permettere
        # la modifica della sola parte centrale
        # Parte bassa del disegno
        bottom = ""
        # Parte alta del disegno
        top = ""
        if self.nErrors >= 1:
            bottom = "|\n|\n|\n|\n" + self.base
        if self.nErrors >= 2:
            top = self.error1
        if self.nErrors >= 3:
            top = self.error1 + self.error2
            bottom = self.base
        if self.nErrors == 3:
            top += self.error7 + self.error7
        if self.nErrors >= 4:
            if self.nErrors != 9:
                top = top + emoji.emojize(self.error3, use_aliases=True)
            else:
                top = top + emoji.emojize(self.error8, use_aliases=True)
            bottom = self.base
        if self.nErrors == 5:
            top = top + self.error4
        if self.nErrors == 6:
            top = top + self.error5
        if self.nErrors >= 7:
            top= top + self.error6
        if self.nErrors == 8:
            top = top + self.error4
        if self.nErrors >= 9:
            top = top + self.error5
        return top + bottom

    def error(self):
        # Incrementa il numero degli errori
        self.nErrors += 1
        # Ritorna due elementi:
        # 1_ se il giocatore è arrivato al numero massimo di errori
        # 2_ il disegno dell'impiccato
        if self.nErrors == 9:
            return True, self.draw()
        else:
            return False, self.draw()