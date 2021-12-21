from burnday.repo.entity_serialization import create_burn_status

def burn_status_for_county(county_name):
    """Retrieves all BurnStatus entities from persistant storage for county_name

        Parameters
        ----------
        burn_day: datetime.date
            day the burn_status applies to

        burn_status: str
            description of whether fuel burning is allowed for the location

        county_name: str
            name of the county to return burn status of

        Returns
        -------
        county_burn_status: list
            list of BurnStatus entities or None if no BurnStatus entites were found
            for the passed county_name

        str_validation_error: None
            str if any unexpected error occurred when loading 
    """
    '''
        TODO - load dynamoDB table persistant storage
        PK - county_name
        SK - Date
        burn_status - str

        from boto3.dynamodb import conditions
        import boto3
        dynamodb_table = boto3.resource(
            service_name="dynamodb",
            region_name=os.environ.get("AWS_REGION")
        ).Table(table_name)

        existing_items = dynamo_table.query(
            KeyConditionExpression=(
                conditions.Key("PK").eq("burnday#" + county_name)
            )
        )

        if existing_items["Count"] == 0:
            return(None, None)

        for burn_status_item in existing_items["Items"]:
            create_burn_status()

        
    '''
    pass