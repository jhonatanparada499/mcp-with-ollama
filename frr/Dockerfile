FROM frrouting/frr:v8.4.0

# install telnet
RUN apk add --no-cache busybox-extras

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
