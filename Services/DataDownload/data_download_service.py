import pandas as pd
import numpy as np
from datetime import datetime
from Oanda.APIServices.historical_data_downloader import HistoricalDataDownloader


class DataDownloadService:
    def __init__(self):
        self.oanda_data_downloader = HistoricalDataDownloader()

    def get_historical_data(self, currency_pair, candle_types, time_frame_granularity, from_time, to_time):
        candles, error_message = self.oanda_data_downloader.get_historical_data(currency_pair, candle_types,
                                                                                time_frame_granularity, from_time,
                                                                                to_time)

        if error_message is not None:
            return None, error_message

        np_data = []
        column_names = ['Date']
        i = 0

        for candle in candles:
            curr_date = candle.time
            curr_date = datetime.utcfromtimestamp(int(float(curr_date))).strftime('%Y-%m-%d %H:%M:%S')
            row = [curr_date]

            if 'bid' in candle_types:
                row.extend([float(candle.bid.o), float(candle.bid.h), float(candle.bid.l), float(candle.bid.c)])

                if i == 0:
                    column_names.extend(['Bid_Open', 'Bid_High', 'Bid_Low', 'Bid_Close'])

            if 'ask' in candle_types:
                row.extend([float(candle.ask.o), float(candle.ask.h), float(candle.ask.l), float(candle.ask.c)])

                if i == 0:
                    column_names.extend(['Ask_Open', 'Ask_High', 'Ask_Low', 'Ask_Close'])

            if 'mid' in candle_types:
                row.extend([float(candle.mid.o), float(candle.mid.h), float(candle.mid.l), float(candle.mid.c)])

                if i == 0:
                    column_names.extend(['Mid_Open', 'Mid_High', 'Mid_Low', 'Mid_Close'])

            np_data.append(row)
            i += 1

        np_data = np.array(np_data)
        candles_df = pd.DataFrame(np_data, columns=column_names)

        return candles_df, None
