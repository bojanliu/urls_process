#coding:utf-8
#file_name:urls_process.py
'''此脚本用于从url中提取出域名'''

import os

def main():
    file_name=raw_input(u'请输入待处理文件名：')
    #返回该脚本所在路径，故用时待处理文件需要和脚本在同一路径
    f=open(os.path.abspath('.')+'\\'+file_name,'r')
    data=f.readlines()
    f.close()

    output=[]
    for item in data:
        if 'made-in-china' in item:
            output.append('MIC')
        else:
            if item.startswith('http://www'):
                index=item.find('/',12,100)
                output.append(item[11:index])
            elif item.startswith('https://www'):
                index=item.find('/',13,100)
                output.append(item[12:index])
            elif item.startswith('www'):
                index=item.find('/',5,100)
                output.append(item[4:index])
            elif item.startswith('http://'):
                index=item.find('/',7,100)
                output.append(item[7:index])
            elif item.startswith('https://'):
                index=item.find('/',8,100)
                output.append(item[8:index])
            else:
                index=item.find('/',0,100)
                output.append(item[:index])

    f_output=open(os.path.abspath('.')+'\\output.txt','a')
    for item in output:
        f_output.write(item+'\n')
    print 'OK'

if __name__ =='__main__':
    main()


        
        
