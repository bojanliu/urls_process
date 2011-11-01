#coding:utf-8
#file_name:urls_process.py
'''此脚本用于对url进行清理;使用前需要将原始的txt文件
另存为utf-8格式，不然会乱码'''

import os

def main():
    file_name=raw_input(u'请输入待处理文件名：')
    #返回该脚本所在路径，故用时待处理文件需要和脚本在同一路径
    old=open(os.path.abspath('.')+'\\'+file_name,'r')
    new=open(os.path.abspath('.')+'\\output.txt','a')
    data=old.readlines()
    old.close()
    
    for item in data:
        if 'made-in-china' in item:#处理MIC的url
            last_slash=item.rfind('/')#反向查找最后一个斜杠
            if last_slash!=-1:#如果有/则截取/前字符，去掉多余后缀
                item=item[:last_slash]
            
            start_index=item.rfind('//')
            if start_index!=-1:#去掉前缀
                item=item[start_index+2:]
            
            
        else:#处理非MIC的url
            if 'www.' in item[:12]:#有'www'的情况
                start_index=item.find('.',0,12)+1#第一个点号的位置+1
            elif '//' in item[:8]:#没有'www'的情况
                start_index=item.find('//',0,8)+2
            else:#没有任何前缀的情况
                start_index=0
                
            end_index=item.find('/',start_index,100)
            if end_index!=-1:#有斜杠的情况
                item=item[start_index:end_index]
            else:#没有斜杠的情况
                item=item[start_index:]

        new.write(item+'\n')#将经过处理的urls字符串写入新文件
    
    new.close()
    print 'the job has done!'

if __name__ =='__main__':
    main()


        
        
