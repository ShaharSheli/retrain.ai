FROM python:3.7-slim

COPY requirements.txt /opt/base_docker/

COPY input_data /opt/base_docker/

COPY output_data /opt/base_docker/

RUN pip install -r /opt/base_docker/requirements.txt

WORKDIR /opt/base_docker/
