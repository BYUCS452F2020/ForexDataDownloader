import unittest
from Oanda.APIServices.historical_data_downloader import HistoricalDataDownloader


class HistoricalDataDownloaderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.historical_data_downloader = HistoricalDataDownloader()

    def test_invalid_currency_pair(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('hammy wammy', ['ask'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid currency pair')

    def test_invalid_candle_type(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', ['ask', 'hello'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid candle type')

    def test_invalid_time_frame_granularity(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', ['ask'], '10',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid time frame granularity')

    def test_invalid_from_time(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', ['ask'], 'H1',
                                                                                     '2020-09-15 00:00:',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid from/to date')

    def test_invalid_to_time(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', ['ask'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 :00:00')

        self.assertEqual(error_message, 'Invalid from/to date')

    def test_bid_success(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', ['bid'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertIsNotNone(candles)

    def test_ask_success(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', ['ask'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertIsNotNone(candles)

    def test_mid_success(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', ['mid'], 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertIsNotNone(candles)

    def test_multiple_candle_type_success(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', ['ask', 'bid', 'mid'],
                                                                                     'H1', '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertIsNotNone(candles)

    def test_candle_length(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', ['ask', 'bid', 'mid'],
                                                                                     'H1', '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(len(candles), 12)


if __name__ == '__main__':
    unittest.main()
