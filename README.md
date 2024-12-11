# Usage

- Run the server. Use envvars `RECORD_DIR`, `LISTEN_IP` and `LISTEN_PORT` for configuration
- Add an NS record for the `_acme-challenge` subdomain pointing to the TXT DNS server's domain
- Run certbot with the following hook:

```
certbot certonly \
  --manual \
  --manual-auth-hook 'echo ${CERTBOT_VALIDATION} > /path/to/dns_txt_records/_acme-challenge.${CERTBOT_DOMAIN}' \
  --preferred-challenges=dns \
  -d $DOMAIN \
  --email $EMAIL_ADDRESS \
  --agree-tos
```
