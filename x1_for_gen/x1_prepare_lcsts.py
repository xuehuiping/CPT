# -*- coding: utf-8 -*-
# @Time   : 2021/11/12 下午8:12
# @Author : xuehuiping

'''
刚才整理数据的代码，不知道放哪里了，还是删了？
孩子在身边，就是不行，随时被打断。
'''

import os
import json
import random

folder = '/Users/xuehuiping/dataset/lcsts_part_1/'

articles = open(os.path.join(folder, 'article.txt')).readlines()
summarys = open(os.path.join(folder, 'summary.txt')).readlines()

samples = []
for summary, article in zip(summarys, articles):
    sample = {}
    sample['summarization'] = summary.strip()
    sample['article'] = article.strip()
    samples.append(sample)

# 随机打乱顺序
random.shuffle(samples)

# 总样本数
count = len(samples)
print('总样本数：', count)

# 便于计算，只取100个样本
samples = samples[0:100]

# 划分训练集、测试集、验证集
n_dev = (int)(count * 0.1)
n_test = (int)(count * 0.1)
# 训练集占比80%
n_train = count - n_dev - n_test

dev = samples[0:n_dev]
test = samples[n_dev: n_dev + n_test]
train = samples[n_dev + n_test:]

json.dump(train, open(os.path.join(folder, 'train.json'), 'w'))
json.dump(test, open(os.path.join(folder, 'test.json'), 'w'))
json.dump(dev, open(os.path.join(folder, 'dev.json'), 'w'))

print('训练集个数：', len(train))
print('测试集个数：', len(test))
print('验证集个数：', len(dev))
