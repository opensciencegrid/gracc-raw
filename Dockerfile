FROM logstash:2.3

COPY gracc-raw.conf gracc-raw-template.json /etc/gracc-stash/

CMD ["-f", "/etc/gracc-stash/gracc-raw.conf","--allow-env"]
