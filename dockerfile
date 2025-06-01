FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /portfolio

# Copy requirements and install Python dependencies
COPY requirements.txt .

COPY libs/ libs/

RUN apt-get update && apt-get install -y default-jre

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install ./libs/rag_pipeline-1.0-py3-none-any.whl

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
