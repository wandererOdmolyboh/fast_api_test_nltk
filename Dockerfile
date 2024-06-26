FROM python:3.9

RUN mkdir /fast_api_nltk

ENV PYTHONPATH=/fast_api_nltk

WORKDIR /fast_api_nltk

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
