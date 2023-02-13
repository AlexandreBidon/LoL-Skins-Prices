FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api /code/api
COPY ./database /code/database
COPY ./user /code/user
COPY ./mail_service /code/mail_service
COPY ./main.py /code/main.py

CMD ["python", "./main.py"]