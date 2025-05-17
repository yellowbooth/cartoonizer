FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04

# Set up system
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 python3-pip git wget curl unzip \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3 as default
RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app
COPY . .

# Install Python packages
RUN pip install --upgrade pip \
 && pip install torch torchvision \
 && pip install -r requirements.txt

CMD ["runpod", "start"]
