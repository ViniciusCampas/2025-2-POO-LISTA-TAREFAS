from abc import ABC, abstractmethod
from datetime import datetime

class Mensagem(ABC):


    def __init__(self, conteudo: str):
        self._conteudo = conteudo
        self._data_envio = datetime.now()

    @abstractmethod
    def exibir_detalhes(self):
        pass


class MensagemTexto(Mensagem):
    def exibir_detalhes(self):
        return f"[Texto] '{self._conteudo}' (enviada em {self._data_envio})"


class MensagemVideo(Mensagem):
    def __init__(self, conteudo: str, arquivo: str, formato: str, duracao: int):
        super().__init__(conteudo)
        self._arquivo = arquivo
        self._formato = formato
        self._duracao = duracao

    def exibir_detalhes(self):
        return (f"[Vídeo] '{self._conteudo}' - Arquivo: {self._arquivo} "
                f"({self._formato}, {self._duracao}s) - Enviada em {self._data_envio}")


class MensagemFoto(Mensagem):
    def __init__(self, conteudo: str, arquivo: str, formato: str):
        super().__init__(conteudo)
        self._arquivo = arquivo
        self._formato = formato

    def exibir_detalhes(self):
        return (f"[Foto] '{self._conteudo}' - Arquivo: {self._arquivo} "
                f"({self._formato}) - Enviada em {self._data_envio}")


class MensagemArquivo(Mensagem):
    def __init__(self, conteudo: str, arquivo: str, formato: str):
        super().__init__(conteudo)
        self._arquivo = arquivo
        self._formato = formato

    def exibir_detalhes(self):
        return (f"[Arquivo] '{self._conteudo}' - Arquivo: {self._arquivo} "
                f"({self._formato}) - Enviada em {self._data_envio}")


class Canal(ABC):

    @abstractmethod
    def enviar_mensagem(self, mensagem: Mensagem):
        pass


class WhatsApp(Canal):
    def __init__(self, numero: str):
        self._numero = numero

    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"Enviando via WhatsApp para {self._numero}: {mensagem.exibir_detalhes()}")


class Telegram(Canal):
    def __init__(self, identificador):

        self._identificador = identificador

    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"Enviando via Telegram para {self._identificador}: {mensagem.exibir_detalhes()}")


class Facebook(Canal):
    def __init__(self, usuario: str):
        self._usuario = usuario

    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"Enviando via Facebook para @{self._usuario}: {mensagem.exibir_detalhes()}")


class Instagram(Canal):
    def __init__(self, usuario: str):
        self._usuario = usuario

    def enviar_mensagem(self, mensagem: Mensagem):
        print(f"Enviando via Instagram para @{self._usuario}: {mensagem.exibir_detalhes()}")



texto = MensagemTexto("Olá, tudo bem?")
video = MensagemVideo("Veja esse vídeo!", "video123.mp4", "mp4", 120)
foto = MensagemFoto("Olha essa foto!", "foto_praia.jpg", "jpg")
arquivo = MensagemArquivo("Segue o documento", "contrato.pdf", "pdf")

whatsapp = WhatsApp("+5511987654321")
telegram = Telegram("@vinicius")
facebook = Facebook("vinicius.fb")
instagram = Instagram("vinicius_insta")

whatsapp.enviar_mensagem(texto)
telegram.enviar_mensagem(video)
facebook.enviar_mensagem(foto)
instagram.enviar_mensagem(arquivo)
