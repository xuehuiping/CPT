2021-11-12 16:21:30

https://github.com/fastnlp/CPT

复旦 邱锡鹏团队做的中文BART



### 微调

The code and running examples are listed in the corresponding folders of the fine-tuning tasks.

- **`classification`**: [Fine-tuning](https://github.com/fastnlp/CPT/blob/master/finetune/classification/README.md) for sequence classification with either external classifiers or prompt-based learning.
- **`cws`**: [Fine-tuning](https://github.com/fastnlp/CPT/blob/master/finetune/cws/README.md) for Chinese Word Segmentation with external classifiers.
- **`generation`**: [Fine-tuning](https://github.com/fastnlp/CPT/blob/master/finetune/generation/README.md) for abstractive summarization and data-to-text generation.
- **`mrc`**: [Fine-tuning](https://github.com/fastnlp/CPT/blob/master/finetune/mrc/README.md) for Span-based Machine Reading Comprehension with exteranl classifiers.
- **`ner`**: [Fine-tuning](https://github.com/fastnlp/CPT/blob/master/finetune/ner/README.md) for Named Entity Recognition.



### 微调文本生成任务

给的数据例子有3种：adgen、lcsts、csl

demo_data/adgen/ directory目录有示例



开始运行：

```python run_gen.py --model_path /path/to/checkpoint --dataset adgen --data_dir demo_data```

生成结果在./output/adgen/1/ .

评估： [ROUGE](https://github.com/pltrdy/rouge) 、[BLEU-4](https://github.com/TsinghuaAI/CPM-2-Finetune/blob/b37b07da4bf834c7a3b7e8188662df91eddb9b0a/generation_metrics.py#L89)

作者已经给出了示例输入和输出。已试可行。

---

---



以这里为根目录，进行文件的组织和引用。

环境用CPT。

```
conda activate CPT
```

### 代码准备
`modeling_cpt.py`、`bleu_metric.py`、`utils.py`、`run_bleu.py`
这4个文件，从原始的目录`../finetune/generation/`下面拷贝过来。

### 微调文本摘要生成模型

```
python run_gen.py --model_path fnlp/bart-base-chinese \
 --dataset adgen --data_dir demo_data
```

命令行可以运行

在`jupyter`，打印命令

### 评估

`run_bleu.py`

打印结果：0.004612

这个数字如何？代表什么？

这是bleu。


### 使用LCSTS数据进行微调

结果见note2。


---


### 问题及记录

这模型文件是存在哪里呢？怎么映射？
loading file https://huggingface.co/fnlp/bart-base-chinese/resolve/main/vocab.txt from cache at /Users/xuehuiping/.cache/huggingface/transformers/feb7fcba07a5cd52dab8daea7c7654f9f450cf4e2586eb946df713da5b44d5e4.accd894ff58c6ff7bd4f3072890776c14f4ea34fcc08e79cd88c2d157756dceb
loading file https://huggingface.co/fnlp/bart-base-chinese/resolve/main/added_tokens.json from cache at None
loading file https://huggingface.co/fnlp/bart-base-chinese/resolve/main/special_tokens_map.json from cache at /Users/xuehuiping/.cache/huggingface/transformers/c7a2ad3ce29650bde9ea8929d9d4414f1472f2eaee89e1700413a60725333838.dd8bd9bfd3664b530ea4e645105f557769387b3da9f79bdb55ed556bdd80611d
loading file https://huggingface.co/fnlp/bart-base-chinese/resolve/main/tokenizer_config.json from cache at /Users/xuehuiping/.cache/huggingface/transformers/e8916bb2271881244e34cad9e88d11ef38394196b1d328d76773fde6934c0ef9.4930bdcbc6f75dead7cdeadc249fdb55dcb3cd75bdcee68ee5fcd8aeb6e6e359
loading file https://huggingface.co/fnlp/bart-base-chinese/resolve/main/tokenizer.json from cache at None
loading configuration file https://huggingface.co/fnlp/bart-base-chinese/resolve/main/config.json from cache at /Users/xuehuiping/.cache/huggingface/transformers/e0ab1af8221a3166de9abfc42b6eb4275cfe6ee6ee31a99937350dfae50cc659.b46ea2f32c0c0a3eb762ff2b81ebfe0a058025072aa60e54714633acdd9ca36e
loading weights file https://huggingface.co/fnlp/bart-base-chinese/resolve/main/pytorch_model.bin from cache at /Users/xuehuiping/.cache/huggingface/transformers/9032bba23e7bf4f5ef19608e2158df5ceb26f362b42e2b8cf5b07ea175f1c1e9.2251c3a1e4e718fc7d03740d3283002a38b4fb4b94f6f2461c49426385adc6dc
