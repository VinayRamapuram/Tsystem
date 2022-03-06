import pytest
from exercise_one import get_exchange_rate, get_raw_data
from exercise_two import get_transactions, get_symmetric_identifier


@pytest.mark.parametrize('source', ['GBP'])
def test_currency_conversion_valid(source):
    """
    Validating Columns for valid Data
    :param source: GBP
    :return:
    """
    data = get_exchange_rate(source=source)
    actual_columns = list(data.columns)
    excepted_columns = ['TIME_PERIOD', 'OBS_VALUE']
    assert actual_columns == excepted_columns


@pytest.mark.parametrize('source', ['TSYSTEM'])
def test_currency_conversion_invalid(source):
    """
    Validating type of response for invalid Data
    :param source: TSYSTEM
    :return:
    """
    data = get_exchange_rate(source=source)
    assert type(data) == str


@pytest.mark.parametrize('identifier', ['M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N'])
def test_get_raw_data_valid(identifier):
    """
    Validating Columns for valid Data
    :param source: 'M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N'
    :return:
    """
    data = get_raw_data(identifier=identifier)
    actual_columns = list(data.columns)
    excepted_columns = ['TIME_PERIOD', 'OBS_VALUE']
    assert actual_columns == excepted_columns


@pytest.mark.parametrize('identifier', ['M.N.I8'])
def test_get_raw_data_invalid(identifier):
    """
    Validating Columns for valid Data
    :param source: 'M.N.I8'
    :return:
    """
    data = get_raw_data(identifier=identifier)
    assert type(data) == str

# Exercise two


@pytest.mark.parametrize('identifier', ['Q.DE.N.A.A20.A.1.AT.2000.Z01.E'])
def test_get_transactions(identifier):
    """
    Transaction data can be retrieved from the REST API of the European Central Bank, using the URL below:
   https://sdw-wsrest.ecb.europa.eu/service/data/BSI/Q.HR.N.A.A20.A.1.AT.2000.Z01.E?detail=dataonly
    Validating columns
    identifier: Q.DE.N.A.A20.A.1.AT.2000.Z01.E
    """
    data = get_transactions(identifier=identifier)
    actual_columns = list(data.columns)
    excepted_columns = ['IDENTIFIER', 'TIME_PERIOD', 'OBS_VALUE']
    assert actual_columns == excepted_columns



