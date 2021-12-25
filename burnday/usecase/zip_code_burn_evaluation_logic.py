
import logging
def default_burn_rules(populated_burn_status):
    """Provides a generic burn message based on air quality status
        Parameters
        ----------
        populated_burn_status: BurnStatus
            if populated_burn_status.air_quality_index is None, 
            no attributes are modified
    """
    logging.info("default_burn_rules - air quality message")
    generic_air_quality_message = "air quality status is in the {aqi_range} range"


    if populated_burn_status.air_quality_index in range(0, 51):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range="healthy"
        )
    if populated_burn_status.air_quality_index in range(51, 101):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range="moderate"
        )

    if populated_burn_status.air_quality_index in range(101, 151):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range="unhealthy for sensitive groups"
        )

    if populated_burn_status.air_quality_index in range(151, 201):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range="unhealthy"
        )

    if populated_burn_status.air_quality_index in range(201, 301):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range="very unhealthy"
        )

    if populated_burn_status.air_quality_index >= 301:
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range="hazardous"
        )

