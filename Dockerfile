FROM python:3.11.4-slim
ENV PYTHONUNBUFFERERD 1 
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt 
RUN rm requirements.txt 
COPY . /code/

