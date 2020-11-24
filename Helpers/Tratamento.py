from unicodedata import normalize


class Tratamento:

    def retira_acento(self, texto: str) -> str:
        count_n = texto.count('\n')
        texto = texto.replace('\n', '', count_n)
        target = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
        return target

    def tratamento_header(self, header: list) -> list:
        header_tratada = []
        for item in header:
            item = self.tratamento_espaco(item)
            item = str(item).lower().replace("\n", "")
            item = self.retira_acento(item)
            swap_space = (item.count(' '))
            if swap_space != 0:
                item = item.replace(" ", "_", swap_space)
            header_tratada.append(item)
        return header_tratada

    def tratamento_linha(self, texto_linha: str) -> str:
        item = texto_linha
        item = self.tratamento_espaco(item)
        return item

    def tratamento_espaco(self, texto: str) -> str:
        texto = texto.strip()
        texto.count('\n')
        texto.count('  ')
        for x in range(texto.count('  ')):
            texto = texto.replace('  ', ' ')
        return texto

    def colorir(self, texto: str, cor='amarelo') -> str:
        if cor == 'amarelo':
            return f'\033[33m{texto}\033[0;0m'
        elif cor == 'azul':
            return f'\033[34m{texto}\033[0;0m'
        else:
            return texto
