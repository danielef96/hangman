class PlayerManager():
    def __init__(self, *args, **kwargs):
        super(PlayerManager, self).__init__(*args, **kwargs)
        self.file="player.txt"

    def aggiungiPlayer(self, namePlayer):
        infile = open(self.file, 'a')
        infile.write('\n'+str(namePlayer))
        infile.close()

    def nPlayer(self):
        chatId = []
        infile = open(self.file)
        infile.readline()
        n = 0
        line = infile.readline()
        while line != "":
            if line not in chatId:
                n += 1
                chatId.append(line)
            line = infile.readline()
        infile.close()
        # Aggiorno il file
        self.scriviLista(chatId)
        return "Numero di utenti che hanno usato il nostro Hangman è " + str(n)

    def scriviLista(self, lista):
        infile = open(self.file, 'w')
        #Inserisco la prima riga di descrizione
        infile.write("FirstName degli utenti che hanno giocato almeno una volta HANGMAN:\n")
        for elem in lista:
            infile.write(elem)
        infile.close()
