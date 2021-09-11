import glob
import shutil

from Edi_Library.parse_837 import Parse837


class Main:
    def __init__(self, edi_file):
        self.__edi_file = edi_file
        shutil.move(self.__edi_file, '../edi_files/')
        self.__parse_file()

    def __parse_file(self):
        self.__edi_files = glob.glob('../edi_files/*.*')
        for edi_file in self.__edi_files:
            if edi_file.split('.')[-1] == '837':
                Parse837(edi_file)

