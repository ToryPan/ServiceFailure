import pandas as pd
import numpy as np

def get_sbDF(base_path,file_prefix):
    out = pd.DataFrame()
    for b in range(1,16):
        out = out.append([b])
        path = base_path+'{}{}.txt'.format(file_prefix,b)
        with open(path) as f:
            fi = f.readlines()
        fi = [c.replace("\n", "") for c in fi]
        out = out.append(fi)
    out = out.reset_index(drop=True)
    return out

def get_final(sp):
    sp_data = pd.DataFrame(columns=['epoch','eval_acc','eval_auc','eval_loss','eval_precision','eval_recall','global_step','loss'])
    for i in range(sp.shape[0]):
        b = i//8
        if i%8==0:
            j=0
        if str(sp[0][i]).find('=')>0:
            sp_data.loc[b,sp_data.columns[j]] = float(sp[0][i].split('=')[1].strip())
        else:
            sp_data.loc[b,sp_data.columns[j]] = sp[0][i]
        j+=1
    sp_data['eval_f1'] = sp_data.apply(lambda x: 2*x['eval_precision']*x['eval_recall']/(x['eval_precision']+x['eval_recall']) if x['eval_precision']+ x['eval_recall']>0 else 0,axis = 1)
    return sp_data

# file path
#eval
base_path = 'output/hxsb1/'#hxsb
hxsbdf = get_sbDF(base_path,'output_hxsb')
hxsbdf = get_final(hxsbdf)
#train
base_path = 'output/hxsb1/'#hxsb
hxsbdf_train = get_sbDF(base_path,'train_output_hxsb')
hxsbdf_train = get_final(hxsbdf_train)
# eval
base_path = 'output/jcsb1/'#jcsb
jcsbdf = get_sbDF(base_path,'output_jcsb')
jcsbdf = get_final(jcsbdf)
# train
base_path = 'output/jcsb1/'#jcsb
jcsbdf_train = get_sbDF(base_path,'train_output_jcsb')
jcsbdf_train = get_final(jcsbdf_train)

# sjhx
#eval
base_path = 'output/sjhx/'#hxsb
sjhxdf = get_sbDF(base_path,'output_sjhx')
sjhxdf = get_final(sjhxdf)
#train
base_path = 'output/sjhx/'#hxsb
sjhxdf_train = get_sbDF(base_path,'train_output_sjhx')
sjhxdf_train = get_final(sjhxdf_train)
# pthx
#eval
base_path = 'output/pthx/'#hxsb
pthxdf = get_sbDF(base_path,'output_pthx')
pthxdf = get_final(pthxdf)
#train
base_path = 'output/pthx/'#hxsb
pthxdf_train = get_sbDF(base_path,'train_output_pthx')
pthxdf_train = get_final(pthxdf_train)

# sjjc
#eval
base_path = 'output/sjjc/'#hxsb
sjjcdf = get_sbDF(base_path,'output_sjjc')
sjjcdf = get_final(sjjcdf)
#train
base_path = 'output/sjjc/'#hxsb
sjjcdf_train = get_sbDF(base_path,'train_output_sjjc')
sjjcdf_train = get_final(sjjcdf_train)
# ptjc
#eval
base_path = 'output/ptjc/'#hxsb
ptjcdf = get_sbDF(base_path,'output_ptjc')
ptjcdf = get_final(ptjcdf)
#train
base_path = 'output/ptjc/'#hxsb
ptjcdf_train = get_sbDF(base_path,'train_output_ptjc')
ptjcdf_train = get_final(ptjcdf_train)

# plot func
import matplotlib.pyplot as plt 
def plot_acc(trainData,name):

    loss = trainData.iloc[:,0]
    val_loss = trainData.iloc[:,2]
    f1 = trainData.iloc[:,1]
    val_f1 = trainData.iloc[:,3]
    epochs = range(1, len(loss) + 1)
    plt.plot(epochs, loss, '#281f1d', label='Training loss',linestyle = '--') 
    plt.plot(epochs, val_loss, '#281f1d', label='Validation loss',linestyle = '-.') 
    plt.title(name+' - Loss') 
    plt.legend(loc='upper right')
    plt.figure() 
    plt.plot(epochs, f1, '#281f1d', label='Training f1',linestyle = '--') 
    plt.plot(epochs, val_f1, '#281f1d', label='Validation f1',linestyle = '-.') 
    plt.title(name+' - F1 score') 
    plt.legend(loc='lower right')
    plt.show()

# predict big data
hxsb_pre = pd.read_table('output/bigdata_pre/hxsb.tsv',header=None)
jcsb_pre = pd.read_table('output/bigdata_pre/jcsb.tsv',header=None)
sjjc_pre = pd.read_table('output/bigdata_pre/sjjc.tsv',header=None)
ptjc_pre = pd.read_table('output/bigdata_pre/ptjc.tsv',header=None)
sjhx_pre = pd.read_table('output/bigdata_pre/sjhx.tsv',header=None)
pthx_pre = pd.read_table('output/bigdata_pre/pthx.tsv',header=None)
big_data = pd.read_excel('data_clean/big_data.xls')
big_data['hxsb_pre'] = hxsb_pre.apply(lambda x: 1 if x[1]>x[0] else 0,axis=1)
big_data['jcsb_pre'] = jcsb_pre.apply(lambda x: 1 if x[1]>x[0] else 0,axis=1)
big_data['sjjc_pre'] = sjjc_pre.apply(lambda x: 1 if x[1]>x[0] else 0,axis=1)
big_data['ptjc_pre'] = ptjc_pre.apply(lambda x: 1 if x[1]>x[0] else 0,axis=1)
big_data['sjhx_pre'] = sjhx_pre.apply(lambda x: 1 if x[1]>x[0] else 0,axis=1)
big_data['pthx_pre'] = pthx_pre.apply(lambda x: 1 if x[1]>x[0] else 0,axis=1)