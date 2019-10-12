FROM python:3.6

LABEL maintainer="Jose Miguel Miranda Sanabria"

RUN    apt-get update && apt-get install -y libldap2-dev libsasl2-dev
COPY requirements.txt /tmp/requirements.txt 
RUN pip install -r /tmp/requirements.txt

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
