import statistics
from dataclasses import dataclass
from typing import Protocol

from exchange import Exchange

class TradingStrategy(Protocol):
    """Trading stategies"""
    def should_buy(self, prices: list[int]) -> bool:
        raise NotImplementedError()

    def should_sell(self, prices: list[int]) -> bool:
        raise NotImplementedError()

class AverageTradingStategy:
    """Trading strategies based on price average"""

    def should_buy(self, prices: list[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] < statistics.mean(list_window)
    
    def should_sell(self, prices: list[int]) -> bool:
         list_window = prices[-3:]
         print(list_window)
         return prices[-1] > statistics.mean(list_window)
    
class MinMaxTradingStrategy:
    """Trading strategies based on min/max"""

    def should_buy(self, prices: list[int]) -> bool:
        #buy if its below $32,000
        return prices[-1] < 32_000_00
    
    def should_sell(self, prices: list[int]) -> bool:
        return prices[-1] > 32_000_00

@dataclass
class TradingBot:
    """Trading bot"""
    exchange: Exchange
    trading_strategy: TradingStrategy

    def run(self, symbol) -> None:
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.trading_strategy.should_buy(prices)
        should_sell = self.trading_strategy.should_sell(prices)

        if should_buy:
            self.exchange.buy(symbol, 10)
        elif should_sell:

            self.exchange.sell(symbol, 10)
        else:
            print(f"No action needed for {symbol}")
    
def main() -> None:
    exchange = Exchange()
    exchange.connect()

    trading_strategy = MinMaxTradingStrategy()

    bot = TradingBot(exchange, trading_strategy)
    bot.run("BTC/USD")

if __name__ == "__main__":
    main()