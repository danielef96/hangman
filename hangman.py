import telepot
import emoji
from telepot.loop import MessageLoop
import time
# Gestore della tastiera
import keyboardManager as kM
# Gestore della partita
import gameManager as gM
#Memorizza i chatId
import playerManager as pM
# Gestione Thread
from telepot.delegate import pave_event_space, per_chat_id, create_open

class Hangman(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Hangman, self).__init__(*args, **kwargs)
        self.kManager = kM.KeyboardManager()
        self.gManager = gM.GameManager()
        self.pManager = pM.PlayerManager()
        print(args)
        self.pManager.aggiungiPlayer(args[0][1]['from']['first_name'])

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(msg)
        # Verifica se il campo testo è presente
        if 'text' in msg:
            command = msg['text']
            if command == '/start' or command == '/start@fierino_bot':
                msg = emoji.emojize("Benvenuto in questo fierissimo Bot "
                                    "\nnato per opera di Baldi Umberto, "
                                    "\nFea Daniele e Gerbo Rosita!!"
                                    "\nSei pronto a rischiare la tua vita?"
                                    "\n\nQuesti sono i comandi che puoi utilizzare:"
                                    "\n/start - Per far partire il bot"
                                    "\n/newgame - Per iniziare una nuova partita"
                                    "\n/stop - Per terminare una partita in corso"
                                    "\n/credits - Per avere informazioni sui creatori"
                                    "\n\nBuon divertimento :skull:")
                bot.sendMessage(chat_id, msg, reply_markup=self.kManager.hideKeyboard())
            elif command == '/newgame' or command == '/newgame@fierino_bot':
                # Imposta la tastiera
                keyboard = self.kManager.reactivateKeyboard()
                word = self.gManager.start()
                bot.sendMessage(chat_id, "Indovina questa parola: \n" + word, reply_markup=keyboard)
            elif command == '/stop' or command == '/stop@fierino_bot':
                message1, message2 = self.gManager.analyseCharacter(command)
                if message1 == "Nessuna partita avviata!":
                    bot.sendMessage(chat_id, "Non ci sono partite avviate!", reply_markup=self.kManager.hideKeyboard())
                else:
                    self.gManager.stop()
                    bot.sendMessage(chat_id, "La partita è stata terminata", reply_markup=self.kManager.hideKeyboard())
            elif command == '/credits' or command == '/credits@fierino_bot':
                bot.sendMessage(chat_id, "Gioco creato da: ", reply_markup=self.kManager.hideKeyboard())
                bot.sendSticker(chat_id, "CAADBAAD7QQAAtz07wP_5L8lBZUxJgI")
                bot.sendMessage(chat_id,"Umberto Baldi")
                bot.sendSticker(chat_id, "CAADBAADzQQAAtz07wNF482NhupEswI")
                bot.sendMessage(chat_id, "Daniele Fea")
                bot.sendSticker(chat_id, "CAADBAAD6wQAAtz07wO7i3E-OPX8ZwI")
                bot.sendMessage(chat_id, "Rosita Gerbo")
            elif command == '/nPlayer':
                bot.sendMessage(chat_id, self.pManager.nPlayer())
            else:
                # Verifica se ci sono partite in corso
                if self.gManager.getStatus():
                    # Testa la funzione di sostituzione di KeyboardManager
                    keyboard, error = self.kManager.getKeyboard(command)
                    if error == False:
                        # Verifica se il carattere è nella parola nascosta
                        message1, message2 = self.gManager.analyseCharacter(command)
                    else:
                        message1 = "Ehhh Volevi!"
                        message2 = self.gManager.getUnderscoredWord() + "\nInserisci una lettera"
                    if self.gManager.getStatus():
                        # Primo messaggio senza tastiera
                        bot.sendMessage(chat_id, message1, reply_markup=keyboard)
                        # Secondo messaggio senza tastiera
                        bot.sendMessage(chat_id, message2, reply_markup=keyboard)
                    else:
                        # Quando la partita finisce la tastiera viene tolta
                        bot.sendMessage(chat_id, message1, reply_markup=self.kManager.hideKeyboard())
                        bot.sendMessage(chat_id, message2, reply_markup=self.kManager.hideKeyboard())
                        if message1 == "Complimenti!":
                            bot.sendSticker(chat_id, "CAADAgADywUAAvoLtghzjRVcMTrAdQI")
                        else:
                            bot.sendSticker(chat_id, "CAADAgADzwUAAvoLtghqW-jV47OCcgI")
                else:
                    bot.sendMessage(chat_id, "Non ci sono partite avviate!", reply_markup=self.kManager.hideKeyboard())
        else:
            # Gestisce il caso di ricezione di messaggi senza testo
            bot.sendSticker(chat_id,"CAADBAAD5QQAAtz07wNi4h5bfhpFhQI")

#TOKEN = "319468489:AAFAQTMKLweXD-dVe0vY_pP8-3hqfO0YPWU"
TOKEN = "182773190:AAGDU1sPWgHVhE8RcXgnKphAybTDwTlkpPM"
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, Hangman, timeout=120),
])
MessageLoop(bot).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)