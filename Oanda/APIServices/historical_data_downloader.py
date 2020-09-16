import v20
from datetime import datetime
from Oanda.Config.config import Config


"""
A class for downloading historical forex data
"""
class HistoricalDataDownloader:
    """
    The init function sets up valid values for various parameters that will need to be passed in before downloading
    historical data
    """
    def __init__(self):
        # A list of currency pairs that we can download data for
        self.available_currency_pairs = ['EUR_USD', 'GBP_USD', 'USD_JPY', 'USD_CHF','USD_CAD', 'AUD_USD', 'NZD_USD',
                                         'EUR_GBP', 'EUR_CHF', 'GBP_JPY']

        # A list of valid candle types
        self.available_candle_types = ['bid', 'ask', 'mid']

        # A list of valid time frame granularities (M1 = 1 minute, H4 = 4 hours, W = week, etc.)
        self.available_time_frame_granularities = ['M1', 'M5', 'M15', 'M30', 'H1', 'H4', 'D1', 'W', 'M']

    """
    This is a helper function that will make sure the parameters passed to the historical data download function are 
    valid
    
    Parameters:
        currency_pair (str): The currency pair to grab data for
        candle_types (str): The type of candles to get (bid, ask, or mid)
        time_frame_granularity (str): The time frame to make each candle
        from_time (str): The first date/time to grab the candles from
        to_time (str): The last date/time to grab the candles from
        
    Returns:
        A boolean (true if the parameters passes, false otherwise) and an error message (null if the parameters pass)
    """
    def _check_historical_data_parameters(self, currency_pair, candle_types, time_frame_granularity, from_time, to_time):
        if currency_pair not in self.available_currency_pairs:
            return False, 'Invalid currency pair'

        if not set(candle_types).issubset(set(self.available_candle_types)):
            return False, 'Invalid candle type'

        if time_frame_granularity not in self.available_time_frame_granularities:
            return False, 'Invalid time frame granularity'

        try:
            datetime.strptime(from_time, '%Y-%m-%d %H:%M:%S')
            datetime.strptime(to_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return False, 'Invalid from/to date'

        return True, None

    """
    This is the main function for grabbing historical data
    
    Parameters:
        currency_pair (str): The currency pair to grab data for
        candle_types (str): The type of candles to get (bid, ask, or mid)
        time_frame_granularity (str): The time frame to make each candle
        from_time (str): The first date/time to grab the candles from
        to_time (str): The last date/time to grab the candles from
        
    Returns:
        A list of the candles (null if the parameters are incorrect or if there was an error) and an error message 
        (null if the data download was successful)
    """
    def get_historical_data(self, currency_pair, candle_types, time_frame_granularity, from_time, to_time):
        valid_params, error_message = self._check_historical_data_parameters(currency_pair, candle_types,
                                                                             time_frame_granularity, from_time,
                                                                             to_time)

        if not valid_params:
            return None, error_message

        api_context = v20.Context(
            Config.get_host_name(),
            Config.get_port(),
            Config.get_ssl(),
            application="sample_code",
            token=Config.get_api_token(),
            datetime_format=Config.get_date_format()
        )

        kwargs = {}

        kwargs['granularity'] = time_frame_granularity
        kwargs['fromTime'] = api_context.datetime_to_str(datetime.strptime(from_time, '%Y-%m-%d %H:%M:%S'))
        kwargs['toTime'] = api_context.datetime_to_str(datetime.strptime(to_time, '%Y-%m-%d %H:%M:%S'))

        for candle_type in candle_types:
            if candle_type == 'bid':
                kwargs['price'] = 'B' + kwargs.get('price', '')

            elif candle_type == 'ask':
                kwargs['price'] = 'A' + kwargs.get('price', '')

            elif candle_type == 'mid':
                kwargs['price'] = 'M' + kwargs.get('price', '')

        response = api_context.instrument.candles(currency_pair, **kwargs)

        if response.status != 200:
            return None, response + '\n' + response.body

        return response.get("candles", 200), None
