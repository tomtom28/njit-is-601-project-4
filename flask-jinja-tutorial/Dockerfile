FROM python:3.8

EXPOSE 5001

WORKDIR /flask-jinja-tutorial

COPY requirements.txt /flask-jinja-tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-jinja-tutorial

CMD python routes.py