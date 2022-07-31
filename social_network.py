import pandas as pd 
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import re
import opencc #繁体转换
import jieba
import jieba.analyse#TF-IDF
import jieba.posseg
import os
import math
def stopwordslist(filepath1,filepath2):   # 定义函数创建停用词列表
    stopword1 = [line.strip() for line in open(filepath1, 'r',encoding='UTF-8').readlines()]    #以行的形式读取停用词表，同时转换为列表
    stopword2 = [line.strip() for line in open(filepath2, 'r',encoding='UTF-8').readlines()]
    return stopword1+stopword2

def get_jieba(data_review):
    '''
    给定一条array数据，得到分词后的结果
    '''
    
    
    wordClass = ['n','nr', 'nz','v','vd','vn', 'a', 'ad', 'an', 'd', 'r', 'per'] # 需要的词性
    jieba_path = 'jieba_dic'
    jieba.load_userdict(os.path.join(jieba_path,'dict.txt'))
    stopwords = stopwordslist(os.path.join(jieba_path,"stop_words.txt"),os.path.join(jieba_path,"stop_words_user.txt"))
    synonym_words = pd.read_excel(os.path.join(jieba_path,"synonym_list.xls"))
    synonym_origin = list(synonym_words['origin'])
    synonym_new = list(synonym_words['new'])
    
    
    
    
    comments_origin = opencc.OpenCC('t2s').convert(data_review) #转换为简体
    comments = comments_origin.replace(' ', '').replace('\n', '').replace('\r', '')#去空格和换行符
    comments_class = jieba.posseg.lcut(comments)
    lastsentences = ''
    for word,cha in comments_class:     #for循环遍历分词后的每个词语
        cha = cha.lower()
        if word not in stopwords and not word.isdigit() and len(word)>1 and not word.encode().isalnum() :     #判断分词后的词语是否在停用词表内
            if word in synonym_origin:
                index = synonym_origin.index(word)
                word = synonym_new[index]
            if word != '\t':
                lastsentences += word
                lastsentences += "/"
            
        
        comments_Disjunctive_lis = lastsentences[:-1].split("/") # 这是列表
        comments_Disjunctive_lis = list(set(comments_Disjunctive_lis))
        comments_Disjunctive = ' '.join(comments_Disjunctive_lis) # 转换成空格连接形式
    return(comments_Disjunctive)

data_all['words'] = data_all['summary'].apply(get_jieba)

def make_dict(comment_datas):
    comment_dict = dict()
    for comment in comment_datas:
        comment_list = comment.split()
        for word in comment_list:
            if word not in comment_dict:
                comment_dict[word] = 1
            else:
                comment_dict[word] +=1
    comment_list_sort = sorted(comment_dict.items(),key=lambda x:x[1],reverse=True)
    return comment_dict,comment_list_sort

comment_data_all_dict,comment_data_all_list_sort = make_dict(commemts_data_all)

def get_t_seg(topwords,text):
    '''
    topwords:传入的词汇表
    text：传入的文本：str,每段文本用/n分割
    synonym_words：合并词
    stop_words：停用词
    
    text：传入的文本：list,每段文本内用 空格 分隔
    synonym_words：删除
    stop_words：删除
    '''
    word_docs = {}
    text_lines_seg =[]
    for line in text:
        t_seg = []
        for word in line.split():
            if word in topwords:
                t_seg.append(word)
        t_seg=list(set(t_seg))
        text_lines_seg.append(t_seg)
        for word in t_seg:
            word_docs[word]=word_docs.get(word,0)+1
    return text_lines_seg,word_docs

def get_comatrix(text_lines_seg,topwords):
    comatrix = pd.DataFrame(np.zeros([len(topwords),len(topwords)]),columns=topwords,index=topwords)
    for t_seg in text_lines_seg:
        for i in range(len(t_seg)-1):
                for j in range(i+1,len(t_seg)):
                    comatrix.loc[t_seg[i],t_seg[j]]+=1
    for k in range(len(comatrix)):
        comatrix.iloc[k,k]=0
    return comatrix

def get_net(co_matrix,topwords):
    g = nx.Graph()
    for i in range(len(topwords)-1):
        word = topwords[i]
        for j in range(i+1,len(topwords)):
            w=0
            word2 = topwords[j]
            w = co_matrix.loc[word][word2]+co_matrix.loc[word2][word]
            if w>0:
                g.add_edge(word,word2,weight=w)
    return g

data_all_words = [word[0] for word in comment_data_all_list_sort if word[1]>=10]

comments_data_all_seg,comments_data_all_doc = get_t_seg(data_all_words,commemts_data_all)
co_matrix_data_all = get_comatrix(comments_data_all_seg,data_all_words)
co_net_data_all =get_net(co_matrix_data_all,data_all_words)

nx.write_gexf(co_net_data_all,"./result/word_cooccurrence.gexf")

# predictclass
data_node = pd.read_csv('dot.csv')
data_class_dict = dict()
for i,j in zip(data_node['Label'],data_node['modularity_class']):
    data_class_dict[i] = j

def get_class(words):
    words_lis = words.split(' ')
    class_lis = []
    for word in words_lis:
        class_lis.append(data_class_dict.get(word,5))
    return list(set(class_lis))

data_all['class_sub'] = data_all['words'].apply(get_class)

