import os
import codecs
import configparser

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
        self.cf.write(open(configPath,'w'))

    def get_section(self, title, name):
        value = self.cf.get(title, name)
        return value

    def add_section(self, title):
        self.cf.add_section(title)
        
    def set_section(self, title, name, info):
        self.cf.set(title, name, info) 




    