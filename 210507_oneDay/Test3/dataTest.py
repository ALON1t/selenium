from  ddt import ddt,unpack,data,file_data
import sys,csv

def getCsc(file_name):
    rows = []
    path = sys.path[0]  # 当前文件所在路径
    # 打开文件   rt->读取
    with open(path + 'data/' + file_name, 'rt') as f:
        # csv工具  分隔号是逗号
        readers = csv.reader(f, delimiter=',', quotechar='|')
        # 一行一行的读，放到readers里
        next(readers, None)
        # 一行一行的遍历  每一行里面的每个数据放到数组里面
        for row in readers:
            temprows = []
            for i in row:
                # [肖战，肖战，百度搜素]
                temprows.append(i)
            rows.append(temprows)
        return rows