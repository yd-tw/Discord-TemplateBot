import logging as log

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
log.basicConfig(level=log.DEBUG, filename='.log', filemode='a', format=FORMAT, encoding='utf-8')

def main():
    log.debug('這是一條DEBUG紀錄')
    log.info('這是一條INFO紀錄')
    log.warning('這是一條WARNING紀錄')
    log.error('這是一條ERROR紀錄')
    log.critical('這是一條CRITICAL紀錄')

if __name__ == "__main__":
    main()