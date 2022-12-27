FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /assingment-online
WORKDIR /assingment-online
RUN pip install --upgrade pip
COPY requirements.txt /assingment-online/

RUN pip install -r requirements.txt
COPY . /assingment-online/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]