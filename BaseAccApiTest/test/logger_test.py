from BaseAccApiTest.utils import logger

logger.setup_logger('DEBUG')


logger.log_debug('debug信息')
logger.log_info('info信息')
logger.log_warning('warning信息')
logger.log_error('error信息')
logger.log_critical('critical信息')
