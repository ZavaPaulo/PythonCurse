import telebot

CHAVE_API = "MINHA_CHAVE_API"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma das opção para continuar (Clique no item):
    /opcao1 Fazer pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraço para o autor
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)
bot.polling()

# Aula incompleta, terminar de ver
# A internet da UniFil, `computacaounifil` não permite o uso do telegram.