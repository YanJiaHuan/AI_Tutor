import warnings
warnings.filterwarnings('ignore')

from datasets import load_dataset
# load dataset
raw_datasets = load_dataset('glue','mrpc')
raw_train_dataset = raw_datasets['train']
print(raw_train_dataset[:2])
# print(raw_datasets.features)

# load pre-trained tokenizer

from transformers import AutoTokenizer

checkpoint = 'bert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def tokenize_function(example):
    return tokenizer(example['sentence1'],example['sentence2'],truncation = True)

tokenized_datasets = raw_datasets.map(tokenize_function,batched = True)

# Dataloader: data2batch
from transformers import DataCollatorWithPadding
# with padding, every data point has same length
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# training

# Load training config
from transformers import TrainingArguments
training_args = TrainingArguments('test-trainer')

# load model

from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained(checkpoint,num_labels = 2)

from transformers import Trainer
trainer = Trainer(
    model,
    training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
    data_collator=data_collator,
    tokenizer=tokenizer
)

# trainer.train()/

# test
print(tokenized_datasets['validation'])
predictions = trainer.predict(tokenized_datasets['validation'])

import numpy as np
print(predictions.predictions.shape)

preds = np.argmax(predictions.predictions, axis=-1)
print(preds)
print(predictions.label_ids)
# huggingface provide simple validation metric function
from datasets import load_metric
metric = load_metric('glue','mrpc')

final_score = metric.compute()
metric.add_batch(predictions=preds, references=predictions.label_ids)
score = metric.compute()
print(score)
