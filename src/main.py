from samples.calculator_sample import CalculadoraBot
from samples.notepad_semple import NotepadBot
from samples.fortinet_sample import FortineBot 



if __name__ == '__main__':

    _filename = 'file.txt'
    _filepath = 'C:\\Users\\jigor\\Desktop\\'
    _texto = 'Meu texto'

    bot = NotepadBot()
    bot.criar_arquivo(_texto, _filepath, _filename)

    bot = CalculadoraBot()
    bot.soma_positivo(1, 2)

    bot = FortineBot()
    bot.conectar_vpn(4, '106189', 'epm@4976')

