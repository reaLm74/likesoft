FROM python:3.9-slim
WORKDIR /likesoft
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
