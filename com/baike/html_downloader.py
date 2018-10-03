'''
Created on 2018年10月2日

@author: Administrator
'''
#coding:utf-8
import urllib.request


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return
       # print(urllib.request.urlopen('https://sh.ke.com/').getcode())
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
    
    



