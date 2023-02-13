import uvicorn
import logging
from api.web_service import WebService
from sys import stdout



def main():
    """
    Runs the web service
    """
    web_service = WebService()
    uvicorn.run(web_service.app, host="0.0.0.0", port=80)


if __name__ == "__main__":
    # Define logger
    logger = logging.getLogger('python_logs')

    logger.setLevel(logging.DEBUG) # set logger level
    logFormatter = logging.Formatter\
    ("%(name)-12s %(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s")
    consoleHandler = logging.StreamHandler(stdout) #set streamhandler to stdout
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    #logging.basicConfig(filename='info.log', level=logging.INFO)
    logger.info('API start')
    main()
    logger.info('API shutdown')