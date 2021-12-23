from copy import deepcopy

import csv

def _apply_fine_particulate_matter_2_5(aqi_breakpoints):
    """Populates air quality index breakpoints for the PM2.5

        Parameters
        -------
        aqi_breakpoints: dict
            key is an int representing the air quality index, populates the following values
            {
                "aqi_category": str,
                "aqi_lower": float,
                "aqi_upper": float,
                "pm_2_5_lower": float,
                "pm_2_5_upper": float,
                "pm_10_lower": float,
                "pm_10_upper": float
            }
    """
    with open("burnday/entities/aqi_breakpoints.csv", "r") as aqi_mapping:
        aqi_reader = csv.reader(aqi_mapping, delimiter=',')
        for aqi_row in aqi_reader:
            if ((aqi_row[0] != "Acceptable PM2.5 AQI & Speciation Mass") and 
                (aqi_row[2] != "7")):
                continue
            for air_quality_index_value in range(int(aqi_row[5]), int(aqi_row[6]) + 1):
                aqi_breakpoints[air_quality_index_value] = {
                    "aqi_category": aqi_row[4],
                    "aqi_lower": int(aqi_row[5]),
                    "aqi_upper": int(aqi_row[6]),
                    "pm_2_5_lower": float(aqi_row[7]),
                    "pm_2_5_upper": float(aqi_row[8])
                }



def _apply_moderate_aqi_category(aqi_breakpoints):
    """Populates dict keys with the air quality index values in the moderate category

        Parameters
        -------
        aqi_breakpoints: dict
            key is an int representing the air quality index, value is a dict with the
            following structure:
            {
                "aqi_category": str,
                "aqi_lower": float,
                "aqi_upper": float,
                "pm_2_5_lower": float,
                "pm_2_5_upper": float,
                "pm_10_lower": float,
                "pm_10_upper": float
            }
    """
    for air_quality_value in range(51, 101):
        aqi_breakpoints[air_quality_value] = {
            "aqi_category": "moderate",
            "aqi_lower": 51,
            "aqi_upper": 101,
            "pm_2_5_lower": 12.1,
            "pm_2_5_upper": 35.4,
            "pm_10_lower": 0.0,
            "pm_10_upper": 54.0 
        }

def _apply_unhealthy_for_sensitive_aqi_category(aqi_breakpoints):
    """Populates dict keys with the air quality index values in the unhealthy for sensitive category

        Parameters
        -------
        aqi_breakpoints: dict
            key is an int representing the air quality index, value is a dict with the
            following structure:
            {
                "aqi_category": str,
                "aqi_lower": float,
                "aqi_upper": float,
                "pm_2_5_lower": float,
                "pm_2_5_upper": float,
                "pm_10_lower": float,
                "pm_10_upper": float
            }
    """
    for air_quality_value in range(101, 151):
        aqi_breakpoints[air_quality_value] = {
            "aqi_category": "moderate",
            "aqi_lower": 51,
            "aqi_upper": 101,
            "pm_2_5_lower": 35.5,
            "pm_2_5_upper": 55.4,
            "pm_10_lower": 0.0,
            "pm_10_upper": 54.0 
        }


def _air_quality_index_structure(aqi_breakpoints):
    """Populates dict keys for air quality index fields with None

        Parameters
        -------
        aqi_breakpoints: dict
            key is an int representing the air quality index, value is a dict with the
            following structure:
            {
                "aqi_category": str,
                "aqi_lower": float,
                "aqi_upper": float,
                "pm_2_5_lower": float,
                "pm_2_5_upper": float,
                "pm_10_lower": float,
                "pm_10_upper": float
            }
    """
    for possible_air_quality_index_value in range(0, 1000):
        aqi_breakpoints[possible_air_quality_index_value] = {
            "aqi_category": None,
            "aqi_lower": None,
            "aqi_upper": None,
            "pm_2_5_lower": None,
            "pm_2_5_upper": None,
            "pm_10_lower": None,
            "pm_10_upper": None
        }

    

def aqi_to_pm_breakpoints():
    """Static mapping table between the air quality index and the fine particulate matter (PM2.5)
        and the coarse grained particulate matter (PM10)
        https://aqs.epa.gov/aqsweb/documents/codetables/aqi_breakpoints.html

        Returns
        -------
        aqi_breakpoints: dict
            key is an int representing the air quality index, value is a dict with the
            following structure:
            {
                "aqi_category": str,
                "aqi_lower": float,
                "aqi_upper": float,
                "pm_2_5_lower": float,
                "pm_2_5_upper": float,
                "pm_10_lower": float,
                "pm_10_upper": float
            }
            aqi_category = "good", "moderate", "unhealthy for sensitive", "UNHEALTHY", 
            "VERY UNHEALTHY", "HAZARDOUS"

            aqi_lower = air quality index lower bound for given air quality index
            aqi_upper = air quality index upper bound for given air quality index            

            pm_2_5_lower = fine particulate matter lower bound for given air quality index
            pm_2_5_upper = fine particulate matter upper bound for given air quality index

            pm_10_lower = coarse particulate matter lower bound for given air quality index
            pm_10_upper = coarse particulate matter upper bound for given air quality index
    """
    aqi_mapping_table = {}

    _air_quality_index_structure(aqi_breakpoints=aqi_mapping_table)

    _apply_fine_particulate_matter_2_5(aqi_breakpoints=aqi_mapping_table)

    return(deepcopy(aqi_mapping_table))


if __name__ == "__main__":
    print(_apply_fine_particulate_matter_2_5(_air_quality_index_structure({})))[0:50]
    x = {}
    _air_quality_index_structure(x)

    _apply_fine_particulate_matter_2_5(x)
    print(x[0])