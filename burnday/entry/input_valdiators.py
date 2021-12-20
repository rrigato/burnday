from datetime import date


def validate_str_input(str_input, max_len):
    """Confirms input provided from external is a str below max_len

        Parameters
        ----------
        str_input: str
            input that needs to be confirmed as a str

        Returns
        -------
        str_validation_error: None
            str if str_input did not pass validation
    """
    pass


def validate_iso_8601_date(iso_formatted_str):
    """Confirms that provided input is a str in ISO 8601 YYYY-MM-DD format

        Parameters
        ----------
        iso_formatted_str: str
            ISO 8601 YYYY-MM-DD format

        Returns
        -------
        parsed_date: datetime.date
            iso_formatted_str converted to a date

        str_validation_error: None
            str if input validation did not pass
    """
    pass