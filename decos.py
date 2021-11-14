import sys
import logging
import traceback
import inspect
import logs.config_server_log
import logs.config_client_log

if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func):
    def log_saving(*args, **kwargs):
        result = func(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func.__module__}')
        return result
    return log_saving
