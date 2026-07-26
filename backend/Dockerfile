FROM python:3.12-slim

# Prevent Python from buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    tesseract-ocr \
    tesseract-ocr-fra \
    tesseract-ocr-eng \
    poppler-utils \
    libreoffice \
    libgl1 \
    libglib2.0-0 \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 8000

COPY start.sh /app/start.sh

RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]