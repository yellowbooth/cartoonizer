FROM huggingface/transformers-pytorch-gpu:4.26.1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

CMD ["runpod", "start"]
