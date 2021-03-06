from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Union

import requests
from dataclasses_json import dataclass_json, config as dt_json_config, CatchAll
from fake_useragent import UserAgent

BASE_DATA_ENDPOINT_URL = "https://data.rarity.tools/{endpoint}/{collection}"
ua = UserAgent()


@dataclass_json
@dataclass
class Prices:
	prices: Dict[str, list[Union[list[int], float, str]]]
	v: int
	start_date: Optional[datetime] = field(metadata=dt_json_config(field_name="startDate"), default=None)

	unknown_things: CatchAll = None


def get_collection_prices(collection: str) -> Prices:
	res = requests.get(BASE_DATA_ENDPOINT_URL.format(endpoint="prices", collection=collection), headers={
		"User-Agent": ua.random
	})
	json = res.json()

	prices = Prices.from_dict(json)

	return prices
