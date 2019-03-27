from conf.setting import CASE_PATH,CASE_EG,PY_PATH
import os  #获取某个目录下面所有的文件
#行为驱动其实就是关键字驱动，一般用于UI测试
#代码驱动
#数据驱动
#以下是数据驱动是实现
class GetCase(object):
    # def __merge(self):
        # '''
        # 合并所有用例文件，因为一般来说每个功能的测试用例都会写一个单独的测试文件
        # 需要把所有用例写到一个文件里面
        # yml适用于接口之间没有依赖关系的自动化测试
        # :return:
        # '''
        # fw = open('.all_data.yml','w',encoding='utf-8')#提前打开一个文件，把读到的所有文件内容写到这个文件中
        # #只有在循环打开文件的时候W模式的，才会把文件内容情况
        # for f in os.listdir(CASE_PATH):#获取cases目录下面所有的文件
        #     if f.endswith('.yml') or f.endswith('.yaml'):#判断文件是不是以.yml或者.yaml结尾的
        #         #如果是以这种文件格式结尾的，就打开文件，读取文件内容
        #         abs_path = os.path.join(CASE_PATH,f)#因为上面的f是相对路径，所以要拼接成绝对路径
        #         fw.write(open(abs_path,encoding='utf-8').read())#把每个用例文件内容写到循环中

    def creat_py(self):
        '''
        所有的用例使用base_case.eg模板生成新的python用例文件
        :return:
        '''
        base_case_str = open(CASE_EG,encoding='utf-8').read()#读取模板文件里面的内容
        for f in os.listdir(CASE_PATH):#data目录下用例文件
            if f.endswith('.yml') or f.endswith('.yaml'):#判断文件是不是以.yml或者.yaml结尾的
            # if f.endswith(('.yml','.yaml')):
                abs_path = os.path.join(CASE_PATH,f)#拼接用例文件的绝对路径
                class_name = 'Test'+f.replace('.yml','').replace('.yaml','').capitalize()
                #把.yml和.yaml替换成空
                #capitalize把文件名中首字母大写
                #定义模板中类名，还有利用模板生成的python文件名
                new_case_str = base_case_str%(class_name,abs_path)#把模板里面的内容格式化下
                py_file_path = os.path.join(PY_PATH,class_name)#拼接生成的python文件的路径
                open('%s.py'%py_file_path,'w',encoding='utf-8').write(new_case_str)#把模板内容写到文件中
g = GetCase()
g.creat_py()
