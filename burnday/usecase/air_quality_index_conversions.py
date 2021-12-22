def aqi_to_pm_2point5(populated_burn_status):
    """Uses air_quality_index attribute to calculate and mutate the 
        fine_particulate_matter_2_5 attribute for a BurnStatus entity

        Parameters
        ----------
        populated_burn_status: BurnStatus
            if populated_burn_status.air_quality_index is None, no mutation occurs
    """
    pass