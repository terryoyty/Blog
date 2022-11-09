FROM nginx

COPY .config/Blog.conf /etc/nginx/conf.d/Blog.conf

#  sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
#  && apt-get clean \

RUN apt-get update \
    && rm /etc/nginx/conf.d/default.conf \
    # https
    && apt-get install -y --allow-unauthenticated certbot python3-certbot-nginx \
    # vim
    && apt-get install -y vim \
    # ps
    && apt-get install -y procps \
    # 时区
    && rm /etc/localtime \
    && cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime

