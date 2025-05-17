FROM runpod/pytorch:2.0.1-cuda11.7

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

CMD ["runpod", "start"]
