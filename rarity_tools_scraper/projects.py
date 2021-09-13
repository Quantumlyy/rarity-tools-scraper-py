from dataclasses import dataclass, field

import requests
from dataclasses_json import dataclass_json, config as dt_json_config
from fake_useragent import UserAgent
from typing import Tuple  # , Union, Dict

BASE_PROJECTS_STATIC_ENDPOINT_URL = "https://data.rarity.tools/static/{endpoint}/{collection}.json"
ua = UserAgent()


@dataclass_json
@dataclass
class Config:
	id: str
	preview_name: str = field(metadata=dt_json_config(field_name="previewName"))
	contracts: list[dict]
	notes: list[dict]
	images: dict  # Dict[str, Union[bool, str, list[int]]]
	rankings: dict  # Dict[str, Union[str, bool, list[dict]]]
	prop_categories: list[Tuple[str, list[str]]] = field(metadata=dt_json_config(field_name="propCategories"))


def get_collection_config_static(collection: str):
	res = requests.get(BASE_PROJECTS_STATIC_ENDPOINT_URL.format(endpoint="config", collection=collection), headers={
		"User-Agent": ua.random
	})
	json = res.json()

	config = Config.from_dict(json)

	return config
