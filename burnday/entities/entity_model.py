from datetime import date

class BurnStatus:
    """Represents the burn status in a county for one day"""

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
    def county_name(self):
        return(self._county_name)

    @county_name.setter
    def county_name(self, county_name):
        if type(county_name) not in (str, type(None)):
            raise TypeError("BurnStatus - county_name datatype must be a str")
        self._county_name = county_name