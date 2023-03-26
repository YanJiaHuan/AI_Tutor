# NLP_CapstoneProject_ISS
The objective of this project is to develop an intelligent tutor system to assist human to perform the  education activities. 
## ==安装huggingface==
conda install -c huggingface transformers
这个得在pytorch或者tensorflow支持下运行
根据自己电脑去https://pytorch.org/get-started/locally/安装pytorch
conda install pytorch torchvision torchaudio -c pytorch  

## ==一些函数==
- run 'clear_file.py' to clear the file in the folder
- run 'chat_paper.py' to get papers from arxiv according to filter content and keywords
- run 'chat_paper.py' to get papers from arxiv according to filter content and keywords  
Notice: It will first download the papers to local folder, then create folder to keep all the .md files, 
which contains the response from chatgppt
- run 'data_extract.py' to parse pdf and extract summary,methods
, conclusion from .md and combine them into a .json file