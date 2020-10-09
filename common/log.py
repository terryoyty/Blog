import logging
import os
import coloredlogs
from Blog.settings.common import BASE_DIR

LEVEL = logging.WARNING


# 创建Logger
logger = logging.getLogger(__name__)
logger.setLevel(LEVEL)


"""
Handler
"""
# 终端Handler
coloredlogs.install()
# consoleHandler = logging.StreamHandler()
# consoleHandler.setFormatter(formatter)
# logger.addHandler(consoleHandler)

# 文件Handler
log_path = os.path.join(BASE_DIR, 'log/run.log')
fileHandler = logging.FileHandler(log_path, mode='a', encoding='UTF-8')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s:%(funcName)s[%(process)d] %(message)s')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)


if __name__ == '__main__':
    # 打印日志
    logger.debug('debug 信息')
    logger.info('info 信息')
    logger.warning('warn 信息')
    logger.error('error 信息')
    logger.critical('critical 信息')
