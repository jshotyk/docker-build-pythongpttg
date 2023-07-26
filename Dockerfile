FROM python:3.10
ADD main.py .

RUN pip install python-telegram-bot==13 openai

CMD ["python", "main.py"]