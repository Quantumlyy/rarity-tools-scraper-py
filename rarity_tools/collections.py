from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Dict

import requests
from dataclasses_json import dataclass_json
from fake_useragent import UserAgent

COLLECTIONS_ENDPOINT_URL = "https://collections.rarity.tools/static/collections.json"
ua = UserAgent()


@dataclass_json
@dataclass
class ProjectLookup:
	name: str
	addedOrder: Optional[int] = None
	dynamic: Optional[int] = None
	manual: Optional[bool] = None
	contracts: Optional[list[str]] = None
	cv: Optional[int] = None
	itemName: Optional[str] = None
	added: Optional[str] = None
	customHeader: Optional[str] = None


@dataclass_json
@dataclass
class Projects:
	list: list[str]
	lookup: Dict[str, ProjectLookup]


@dataclass_json
@dataclass
class CollectionStats:
	one_day_volume: Optional[float] = None
	one_day_change: Optional[float] = None
	one_day_sales: Optional[float] = None
	one_day_average_price: Optional[float] = None
	seven_day_volume: Optional[float] = None
	seven_day_change: Optional[float] = None
	seven_day_sales: Optional[float] = None
	seven_day_average_price: Optional[float] = None
	total_volume: Optional[float] = None
	total_sales: Optional[float] = None
	total_supply: Optional[float] = None
	num_owners: Optional[float] = None
	average_price: Optional[float] = None
	market_cap: Optional[float] = None
	floor_price: Optional[float] = None


@dataclass_json
@dataclass
class Collection:
	id: str
	slug: str
	name: str
	description: str

	discord_url: Optional[str] = None
	external_url: Optional[str] = None
	image_url: Optional[str] = None
	large_image_url: Optional[str] = None
	banner_image_url: Optional[str] = None
	medium_username: Optional[str] = None
	twitter_username: Optional[str] = None
	instagram_username: Optional[str] = None

	# TODO: convert to date time
	created_date: Optional[str] = None
	stats: Optional[CollectionStats] = None


@dataclass_json
@dataclass
class Collections:
	collections: list[Collection]
	projects: Projects


def get_all_collections() -> Collections:
	res = requests.get(COLLECTIONS_ENDPOINT_URL, headers={
		"User-Agent": ua.random
	})
	json = res.json()

	collections = Collections.from_dict(json)
	for i in range(len(json["collections"])):
		collections.collections[i] = Collection.from_dict(json["collections"][i])

	return collections
