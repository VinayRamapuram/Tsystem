import urllib.request
import xmltodict
from utils import xml_to_pandas
import logging
from custom_logger import setup_logger


exercise_two_logger = setup_logger("exercise_two_logger", "exercise_two_logger.log")


def get_transactions(identifier: str):
    """
    Transaction data can be retrieved from the REST API of the European Central Bank, using the URL below:
   https://sdw-wsrest.ecb.europa.eu/service/data/BSI/Q.HR.N.A.A20.A.1.AT.2000.Z01.E?detail=dataonly


    Reads XML data, extract generic:Obs sub child and make DF.
    Iterate each row of DF collect value of time period and obs value.
    Convert OBS value from obj to float.

    identifier: Q.DE.N.A.A20.A.1.AT.2000.Z01.E
    """
    try:
        url = "https://sdw-wsrest.ecb.europa.eu/service/data/BSI/{}?detail=dataonly".format(identifier)
        exercise_two_logger.info("Hitting URL")
        web_url = urllib.request.urlopen(url)
        data = xmltodict.parse(web_url)
        exercise_two_logger.info("Calling  xml_to_pandas function to get TIME_PERIOD and OBS_VALUE df")
        final_df = xml_to_pandas(data)
        exercise_two_logger.info("Inserting IDENTIFIER data at 0th position")
        final_df.insert(0, 'IDENTIFIER', identifier)
        exercise_two_logger.info(final_df)
        return final_df

    except Exception as error:
        logging.error(repr(error))
        return 'Caught this error: ' + repr(error)


def get_symmetric_identifier(identifier: str,  swap_components: dict) -> str:
    """

    :param identifier: Q.HR.N.A.A20.A.1.AT.2000.Z01.E,
    :param swap_components: swapping appropriate components
    :return: The function should return a new identifier, obtained from the provided one, by swapping components, as
    indicated by the key-value pairs in the provided dictionary. The pairs represent 0-based indices of
components to swap.
    """
    try:
        exercise_two_logger.info("Before Swapping of components {}".format(identifier))

        lst_comps = identifier.split(".")
        for k, v in swap_components.items():
            lst_comps[k],  lst_comps[v] = lst_comps[v],  lst_comps[k]

        swap_identifier = ".".join(i for i in lst_comps)
        exercise_two_logger.info("After Swapping of components {}".format(swap_identifier))
        return swap_identifier

    except Exception as error:
        logging.error(repr(error))
        return 'Caught this error: ' + repr(error)


if __name__ == "__main__":
    get_transactions("Q.HR.N.A.A20.A.1.AT.2000.Z01.E")
    get_symmetric_identifier("Q.HR.N.A.A20.A.1.AT.2000.Z01.E", {1: 7, 2: 3})

