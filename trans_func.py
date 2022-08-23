import os
from shutil import copy
from shutil import rmtree
import sys
import zhconv
import zipfile

class pofile_trans:
    def __init__(self):
        self.file_name = './chinese_s.po'

    def run(self, file_path):
        self.do_trans(file_path)

    def do_trans(self, src_path):
        # Copy zip file from game dir then extracting.
        copy(src_path, ".")
        if zipfile.is_zipfile("scripts.zip"):
            with zipfile.ZipFile("scripts.zip", 'r') as zf:
                zf.extractall()
        # Create new file and write contents after translating.
        pofile_path = './scripts/languages/chinese_s.po'
        temp_file = 'chinese_s.po'
        self.trans_file(pofile_path, temp_file)
        # Instead old po file by translated one.
        os.remove(pofile_path)
        copy(temp_file, pofile_path)
        os.remove(temp_file)
        os.remove("./scripts.zip")
        # Compression.
        with zipfile.ZipFile('scripts.zip', 'w', zipfile.ZIP_DEFLATED) as cf:
            for root, dirs, files in os.walk('./scripts'):
                for filename in files:
                    cf.write(os.path.join(root, filename))
        rmtree('./scripts')
        os.remove(src_path)
        copy("./scripts.zip", src_path)

    def trans_file(self, oldfile, newfile):
        temp_file_oper = open(newfile, 'w', encoding='utf-8')
        if os.path.isfile(oldfile):
            with open(oldfile, 'r', encoding='utf-8') as f:
                for line in f:
                    line = zhconv.convert(line, 'zh-tw')
                    temp_file_oper.write(line)
            temp_file_oper.close()


    def has_zipfile(self):
        if os.path.isfile('scripts.zip'):
            return True
        else:
            return False


if __name__ == "__main__":
    obj = pofile_trans()