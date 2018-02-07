import requests
# import readConfig as readConfig
import sys
sys.path.append("..")
from testFile.readConfig import *
readConfig().get_http

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_section('HTPP','baseurl')
        port = localReadConfig.get_section('port')

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        response = requests.get(self.url, params=self.params)
        # response.raise_for_status()
        return response

test = ConfigHttp()
print(test.get())
