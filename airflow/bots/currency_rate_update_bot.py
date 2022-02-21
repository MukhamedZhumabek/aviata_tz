import datetime

import requests
from datetime import datetime
from logging import getLogger
from time import sleep


import schedule


logger = getLogger(__name__)


class UpdateCurrencyRateBot:

    @classmethod
    def _setup_scheduler(cls):
        cls.update_currency_rate()
        schedule.every().day.at("06:00").do(cls.update_currency_rate)

    @classmethod
    def start(cls):
        cls._setup_scheduler()
        while 1:
            schedule.run_pending()
            sleep(1)

    @classmethod
    def update_currency_rate(cls):
        today = datetime.now().strftime("%d.%m.%Y")
        resp_data = requests.get(f"https://www.nationalbank.kz/rss/get_rates.cfm?fdate={today}")
        with open("/template/currency_rate.xml", "rw") as rate:
            rate.write(resp_data)



def run():
    UpdateCurrencyRateBot.start()
