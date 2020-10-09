FROM delron/elasticsearch-ik:2.4.6-1.0

COPY .config/elasticsearch.yml /usr/share/elasticsearch/config/

RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/config/elasticsearch.yml

USER elasticsearch