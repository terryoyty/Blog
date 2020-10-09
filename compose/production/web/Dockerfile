FROM python

COPY .config/requirements.txt /home/project/Blog/
COPY .config/django-mysql-base /home/project/Blog/
COPY .config/django-mysql-operations /home/project/Blog/
COPY .config/mistune.py /home/project/Blog/

COPY .config/mdeditor/image-handle-paste.js /home/project/Blog/
COPY .config/mdeditor/markdown.html /home/project/Blog/


WORKDIR /home/project/Blog/
RUN sed -i "s@http://deb.debian.org@https://mirrors.aliyun.com@g" /etc/apt/sources.list \
    && apt-get clean \
    && apt-get update \
    && pip install -r requirements.txt -i https://pypi.douban.com/simple/ \
    # 全文检索
    && pip install django-haystack -i https://pypi.douban.com/simple/ \
    && pip install "elasticsearch>=2,<3" -i https://pypi.douban.com/simple/ \
    # mysql版本报错忽略
    && rm /usr/local/lib/python3.8/site-packages/django/db/backends/mysql/base.py \
    && mv django-mysql-base /usr/local/lib/python3.8/site-packages/django/db/backends/mysql/base.py \
    # mysql解码问题
    && rm /usr/local/lib/python3.8/site-packages/django/db/backends/mysql/operations.py \
    && mv django-mysql-operations /usr/local/lib/python3.8/site-packages/django/db/backends/mysql/operations.py \
    # mysql认证问题（RuntimeError: cryptography is required for sha256_password or caching_sha2_p）
    && pip install cryptography -i https://pypi.douban.com/simple/ \
    # vim
    && apt-get install -y vim \
    # 时区
    && rm /etc/localtime \
    && cp /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime \
    # markdown
    && rm /usr/local/lib/python3.8/site-packages/mistune.py \
    && mv mistune.py /usr/local/lib/python3.8/site-packages/mistune.py \
    # mdeditor粘贴上传插件
    && mkdir /usr/local/lib/python3.8/site-packages/mdeditor/static/mdeditor/js/plugins/image-handle-paste \
    && mv image-handle-paste.js /usr/local/lib/python3.8/site-packages/mdeditor/static/mdeditor/js/plugins/image-handle-paste/image-handle-paste.js \
    && rm /usr/local/lib/python3.8/site-packages/mdeditor/templates/markdown.html \
    && mv markdown.html /usr/local/lib/python3.8/site-packages/mdeditor/templates/markdown.html

