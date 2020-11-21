# coding=utf-8
"""
Test Translator
"""
from time import sleep

from googletrans import Translator

import os


class LinesTranslate:
    """ Classe para traduzir linhas de um arquivo. """
    def __init__(self, lines, lang='pt', echo=True):
        self._echo = echo
        self._lines = lines
        self._lang = lang
        self._output = []

    def execute(self):
        """
        Método para executar a tradução.
        :return: self.
        """
        lines = [line.replace('\n', '') for line in self._lines if line.replace('\n', '') != '']
        # print(lines)
        for line in lines:
            translated = False
            while not translated:
                try:
                    t = Translator().translate(line, dest=self._lang)
                except Exception as e:
                    sleep(0.1)
                else:
                    translated = True
                    self._output.append(t.text + '\n')
                    if self._echo:
                        self._info(t)
        return self

    def _info(self, t):
        """
        Método para exibir informações.
        :return: Self.
        """
        print(f'Source: {t.src}')
        print(t.origin)
        print(f'destination: {t.dest}')
        print(t.text)
        print('')
        return self

    @property
    def output(self):
        """
        Método para recuperar a resposta.
        :return: list.
        """
        return self._output


if __name__ == '__main__':
    base_path = 'source/'
    with os.scandir(base_path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)
                fs = open('destination/' + entry.name, 'w', encoding='utf-8')
                try:
                    with open(base_path + entry.name, 'r', encoding='utf-8') as f:
                        lines_original = f.readlines()
                        fs.writelines([line for line in LinesTranslate(lines_original).execute().output])
                finally:
                    fs.close()
