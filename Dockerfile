FROM python:3.7

RUN pip install ddtrace flask \
    && mkdir /app

COPY app.py /app/
WORKDIR /app

CMD ["ddtrace-run", "python", "app.py"]
