FROM python:3.10-bullseye
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "app:app"]