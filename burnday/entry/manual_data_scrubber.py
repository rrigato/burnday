def zip_code_parse(raw_zip_code_data):
    """adhoc zip code parsing of raw county level data, prints out the list of zip codes
    to be used as input for additional mapping

        Parameters
        ----------
        raw_zip_code_data: str
            one zip code per line
    """
    clean_zip_codes = []
    each_line_of_zip = raw_zip_code_data.split("\n")

    for county_zip_data in each_line_of_zip:
        clean_zip_codes.append(int(county_zip_data[0:5]))

    print(clean_zip_codes)

if __name__ == "__main__":
    '''kern county example'''
    zip_code_parse(raw_zip_code_data="""93203	Arvin	Kern County
93203	Di Giorgio	Kern County
93205	Bodfish	Kern County
93206	Buttonwillow	Kern County
93215	Delano	Kern County
93216	Delano	Kern County
93220	Edison	Kern County
93222	Frazier Park	Kern County
93224	Fellows	Kern County
93225	Frazier Park	Kern County
93226	Glennville	Kern County
93238	Kernville	Kern County
93240	Mountain Mesa	Kern County
93240	Lake Isabella	Kern County
93241	Lamont	Kern County
93243	Gorman	Kern County
93243	Lebec	Kern County
93249	Lost Hills	Kern County
93250	McFarland	Kern County
93251	Mckittrick	Kern County
93252	Maricopa	Kern County
93255	Onyx	Kern County
93263	Shafter	Kern County
93268	Taft	Kern County
93276	Tupman	Kern County
93280	Pond	Kern County
93280	Wasco	Kern County
93283	Weldon	Kern County
93285	Wofford Heights	Kern County
93287	Woody	Kern County
93301	Bakersfield	Kern County
93302	Bakersfield	Kern County
93303	Bakersfield	Kern County
93304	Bakersfield	Kern County
93305	Bakersfield	Kern County
93306	Bakersfield	Kern County
93307	Bakersfield	Kern County
93308	Bakersfield	Kern County
93309	Bakersfield	Kern County
93311	Bakersfield	Kern County
93312	Greenacres	Kern County
93312	Bakersfield	Kern County
93313	Pumpkin Center	Kern County
93313	Bakersfield	Kern County
93380	Bakersfield	Kern County
93381	Bakersfield	Kern County
93382	Bakersfield	Kern County
93383	Pumpkin Center	Kern County
93383	Bakersfield	Kern County
93384	Bakersfield	Kern County
93385	Bakersfield	Kern County
93386	Bakersfield	Kern County
93387	Bakersfield	Kern County
93388	Bakersfield	Kern County
93389	Bakersfield	Kern County
93390	Bakersfield	Kern County
93501	Mojave	Kern County
93502	Mojave	Kern County
93504	California City	Kern County
93505	Calif City	Kern County
93505	California City	Kern County
93516	Boron	Kern County
93518	Havilah	Kern County
93518	Caliente	Kern County
93519	Cantil	Kern County
93519	Mojave	Kern County
93523	Aerial Acres	Kern County
93523	Edwards	Kern County
93527	Pearsonville	Kern County
93527	Inyokern	Kern County
93528	Johannesburg	Kern County
93531	Keene	Kern County
93554	Johannesburg	Kern County
93554	Randsburg	Kern County
93555	Ridgecrest	Kern County
93556	Ridgecrest	Kern County
93560	Willow Springs	Kern County
93560	Rosamond	Kern County
93561	Bear Valley Springs	Kern County
93561	Golden Hills	Kern County
93561	Monolith	Kern County
93561	Stallion Springs	Kern County
93561	Tehachapi	Kern County
93581	Tehachapi	Kern County
93596	Boron	Kern County"""
    )