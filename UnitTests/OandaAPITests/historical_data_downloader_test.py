import unittest
from Oanda.APIServices.historical_data_downloader import HistoricalDataDownloader


class HistoricalDataDownloaderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.historical_data_downloader = HistoricalDataDownloader()

    def test_invalid_currency_pair(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('hammy wammy', 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid currency pair')

    def test_invalid_time_frame_granularity(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', '10',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid time frame granularity')

    def test_invalid_from_time(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', 'H1',
                                                                                     '2020-09-15 00:00:',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(error_message, 'Invalid from/to date')

    def test_invalid_to_time(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD', 'H1',
                                                                                     '2020-09-15 00:00:00',
                                                                                     '2020-09-15 :00:00')

        self.assertEqual(error_message, 'Invalid from/to date')

    def test_valid_request(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD',
                                                                                     'H1', '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertIsNotNone(candles)

    def test_candle_length(self):
        candles, error_message = self.historical_data_downloader.get_historical_data('EUR_USD',
                                                                                     'H1', '2020-09-15 00:00:00',
                                                                                     '2020-09-15 12:00:00')

        self.assertEqual(len(candles), 12)


if __name__ == '__main__':
    unittest.main()
