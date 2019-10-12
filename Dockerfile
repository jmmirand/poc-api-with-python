FROM python:3.6

LABEL maintainer="Jose Miguel Miranda Sanabria"


ENV  http_proxy=http://proxyapps.gsnet.corp:80
ENV  https_proxy=http://proxyapps.gsnet.corp:80
ENV no_proxy=localhost,gsnet.corp,gsnetcloud.corp
ENV  PIP_CONFIG_FILE=pip.conf
ADD pip.conf pip.conf


RUN    apt-get update && apt-get install -y libldap2-dev libsasl2-dev
COPY requirements.txt /tmp/requirements.txt 
RUN pip install -r /tmp/requirements.txt



COPY src /src/

ENV http_proxy=
ENV https_proxy=
ENV no_proxy= 


EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
