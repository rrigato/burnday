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
                "aqi_color": str,
                "pm_2_5_lower": float,
                "pm_2_5_upper": float,
                "pm_10_lower": float,
                "pm_10_upper": float

            }
    """
    for air_quality_value in range(0, 51):
        aqi_breakpoints[air_quality_value] = {
            "aqi_category": "good",
            "aqi_color": "green",
            "pm_2_5_lower": 0.0,
            "pm_2_5_upper": 12.0,
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
                "aqi_color": str,
                "pm_2_5_lower": float,
                "pm_2_5_upper": float,
                "pm_10_lower": float,
                "pm_10_upper": float

            }
            aqi_category = "good", "MODERATE", "UNHEALTHY FOR SENSITIVE", "UNHEALTHY", 
            "VERY UNHEALTHY", "HAZARDOUS"
            aqi_color = color to symbolize category
            https://www.epa.gov/outdoor-air-quality-data/air-data-basic-information

            pm_2_5_lower = fine particulate matter lower bound for given air quality index
            pm_2_5_upper = fine particulate matter upper bound for given air quality index

            pm_10_lower = coarse particulate matter lower bound for given air quality index
            pm_10_upper = coarse particulate matter upper bound for given air quality index
    """
    aqi_mapping_table = {}

    _apply_good_aqi_category(aqi_breakpoints=aqi_mapping_table)

    return(deepcopy(aqi_mapping_table))
