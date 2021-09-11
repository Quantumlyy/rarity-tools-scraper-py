from __future__ import annotations

from dataclasses import dataclass

import requests
from dataclasses_json import dataclass_json
from fake_useragent import UserAgent

COLLECTIONS_ENDPOINT_URL = "https://collections.rarity.tools/static/collections.json"
ua = UserAgent()


@dataclass_json
@dataclass
class ProjectLookup:
	name: str
	itemName: str | None
	added: str | None
	addedOrder: int | None
	dynamic: int | None
	manual: bool | None
	customHeader: str | None
	contracts: list[str] | None
	cv: int | None


@dataclass_json
@dataclass
class Projects:
	list: list[str]
	lookup: dict  # [str, ProjectLookup]


@dataclass_json
@dataclass
class Collection:
	id: str
	slug: str
	name: str
	# TODO: convert to date time
	created_date: str
	description: str
	discord_url: str | None
	external_url: str | None
	image_url: str | None
	large_image_url: str | None
	banner_image_url: str | None
	medium_username: str | None
	twitter_username: str | None
	instagram_username: str | None

	stats: dict


@dataclass_json
@dataclass
class Collections:
	collections: list[Collection]
	projects: Projects


def get_all_collections() -> Collections:
	res = requests.get(COLLECTIONS_ENDPOINT_URL, headers={
		"User-Agent": ua.random
	})

	return Collections.from_dict(res.json())
