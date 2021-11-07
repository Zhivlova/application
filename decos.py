import sys
import logging
import traceback
import inspect
import logs.config_server_log
import logs.config_client_log

if sys.argv[0].find('client') == -1:
    SERVER_LOGGER = logging.getLogger('server')
else:
    SERVER_LOGGER = logging.getLogger('client')


def log(func):
    def log_saving(*args, **kwargs):
        result = func(*args, **kwargs)
        SERVER_LOGGER.debug(f'Вызвана функция {func.__name__} с параметрами {args}, {kwargs}, '
                            f'Вызов из модуля {func.__module__}. Вызов из'
                            f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
                            f'вызов из функции {inspect.stack()[1][3]}')
        return result

    return log_saving()
