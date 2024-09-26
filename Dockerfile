FROM python:3.9-slim

WORKDIR /app

# remember first prepare the config.json with OPENAI_API_KEY & SYSTEM_PROMPT
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]

