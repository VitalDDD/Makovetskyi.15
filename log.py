import logging
import server


def main():

    logger = logging.getLogger("exampleApp")
    logger.setLevel("INFO")

    # create the logging file handler
    fhand = logging.FileHandler("snake.log")

    form = logging.Formatter('{asctime} - {name} - {levelname} - {message}', style='{')
    fhand.setFormatter(form)

    # add handler to logger object
    logger.addHandler(fhand)

    logger.info("Program server started")
    server.serv()
    logger.info("Program server finished")


if __name__ == "__main__":
    main()