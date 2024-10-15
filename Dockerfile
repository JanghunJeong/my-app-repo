FROM python:3.9-slim

WORKDIR /app

# 필요한 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# Flask 애플리케이션 실행
CMD ["python", "app.py"]

