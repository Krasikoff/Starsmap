FROM python:3.7-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY requirements.txt .
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip3 install -r requirements.txt --no-cache-dir
COPY app .
CMD ["gunicorn", "starsmap.wsgi:application", "--bind", "0:8000"]