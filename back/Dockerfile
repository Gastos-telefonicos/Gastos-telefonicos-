FROM python:3.9
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN  pip install --default-timeout=100 -r requirements.txt
RUN mkdir /src
RUN mkdir /data
COPY /src /app/src
COPY /data /app/data
COPY /* /app/
ENTRYPOINT ["python3"]
CMD ["app.py"]