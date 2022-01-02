from burnday.entities import domain_specific_terminology

import logging



def default_burn_rules(populated_burn_status):
    """Mutates populated_burn_status.burn_status with air_quality_index category

        Parameters
        ----------
        populated_burn_status: BurnStatus
            burn_status attribute will be mutated, fine_particulate_matter_2_5 must be populated 

    """
    logging.info("default_burn_rules - air quality message")
    generic_air_quality_message = "air quality status is in the {aqi_range} range"


    if populated_burn_status.air_quality_index in range(0, 51):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range=domain_specific_terminology.AQI_CATEGORY_ZERO
        )

    if populated_burn_status.air_quality_index in range(51, 101):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range=domain_specific_terminology.AQI_CATEGORY_ONE
        )

    if populated_burn_status.air_quality_index in range(101, 151):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range=domain_specific_terminology.AQI_CATEGORY_TWO
        )

    if populated_burn_status.air_quality_index in range(151, 201):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range=domain_specific_terminology.AQI_CATEGORY_THREE
        )

    if populated_burn_status.air_quality_index in range(201, 301):
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range=domain_specific_terminology.AQI_CATEGORY_FOUR
        )

    if populated_burn_status.air_quality_index >= 301:
        populated_burn_status.burn_status = generic_air_quality_message.format(
            aqi_range=domain_specific_terminology.AQI_CATEGORY_FIVE
        )


def _get_california_valley_default_burn_rules(populated_burn_status):
    """Applies wood burning curtailment rules for California Valley

        https://valleyair.org/rule4901/documents/FAQ-Rule4901.pdf
        https://www.valleyair.org/rules/currntrules/r4901.pdf

        Parameters
        ----------
        populated_burn_status: BurnStatus
            will not be mutated by this function 

        Returns
        -------
        burn_status: str
            description of whether fuel burning is allowed for the location
    """
    if populated_burn_status.fine_particulate_matter_2_5 < 20.0:
        return(domain_specific_terminology.CALIFORNIA_TIER_ZERO)

    if populated_burn_status.fine_particulate_matter_2_5 < 65.0:
        return(domain_specific_terminology.CALIFORNIA_TIER_ONE)

    return(domain_specific_terminology.CALIFORNIA_TIER_TWO)


def california_valley_default_burn_rules(populated_burn_status):
    """Mutates populated_burn_status.burn_status with default burn status regulations 
        based on rule 4901: 

        https://valleyair.org/rule4901/documents/FAQ-Rule4901.pdf
        https://www.valleyair.org/rules/currntrules/r4901.pdf

        Parameters
        ----------
        populated_burn_status: BurnStatus
            burn_status attribute will be mutated, fine_particulate_matter_2_5 must be populated 
    """
    logging.info("california_valley_default_burn_rules - ")
    populated_burn_status.burn_status =_get_california_valley_default_burn_rules(
        populated_burn_status=populated_burn_status
    )


def _get_ca_valley_hot_spot_burn_rules(populated_burn_status):
    """Applies wood burning curtailment rules for California 'hot spot' specific locations

        https://valleyair.org/rule4901/documents/FAQ-Rule4901.pdf
        https://www.valleyair.org/rules/currntrules/r4901.pdf

        Parameters
        ----------
        populated_burn_status: BurnStatus
            will not be mutated by this function

        Returns
        -------
        burn_status: str
            description of whether fuel burning is allowed for the location
    """
    if populated_burn_status.fine_particulate_matter_2_5 < 12.0:
        return(domain_specific_terminology.CALIFORNIA_TIER_ZERO)

    if populated_burn_status.fine_particulate_matter_2_5 < 35.0:
        return(domain_specific_terminology.CALIFORNIA_TIER_ONE)

    return(domain_specific_terminology.CALIFORNIA_TIER_TWO)


def ca_valley_hot_spot_burn_rules(populated_burn_status):
    """Mutates populated_burn_status.burn_status with California 
        'hot spot' specific location burning regulations based on rule 4901: 

        https://valleyair.org/rule4901/documents/FAQ-Rule4901.pdf
        https://www.valleyair.org/rules/currntrules/r4901.pdf

        Parameters
        ----------
        populated_burn_status: BurnStatus
            if populated_burn_status.air_quality_index is None, 
            no attributes are modified
    """
    logging.info("ca_valley_hot_spot_burn_rules - ")
    populated_burn_status.burn_status =_get_ca_valley_hot_spot_burn_rules(
        populated_burn_status=populated_burn_status
    )



def _get_washington_state_burn_rules(populated_burn_status):
    """Applies wood burning curtailment rules 

        https://apps.leg.wa.gov/rcw/default.aspx?cite=70A.15.3580
        https://pscleanair.gov/FAQ.aspx?TID=19
        

        Parameters
        ----------
        populated_burn_status: BurnStatus
            no mutation occurs

        Returns
        -------
        burn_status: str
            description of whether fuel burning is allowed for the location
    """
    if populated_burn_status.fine_particulate_matter_2_5 <= 30.0:
        return(domain_specific_terminology.NO_BURN_RESTRICTIONS)

    return(domain_specific_terminology.WASHINGTON_STAGE_ONE)

def washington_state_burn_rules(populated_burn_status):
    """Mutates populated_burn_status.burn_status with Washington state section RCW 70A.15.3580

        https://apps.leg.wa.gov/rcw/default.aspx?cite=70A.15.3580
        https://pscleanair.gov/FAQ.aspx?TID=19
        

        Parameters
        ----------
        populated_burn_status: BurnStatus
            if populated_burn_status.air_quality_index is None
    """
    populated_burn_status.burn_status = _get_washington_state_burn_rules(
        populated_burn_status=populated_burn_status
    )




def _get_ca_south_coast_burn_rules(populated_burn_status):
    """Applies wood burning curtailment rules for the California South Coast 
        Air Quality Management District rule 445:

        http://www.aqmd.gov/docs/default-source/rule-book/rule-iv/rule-445.pdf
        https://www.aqmd.gov/home/programs/community/cbyb---faq#3

        Parameters
        ----------
        populated_burn_status: BurnStatus
            will not be mutated by this function

        Returns
        -------
        burn_status: str
            description of whether fuel burning is allowed for the location
    """
    if populated_burn_status.fine_particulate_matter_2_5 < 30.0:
        return(domain_specific_terminology.CA_SOUTH_COAST_BURNING_ALLOWED)

    return(domain_specific_terminology.CA_SOUTH_COAST_BURN_BAN)


def ca_south_coast_burn_rules(populated_burn_status):
    """Mutates populated_burn_status.burn_status with the California South Coast 
        Air Quality Management District rule 445:

        http://www.aqmd.gov/docs/default-source/rule-book/rule-iv/rule-445.pdf
        https://www.aqmd.gov/home/programs/community/cbyb---faq#3

        Parameters
        ----------
        populated_burn_status: BurnStatus
            if populated_burn_status.air_quality_index is None, 
            no attributes are modified
    """
    logging.info("ca_south_coast_burn_rules - ")
    populated_burn_status.burn_status =_get_ca_south_coast_burn_rules(
        populated_burn_status=populated_burn_status
    )