from datetime import date

class BurnStatus:
    """Represents the burn status in a location for one day"""

    @property
    def burn_day(self):
        return(self._burn_day)

    @burn_day.setter
    def burn_day(self, burn_day):
        if type(burn_day) not in (date, type(None)):
            raise TypeError("BurnStatus - burn_day datatype must be a date")
        self._burn_day = burn_day

    @property
    def burn_status(self):
        return(self._burn_status)

    @burn_status.setter
    def burn_status(self, burn_status):
        if type(burn_status) not in (str, type(None)):
            raise TypeError("BurnStatus - burn_status datatype must be a str")
        self._burn_status = burn_status


    @property
    def zip_code(self):
        return(self._zip_code)

    @zip_code.setter
    def zip_code(self, zip_code):
        if type(zip_code) not in (int, type(None)):
            raise TypeError("BurnStatus - zip_code datatype must be a int")
        self._zip_code = zip_code



    @property
    def air_quality_index(self):
        return(self._air_quality_index)

    @air_quality_index.setter
    def air_quality_index(self, air_quality_index):
        if type(air_quality_index) not in (int, float, type(None)):
            raise TypeError("BurnStatus - air_quality_index datatype must be a int/float")
        self._air_quality_index = air_quality_index



    @property
    def fine_particulate_matter_2_5(self):
        return(self._fine_particulate_matter_2_5)

    @fine_particulate_matter_2_5.setter
    def fine_particulate_matter_2_5(self, fine_particulate_matter_2_5):
        if type(fine_particulate_matter_2_5) not in (int, float, type(None)):
            raise TypeError(
                "BurnStatus - fine_particulate_matter_2_5 datatype must be a int/float"
            )
        self._fine_particulate_matter_2_5 = fine_particulate_matter_2_5


    @property
    def coarse_particulate_matter_10(self):
        return(self._coarse_particulate_matter_10)

    @coarse_particulate_matter_10.setter
    def coarse_particulate_matter_10(self, coarse_particulate_matter_10):
        if type(coarse_particulate_matter_10) not in (int, float, type(None)):
            raise TypeError(
                "BurnStatus - coarse_particulate_matter_10 datatype must be a int/float"
                )
        self._coarse_particulate_matter_10 = coarse_particulate_matter_10