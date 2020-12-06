import wget
import json
import zipfile
import os


class _back:
    def __init__(self):
        self.setting_io = open('setting.json', 'r') #对设定的读取
        self.list_packet = open('list.json', 'r')   #从list.json读取软件包信息

    def _url(self, name):
        #从list.json中获取url,简单得很
        for list_name in json.load(self.list_packet):
            if name == list_name['name']:
                return list_name

    def settings(self):
        #就一行语句，加载设定
        return json.load(self.setting_io)

    def _down(self, name):
        _class = _back()    #获取类的对象
        url = _class._url(name) #获取url字典
        if not url: #如果url没被找到
            return False    #返回否值
        else:
            return _class.settings()['dir'] + url['name']   #返回一个下载的保存值,为目录+文件名

class back(_back):
    def remove(self, dir_name):
        #删除文件&目录
        if os.path.exists(dir_name):    #检测文件，没啥好说的
            os.remove(dir_name)
        return True

    def out_zip(self, dir):     #将下载下来的包解压
        #都没啥可说的
        zip_dir = zipfile.ZipFile(dir)
        zip_dir.extractall()
        back.remove(dir_name=dir)   #解压完成后删掉原来的文件
        return True

    def get_list(self):
        wget.download(_back.settings()['r_list'],out='list.json')   #获取包的目录文件

    def down(self, name):       #下载软件包
        url = _back._url(name=name)['href']     #获取链接
        if not url:     #如果url没有被找到，就返回假值
            return False
        else:       #如果是，就下载并返回真
            log = wget.download(url, _back._down(name=name))        #下载日志
            return True, log
