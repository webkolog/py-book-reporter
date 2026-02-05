# Hafif bir Python imajı
FROM python:3.10-slim

# Çalışma dizinini
WORKDIR /app

# Gerekli sistem paketlerini yükle (Pandas için gerekebilir)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Bağımlılıkları kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodlarını kopyala
COPY . .

# Flask'ın dış dünyadan erişilebilir olması için portu aç
EXPOSE 5000

# Uygulamayı çalıştır
CMD ["python", "book_reporter.py"]