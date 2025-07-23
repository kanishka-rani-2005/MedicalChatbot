Medical Chatbot using LLAMA2


Create environment

```bash

conda create -p venv python=3.8 -y

```

Activate environment

```bash
conda activate venv
```


Install libraries

```bash
pip install -r requirements.txt
```



```ini

PINCONE_API_KEY='XXXXXXXXXXXXXXXXXXXXXXXXX'
```

### Download the quantize model from link provided 

```ini

llama-2-7b-chat.ggmlv3.q4_0.bin


https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

```

### Store vectors in Pinecone

```bash
python store_index.py
```


### Run the chatbot
```bash
python app.py
```

Now,
```bash

open up localhost:
```

### Techstack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone
- Huggingface Transformers
