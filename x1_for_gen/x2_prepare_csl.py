# -*- coding: utf-8 -*-
# @Time   : 2021/11/15 上午10:07
# @Author : xuehuiping
import json

samples = []
lines = open('/Users/xuehuiping/dataset/csl_title_public/csl_title_test.json').readlines()
for line in lines:
    data = json.loads(line)
    sample = {}
    sample['summarization'] = data['title'].strip()
    sample['article'] = data['abst'].strip()
    samples.append(sample)

json.dump(samples, open('test.json', 'w'))
