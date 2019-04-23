FROM python:3.7

RUN apt-get update -qq
RUN apt-get install -y --no-install-recommends

ADD . app
WORKDIR /app

# Pythonで利用するライブラリをインストール
RUN pip install -r ./requirements.txt
