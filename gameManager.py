import wordManager as wM
import hangManager as hM

class GameManager():
    def __init__(self, *args, **kwargs):
        super(GameManager, self).__init__(*args, **kwargs)
        # Variabili Globali
        self.startedGame = False
        self.hManager = hM.HangManager()
        self.wManager = wM.WordManager()

    def start(self):
        # Inizializza il modulo di gestione degli errori
        self.hManager.initError()
        # Viene generata la parola
        hidden = self.wManager.newWord()
        # Segnala che una partita è avviata
        self.startedGame = True
        return hidden

    def analyseCharacter(self, character):
        if self.startedGame:
            if self.wManager.replace(character):
                # Verifica se la parola è stata indovinata
                if self.wManager.isFinished():
                    # Segnala che la partita è terminata
                    self.startedGame = False
                    # Il primo parametro è True se si deve richiamare l'impiccato
                    return "Complimenti!", "Hai indovinato la parola: \n"+ self.wManager.getHiddenWord().upper()
                else:
                    return "La lettera è presente!", self.wManager.getUnderscoredWord().upper() + "\nInserisci una lettera:"
            else:
                # Verifica se si è raggiunto il numero massimo di errori
                lost, hanged = self.hManager.error()
                if lost:
                    self.startedGame = False
                    return hanged, "Hai perso! La parola era \n" + (self.wManager.getHiddenWord()).upper()
                else:
                    return hanged, "Carattere non trovato! \n" + self.wManager.getUnderscoredWord() + "\nInserisci una lettera:"
        return "Nessuna partita avviata!", "Nessuna partita avviata!"

    def getUnderscoredWord(self):
        if self.startedGame:
            return self.wManager.getUnderscoredWord()
        else:
            return "Nessuna partita avviata!"

    def getStatus(self):
        return self.startedGame

    def stop(self):
        self.startedGame = False