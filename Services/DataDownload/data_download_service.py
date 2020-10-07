import pandas as pd
import numpy as np
from datetime import datetime
from Oanda.APIServices.historical_data_downloader import HistoricalDataDownloader


"""
A service class that will call the data downloader class to get historical currency data and then format it as a 
data frame
"""
class DataDownloadService:
    """
    The init function creates a historical data downloader object
    """
    def __init__(self):
        self.oanda_data_downloader = HistoricalDataDownloader()

    """
    Helper function for formatting candle data once it is retrieved from the Oanda API

    Parameters:
        candles (list): List containing the data for each candle
        candle_types (str): The type of candles that were retrieved (bid, ask, and/or mid)

    Returns:
        A formatted data frame of the candles
    """
    def _format_candle_data(self, candles, candle_types):
        # Create an empty list that will hold each row of data
        np_data = []

        # Instantiate the list of data frame column names
        column_names = ['Date']
        i = 0

        # Iterate through each candle in the candle/currency data
        for candle in candles:
            # Grab the date of the current candle and it add it to a new row of data
            curr_date = candle.time
            curr_date = datetime.utcfromtimestamp(int(float(curr_date))).strftime('%Y-%m-%d %H:%M:%S')
            row = [curr_date]

            # If bid prices were asked for, add the open, high, low, and close bid prices to the row
            if 'bid' in candle_types:
                row.extend([float(candle.bid.o), float(candle.bid.h), float(candle.bid.l), float(candle.bid.c)])

                # Update the list of column names if we're on the first iteration
                if i == 0:
                    column_names.extend(['Bid_Open', 'Bid_High', 'Bid_Low', 'Bid_Close'])

            # If ask prices were asked for, add the open, high, low, and close ask prices to the row
            if 'ask' in candle_types:
                row.extend([float(candle.ask.o), float(candle.ask.h), float(candle.ask.l), float(candle.ask.c)])

                # Update the list of column names if we're on the first iteration
                if i == 0:
                    column_names.extend(['Ask_Open', 'Ask_High', 'Ask_Low', 'Ask_Close'])

            # If mid prices were asked for, add the open, high, low, and close mid prices to the row
            if 'mid' in candle_types:
                row.extend([float(candle.mid.o), float(candle.mid.h), float(candle.mid.l), float(candle.mid.c)])

                # Update the list of column names if we're on the first iteration
                if i == 0:
                    column_names.extend(['Mid_Open', 'Mid_High', 'Mid_Low', 'Mid_Close'])

            # Once all the values have been added to the current row, add the row to the overall list of data
            np_data.append(row)
            i += 1

        # Convert the list of data to a numpy array (needed to create a pandas data frame)
        np_data = np.array(np_data)

        # Use the numpy array of data and the column names to create a pandas data frame
        candles_df = pd.DataFrame(np_data, columns=column_names)

        # Return the formatted data frame
        return candles_df

    """
    This is the main function for grabbing historical data
    
    Parameters:
        currency_pair (str): The currency pair to grab data for
        candle_types (str): The type of candles to get (bid, ask, or mid)
        time_frame_granularity (str): The time frame to make each candle
        from_time (str): The first date/time to grab the candles from
        to_time (str): The last date/time to grab the candles from
        
    Returns:
        A data frame of the candles (null if the parameters are incorrect or if there was an error) and an error message 
        (null if the data retrieval was successful)
    """
    def get_historical_data(self, currency_pair, time_frame_granularity, from_time, to_time):
        # Call the Oanda data download service in order to get the historical currency data
        candles, error_message = self.oanda_data_downloader.get_historical_data(currency_pair, time_frame_granularity,
                                                                                from_time, to_time)

        # Return null for the candle data frame plus the error message if there was an error when retrieving the data
        if error_message is not None:
            return None, error_message

        # If there wasn't an error, format the historical currency/candle data as a data frame
        candle_types = ['bid', 'ask']
        candles_df = self._format_candle_data(candles, candle_types)

        # Return the data frame and null for the error message
        return candles_df, None
