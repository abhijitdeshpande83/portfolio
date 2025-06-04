FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /portfolio

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    cron \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
COPY libs/ libs/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install ./libs/rag_pipeline-2.0-py3-none-any.whl

# Copy all project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Copy and set startup script
COPY start.sh /start.sh
COPY crontab.txt /etc/cron.d/my-cron-job

# Make scripts executable
RUN chmod +x /start.sh
RUN chmod +x /portfolio/cleanup.sh

# Add crontab and apply it
RUN chmod 0644 /etc/cron.d/my-cron-job
RUN crontab /etc/cron.d/my-cron-job

# Run the startup script
CMD ["/start.sh"]