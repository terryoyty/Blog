FROM mysql

COPY .config/mysql.cnf /etc/mysql/conf.d/mysql.cnf

RUN rm /etc/localtime \
    && cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime \