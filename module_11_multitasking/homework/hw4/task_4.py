import logging
import random

import threading
import time

from threading import Lock
TOTAL_TICKETS = 10
TOTAL_NUMBER_OF_SEATS = 100

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        global TOTAL_NUMBER_OF_SEATS
        is_running = True
        while is_running:

            self.random_sleep()
            with self.sem:

                # TODO добавленный блок кода:
                type = "\t" * 10
                logger.info(f'{type}sold total tickets----{self.tickets_sold}')
                if TOTAL_TICKETS == 4:
                    if TOTAL_NUMBER_OF_SEATS - self.tickets_sold == TOTAL_TICKETS:
                        continue
                    else:
                        with Lock():
                            TOTAL_TICKETS = self.boss_add_tiskets(TOTAL_TICKETS)
                # -----

                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.getName()} sold one;  {TOTAL_TICKETS} left')

                # TODO добавленный блок кода:
                if TOTAL_NUMBER_OF_SEATS == self.tickets_sold:
                    is_running = False
                # -----

        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    @staticmethod
    def random_sleep():
        time.sleep(random.randint(0, 1))

    @staticmethod
    def boss_add_tiskets(total_tickets):
        total_tickets += 6
        return total_tickets


def main():
    semaphore = threading.Semaphore()
    sellers = []
    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()


if __name__ == '__main__':
    main()


