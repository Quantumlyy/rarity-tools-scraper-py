from dataclasses import dataclass, field

import requests
from dataclasses_json import dataclass_json, config as dt_json_config, CatchAll
from fake_useragent import UserAgent
from typing import Any, Union, Optional

BASE_PROJECTS_STATIC_ENDPOINT_URL = "https://projects.rarity.tools/static/{endpoint}/{collection}.json"
ua = UserAgent()


@dataclass_json
@dataclass
class ConfigRankingsPreset:
	id: str
	name: str
	method: str
	normalize: bool
	uniqueness: bool
	weights: bool
	combined: bool
	prop_weights: dict = field(metadata=dt_json_config(field_name="propWeights"), default=None)


@dataclass_json
@dataclass
class ConfigRankings:
	presets: list[ConfigRankingsPreset]
	default_preset: Optional[str] = field(metadata=dt_json_config(field_name="defaultPreset"), default=None)
	default_matches: Optional[bool] = field(metadata=dt_json_config(field_name="defaultMatches"), default=None)
	enable_methods: Optional[bool] = field(metadata=dt_json_config(field_name="enableMethods"), default=None)
	enable_uniqueness: Optional[bool] = field(metadata=dt_json_config(field_name="enableUniqueness"), default=None)
	enable_matches: Optional[bool] = field(metadata=dt_json_config(field_name="enableMatches"), default=None)
	enable_combined: Optional[bool] = field(metadata=dt_json_config(field_name="enableCombined"), default=None)
	disable_normalization: Optional[bool] = field(metadata=dt_json_config(field_name="disableNormalization"), default=None)
	disable_settings: Optional[bool] = field(metadata=dt_json_config(field_name="disableSettings"), default=None)
	show_weights: Optional[bool] = field(metadata=dt_json_config(field_name="showWeights"), default=None)


@dataclass_json
@dataclass
class Config:
	id: str
	preview_name: str = field(metadata=dt_json_config(field_name="previewName"))
	contracts: list[dict]
	notes: list[dict]
	images: dict  # Dict[str, Union[bool, str, list[int]]]
	rankings: ConfigRankings
	# list[Tuple[str, list[str]]]
	prop_categories: list[Any] = field(metadata=dt_json_config(field_name="propCategories"))

	unknown_things: CatchAll = None


@dataclass_json
@dataclass
class BasePropDef:
	name: str
	type: str

	is_match: Optional[bool] = field(metadata=dt_json_config(field_name="isMatch"), default=None)
	matching_value: Optional[str] = field(metadata=dt_json_config(field_name="matchingValue"), default=None)

	is_combined: Optional[bool] = field(metadata=dt_json_config(field_name="isCombined"), default=None)

	properties: Optional[list[str]] = None
	pvs: Optional[list[list[Union[str, int]]]] = None

	unknown_things: CatchAll = None


@dataclass_json
@dataclass
class StaticData:
	base_prop_defs: list[BasePropDef] = field(metadata=dt_json_config(field_name="basePropDefs"))
	items = list[list[Union[str, int, list[int]]]]
	tag_nones: bool = field(metadata=dt_json_config(field_name="tagNones"))
	combined_props: dict = field(metadata=dt_json_config(field_name="combinedProps"))
	combinations: list[Any]

	unknown_things: CatchAll = None


def get_collection_config_static(collection: str):
	res = requests.get(BASE_PROJECTS_STATIC_ENDPOINT_URL.format(endpoint="config", collection=collection), headers={
		"User-Agent": ua.random
	})
	json = res.json()

	config = Config.from_dict(json)

	return config


def get_collection_staticdata_static(collection: str):
	res = requests.get(BASE_PROJECTS_STATIC_ENDPOINT_URL.format(endpoint="staticdata", collection=collection), headers={
		"User-Agent": ua.random
	})
	json = res.json()

	data = StaticData.from_dict(json)

	return data
