FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "bot/__main__.py:app", "--host", "0.0.0.0", "--port", "7860"]
