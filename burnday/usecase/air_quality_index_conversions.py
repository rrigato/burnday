from burnday.entities.air_quality_index_mapper import aqi_to_pm_breakpoints
def _aqi_conversion_formula(aqi_value, metric_lower_bound_name, metric_upper_bound_name):
    """"""
    '''
        TODO - 
        aqi_breakpoints = aqi_to_pm_breakpoints()
        pm = 
        (aqi*(metric_upper_breakpoint - metric_lower_breakpoint) + aqi_upper*metric_lower - aqi_lower*metric_lower)
        / (aqi_upper - aqi_lower)
        
    '''
    pass

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
    '''
        TODO-
        _aqi_conversion_formula(
            aqi_value=populated_burn_status.air_quality_index,
            metric_lower_bound_name="pm_2_5_lower",
            metric_upper_bound_name="pm_2_5_upper"
        )
    '''   




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