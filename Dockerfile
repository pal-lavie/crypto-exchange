FROM python:3.6-slim-buster

WORKDIR /crypto_exchange

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "4000"]

ENTRYPOINT ["python", "crypto_exchange/app.py"]