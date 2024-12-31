FROM python:3.11-slim
WORKDIR /app
COPY dns_txt ./
COPY certbot_cmd ./
COPY auth_hook ./
RUN chmod +x dns_txt
RUN chmod +x certbot_cmd
RUN chmod +x auth_hook
RUN pip install dnslib
RUN mkdir /app/dns_txt_records
EXPOSE 53/udp
ENV PATH=$PATH:/app
ENV LISTEN_IP="0.0.0.0"
ENV LISTEN_PORT="53"
ENV RECORD_DIR="/app/dns_txt_records"
VOLUME /app/dns_txt_records
ENTRYPOINT []
CMD ["dns_txt"]
