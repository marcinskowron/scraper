FROM python:3.9-slim

COPY ./fast_api.py /app/fast_api.py
COPY ./scraper.py /app/scraper.py
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "fast_api:app", "--host=0.0.0.0"]