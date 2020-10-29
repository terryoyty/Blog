from qiniu import Auth, put_file, put_data
from common.log import logger
from common.o_uuid import get_uuid


class QiniuYun:

    AccessKey = 'KVX9hH5kmbDw9BWRLpXEbX4p55-UqBVGH6M2GGZX'
    SecretKey = 'T9PsCCgKhjY-Fhhne8UqjJwoB6nQpHAdUwe4G9ZD'
    # 构建鉴权对象
    q = Auth(AccessKey, SecretKey)
    # 要上传的空间
    BucketName = 'terry-arsenal'
    Url = 'http://cdn.terryoyty.com/'

    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    # 创建上传后保存的文件名
    @staticmethod
    def _create_filename():
        random_str = get_uuid()
        filename = random_str + '.png'

        return filename

    # 生成上传 Token，可以指定过期时间等
    @classmethod
    def _get_token(cls, filename):
        """

        :param filename: 上传后保存的文件名
        :return:
        """
        token = cls.q.upload_token(cls.BucketName, filename, 60)

        return token

    # 上传文件
    @classmethod
    def upload(cls, filedata, filename=None):
        """

        :param filedata: 要上传文件数据
        :param filename: 上传后保存的文件名，默认为None不指定文件名，由七牛云生成文件名
        :return:
        """
        token = cls._get_token(filename)
        ret, info = put_data(token, filename, filedata)

        if not info.ok():
            logger.error(info)
            raise

        file_url = cls.Url + ret.get('hash')

        return file_url


if __name__ == '__main__':
    qny = QiniuYun()
    url = qny.upload(r'F:\SpiderProject\TikTokSpiderApi\static\user\images\success.png')
    print(url)