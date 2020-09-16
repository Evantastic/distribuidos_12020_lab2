FROM python:buster
COPY requirements.txt .
RUN git clone https://github.com/Evantastic/distribuidos_common.git \
    && pip install -r distribuidos_common/requirements.txt \
    && pip install ./distribuidos_common \
    && pip install -r requirements.txt
WORKDIR /app