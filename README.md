# gracc-raw

The gracc-raw agent processes raw accounting records (e.g. from the
gracc-collector) from a RabbitMQ queue, enriches and normalizes them,
and indexes them into Elasticsearch.

Currently this agent is a `logstash` config. The `input` and `output`
blocks will need to be customized to point to the RabbitMQ and 
Elasticsearch hosts with any needed auth and config settings.

To use systemd instances, copy the `gracc-raw.conf` file to
`/etc/gracc/gracc-raw.<instance>.conf`; then you can run 
`systemctl start gracc-raw@<instance>` to start a `gracc-raw`
logstash instance with that config.
