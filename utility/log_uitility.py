import  os
import  json
import  logging
import  logging.config
import sys
import time
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler


def setup_logging(default_path = "logconfig.conf",default_level = logging.DEBUG,env_key = "LOG_CFG"):
    path = default_path
    value = os.getenv(env_key,None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path,"r") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level = default_level)


class MyRotatingFileHandler(TimedRotatingFileHandler):
    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.rotation_filename(self.baseFilename + "." +
                                     time.strftime(self.suffix, timeTuple))
        if os.path.exists(dfn):
            os.remove(dfn)
        self.rotate(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        #If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:           # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt







setup_logging(sys.path[0]+"/logconfig.conf")
while True:
    logging.info('1  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('2  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('3  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    logging.info('sleep 60s')
    time.sleep(60)

