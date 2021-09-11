import glob

from Edi_Library.parse_837 import Parse837

if __name__ == '__main__':
    edi_files = glob.glob('../edi_files/*.*')
    for edi_file in edi_files:
        if edi_file.split('.')[-1] == '837':
            parse837 = Parse837(edi_file)
            print(parse837.edi_parsed)
            print()
            print(parse837.extract_index_data())
