import pandas as pd
import yaml

de_data = pd.read_csv("data.csv")

#list to str
def str_lis(mstr_lis):
    try:
        bb = yaml.load(mstr_lis)
        return bb[0]
    except:
        return str(mstr_lis)[2:-2]

de_data["title"] = de_data["title"].apply(str_lis)
de_data["username"] = de_data["username"].apply(str_lis)
de_data["time"] = de_data["mtime"].apply(str_lis)

# detail_info
def detail_proc(lis_str):
    lis_str = str(lis_str)
    my_lis = []
    aa_lis =yaml.load_all(lis_str,Loader=yaml.FullLoader)
    for li in aa_lis:
        my_lis = li
    toushu_obj = ["投诉编号","投诉对象","投诉问题","投诉要求","涉诉金额","投诉进度"]
    content_lis = ["","","","","",""]
    for i in range(len(toushu_obj)):
        for l in my_lis:
            if l[0]==toushu_obj[i]:
                content_lis[i]=l[1]
    return(content_lis[0],content_lis[1],content_lis[2],content_lis[3],content_lis[4],content_lis[5])
  
de_data[["投诉编号","投诉对象","投诉问题","投诉要求","涉诉金额","投诉进度"]] = de_data.apply(lambda xx:detail_proc(xx["complaint_detail"]),axis=1,result_type="expand")

# process_detail
def process_detail_proc(lis_str):
    lis_str = str(lis_str)
    my_lis = []
    aa_lis =yaml.load_all(lis_str,Loader=yaml.FullLoader)
    try:
        for li in aa_lis:
            my_lis = li
    except:
        my_lis = [lis_str]
    return(my_lis)

total_lis = []
for i in my_data["process_detail"]:
    cc = process_detail_proc(i)
    total_lis.append(cc)

def get_lis_2(mlis):
    total_lis_2 = []
    max_len = len(max(mlis, key=len))
    n = len(mlis)
    for i in range(max_len):
        total_lis_2.append([[1]])
        for j in range(n):
            total_lis_2[i].append([1])
    for i in range(max_len):
        for j in range(n):
            try:
                total_lis_2[i][j]=mlis[j][i]
            except:
                total_lis_2[i][j] = ""
    return(total_lis_2)
my_liss = get_lis_2(total_lis)

for mmmlis in range(len(my_liss)):
    my_data[mmmlis] = my_liss[mmmlis][0:2518]