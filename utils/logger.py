# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:18:42 2022

@author: Accubits
"""

"""
Usage of logger
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
"""

import logging
import logging.config

logging.config.fileConfig( 'logging.ini' ,  defaults={ 'logfilename' : 'logs/esp_calculation_log.log' }, disable_existing_loggers=False)

logger = logging.getLogger('root')
