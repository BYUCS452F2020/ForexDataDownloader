import unittest
from Services.DataDownload.data_download_service import DataDownloadService


class DataDownloadServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data_download_service = DataDownloadService()

    def test_invalid_currency_pair(self):
        candles_df, error_message = self.data_download_service.get_historical_data('hammy wammy', ['ask'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid currency pair')

    def test_invalid_candle_type(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['ask', 'hello'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid candle type')

    def test_invalid_time_frame_granularity(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['ask'], '10',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid time frame granularity')

    def test_invalid_from_time(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['ask'], 'H1',
                                                                                     '2020-09-15 00:00:',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid from/to date')

    def test_invalid_to_time(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['ask'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 :00:00')

        self.assertEqual(error_message, 'Invalid from/to date')

    def test_bid_success(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['bid'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertIsNotNone(candles_df)

    def test_ask_success(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['ask'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertIsNotNone(candles_df)

    def test_mid_success(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['mid'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertIsNotNone(candles_df)

    def test_multiple_candle_type_success(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['ask', 'bid', 'mid'],
                                                                                     'H1', '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertIsNotNone(candles_df)

    def test_candle_df_length(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['ask', 'bid', 'mid'],
                                                                                     'H1', '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(len(candles_df), 12)

    def test_candle_df_shape(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['ask', 'bid', 'mid'],
                                                                                     'H1', '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(candles_df.shape, (12, 13))

    def test_candle_df_column_names(self):
        candles_df, error_message = self.data_download_service.get_historical_data('EUR_USD', ['ask', 'bid'], 'H1',
                                                                                   '2020-09-15 00:00:00',
                                                                                   '2020-09-15 12:00:00')

        self.assertEqual(list(candles_df.columns), ['Date', 'Bid_Open', 'Bid_High', 'Bid_Low', 'Bid_Close', 'Ask_Open',
                                                    'Ask_High', 'Ask_Low', 'Ask_Close'])


if __name__ == '__main__':
    unittest.main()
