FROM nginx

COPY .config/Blog.conf /etc/nginx/conf.d/Blog.conf

#  sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
#  && apt-get clean \

RUN sed -i "s@http://deb.debian.org@https://mirrors.aliyun.com@g" /etc/apt/sources.list \
    && apt clean \
    && apt update \
    && rm /etc/nginx/conf.d/default.conf \
    # https
    && apt install -y --allow-unauthenticated certbot python3-certbot-nginx \
    # vim
    && apt install -y vim \
    # ps
    && apt install -y procps \
    # 时区
    && rm /etc/localtime \
    && cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime

