FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py main.py
COPY customer_list.csv customer_list.csv
CMD ["python", "-u", "main.py"]