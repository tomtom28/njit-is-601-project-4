FROM python:3.8

EXPOSE 5004

WORKDIR /app5

COPY requirements.txt /app5
RUN pip install  -r requirements.txt --upgrade pip

COPY . /app5

CMD python app.py