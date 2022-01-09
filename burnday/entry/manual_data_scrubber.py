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
    zip_code_parse(raw_zip_code_data="""ZIP Code 91701	General	Rancho Cucamonga	38,976	Pacific	909
ZIP Code 91708	General	Chino	3,369	Pacific	909/840
ZIP Code 91709	General	Chino Hills	74,796	Pacific	909/840
ZIP Code 91710	General	Chino	80,358	Pacific	909/840
ZIP Code 91729	P.O. Box	Rancho Cucamonga	0	Pacific	909/951/840
ZIP Code 91730	General	Rancho Cucamonga	66,925	Pacific	909/951/840
ZIP Code 91737	General	Rancho Cucamonga	24,740	Pacific	909
ZIP Code 91739	General	Rancho Cucamonga	34,794	Pacific	909
ZIP Code 91743	P.O. Box	Guasti	0	Pacific	909/951/840
ZIP Code 91758	General	Ontario	0	Pacific	909/951/840
ZIP Code 91759	P.O. Box	Mt Baldy	476	Pacific	760
ZIP Code 91761	General	Ontario	56,913	Pacific	909/951/840
ZIP Code 91762	General	Ontario	55,857	Pacific	909
ZIP Code 91763	General	Montclair	36,375	Pacific	909/951/840
ZIP Code 91764	General	Ontario	54,086	Pacific	909/951/840
ZIP Code 91784	General	Upland	25,938	Pacific	909/840
ZIP Code 91785	P.O. Box	Upland	0	Pacific	909
ZIP Code 91786	General	Upland	51,165	Pacific	909/840
ZIP Code 92242	General	Earp	1,539	Pacific	760/442
ZIP Code 92252	General	Joshua Tree	9,647	Pacific	442/760
ZIP Code 92256	General	Morongo Valley	3,588	Pacific	442/760
ZIP Code 92267	P.O. Box	Parker Dam	126	Pacific	760
ZIP Code 92268	P.O. Box	Pioneertown	574	Pacific	760/442
ZIP Code 92277	General	Twentynine Palms	23,911	Pacific	760/442
ZIP Code 92278	P.O. Box	Twentynine Palms	3,846	Pacific	760/442
ZIP Code 92280	General	Vidal	14	Pacific	442
ZIP Code 92284	General	Yucca Valley	25,095	Pacific	760/442
ZIP Code 92285	General	Landers	2,632	Pacific	760/442
ZIP Code 92286	P.O. Box	Yucca Valley	0	Pacific	760/442
ZIP Code 92301	General	Adelanto	32,725	Pacific	760/442
ZIP Code 92304	P.O. Box	Amboy	17	Pacific	760/442
ZIP Code 92305	General	Angelus Oaks	535	Pacific	909
ZIP Code 92307	General	Apple Valley	37,630	Pacific	760/442
ZIP Code 92308	General	Apple Valley	39,837	Pacific	760/442
ZIP Code 92309	General	Baker	763	Pacific	760/442
ZIP Code 92310	General	Fort Irwin	8,845	Pacific	760/442
ZIP Code 92311	General	Barstow	31,894	Pacific	760/442
ZIP Code 92312	P.O. Box	Barstow	0	Pacific	760/442
ZIP Code 92313	General	Grand Terrace	12,025	Pacific	909/951
ZIP Code 92314	General	Big Bear City	10,162	Pacific	909/442
ZIP Code 92315	General	Big Bear Lake	5,094	Pacific	909
ZIP Code 92316	General	Bloomington	30,830	Pacific	909/840
ZIP Code 92317	P.O. Box	Blue Jay	0	Pacific	909/442/760
ZIP Code 92318	General	Bryn Mawr	0	Pacific	909/840/951
ZIP Code 92321	P.O. Box	Cedar Glen	1,522	Pacific	909/840
ZIP Code 92322	P.O. Box	Cedarpines Park	1,257	Pacific	909/442/760
ZIP Code 92323	General	Cima	0	Pacific	760/442
ZIP Code 92324	General	Colton	56,505	Pacific	909/840/951
ZIP Code 92325	P.O. Box	Crestline	9,391	Pacific	909/442/760
ZIP Code 92327	General	Daggett	632	Pacific	760/442
ZIP Code 92329	P.O. Box	Phelan	0	Pacific	760/442
ZIP Code 92331	P.O. Box	Fontana	0	Pacific	909/840
ZIP Code 92332	General	Essex	65	Pacific	760/442
ZIP Code 92333	P.O. Box	Fawnskin	472	Pacific	909
ZIP Code 92334	P.O. Box	Fontana	0	Pacific	909/840
ZIP Code 92335	General	Fontana	95,397	Pacific	909/840
ZIP Code 92336	General	Fontana	88,419	Pacific	909/840
ZIP Code 92337	General	Fontana	37,849	Pacific	909/840
ZIP Code 92338	General	Ludlow	12	Pacific	442
ZIP Code 92339	General	Forest Falls	885	Pacific	909
ZIP Code 92340	P.O. Box	Hesperia	0	Pacific	760/442
ZIP Code 92341	P.O. Box	Green Valley Lake	410	Pacific	909
ZIP Code 92342	General	Helendale	6,379	Pacific	760
ZIP Code 92344	General	Hesperia	20,769	Pacific	442/760
ZIP Code 92345	General	Hesperia	78,715	Pacific	760/442
ZIP Code 92346	General	Highland	54,923	Pacific	909/840
ZIP Code 92347	General	Hinkley	1,692	Pacific	442/760
ZIP Code 92350	Unique	Loma Linda	0	Pacific	909/840/951
ZIP Code 92352	P.O. Box	Lake Arrowhead	8,004	Pacific	909/442/760
ZIP Code 92354	General	Loma Linda	21,559	Pacific	909/840/951
ZIP Code 92356	General	Lucerne Valley	6,455	Pacific	760/442
ZIP Code 92357	Unique	Loma Linda	0	Pacific	909/840/951
ZIP Code 92358	General	Lytle Creek	707	Pacific	760
ZIP Code 92359	General	Mentone	8,103	Pacific	909
ZIP Code 92363	General	Needles	5,321	Pacific	760/442
ZIP Code 92364	General	Nipton	90	Pacific	760/442
ZIP Code 92365	General	Newberry Springs	2,637	Pacific	760/442
ZIP Code 92366	General	Mountain Pass	0	Pacific	442/760
ZIP Code 92368	General	Oro Grande	1,113	Pacific	760/442
ZIP Code 92369	P.O. Box	Patton	0	Pacific	909/840
ZIP Code 92371	General	Phelan	16,763	Pacific	760/442
ZIP Code 92372	General	Pinon Hills	6,220	Pacific	760/661/442
ZIP Code 92373	General	Redlands	33,423	Pacific	909/840
ZIP Code 92374	General	Redlands	40,267	Pacific	909/840
ZIP Code 92375	P.O. Box	Redlands	0	Pacific	909/840
ZIP Code 92376	General	Rialto	81,516	Pacific	909/840
ZIP Code 92377	General	Rialto	19,989	Pacific	909/840
ZIP Code 92378	P.O. Box	Rimforest	183	Pacific	909/442/760
ZIP Code 92382	P.O. Box	Running Springs	5,268	Pacific	909/840
ZIP Code 92385	P.O. Box	Skyforest	313	Pacific	909/840
ZIP Code 92386	P.O. Box	Sugarloaf	2,270	Pacific	909/442
ZIP Code 92391	P.O. Box	Twin Peaks	2,534	Pacific	909/442/760
ZIP Code 92392	General	Victorville	54,858	Pacific	760/442
ZIP Code 92393	P.O. Box	Victorville	0	Pacific	442/760/909
ZIP Code 92394	General	Victorville	33,237	Pacific	760/442
ZIP Code 92395	General	Victorville	42,400	Pacific	442/760/909
ZIP Code 92397	General	Wrightwood	4,894	Pacific	760/442
ZIP Code 92398	P.O. Box	Yermo	1,379	Pacific	760/442
ZIP Code 92399	General	Yucaipa	52,606	Pacific	909
ZIP Code 92401	General	San Bernardino	1,932	Pacific	909/951/840
ZIP Code 92402	P.O. Box	San Bernardino	0	Pacific	909/951/840
ZIP Code 92403	General	San Bernardino	0	Pacific	909/951/840
ZIP Code 92404	General	San Bernardino	58,271	Pacific	909/840
ZIP Code 92405	General	San Bernardino	28,873	Pacific	909/840
ZIP Code 92406	P.O. Box	San Bernardino	0	Pacific	909/951/840
ZIP Code 92407	General	San Bernardino	56,689	Pacific	909/442/760
ZIP Code 92408	General	San Bernardino	15,271	Pacific	909
ZIP Code 92410	General	San Bernardino	49,410	Pacific	909/951/840
ZIP Code 92411	General	San Bernardino	26,214	Pacific	909
ZIP Code 92413	P.O. Box	San Bernardino	0	Pacific	909/951/840
ZIP Code 92415	Unique	San Bernardino	0	Pacific	909/951/840
ZIP Code 92418	Unique	San Bernardino	0	Pacific	909/951/840
ZIP Code 92423	P.O. Box	San Bernardino	0	Pacific	909/951/840
ZIP Code 92427	P.O. Box	San Bernardino	0	Pacific	909/951/840
ZIP Code 93562	General	Trona	1,818	Pacific	442/760
ZIP Code 93592	P.O. Box	Trona	64	Pacific	442/760"""
    )