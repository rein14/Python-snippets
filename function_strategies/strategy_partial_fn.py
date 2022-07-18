from decimal import MIN_EMIN
import statistics
from dataclasses import dataclass
from typing import Callable, Protocol
from functools import partial

from exchange import Exchange

TradingStrategyFunction = Callable[[int], bool]

def should_buy_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[-window_size:]
    return prices[-1] < statistics.mean(list_window)
 
def should_sell_avg(prices: list[int], window_size: int) -> bool:
        list_window = prices[-window_size:]
        return prices[-1] > statistics.mean(list_window)

def should_buy_minmax(prices: list[int], min_price: int) -> bool:
    #buy if its below $32,000
    return prices[-1] < min_price
 
def should_sell_minmax(prices: list[int], max_price: int) -> bool:
    return prices[-1] > max_price

@dataclass
class TradingBot:
    """Trading bot"""
    exchange: Exchange
    buy_strategy: TradingStrategyFunction
    sell_strategy: TradingStrategyFunction

    def run(self, symbol) -> None:
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.buy_strategy(prices)
        should_sell = self.sell_strategy(prices)

        if should_buy:
            self.exchange.buy(symbol, 10)
        elif should_sell:

            self.exchange.sell(symbol, 10)
        else:
            print(f"No action needed for {symbol}")
    
def main() -> None:
    exchange = Exchange()
    exchange.connect()

    buy_strategy = partial(should_buy_minmax, max_price =32_000_00)
    sell_strategy = partial(should_sell_minmax, min_price =38_000_00)
    bot = TradingBot(exchange, should_buy_minmax, should_buy_minmax)
    bot.run("BTC/USD")

if __name__ == "__main__":
    main()