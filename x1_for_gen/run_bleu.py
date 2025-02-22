import os
from utils import load_json
from transformers import BertTokenizer
from bleu_metric import Metric

# 需要计算bleu的文本文件所在的目录
arch = 'output'
tokenizer = BertTokenizer.from_pretrained('fnlp/bart-base-chinese')
dataset = 'adgen'
# dataset = 'lcsts'
test_set = load_json('demo_data/SUMMARY.{}/test.json'.format(dataset))

labels = []
for data in test_set:
    ids = tokenizer.encode(data['summarization'])
    labels.append(tokenizer.decode(ids, skip_special_tokens=True))
labels = [[label.strip().split(' ')] for label in labels]

metric = Metric(None)
idxs = os.listdir(os.path.join(arch, dataset))
scores = []
for idx in sorted(idxs):
    path = os.path.join(arch, dataset, idx, 'test_generations.txt')
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    lines = [line.split(' ') for line in lines]
    metric.hyps = lines
    metric.refs = labels
    # 如果是少量的样本进行评估，可以打印看看结果
    for label, predict in zip(labels, lines):
        print('label: ' + ''.join(label[0]))
        print('predict: ' + ''.join(predict))
        print()
    scores.append(metric.calc_bleu_k(4))
print(sum(scores) / len(scores))
