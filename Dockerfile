FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV TZ=Indian/Reunion

RUN apt update -yq \
&& apt-get upgrade -yq \
&& apt-get install curl -y \
&& apt-get install tzdata -y \
&& apt-get install python3 -y \
&& apt-get install python3-pip -y \
&& apt-get install nano -y \
&& apt-get install gcc -y \
&& apt-get install unixodbc -y \
&& apt-get install unixodbc-dev -y \
&& apt-get install libodbc1 odbcinst odbcinst1debian2 -y \
&& apt-get install --reinstall build-essential -y \
&& apt-get clean -y

ADD . /app/

WORKDIR /app

RUN dpkg -i ./resources/ibm-iaccess-1.1.0.15-1.0.amd64.deb

COPY ./resources/odbc_source.ini /etc/odbc.ini

RUN chmod 777 /etc/odbc.ini

RUN pip3 install -r requirements.txt

RUN rm /etc/localtime

RUN ln -s /usr/share/zoneinfo/Indian/Reunion /etc/localtime

EXPOSE 45888

CMD ["uvicorn", "main:app", "--port", "45888", "--host", "0.0.0.0"]