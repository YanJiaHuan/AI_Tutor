from transformers import AutoTokenizer
from transformers import AutoModel
checkpoint  = 'distilbert-base-uncased-finetuned-sst-2-english'
# load tokenizer
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# load model
model = AutoModel.from_pretrained(checkpoint)

raw_inputs = [
    'Pre-trained models have achieved state-of-the-art results in various Natural Language Processing tasks. Recent works such as T5 [1] and GPT-3 [2] have shown that scaling up pre-trained language models can improve their generalization abilities. Particularly, the GPT-3 model with 175 billion parameters shows its strong task-agnostic zero-shot/few-shot learning capabilities. Despite their success, these large-scale models are trained on plain texts without introducing knowledge such as linguistic knowledge and world knowledge. In addition, most large-scale models are trained in an auto-regressive way.',
    'As a result, this kind of traditional ﬁne-tuning approach demonstrates relatively weak performance when solving downstream language understanding tasks.',
    'in order to solve the above problems, we propose a uniﬁed framework named ERNIE 3.0 for pre-training large-scale knowledge enhanced models. ',
    'It fuses auto-regressive network and auto-encoding network, so that the trained model can be easily tailored for both natural language understanding and generation tasks with zero-shot learning, few-shot learning or ﬁne-tuning.',
    'We trained the model with 10 billion parameters on a 4TB corpus consisting of plain texts and a large-scale knowledge graph.',
    'Empirical results show that the model outperforms the state-of-the-art models on 54 Chinese NLP tasks, and its English version achieves the ﬁrst place on the SuperGLUE [3] benchmark (July 3, 2021), surpassing the human performance by +0.8% (90.6% vs. 89.8%)'
]  #data from ERNIE3.0 paper abstract

inputs = tokenizer(raw_inputs, padding = True, truncation = True, return_tensors = 'pt') # return pytorch format tensor, in the representation of ids

print(inputs['input_ids'][0]) # get the ids of the first sentence

sentence = tokenizer.decode(inputs['input_ids'][0]) # back to the words of first sentence
print(sentence)

