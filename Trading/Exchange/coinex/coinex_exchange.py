#  Drakkar-Software OctoBot-Tentacles
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.

import octobot_trading.exchanges as exchanges

class Coinex(exchanges.SpotCCXTExchange):
    DESCRIPTION = ""
    MAX_PAGINATION_LIMIT: int = 100

    @classmethod
    def get_name(cls):
        return 'coinex'

    @classmethod
    def is_supporting_exchange(cls, exchange_candidate_name) -> bool:
        return cls.get_name() == exchange_candidate_name

    def get_market_status(self, symbol, price_example=None, with_fixer=True):
        return self.get_fixed_market_status(symbol, price_example=price_example, with_fixer=with_fixer)

    async def get_open_orders(self, symbol=None, since=None, limit=None, **kwargs) -> list:
        return await super().get_open_orders(symbol=symbol,
                                             since=since,
                                             limit=self._fix_limit(limit),
                                             **kwargs)

    async def get_closed_orders(self, symbol=None, since=None, limit=None, **kwargs) -> list:
        return await super().get_closed_orders(symbol=symbol,
                                               since=since,
                                               limit=self._fix_limit(limit),
                                               **kwargs)

    def _fix_limit(self, limit: int) -> int:
        return min(self.MAX_PAGINATION_LIMIT, limit)