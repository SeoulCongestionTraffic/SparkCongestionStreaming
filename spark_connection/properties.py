"""
API에 필요한것들
"""
import sys
import configparser
from pathlib import Path


path = Path(__file__).parent.parent
parser = configparser.ConfigParser()
parser.read(f"{path}/config/setting.conf")



# AGE TOPIC
DEVMKT_AGE: str = parser.get("AGETOPIC", "dev_market_AGE")
PALCULT_AGE: str = parser.get("AGETOPIC", "palace_culture_AGE")
PARK_AGE: str = parser.get("AGETOPIC", "park_AGE")
POPAREA_AGE: str = parser.get("AGETOPIC", "pop_area_AGE")
TOURZONE_AGE: str = parser.get("AGETOPIC", "tourist_zone_AGE")

DEVMKT_NOF_AGE: str = parser.get("AGETOPIC", "dev_market_noFCST_AGE")
PALCULT_NOF_AGE: str = parser.get("AGETOPIC", "palace_culture_noFCST_AGE")
PARK_NOF_AGE: str = parser.get("AGETOPIC", "park_noFCST_AGE")
POPAREA_NOF_AGE: str = parser.get("AGETOPIC", "pop_area_noFCST_AGE")
TOURZONE_NOF_AGE: str = parser.get("AGETOPIC", "tourist_zone_noFCST_AGE")

# ------------------------------------------------------------------------------

# GENDER TOPIC
DEVMKT_GENDER: str = parser.get("GENDERTOPIC", "dev_market_GENDER")
PALCULT_GENDER: str = parser.get("GENDERTOPIC", "palace_culture_GENDER")
PARK_GENDER: str = parser.get("GENDERTOPIC", "park_GENDER")
POPAREA_GENDER: str = parser.get("GENDERTOPIC", "pop_area_GENDER")
TOURZONE_GENDER: str = parser.get("GENDERTOPIC", "tourist_zone_GENDER")

DEVMKT_NOF_GENDER: str = parser.get("GENDERTOPIC", "dev_market_noFCST_GENDER")
PALCULT_NOF_GENDER: str = parser.get("GENDERTOPIC", "palace_culture_noFCST_GENDER")
PARK_NOF_GENDER: str = parser.get("GENDERTOPIC", "park_noFCST_GENDER")
POPAREA_NOF_GENDER: str = parser.get("GENDERTOPIC", "pop_area_noFCST_GENDER")
TOURZONE_NOF_GENDER: str = parser.get("GENDERTOPIC", "tourist_zone_noFCST_GENDER")


# ------------------------------------------------------------------------------

AVG_AGE_TOPIC: str = parser.get("AVGTOPIC", "avg_age_topic")
AVG_GENDER_TOPIC: str = parser.get("AVGTOPIC", "avg_gender_topic")
AVG_N_AGE_TOPIC: str = parser.get("AVGTOPIC", "avg_n_age_topic")
AVG_N_GENDER_TOPIC: str = parser.get("AVGTOPIC", "avg_n_gender_topic")

