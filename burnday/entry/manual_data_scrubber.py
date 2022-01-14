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
    zip_code_parse(raw_zip_code_data="""ZIP Code 91752	General	Mira Loma	30,047	Pacific	951
ZIP Code 92201	General	Indio	61,827	Pacific	760/442
ZIP Code 92202	P.O. Box	Indio	0	Pacific	760/442
ZIP Code 92203	General	Indio	25,605	Pacific	760/442
ZIP Code 92210	General	Indian Wells	4,677	Pacific	760/442
ZIP Code 92211	General	Palm Desert	24,294	Pacific	760
ZIP Code 92220	General	Banning	31,638	Pacific	951
ZIP Code 92223	General	Beaumont	43,605	Pacific	909
ZIP Code 92225	General	Blythe	24,310	Pacific	760/442
ZIP Code 92226	P.O. Box	Blythe	0	Pacific	760/442
ZIP Code 92230	General	Cabazon	2,550	Pacific	951
ZIP Code 92234	General	Cathedral City	51,151	Pacific	760
ZIP Code 92235	P.O. Box	Cathedral City	0	Pacific	760
ZIP Code 92236	General	Coachella	41,083	Pacific	760
ZIP Code 92239	P.O. Box	Desert Center	223	Pacific	760/442
ZIP Code 92240	General	Desert Hot Springs	34,722	Pacific	760/442
ZIP Code 92241	General	Desert Hot Springs	8,803	Pacific	760/442
ZIP Code 92247	P.O. Box	La Quinta	0	Pacific	760
ZIP Code 92248	P.O. Box	La Quinta	0	Pacific	760
ZIP Code 92253	General	La Quinta	37,262	Pacific	760
ZIP Code 92254	General	Mecca	12,768	Pacific	760/442
ZIP Code 92255	P.O. Box	Palm Desert	0	Pacific	760/442
ZIP Code 92258	P.O. Box	North Palm Springs	861	Pacific	760/442/951
ZIP Code 92260	General	Palm Desert	31,753	Pacific	760/442
ZIP Code 92261	P.O. Box	Palm Desert	0	Pacific	760/442
ZIP Code 92262	General	Palm Springs	26,179	Pacific	760/442/951
ZIP Code 92263	P.O. Box	Palm Springs	0	Pacific	760/442/951
ZIP Code 92264	General	Palm Springs	19,383	Pacific	760/442/951
ZIP Code 92270	General	Rancho Mirage	17,220	Pacific	760
ZIP Code 92274	General	Thermal	19,801	Pacific	760
ZIP Code 92276	General	Thousand Palms	7,585	Pacific	760
ZIP Code 92282	General	Whitewater	1,239	Pacific	442
ZIP Code 92320	General	Calimesa	7,788	Pacific	909
ZIP Code 92501	General	Riverside	20,970	Pacific	951/909
ZIP Code 92502	P.O. Box	Riverside	0	Pacific	951/909
ZIP Code 92503	General	Riverside	84,519	Pacific	951/909
ZIP Code 92504	General	Riverside	53,778	Pacific	951/909
ZIP Code 92505	General	Riverside	47,672	Pacific	951/909
ZIP Code 92506	General	Riverside	44,001	Pacific	951/909
ZIP Code 92507	General	Riverside	58,002	Pacific	951/909
ZIP Code 92508	General	Riverside	35,000	Pacific	909
ZIP Code 92509	General	Jurupa Valley	75,196	Pacific	951
ZIP Code 92513	P.O. Box	Riverside	0	Pacific	951/909
ZIP Code 92514	P.O. Box	Riverside	0	Pacific	951/909
ZIP Code 92516	P.O. Box	Riverside	0	Pacific	951/909
ZIP Code 92517	P.O. Box	Riverside	0	Pacific	951/909
ZIP Code 92518	General	March Air Reserve Base	1,162	Pacific	951
ZIP Code 92519	P.O. Box	Riverside	0	Pacific	951/909
ZIP Code 92521	Unique	Riverside	0	Pacific	951/909
ZIP Code 92522	Unique	Riverside	0	Pacific	951/909
ZIP Code 92530	General	Lake Elsinore	50,216	Pacific	951
ZIP Code 92531	P.O. Box	Lake Elsinore	0	Pacific	951
ZIP Code 92532	General	Lake Elsinore	18,644	Pacific	951
ZIP Code 92536	General	Aguanga	3,810	Pacific	951
ZIP Code 92539	General	Anza	4,734	Pacific	951
ZIP Code 92543	General	Hemet	33,555	Pacific	951/909
ZIP Code 92544	General	Hemet	44,734	Pacific	951/909
ZIP Code 92545	General	Hemet	39,457	Pacific	951/909
ZIP Code 92546	P.O. Box	Hemet	0	Pacific	951/909
ZIP Code 92548	General	Homeland	6,643	Pacific	951
ZIP Code 92549	P.O. Box	Idyllwild	3,926	Pacific	951
ZIP Code 92551	General	Moreno Valley	30,815	Pacific	951
ZIP Code 92552	P.O. Box	Moreno Valley	0	Pacific	951
ZIP Code 92553	General	Moreno Valley	73,722	Pacific	951
ZIP Code 92554	P.O. Box	Moreno Valley	0	Pacific	909
ZIP Code 92555	General	Moreno Valley	39,076	Pacific	951
ZIP Code 92556	P.O. Box	Moreno Valley	0	Pacific	909
ZIP Code 92557	General	Moreno Valley	50,320	Pacific	951
ZIP Code 92561	General	Mountain Center	1,661	Pacific	442/760
ZIP Code 92562	General	Murrieta	62,079	Pacific	951
ZIP Code 92563	General	Murrieta	53,892	Pacific	951
ZIP Code 92564	P.O. Box	Murrieta	0	Pacific	951
ZIP Code 92567	General	Nuevo	9,459	Pacific	951
ZIP Code 92570	General	Perris	53,697	Pacific	951
ZIP Code 92571	General	Perris	52,516	Pacific	951
ZIP Code 92572	P.O. Box	Perris	0	Pacific	951
ZIP Code 92581	P.O. Box	San Jacinto	0	Pacific	951/909
ZIP Code 92582	General	San Jacinto	15,649	Pacific	951
ZIP Code 92583	General	San Jacinto	30,236	Pacific	951/909
ZIP Code 92584	General	Menifee	43,400	Pacific	951
ZIP Code 92585	General	Menifee	17,797	Pacific	951
ZIP Code 92586	General	Menifee	19,815	Pacific	951
ZIP Code 92587	General	Menifee	16,675	Pacific	951
ZIP Code 92589	P.O. Box	Temecula	0	Pacific	951/909
ZIP Code 92590	General	Temecula	3,660	Pacific	951/909
ZIP Code 92591	General	Temecula	38,272	Pacific	951/909
ZIP Code 92592	General	Temecula	72,492	Pacific	951/909
ZIP Code 92593	P.O. Box	Temecula	0	Pacific	951/909
ZIP Code 92595	General	Wildomar	29,851	Pacific	951
ZIP Code 92596	General	Winchester	23,172	Pacific	951
ZIP Code 92599	Unique	Perris	0	Pacific	951
ZIP Code 92860	General	Norco	27,198	Pacific	909
ZIP Code 92877	P.O. Box	Corona	0	Pacific	951
ZIP Code 92878	General	Corona	0	Pacific	951
ZIP Code 92879	General	Corona	46,745	Pacific	951/909
ZIP Code 92880	General	Corona	58,763	Pacific	909
ZIP Code 92881	General	Corona	30,991	Pacific	951/909
ZIP Code 92882	General	Corona	67,917	Pacific	951/909
ZIP Code 92883	General	Corona	29,301	Pacific	951"""
    )