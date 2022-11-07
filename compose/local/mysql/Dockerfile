FROM mysql:8.0.28

COPY .config/mysql.cnf /etc/mysql/conf.d/mysql.cnf

RUN rm /etc/localtime \
    && cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime \