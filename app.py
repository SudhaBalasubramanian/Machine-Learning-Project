from flask import Flask

app=Flask(__name__)

from housing.logger import logging
from housing.exception import HousingException
import sys

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("Testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("Testing logging module")
    return "test CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)