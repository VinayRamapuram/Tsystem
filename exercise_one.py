import urllib.request
import xmltodict
from utils import xml_to_pandas
import logging
from custom_logger import setup_logger


exercise_one_logger = setup_logger("exercise_one_logger", "exercise_one_logger.log")


def get_exchange_rate(source: str, target: str = "EUR"):
    """
    Exchange rate data can be retrieved from the REST API of the European Central Bank, using the URL below:
    https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.GBP.EUR.SP00.A?detail=dataonly

    Reads XML data, extract generic:Obs sub child and make DF.
    Iterate each row of DF collect value of time period and obs value.
    Convert OBS value from obj to float.

    :param source: GBP or PLN (must be valid source)
    :param target: EUR
    :return: Data frame or exception message
    """
    try:
        url = 'https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.{source}.{target}.SP00.A?detail=dataonly' \
                .format(source=source, target=target)

        exercise_one_logger.info("Hitting URL")
        web_url = urllib.request.urlopen(url)
        data = xmltodict.parse(web_url)
        exercise_one_logger.info("Calling  xml_to_pandas function to get TIME_PERIOD and OBS_VALUE df")
        final_df = xml_to_pandas(data)
        exercise_one_logger.info(final_df)
        return final_df

    except Exception as error:
        logging.error(repr(error))
        return 'Caught this error: ' + repr(error)


def get_raw_data(identifier: str):
    try:
        url = "https://sdw-wsrest.ecb.europa.eu/service/data/BP6/{}?".format(identifier)
        exercise_one_logger.info("Hitting Identifier URL")
        web_url = urllib.request.urlopen(url)
        data = xmltodict.parse(web_url)
        exercise_one_logger.info("Calling xml_to_pandas function to get TIME_PERIOD and OBS_VALUE df")
        df = xml_to_pandas(data)
        exercise_one_logger.info(df)
        return df
    except Exception as error:
        return 'Caught this error: ' + repr(error)


if __name__ == "__main__":
    rate_data_df = get_exchange_rate(source="GBP")
    get_raw_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N")

