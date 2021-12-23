from copy import deepcopy

def _apply_good_aqi_category(aqi_breakpoints):
    """Populates dict keys with the air quality index values in the good range

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
    for air_quality_value in range(0, 51):
        aqi_breakpoints[air_quality_value] = {
            "aqi_category": "good",
            "aqi_lower": 0,
            "aqi_upper": 50,
            "pm_2_5_lower": 0.0,
            "pm_2_5_upper": 12.0,
            "pm_10_lower": 0.0,
            "pm_10_upper": 54.0 
        }


def _apply_moderate_aqi_category(aqi_breakpoints):
    """Populates dict keys with the air quality index values in the moderate range

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
            aqi_category = "good", "moderate", "UNHEALTHY FOR SENSITIVE", "UNHEALTHY", 
            "VERY UNHEALTHY", "HAZARDOUS"

            aqi_lower = air quality index lower bound for given air quality index
            aqi_upper = air quality index upper bound for given air quality index            

            pm_2_5_lower = fine particulate matter lower bound for given air quality index
            pm_2_5_upper = fine particulate matter upper bound for given air quality index

            pm_10_lower = coarse particulate matter lower bound for given air quality index
            pm_10_upper = coarse particulate matter upper bound for given air quality index
    """
    aqi_mapping_table = {}

    _apply_good_aqi_category(aqi_breakpoints=aqi_mapping_table)

    _apply_moderate_aqi_category(aqi_breakpoints=aqi_mapping_table)

    return(deepcopy(aqi_mapping_table))
