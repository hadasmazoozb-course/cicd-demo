# שלב 1: בנייה ובדיקות (המטבח)
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# הרצת הבדיקות כחלק מתהליך הבנייה
RUN python test_app.py

# שלב 2: הרצה (הדוכן)
FROM python:3.9-slim
WORKDIR /app
# העתקת החבילות שהותקנו בשלב הקודם
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app/app.py .
EXPOSE 5000
CMD ["python", "app.py"]
