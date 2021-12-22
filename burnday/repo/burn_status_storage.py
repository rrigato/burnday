from burnday.repo.entity_serialization import create_burn_status

def burn_status_for_zip(zip_code):
    """Retrieves all BurnStatus entities from persistant storage for zip_code

        Parameters
        ----------
        burn_day: datetime.date
            day the burn_status applies to

        burn_status: str
            description of whether fuel burning is allowed for the location

        zip_code: int
            numeric postal code
            

        Returns
        -------
        location_burn_status: list
            list of BurnStatus entities or None if no BurnStatus entites were found
            for the passed zip_code

        str_validation_error: None
            str if any unexpected error occurred when loading 
    """
    '''
        TODO - load dynamoDB table persistant storage
        PK - zip_code
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
                conditions.Key("PK").eq("burnday#" + zip_code)
            )
        )

        if existing_items["Count"] == 0:
            return(None, None)

        for burn_status_item in existing_items["Items"]:
            create_burn_status()

        
    '''
    pass