from burnday.entities.air_quality_index_mapper import aqi_to_pm_breakpoints

import logging

def _aqi_conversion_formula(aqi_value, metric_lower_bound_name, metric_upper_bound_name):
    """Converts the air quality index to another metric

        Parameters
        ----------
        aqi_value: int
            air quality index value

        metric_lower_bound_name: str
            Name of the metric lower bound from aqi_to_pm_breakpoints to apply conversion for

        metric_lower_bound_name: str
            Name of the metric upper bound from aqi_to_pm_breakpoints to apply conversion for

        Returns
        -------
        converted_metric_value: float
            rounded to 3 decimal places 
    """
    '''
        TODO - 
        aqi_breakpoints = aqi_to_pm_breakpoints()
        pm = 
        (aqi*(metric_upper_breakpoint - metric_lower_breakpoint) + aqi_upper*metric_lower_breakpoint - aqi_lower*metric_upper_breakpoint)
        / (aqi_upper - aqi_lower)
        
    '''
    aqi_breakpoints = aqi_to_pm_breakpoints()

    '''
        TODO - 
        inline metric lookups
        round to only 2 decimal places?
    '''
    metric_lower_breakpoint = aqi_breakpoints[aqi_value][metric_lower_bound_name]
    metric_upper_breakpoint = aqi_breakpoints[aqi_value][metric_upper_bound_name]

    return(
        round(
        (
            aqi_value*(metric_upper_breakpoint - metric_lower_breakpoint) 
            + aqi_breakpoints[aqi_value]["aqi_upper"]*metric_lower_breakpoint - aqi_breakpoints[aqi_value]["aqi_lower"]*metric_upper_breakpoint
        )
        /
        (aqi_breakpoints[aqi_value]["aqi_upper"] - aqi_breakpoints[aqi_value]["aqi_lower"]),
        3
        )
    )
    

def aqi_to_pm_2point5(populated_burn_status):
    """Uses populated_burn_status.air_quality_index to calculate and mutate the 
        populated_burn_status.fine_particulate_matter_2_5 attribute

        Parameters
        ----------
        populated_burn_status: BurnStatus
            if populated_burn_status.air_quality_index is None, 
            no attributes are modified
    """
    if populated_burn_status.air_quality_index is None:
        return(None)


    logging.info("aqi_to_pm_2point5 - fine_particulate_matter_2_5 calculation")
    populated_burn_status.fine_particulate_matter_2_5 = _aqi_conversion_formula(
        aqi_value=populated_burn_status.air_quality_index,
        metric_lower_bound_name="pm_2_5_lower",
        metric_upper_bound_name="pm_2_5_upper"
    )

    logging.info("aqi_to_pm_2point5 - fine_particulate_matter_2_5 value - " 
        + str(populated_burn_status.fine_particulate_matter_2_5))





def aqi_to_pm_10(populated_burn_status):
    """Uses populated_burn_status.air_quality_index attribute to calculate and mutate the 
        populated_burn_status.coarse_particulate_matter_10 attribute

        Parameters
        ----------
        populated_burn_status: BurnStatus
            if populated_burn_status.air_quality_index is None, 
            no attributes are modified
    """
    pass