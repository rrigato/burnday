def zip_code_parse(raw_zip_code_data):
    """adhoc zip code parsing of raw county level data, prints out the list of zip codes
    to be used as input for additional mapping from the website:
    
    https://www.zip-codes.com/county/ca-los-angeles.asp

        Parameters
        ----------
        raw_zip_code_data: str
            one zip code per line
    """
    clean_zip_codes = []
    each_line_of_zip = raw_zip_code_data.split("\n")

    for county_zip_data in each_line_of_zip:
        clean_zip_codes.append(int(county_zip_data.split("ZIP Code ")[1][0:5]))

    print(clean_zip_codes)

if __name__ == "__main__":
    '''kern county example'''
    zip_code_parse(raw_zip_code_data="""ZIP Code 93201	P.O. Box	Alpaugh	1,348	Pacific	661/559
ZIP Code 93207	General	California Hot Springs	263	Pacific	661
ZIP Code 93208	P.O. Box	Camp Nelson	104	Pacific	559
ZIP Code 93218	P.O. Box	Ducor	994	Pacific	559
ZIP Code 93219	General	Earlimart	10,194	Pacific	661/559
ZIP Code 93221	General	Exeter	14,945	Pacific	559
ZIP Code 93223	General	Farmersville	10,604	Pacific	559
ZIP Code 93227	P.O. Box	Goshen	0	Pacific	559
ZIP Code 93235	General	Ivanhoe	4,559	Pacific	559
ZIP Code 93237	P.O. Box	Kaweah	0	Pacific	559
ZIP Code 93244	General	Lemon Cove	534	Pacific	559
ZIP Code 93247	General	Lindsay	17,423	Pacific	559
ZIP Code 93256	General	Pixley	5,753	Pacific	559
ZIP Code 93257	General	Porterville	75,004	Pacific	559
ZIP Code 93258	P.O. Box	Porterville	2,046	Pacific	559
ZIP Code 93260	General	Posey	200	Pacific	661
ZIP Code 93261	P.O. Box	Richgrove	3,099	Pacific	559
ZIP Code 93262	General	Sequoia National Park	63	Pacific	559
ZIP Code 93265	General	Springville	3,699	Pacific	559
ZIP Code 93267	General	Strathmore	6,237	Pacific	559
ZIP Code 93270	General	Terra Bella	5,837	Pacific	559
ZIP Code 93271	General	Three Rivers	2,276	Pacific	559
ZIP Code 93272	General	Tipton	3,583	Pacific	559
ZIP Code 93274	General	Tulare	69,721	Pacific	559
ZIP Code 93275	P.O. Box	Tulare	0	Pacific	559
ZIP Code 93277	General	Visalia	50,607	Pacific	559
ZIP Code 93278	P.O. Box	Visalia	0	Pacific	559
ZIP Code 93279	P.O. Box	Visalia	0	Pacific	559
ZIP Code 93282	P.O. Box	Waukena	0	Pacific	559
ZIP Code 93286	General	Woodlake	9,548	Pacific	559
ZIP Code 93290	P.O. Box	Visalia	0	Pacific	559
ZIP Code 93291	General	Visalia	52,849	Pacific	559
ZIP Code 93292	General	Visalia	39,032	Pacific	559
ZIP Code 93603	General	Badger	222	Pacific	559
ZIP Code 93615	General	Cutler	6,042	Pacific	559
ZIP Code 93618	General	Dinuba	28,262	Pacific	559
ZIP Code 93633	P.O. Box	Kings Canyon National Pk	25	Pacific	559
ZIP Code 93647	General	Orosi	11,874	Pacific	559
ZIP Code 93666	P.O. Box	Sultana	692	Pacific	559
ZIP Code 93670	P.O. Box	Yettem	0	Pacific	559
ZIP Code 93673	P.O. Box	Traver	713	Pacific	559"""
    )