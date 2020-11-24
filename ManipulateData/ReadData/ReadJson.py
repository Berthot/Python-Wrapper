import json


class ReadJson:

    def __init__(self, path):
        self._path = path
        self._dicionarioAtual = self.__abre_json_retorna_dict()
        self._jsonData = ''
        self.jsonHeader = []

    def __abre_json_retorna_dict(self):
        caminho = self._path
        try:
            config = json.loads(open(caminho, encoding="utf8").read())
            return config
        except FileNotFoundError:
            raise ValueError("Arquivo " + str(caminho) + " Não encontrado ")

    def get_header(self, print_text=False):
        if print_text:
            for x in self.jsonHeader:
                print(x)
        return self.jsonHeader

    def dictionary(self, key_name):
        # key é a chave do dic, value o resto
        dic = self._dicionarioAtual
        if dic is None:
            raise ValueError("Dicionario nao pode ser aberto")
        fast_dic = {}
        see_header = True
        for line in dic:
            if line == {}:
                continue
            if see_header:
                for h in line:
                    self.jsonHeader.append(h)
                see_header = False
            # fastDic[str(line['id'])] = line['data']
            fast_dic[str(line[key_name])] = line
        return fast_dic

    # def writeJson(self, data):
    #     with open(self._path, "w", encoding='utf8') as jsonFile:
    #         json.dump(data, jsonFile, ensure_ascii=False)
