'''
Created on 2018年10月2日

@author: Administrator
'''
#coding:utf-8

class HtmlOutputer(object):
    def __init__(self):
        self.data=[]
    
    def collect_data(self,data):
        if data is None:
            return
        self.data.append(data)

    
    def output_html(self):
        fout = open('output.html','w',encoding='utf-8')
        
        fout.write('<html>')
        fout.write('<head>')
        fout.write('<meta charset="UTF-8">')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table>')
        str=''
        for data in self.data:
            str=str+'<tr>'+'<td>%s</td>' % data['url']+'<td>%s</td>' % data['title'].encode('utf-8').decode('utf-8')+'<td>%s</td>' % data['summary'].encode('utf-8').decode('utf-8')+'</tr>'
        fout.write(str)
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        print(fout)
        fout.close()
    
    
    
    



