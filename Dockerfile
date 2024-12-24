FROM python:3.12.3-slim

RUN apt update -y

RUN mkdir app

COPY ./static /app/static
COPY ./templates /app/templates
COPY ./req.txt /app
COPY ./main.py /app
COPY ./models.py /app

WORKDIR /app

RUN pip install --no-cache-dir -r req.txt

# ENTRYPOINT [ "tail", "-f", "/dev/null" ]
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]