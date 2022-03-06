DEFAULT_SRC = 'GBP'
DEFAULT_TARGET = 'EUR'
URL = 'https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.{source}.{target}.SP00.A?detail=dataonly'\
    .format(source=DEFAULT_SRC, target=DEFAULT_TARGET)
