FROM python:3.7

RUN pip install flask \
    && mkdir /app

COPY app.py /app/
WORKDIR /app

CMD ["python", "app.py"]
