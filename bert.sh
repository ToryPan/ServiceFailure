#!/bin/bash

my_file=('output_sjjc')
export BERT_BASE_DIR=/root/autodl-nas/bert/bert-master/model/chinese_L-12_H-768_A-12
export GLUE_DIR=/root/autodl-nas/data/hxsb_data_update/update1

time1=$(date "+%Y%m%d%H%M%S")
export result_dir=/root/autodl-nas/output/$time1
mkdir $result_dir

for file in ${my_file[@]}
do
    export TRAINED_CLASSIFIER=/root/autodl-nas/bert/bert-master/$file
    
    for i in $(seq 1 20)
	do
	export epoch_num=$i
	python /root/autodl-nas/bert/bert-master/run_classifier.py \
      --task_name=$file \
      --do_train=true \
      --do_eval=true \
      --data_dir=$GLUE_DIR/ \
      --vocab_file=$BERT_BASE_DIR/vocab.txt \
      --bert_config_file=$BERT_BASE_DIR/bert_config.json \
      --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
      --max_seq_length=300 \
      --train_batch_size=6 \
      --learning_rate=2e-5 \
      --num_train_epochs=$epoch_num \
      --output_dir=$TRAINED_CLASSIFIER
      mv $TRAINED_CLASSIFIER/eval_results.txt  $result_dir/$file$i.txt
      python /root/autodl-nas/bert/bert-master/run_classifier_train.py \
      --task_name=$file \
      --do_train=true \
      --do_eval=true \
      --data_dir=$GLUE_DIR/ \
      --vocab_file=$BERT_BASE_DIR/vocab.txt \
      --bert_config_file=$BERT_BASE_DIR/bert_config.json \
      --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
      --max_seq_length=300 \
      --train_batch_size=6 \
      --learning_rate=2e-5 \
      --num_train_epochs=$epoch_num \
      --output_dir=$TRAINED_CLASSIFIER
      mv $TRAINED_CLASSIFIER/eval_results.txt  $result_dir/train_$file$i.txt
      #rm -r $TRAINED_CLASSIFIER
    done
    rm -r $TRAINED_CLASSIFIER
done
#zip -r /root/autodl-nas/output/$time1.zip $result_dir
#export $(cat /proc/1/environ |tr '\0' '\n' | grep MATCLOUD_CANCELTOKEN)&&/public/script/matncli node cancel -url https://matpool.com/api/public/node
