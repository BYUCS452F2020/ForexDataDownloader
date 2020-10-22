config_vars = {
    'host_name': 'api-fxpractice.oanda.com',
    'streaming_host_name': 'stream-fxpractice.oanda.com',
    'port': '443',
    'ssl': 'true',
    'api_token': '0fdee14291db67f21f5185341842f29f-57bb33b027f07fac165ef555083d9bee',
    'username': 'cs452datadownloader',
    'date_format': 'UNIX',
    'account': '101-001-16464625-001',
    'db_file_path': '/Users/mymac/Google_Drive/CS/CS452/ForexDataDownloader/ForexDataDownloader/Database/forex.db'
}


class Config(object):

    @staticmethod
    def get_host_name():
        return config_vars['host_name']

    @staticmethod
    def get_streaming_host_name():
        return config_vars['streaming_host_name']

    @staticmethod
    def get_port():
        return config_vars['port']

    @staticmethod
    def get_ssl():
        return config_vars['ssl']

    @staticmethod
    def get_api_token():
        return config_vars['api_token']

    @staticmethod
    def get_username():
        return config_vars['username']

    @staticmethod
    def get_date_format():
        return config_vars['date_format']

    @staticmethod
    def get_account():
        return config_vars['account']

    @staticmethod
    def get_db_file_path():
        return config_vars['db_file_path']
