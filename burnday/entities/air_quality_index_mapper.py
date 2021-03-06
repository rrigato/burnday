from copy import deepcopy

import csv
import logging

def _load_csv_for_parameter(metric_to_convert_to, duration_description):
    """loads aqi_breakpoints.csv metadata for converting the air quality index 
        to other metrics

        Parameters
        -------
        metric_to_convert_to: str
            metric you want to convert to, filters first column of aqi_breakpoints.csv

        duration_description: str
            time period used when calculating the metric, fourth column of the csv

        Returns
        -------
        selected_metric_mapping: list
            Each element is a dict containing the following keys:

            "Parameter" - str - corresponds to metrics you want to convert to such
                as PM2.5 fine particulate matter

            "Parameter code" - str -

            "Duration code" - str - corresponds to a code for duration description

            "Duration Description" - str -

            "AQI Category" - str - Air Quality Index category

            "Low AQI" - int - Lower bound of air quality 
                Example AQI of 85 will result in this element being 51

            "High AQI" - int - Upper bound of air quality 
                Example AQI of 85 will result in this element being 100

            "Low Breakpoint" - float - lower bound of metric you are converting to 
                Example converting AQI of 85 to PM2.5 will result in this element being 12.1

            "High Breakpoint" - float - Upper bound of metric you are converting to 
                Example converting AQI of 85 to PM2.5 will result in this element being 35.4

    """
    selected_metric_mapping = []

    with open("burnday/entities/aqi_breakpoints.csv", "r") as aqi_mapping:
        aqi_reader = csv.DictReader(aqi_mapping, delimiter=',')
        
        for aqi_category in aqi_reader:
            aqi_category["Low AQI"] = int(aqi_category["Low AQI"])
            aqi_category["High AQI"] = int(aqi_category["High AQI"])
            aqi_category["Low Breakpoint"] = float(aqi_category["Low Breakpoint"])
            aqi_category["High Breakpoint"] = float(aqi_category["High Breakpoint"])
            if (
                    (aqi_category["Parameter"] == metric_to_convert_to) 
                    and 
                    (aqi_category["Duration Description"] == duration_description)
                ):
                selected_metric_mapping.append(aqi_category)

    return(selected_metric_mapping)


def _aqi_breakpoints_wrapper(aqi_breakpoints, aqi_category, metric_prefix):
    """Populates aqi_breakpoints for lower and upper thresholds

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

        aqi_category: list
            Each element is a dict containing the following keys:

            "Parameter" - str - corresponds to metrics you want to convert to such
                as PM2.5 fine particulate matter

            "Parameter code" - str -

            "Duration code" - str - corresponds to a code for duration description

            "Duration Description" - str -

            "AQI Category" - str - Air Quality Index category

            "Low AQI" - int - Lower bound of air quality 
                Example AQI of 85 will result in this element being 51

            "High AQI" - int - Upper bound of air quality 
                Example AQI of 85 will result in this element being 100

            "Low Breakpoint" - float - lower bound of metric you are converting to 
                Example converting AQI of 85 to PM2.5 will result in this element being 12.1

            "High Breakpoint" - float - Upper bound of metric you are converting to 
                Example converting AQI of 85 to PM2.5 will result in this element being 35.4

        metric_prefix: str
            will be used for populating the aqi_breakpoints keys with the following logic:
            <metric_prefix>_lower 
            <metric_prefix>_upper
    """
    for aqi_value in range(aqi_category["Low AQI"], (aqi_category["High AQI"] + 1)):

        aqi_breakpoints[aqi_value]["aqi_category"] = aqi_category["AQI Category"]
        aqi_breakpoints[aqi_value]["aqi_lower"] = aqi_category["Low AQI"]
        aqi_breakpoints[aqi_value]["aqi_upper"] = aqi_category["High AQI"]
        aqi_breakpoints[aqi_value][metric_prefix + "_lower"] = aqi_category["Low Breakpoint"]
        aqi_breakpoints[aqi_value][metric_prefix + "_upper"] = aqi_category["High Breakpoint"]



'''
    TODO - 
    take this function and load the coarse_particulate_matter_10 upper and lower bounds
'''
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
                "pm_2_5_upper": float
            }
    """
    for aqi_category in _load_csv_for_parameter(
            metric_to_convert_to="Acceptable PM2.5 AQI & Speciation Mass", 
            duration_description="24 HOUR"
        ):
        _aqi_breakpoints_wrapper(
            aqi_breakpoints=aqi_breakpoints, 
            aqi_category=aqi_category,
            metric_prefix="pm_2_5"
        )


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
    aqi_metric_conversion_mapping = {}

    logging.info("aqi_to_pm_breakpoints - loading aqi metric conversion table")

    _air_quality_index_structure(aqi_breakpoints=aqi_metric_conversion_mapping)

    _apply_fine_particulate_matter_2_5(aqi_breakpoints=aqi_metric_conversion_mapping)

    logging.info("aqi_to_pm_breakpoints - pm2.5 loaded")

    return(deepcopy(aqi_metric_conversion_mapping))


if __name__ == "__main__":
    x = {}
    _air_quality_index_structure(x)

    _apply_fine_particulate_matter_2_5(x)
    print(x[0])
    print(len(x))
