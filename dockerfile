FROM python:3.11-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /portfolio

# Copy requirements and install Python dependencies
COPY requirements.txt .

COPY libs/ libs/

RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install ./libs/rag_pipeline-1.0-py3-none-any.whl

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
