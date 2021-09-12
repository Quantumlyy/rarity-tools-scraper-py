from dataclasses import dataclass
from typing import Optional, Dict

import requests
from dataclasses_json import dataclass_json
from fake_useragent import UserAgent

BASE_COLLECTION_DATA_ENDPOINT_URL = "https://data.rarity.tools/{endpoint}/{collection}"
ua = UserAgent()


@dataclass_json
@dataclass
class Prices:
	prices: Dict[int, list]
	v: int
	startDate: Optional[int] = None


def get_collection_prices(collection: str) -> Prices:
	res = requests.get(BASE_COLLECTION_DATA_ENDPOINT_URL.format(endpoint="prices", collection=collection), headers={
		"User-Agent": ua.random
	})
	json = res.json()

	prices = Prices.from_dict(json)

	return prices
