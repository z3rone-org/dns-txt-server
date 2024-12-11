FROM python:3.11-slim
WORKDIR /app
COPY dns_server.py ./
RUN pip install dnslib
RUN mkdir /app/dns_txt_records
EXPOSE 53/udp
ENV LISTEN_IP="0.0.0.0"
ENV LISTEN_PORT="53"
ENV RECORD_DIR="/app/dns_txt_records"
VOLUME /app/dns_txt_records
CMD ["python", "dns_server.py"]
