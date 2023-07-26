FROM python:3.10-slim
ADD main.py .

RUN pip install python-telegram-bot==13 openai
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]
