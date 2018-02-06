import os
import codecs
import configparser
import sys
sys.setrecursionlimit(1000000)

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

class ReadConfig():
    def __init__(self):
        fd = open(configPath)
        data = fd.read()
        
        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_section(self, title, name):
        value = self.cf.get(title, name)
        return value

    def add_section(self, title):
        self.add_section(title)
        
    def set_section(self, title, name, info):
        self.cf.set(title, name, info)

test = ReadConfig()
# test.add_section('title')
# test.set_section('title','name','info')
print(test.get_section('HTTP','baseurl'))



    