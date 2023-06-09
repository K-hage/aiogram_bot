FROM python:3.10-slim

ENV HOME /code
WORKDIR $HOME

COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt

COPY . .

CMD python main.py