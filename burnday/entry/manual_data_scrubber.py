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
    zip_code_parse(raw_zip_code_data="""ZIP Code 90001	General	Los Angeles	57,110	Pacific	323/213
ZIP Code 90002	General	Los Angeles	51,223	Pacific	323/562/213
ZIP Code 90003	General	Los Angeles	66,266	Pacific	323/213
ZIP Code 90004	General	Los Angeles	62,180	Pacific	323/213
ZIP Code 90005	General	Los Angeles	37,681	Pacific	213/323/310/818/626/562
ZIP Code 90006	General	Los Angeles	59,185	Pacific	213/323
ZIP Code 90007	General	Los Angeles	40,920	Pacific	323/213
ZIP Code 90008	General	Los Angeles	32,327	Pacific	323/213
ZIP Code 90009	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90010	General	Los Angeles	3,800	Pacific	323/310/818/213/626/562
ZIP Code 90011	General	Los Angeles	103,892	Pacific	323/213
ZIP Code 90012	General	Los Angeles	31,103	Pacific	323/213/818
ZIP Code 90013	General	Los Angeles	11,772	Pacific	213/323/424/626/818/562/747/310
ZIP Code 90014	General	Los Angeles	7,005	Pacific	213/323/626/424/818/310/562/747
ZIP Code 90015	General	Los Angeles	18,986	Pacific	213/323/310/626/818/562/424
ZIP Code 90016	General	Los Angeles	47,596	Pacific	424
ZIP Code 90017	General	Los Angeles	23,768	Pacific	213/323/626/310/562/818/424
ZIP Code 90018	General	Los Angeles	49,310	Pacific	323/213
ZIP Code 90019	General	Los Angeles	64,458	Pacific	323/213
ZIP Code 90020	General	Los Angeles	38,967	Pacific	323/310/818/213/626/562
ZIP Code 90021	General	Los Angeles	3,951	Pacific	213/323/424/626/818/562/747/310
ZIP Code 90022	General	Los Angeles	67,179	Pacific	562/323
ZIP Code 90023	General	Los Angeles	45,903	Pacific	323/213
ZIP Code 90024	General	Los Angeles	47,452	Pacific	310/818/323
ZIP Code 90025	General	Los Angeles	42,147	Pacific	310/424/818
ZIP Code 90026	General	Los Angeles	67,869	Pacific	213
ZIP Code 90027	General	Los Angeles	45,151	Pacific	323/818/213/747
ZIP Code 90028	General	Los Angeles	28,714	Pacific	323/818/213/747/310
ZIP Code 90029	General	Los Angeles	38,617	Pacific	323/213
ZIP Code 90030	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90031	General	Los Angeles	39,316	Pacific	323/213
ZIP Code 90032	General	Los Angeles	45,786	Pacific	626
ZIP Code 90033	General	Los Angeles	48,852	Pacific	323/213
ZIP Code 90034	General	Los Angeles	57,964	Pacific	424/310
ZIP Code 90035	General	Los Angeles	28,418	Pacific	310/424
ZIP Code 90036	General	Los Angeles	36,865	Pacific	323/213
ZIP Code 90037	General	Los Angeles	62,276	Pacific	323/424/310/213
ZIP Code 90038	General	Los Angeles	28,917	Pacific	323/213/818/747/310
ZIP Code 90039	General	Los Angeles	28,514	Pacific	818/747/323
ZIP Code 90040	General	Los Angeles	12,520	Pacific	562/323
ZIP Code 90041	General	Los Angeles	27,425	Pacific	323/626/213
ZIP Code 90042	General	Los Angeles	62,430	Pacific	323/626/213
ZIP Code 90043	General	Los Angeles	44,789	Pacific	323/213
ZIP Code 90044	General	Los Angeles	89,779	Pacific	323/310/213
ZIP Code 90045	General	Los Angeles	39,480	Pacific	323
ZIP Code 90046	General	Los Angeles	48,581	Pacific	323
ZIP Code 90047	General	Los Angeles	48,606	Pacific	323/213
ZIP Code 90048	General	Los Angeles	21,397	Pacific	323/310
ZIP Code 90049	General	Los Angeles	35,482	Pacific	818/310
ZIP Code 90050	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90051	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90052	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90053	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90054	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90055	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90056	General	Los Angeles	7,827	Pacific	323
ZIP Code 90057	General	Los Angeles	44,998	Pacific	213
ZIP Code 90058	General	Los Angeles	3,223	Pacific	323/213
ZIP Code 90059	General	Los Angeles	40,952	Pacific	310/213
ZIP Code 90060	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90061	General	Los Angeles	26,872	Pacific	310/323/213
ZIP Code 90062	General	Los Angeles	32,821	Pacific	323/213
ZIP Code 90063	General	Los Angeles	55,758	Pacific	323/213
ZIP Code 90064	General	Los Angeles	25,403	Pacific	310/818
ZIP Code 90065	General	Los Angeles	45,527	Pacific	323/213
ZIP Code 90066	General	Los Angeles	55,277	Pacific	310/424
ZIP Code 90067	General	Los Angeles	2,424	Pacific	310/323
ZIP Code 90068	General	Los Angeles	22,286	Pacific	323/213/310
ZIP Code 90069	General	West Hollywood	20,483	Pacific	818/323
ZIP Code 90070	P.O. Box	Los Angeles	0	Pacific	213
ZIP Code 90071	General	Los Angeles	15	Pacific	213/323/626/424/310/818/562/747
ZIP Code 90072	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90073	P.O. Box	Los Angeles	539	Pacific	310/424/818
ZIP Code 90074	Unique	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90075	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90076	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90077	General	Los Angeles	9,377	Pacific	818/310
ZIP Code 90078	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90079	General	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90080	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90081	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90082	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90083	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90084	Unique	Los Angeles	0	Pacific	310/818/323
ZIP Code 90086	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90087	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90088	Unique	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90089	Unique	Los Angeles	3,217	Pacific	323/213
ZIP Code 90091	P.O. Box	Los Angeles	0	Pacific	562/323
ZIP Code 90093	P.O. Box	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90094	General	Playa Vista	5,464	Pacific	323
ZIP Code 90095	Unique	Los Angeles	3	Pacific	310/818/323
ZIP Code 90096	Unique	Los Angeles	0	Pacific	323/213
ZIP Code 90099	Unique	Los Angeles	0	Pacific	213/323/626/424/310/818/562/747
ZIP Code 90134	General	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90189	Unique	Los Angeles	0	Pacific	213/424/323/818/626/747
ZIP Code 90201	General	Bell Gardens	101,279	Pacific	323
ZIP Code 90202	P.O. Box	Bell	0	Pacific	323
ZIP Code 90209	P.O. Box	Beverly Hills	0	Pacific	310/424/323
ZIP Code 90210	General	Beverly Hills	21,741	Pacific	310/424/323
ZIP Code 90211	General	Beverly Hills	8,434	Pacific	310/424/323
ZIP Code 90212	General	Beverly Hills	11,555	Pacific	310/424/323
ZIP Code 90213	P.O. Box	Beverly Hills	0	Pacific	310/424/323
ZIP Code 90220	General	Compton	49,328	Pacific	310/562/424/323
ZIP Code 90221	General	Compton	53,704	Pacific	310/562/424/323
ZIP Code 90222	General	Compton	31,869	Pacific	310/562/424/323
ZIP Code 90223	P.O. Box	Compton	0	Pacific	310/562/424/323
ZIP Code 90224	P.O. Box	Compton	0	Pacific	310/562/424/323
ZIP Code 90230	General	Culver City	31,766	Pacific	310/424/323
ZIP Code 90231	P.O. Box	Culver City	0	Pacific	310/424/323
ZIP Code 90232	General	Culver City	15,149	Pacific	310/424/323
ZIP Code 90233	P.O. Box	Culver City	0	Pacific	310/424/323
ZIP Code 90239	P.O. Box	Downey	0	Pacific	562
ZIP Code 90240	General	Downey	25,876	Pacific	562
ZIP Code 90241	General	Downey	42,399	Pacific	562
ZIP Code 90242	General	Downey	43,497	Pacific	562
ZIP Code 90245	General	El Segundo	16,654	Pacific	310/424
ZIP Code 90247	General	Gardena	47,487	Pacific	310/424/562/213/323
ZIP Code 90248	General	Gardena	9,947	Pacific	310/424/562/213/323
ZIP Code 90249	General	Gardena	26,669	Pacific	310/424/562/213/323
ZIP Code 90250	General	Hawthorne	93,193	Pacific	310/424/323
ZIP Code 90251	P.O. Box	Hawthorne	0	Pacific	310/424/323
ZIP Code 90254	General	Hermosa Beach	19,506	Pacific	424/310
ZIP Code 90255	General	Huntington Park	75,066	Pacific	323/213
ZIP Code 90260	General	Lawndale	34,924	Pacific	424/310
ZIP Code 90261	General	Lawndale	0	Pacific	424/310
ZIP Code 90262	General	Lynwood	69,745	Pacific	323
ZIP Code 90263	Unique	Malibu	1,612	Pacific	310/424
ZIP Code 90264	P.O. Box	Malibu	0	Pacific	424/310
ZIP Code 90265	General	Malibu	18,116	Pacific	424/310
ZIP Code 90266	General	Manhattan Beach	35,135	Pacific	310
ZIP Code 90267	P.O. Box	Manhattan Beach	0	Pacific	310
ZIP Code 90270	General	Maywood	27,372	Pacific	323
ZIP Code 90272	General	Pacific Palisades	22,986	Pacific	424
ZIP Code 90274	General	Palos Verdes Peninsula	25,209	Pacific	310
ZIP Code 90275	General	Rancho Palos Verdes	41,804	Pacific	310
ZIP Code 90277	General	Redondo Beach	35,293	Pacific	424/310
ZIP Code 90278	General	Redondo Beach	40,071	Pacific	424/310
ZIP Code 90280	General	South Gate	94,396	Pacific	323
ZIP Code 90290	General	Topanga	6,368	Pacific	424/310
ZIP Code 90291	General	Venice	28,341	Pacific	310/424
ZIP Code 90292	General	Marina Del Rey	21,576	Pacific	310/424
ZIP Code 90293	General	Playa Del Rey	12,132	Pacific	310/424
ZIP Code 90294	P.O. Box	Venice	0	Pacific	310/424
ZIP Code 90295	P.O. Box	Marina Del Rey	0	Pacific	310/424
ZIP Code 90296	P.O. Box	Playa Del Rey	0	Pacific	310/424
ZIP Code 90301	General	Inglewood	36,568	Pacific	310/424/323
ZIP Code 90302	General	Inglewood	29,415	Pacific	310/323/424
ZIP Code 90303	General	Inglewood	26,176	Pacific	310
ZIP Code 90304	General	Inglewood	28,210	Pacific	424/310
ZIP Code 90305	General	Inglewood	14,853	Pacific	424/310
ZIP Code 90306	P.O. Box	Inglewood	0	Pacific	310/424/323
ZIP Code 90307	P.O. Box	Inglewood	0	Pacific	310/424/323
ZIP Code 90308	P.O. Box	Inglewood	0	Pacific	310/424/323
ZIP Code 90309	P.O. Box	Inglewood	0	Pacific	310/424/323
ZIP Code 90310	P.O. Box	Inglewood	0	Pacific	310/424/323
ZIP Code 90311	General	Inglewood	0	Pacific	310/424/323
ZIP Code 90312	P.O. Box	Inglewood	0	Pacific	310/424/323
ZIP Code 90401	General	Santa Monica	6,722	Pacific	310/424
ZIP Code 90402	General	Santa Monica	12,250	Pacific	310
ZIP Code 90403	General	Santa Monica	24,525	Pacific	310/424
ZIP Code 90404	General	Santa Monica	21,360	Pacific	310/424
ZIP Code 90405	General	Santa Monica	27,186	Pacific	310/424
ZIP Code 90406	P.O. Box	Santa Monica	0	Pacific	310/424
ZIP Code 90407	P.O. Box	Santa Monica	0	Pacific	310/424
ZIP Code 90408	P.O. Box	Santa Monica	0	Pacific	310/424
ZIP Code 90409	P.O. Box	Santa Monica	0	Pacific	310/424
ZIP Code 90410	P.O. Box	Santa Monica	0	Pacific	310/424
ZIP Code 90411	P.O. Box	Santa Monica	0	Pacific	310/424
ZIP Code 90501	General	Torrance	43,180	Pacific	310/424
ZIP Code 90502	General	Torrance	18,010	Pacific	310/424
ZIP Code 90503	General	Torrance	44,383	Pacific	310/424
ZIP Code 90504	General	Torrance	32,102	Pacific	310/424
ZIP Code 90505	General	Torrance	36,678	Pacific	310
ZIP Code 90506	General	Torrance	0	Pacific	310/424
ZIP Code 90507	P.O. Box	Torrance	0	Pacific	310/424
ZIP Code 90508	P.O. Box	Torrance	0	Pacific	310/424
ZIP Code 90509	P.O. Box	Torrance	0	Pacific	310/424
ZIP Code 90510	P.O. Box	Torrance	0	Pacific	310/424
ZIP Code 90601	General	Whittier	31,974	Pacific	562
ZIP Code 90602	General	Whittier	25,777	Pacific	562
ZIP Code 90603	General	Whittier	20,063	Pacific	562
ZIP Code 90604	General	Whittier	39,407	Pacific	562
ZIP Code 90605	General	Whittier	40,331	Pacific	562
ZIP Code 90606	General	Whittier	32,396	Pacific	562
ZIP Code 90607	P.O. Box	Whittier	0	Pacific	562
ZIP Code 90608	P.O. Box	Whittier	0	Pacific	562
ZIP Code 90609	P.O. Box	Whittier	0	Pacific	562
ZIP Code 90610	P.O. Box	Whittier	0	Pacific	562
ZIP Code 90637	P.O. Box	La Mirada	0	Pacific	562
ZIP Code 90638	General	La Mirada	49,012	Pacific	714
ZIP Code 90639	Unique	La Mirada	0	Pacific	714
ZIP Code 90640	General	Montebello	62,549	Pacific	323/213
ZIP Code 90650	General	Norwalk	105,549	Pacific	562
ZIP Code 90651	P.O. Box	Norwalk	0	Pacific	562
ZIP Code 90652	P.O. Box	Norwalk	0	Pacific	562
ZIP Code 90660	General	Pico Rivera	62,928	Pacific	562
ZIP Code 90661	P.O. Box	Pico Rivera	0	Pacific	562
ZIP Code 90662	P.O. Box	Pico Rivera	0	Pacific	562
ZIP Code 90670	General	Santa Fe Springs	14,866	Pacific	562
ZIP Code 90671	P.O. Box	Santa Fe Springs	0	Pacific	562
ZIP Code 90701	General	Artesia	16,591	Pacific	562/310
ZIP Code 90702	P.O. Box	Artesia	0	Pacific	562/310
ZIP Code 90703	General	Cerritos	49,399	Pacific	562/310
ZIP Code 90704	P.O. Box	Avalon	4,090	Pacific	310/424/562
ZIP Code 90706	General	Bellflower	76,615	Pacific	562
ZIP Code 90707	P.O. Box	Bellflower	0	Pacific	562
ZIP Code 90710	General	Harbor City	25,457	Pacific	310/424
ZIP Code 90711	P.O. Box	Lakewood	0	Pacific	562/310/657/323
ZIP Code 90712	General	Lakewood	31,499	Pacific	562/310/657/323
ZIP Code 90713	General	Lakewood	27,925	Pacific	562/310/657/323
ZIP Code 90714	P.O. Box	Lakewood	0	Pacific	562/310/657/323
ZIP Code 90715	General	Lakewood	20,388	Pacific	562/310
ZIP Code 90716	General	Hawaiian Gardens	14,184	Pacific	562/310
ZIP Code 90717	General	Lomita	21,318	Pacific	310/424
ZIP Code 90723	General	Paramount	54,099	Pacific	562
ZIP Code 90731	General	San Pedro	59,662	Pacific	310/424/562
ZIP Code 90732	General	San Pedro	21,115	Pacific	310/424/562
ZIP Code 90733	P.O. Box	San Pedro	0	Pacific	310/424/562
ZIP Code 90734	P.O. Box	San Pedro	0	Pacific	310/424/562
ZIP Code 90744	General	Wilmington	53,815	Pacific	562/310/323/424
ZIP Code 90745	General	Carson	57,251	Pacific	562
ZIP Code 90746	General	Carson	25,990	Pacific	562
ZIP Code 90747	Unique	Carson	0	Pacific	562
ZIP Code 90748	P.O. Box	Wilmington	0	Pacific	562/310/323/424
ZIP Code 90749	P.O. Box	Carson	0	Pacific	310/424
ZIP Code 90755	General	Signal Hill	11,074	Pacific	562
ZIP Code 90801	P.O. Box	Long Beach	0	Pacific	562/310/714/323
ZIP Code 90802	General	Long Beach	39,347	Pacific	562/310/424/714/323
ZIP Code 90803	General	Long Beach	32,031	Pacific	562
ZIP Code 90804	General	Long Beach	40,311	Pacific	562
ZIP Code 90805	General	Long Beach	93,524	Pacific	562/310/323
ZIP Code 90806	General	Long Beach	42,399	Pacific	562
ZIP Code 90807	General	Long Beach	31,481	Pacific	562/714/657
ZIP Code 90808	General	Long Beach	38,232	Pacific	562/310/657/714/323
ZIP Code 90809	P.O. Box	Long Beach	0	Pacific	562/310/714/323
ZIP Code 90810	General	Long Beach	36,735	Pacific	562
ZIP Code 90813	General	Long Beach	58,911	Pacific	562/310/714/323
ZIP Code 90814	General	Long Beach	19,131	Pacific	562
ZIP Code 90815	General	Long Beach	39,733	Pacific	562/714/657
ZIP Code 90822	General	Long Beach	117	Pacific	562/424/310/714/323
ZIP Code 90831	General	Long Beach	0	Pacific	562/424
ZIP Code 90832	P.O. Box	Long Beach	0	Pacific	562/310/714/323
ZIP Code 90833	General	Long Beach	0	Pacific	562/424
ZIP Code 90840	Unique	Long Beach	0	Pacific	562/714/657
ZIP Code 90842	Unique	Long Beach	0	Pacific	562/310/714/323
ZIP Code 90844	Unique	Long Beach	0	Pacific	562/310/714/323
ZIP Code 90846	Unique	Long Beach	0	Pacific	562/310/714/323
ZIP Code 90847	Unique	Long Beach	0	Pacific	562/310/714/323
ZIP Code 90848	Unique	Long Beach	0	Pacific	562/310/714/323
ZIP Code 90853	P.O. Box	Long Beach	0	Pacific	562/310/714/323
ZIP Code 90895	Unique	Carson	0	Pacific	562
ZIP Code 91001	General	Altadena	36,126	Pacific	626/323
ZIP Code 91003	P.O. Box	Altadena	0	Pacific	626/323
ZIP Code 91006	General	Arcadia	31,715	Pacific	626
ZIP Code 91007	General	Arcadia	34,095	Pacific	626
ZIP Code 91008	General	Duarte	1,391	Pacific	626
ZIP Code 91009	P.O. Box	Duarte	0	Pacific	626
ZIP Code 91010	General	Duarte	26,074	Pacific	626
ZIP Code 91011	General	La Canada Flintridge	20,280	Pacific	818
ZIP Code 91012	P.O. Box	La Canada Flintridge	0	Pacific	818/747
ZIP Code 91016	General	Monrovia	40,598	Pacific	626
ZIP Code 91017	P.O. Box	Monrovia	0	Pacific	626
ZIP Code 91020	General	Montrose	8,415	Pacific	818/747
ZIP Code 91021	P.O. Box	Montrose	0	Pacific	818/747
ZIP Code 91023	P.O. Box	Mount Wilson	0	Pacific	818
ZIP Code 91024	General	Sierra Madre	10,917	Pacific	626
ZIP Code 91025	P.O. Box	Sierra Madre	0	Pacific	626
ZIP Code 91030	General	South Pasadena	25,616	Pacific	626/323
ZIP Code 91031	P.O. Box	South Pasadena	0	Pacific	626/323
ZIP Code 91040	General	Sunland	20,372	Pacific	818/747
ZIP Code 91041	P.O. Box	Sunland	0	Pacific	818/747
ZIP Code 91042	General	Tujunga	27,585	Pacific	747/818
ZIP Code 91043	P.O. Box	Tujunga	0	Pacific	818/747
ZIP Code 91046	P.O. Box	Verdugo City	156	Pacific	818/747
ZIP Code 91066	P.O. Box	Arcadia	0	Pacific	626
ZIP Code 91077	P.O. Box	Arcadia	0	Pacific	626
ZIP Code 91101	General	Pasadena	20,460	Pacific	626/323
ZIP Code 91102	P.O. Box	Pasadena	0	Pacific	626/323
ZIP Code 91103	General	Pasadena	27,480	Pacific	626/323
ZIP Code 91104	General	Pasadena	36,751	Pacific	626/323
ZIP Code 91105	General	Pasadena	11,254	Pacific	626/323
ZIP Code 91106	General	Pasadena	24,229	Pacific	626/323
ZIP Code 91107	General	Pasadena	32,940	Pacific	626/323
ZIP Code 91108	General	San Marino	13,361	Pacific	626
ZIP Code 91109	P.O. Box	Pasadena	0	Pacific	626/323
ZIP Code 91110	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91114	P.O. Box	Pasadena	0	Pacific	626/323
ZIP Code 91115	P.O. Box	Pasadena	0	Pacific	626/323
ZIP Code 91116	P.O. Box	Pasadena	0	Pacific	626/323
ZIP Code 91117	P.O. Box	Pasadena	0	Pacific	626/323
ZIP Code 91118	P.O. Box	San Marino	0	Pacific	626/323
ZIP Code 91121	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91123	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91124	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91125	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91126	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91129	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91182	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91184	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91185	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91188	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91189	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91199	Unique	Pasadena	0	Pacific	626/323
ZIP Code 91201	General	Glendale	22,781	Pacific	818/747/323
ZIP Code 91202	General	Glendale	22,830	Pacific	818/747
ZIP Code 91203	General	Glendale	13,220	Pacific	818/747
ZIP Code 91204	General	Glendale	16,032	Pacific	818/747/323
ZIP Code 91205	General	Glendale	37,810	Pacific	818/323/747
ZIP Code 91206	General	Glendale	33,065	Pacific	323/626/213
ZIP Code 91207	General	Glendale	10,506	Pacific	818/747
ZIP Code 91208	General	Glendale	16,245	Pacific	818/747
ZIP Code 91209	P.O. Box	Glendale	0	Pacific	818/747/323
ZIP Code 91210	General	Glendale	328	Pacific	818/747/323
ZIP Code 91214	General	La Crescenta	30,356	Pacific	818/747
ZIP Code 91221	P.O. Box	Glendale	0	Pacific	818/747/323
ZIP Code 91222	P.O. Box	Glendale	0	Pacific	818/747/323
ZIP Code 91224	P.O. Box	La Crescenta	0	Pacific	818/747/323
ZIP Code 91225	P.O. Box	Glendale	0	Pacific	818/747/323
ZIP Code 91226	P.O. Box	Glendale	0	Pacific	818/747/323
ZIP Code 91301	General	Agoura Hills	25,488	Pacific	818/747
ZIP Code 91302	General	Calabasas	25,709	Pacific	424/310
ZIP Code 91303	General	Canoga Park	26,855	Pacific	818/747
ZIP Code 91304	General	Canoga Park	50,231	Pacific	818/747
ZIP Code 91305	P.O. Box	Canoga Park	0	Pacific	818/747
ZIP Code 91306	General	Winnetka	45,061	Pacific	818/747
ZIP Code 91307	General	West Hills	24,474	Pacific	818
ZIP Code 91308	P.O. Box	West Hills	0	Pacific	818/747
ZIP Code 91309	P.O. Box	Canoga Park	0	Pacific	818/747
ZIP Code 91310	P.O. Box	Castaic	0	Pacific	805/820
ZIP Code 91311	General	Chatsworth	36,557	Pacific	818/747
ZIP Code 91313	P.O. Box	Chatsworth	0	Pacific	818/747
ZIP Code 91316	General	Encino	26,898	Pacific	818
ZIP Code 91321	General	Newhall	34,882	Pacific	661
ZIP Code 91322	P.O. Box	Newhall	0	Pacific	661
ZIP Code 91324	General	Northridge	27,669	Pacific	818/747
ZIP Code 91325	General	Northridge	32,417	Pacific	818/747
ZIP Code 91326	General	Porter Ranch	33,708	Pacific	818/747
ZIP Code 91327	P.O. Box	Northridge	0	Pacific	818/747
ZIP Code 91328	P.O. Box	Northridge	0	Pacific	818/747
ZIP Code 91329	Unique	Northridge	0	Pacific	818/747
ZIP Code 91330	Unique	Northridge	2,702	Pacific	818/747
ZIP Code 91331	General	Pacoima	103,689	Pacific	818/747
ZIP Code 91333	P.O. Box	Pacoima	0	Pacific	818/747
ZIP Code 91334	P.O. Box	Pacoima	0	Pacific	818/747
ZIP Code 91335	General	Reseda	74,363	Pacific	818/747
ZIP Code 91337	P.O. Box	Reseda	0	Pacific	818/747
ZIP Code 91340	General	San Fernando	34,188	Pacific	818/747
ZIP Code 91341	P.O. Box	San Fernando	0	Pacific	818/747
ZIP Code 91342	General	Sylmar	91,725	Pacific	818/747
ZIP Code 91343	General	North Hills	60,254	Pacific	818/747
ZIP Code 91344	General	Granada Hills	51,747	Pacific	818/747
ZIP Code 91345	General	Mission Hills	18,496	Pacific	818/747
ZIP Code 91346	P.O. Box	Mission Hills	0	Pacific	818/747
ZIP Code 91350	General	Santa Clarita	33,348	Pacific	661
ZIP Code 91351	General	Canyon Country	32,362	Pacific	661
ZIP Code 91352	General	Sun Valley	47,807	Pacific	818/626/213/323/747/310
ZIP Code 91353	P.O. Box	Sun Valley	0	Pacific	818/323
ZIP Code 91354	General	Valencia	28,722	Pacific	805/820
ZIP Code 91355	General	Valencia	32,605	Pacific	661
ZIP Code 91356	General	Tarzana	29,458	Pacific	818
ZIP Code 91357	P.O. Box	Tarzana	0	Pacific	818
ZIP Code 91364	General	Woodland Hills	25,851	Pacific	818
ZIP Code 91365	P.O. Box	Woodland Hills	0	Pacific	818
ZIP Code 91367	General	Woodland Hills	39,499	Pacific	818
ZIP Code 91371	Unique	Woodland Hills	1	Pacific	818/747
ZIP Code 91372	P.O. Box	Calabasas	0	Pacific	818
ZIP Code 91376	P.O. Box	Agoura Hills	0	Pacific	818/747
ZIP Code 91380	P.O. Box	Santa Clarita	0	Pacific	805/820
ZIP Code 91381	General	Stevenson Ranch	20,158	Pacific	661
ZIP Code 91382	General	Santa Clarita	0	Pacific	661
ZIP Code 91383	General	Santa Clarita	0	Pacific	805/820
ZIP Code 91384	General	Castaic	29,855	Pacific	661/805/820
ZIP Code 91385	P.O. Box	Valencia	0	Pacific	818/747
ZIP Code 91386	P.O. Box	Canyon Country	0	Pacific	661
ZIP Code 91387	General	Canyon Country	40,328	Pacific	661
ZIP Code 91390	General	Santa Clarita	19,786	Pacific	661
ZIP Code 91392	P.O. Box	Sylmar	0	Pacific	818/747
ZIP Code 91393	P.O. Box	North Hills	0	Pacific	818/747/323
ZIP Code 91394	P.O. Box	Granada Hills	0	Pacific	818/747
ZIP Code 91395	P.O. Box	Mission Hills	0	Pacific	818/747
ZIP Code 91396	P.O. Box	Winnetka	0	Pacific	818/747
ZIP Code 91401	General	Van Nuys	39,285	Pacific	818/323
ZIP Code 91402	General	Panorama City	69,817	Pacific	818
ZIP Code 91403	General	Sherman Oaks	23,484	Pacific	818/747/323/424/213
ZIP Code 91404	P.O. Box	Van Nuys	0	Pacific	818/323/747/424/213
ZIP Code 91405	General	Van Nuys	51,145	Pacific	818/323
ZIP Code 91406	General	Van Nuys	51,558	Pacific	818
ZIP Code 91407	P.O. Box	Van Nuys	0	Pacific	818/323/747/424/213
ZIP Code 91408	P.O. Box	Van Nuys	0	Pacific	818/323/747/424/213
ZIP Code 91409	P.O. Box	Van Nuys	0	Pacific	818/323/747/424/213
ZIP Code 91410	P.O. Box	Van Nuys	0	Pacific	818/323/747/424/213
ZIP Code 91411	General	Van Nuys	24,628	Pacific	818/323/747/424/213
ZIP Code 91412	P.O. Box	Panorama City	0	Pacific	818
ZIP Code 91413	P.O. Box	Sherman Oaks	0	Pacific	818/747/323/424/213
ZIP Code 91416	P.O. Box	Encino	0	Pacific	818/747
ZIP Code 91423	General	Sherman Oaks	30,991	Pacific	818/747/323/424/213
ZIP Code 91426	P.O. Box	Encino	0	Pacific	818/747
ZIP Code 91436	General	Encino	14,372	Pacific	818/747
ZIP Code 91470	Unique	Van Nuys	0	Pacific	818/323/747/424/213
ZIP Code 91482	Unique	Van Nuys	0	Pacific	818/323/747/424/213
ZIP Code 91495	Unique	Sherman Oaks	0	Pacific	818/747/323/424/213
ZIP Code 91496	Unique	Van Nuys	0	Pacific	818/323/747/424/213
ZIP Code 91499	Unique	Van Nuys	0	Pacific	818/323/747/424/213
ZIP Code 91501	General	Burbank	20,849	Pacific	818/747/323
ZIP Code 91502	General	Burbank	11,371	Pacific	818/747/323
ZIP Code 91503	P.O. Box	Burbank	0	Pacific	818/747/323
ZIP Code 91504	General	Burbank	24,939	Pacific	818/626/213/323/310/747
ZIP Code 91505	General	Burbank	30,778	Pacific	818/626/213/323/310
ZIP Code 91506	General	Burbank	18,904	Pacific	818/747/323
ZIP Code 91507	P.O. Box	Burbank	0	Pacific	818/747/323
ZIP Code 91508	P.O. Box	Burbank	0	Pacific	818/747/323
ZIP Code 91510	P.O. Box	Burbank	0	Pacific	818/747/323
ZIP Code 91521	Unique	Burbank	0	Pacific	818/747/323
ZIP Code 91522	Unique	Burbank	0	Pacific	323/213/310
ZIP Code 91523	Unique	Burbank	0	Pacific	818/747/323
ZIP Code 91526	Unique	Burbank	0	Pacific	818/747/323
ZIP Code 91601	General	North Hollywood	37,180	Pacific	818/747/323
ZIP Code 91602	General	North Hollywood	17,473	Pacific	818/747/323
ZIP Code 91603	P.O. Box	North Hollywood	0	Pacific	818/747/323
ZIP Code 91604	General	Studio City	29,034	Pacific	747
ZIP Code 91605	General	North Hollywood	56,343	Pacific	818/323
ZIP Code 91606	General	North Hollywood	44,958	Pacific	818/747/323
ZIP Code 91607	General	Valley Village	27,927	Pacific	818/747/323
ZIP Code 91608	General	Universal City	0	Pacific	818/747/323
ZIP Code 91609	P.O. Box	North Hollywood	0	Pacific	818/747/323
ZIP Code 91610	P.O. Box	Toluca Lake	0	Pacific	818/747/323
ZIP Code 91611	Unique	North Hollywood	0	Pacific	818/747/323
ZIP Code 91612	Unique	North Hollywood	0	Pacific	818/747/323
ZIP Code 91614	P.O. Box	Studio City	0	Pacific	818/747/323
ZIP Code 91615	P.O. Box	North Hollywood	0	Pacific	818/747/323
ZIP Code 91616	P.O. Box	North Hollywood	0	Pacific	818/747/323
ZIP Code 91617	P.O. Box	Valley Village	0	Pacific	818/747/323
ZIP Code 91618	P.O. Box	North Hollywood	0	Pacific	818/747/323
ZIP Code 91702	General	Azusa	59,705	Pacific	626
ZIP Code 91706	General	Baldwin Park	76,571	Pacific	626
ZIP Code 91711	General	Claremont	35,705	Pacific	909
ZIP Code 91714	P.O. Box	City Of Industry	0	Pacific	626/323/818
ZIP Code 91715	P.O. Box	City Of Industry	0	Pacific	626/323/818
ZIP Code 91716	P.O. Box	City Of Industry	0	Pacific	626/323/818
ZIP Code 91722	General	Covina	34,409	Pacific	626/909/562
ZIP Code 91723	General	Covina	18,275	Pacific	626/909/562
ZIP Code 91724	General	Covina	26,184	Pacific	626/909/562
ZIP Code 91731	General	El Monte	29,591	Pacific	626/323
ZIP Code 91732	General	El Monte	61,386	Pacific	626/323
ZIP Code 91733	General	South El Monte	43,896	Pacific	626/323
ZIP Code 91734	P.O. Box	El Monte	0	Pacific	626/323
ZIP Code 91735	Unique	El Monte	0	Pacific	626/323
ZIP Code 91740	General	Glendora	25,356	Pacific	626
ZIP Code 91741	General	Glendora	25,824	Pacific	626
ZIP Code 91744	General	La Puente	85,040	Pacific	626
ZIP Code 91745	General	Hacienda Heights	54,013	Pacific	626
ZIP Code 91746	General	La Puente	30,485	Pacific	626
ZIP Code 91747	P.O. Box	La Puente	0	Pacific	626
ZIP Code 91748	General	Rowland Heights	45,406	Pacific	626
ZIP Code 91749	P.O. Box	La Puente	0	Pacific	626
ZIP Code 91750	General	La Verne	33,249	Pacific	909/626
ZIP Code 91754	General	Monterey Park	32,742	Pacific	818
ZIP Code 91755	General	Monterey Park	27,496	Pacific	818
ZIP Code 91756	Unique	Monterey Park	0	Pacific	818
ZIP Code 91765	General	Diamond Bar	46,457	Pacific	909
ZIP Code 91766	General	Pomona	71,599	Pacific	909/626/840
ZIP Code 91767	General	Pomona	48,068	Pacific	909/626/840
ZIP Code 91768	General	Pomona	34,537	Pacific	909/626/840
ZIP Code 91769	P.O. Box	Pomona	0	Pacific	909/626/840
ZIP Code 91770	General	Rosemead	62,097	Pacific	626
ZIP Code 91771	Unique	Rosemead	0	Pacific	626
ZIP Code 91772	Unique	Rosemead	0	Pacific	626
ZIP Code 91773	General	San Dimas	33,119	Pacific	909
ZIP Code 91775	General	San Gabriel	23,988	Pacific	626
ZIP Code 91776	General	San Gabriel	38,475	Pacific	626
ZIP Code 91778	P.O. Box	San Gabriel	0	Pacific	626
ZIP Code 91780	General	Temple City	34,332	Pacific	626
ZIP Code 91788	P.O. Box	Walnut	0	Pacific	909
ZIP Code 91789	General	Walnut	43,079	Pacific	909
ZIP Code 91790	General	West Covina	44,907	Pacific	626
ZIP Code 91791	General	West Covina	32,414	Pacific	626
ZIP Code 91792	General	West Covina	30,854	Pacific	626
ZIP Code 91793	P.O. Box	West Covina	0	Pacific	626
ZIP Code 91801	General	Alhambra	52,735	Pacific	626/323/818
ZIP Code 91802	P.O. Box	Alhambra	0	Pacific	626/323/818
ZIP Code 91803	General	Alhambra	30,322	Pacific	626/323/818
ZIP Code 91804	General	Alhambra	0	Pacific	626/323/818
ZIP Code 91896	P.O. Box	Alhambra	0	Pacific	626/323/818
ZIP Code 91899	P.O. Box	Alhambra	0	Pacific	626/323/818
ZIP Code 93510	General	Acton	7,993	Pacific	661
ZIP Code 93532	General	Lake Hughes	2,932	Pacific	661
ZIP Code 93534	General	Lancaster	39,341	Pacific	661
ZIP Code 93535	General	Lancaster	72,046	Pacific	661
ZIP Code 93536	General	Lancaster	70,918	Pacific	661
ZIP Code 93539	P.O. Box	Lancaster	0	Pacific	661
ZIP Code 93543	General	Littlerock	13,033	Pacific	661
ZIP Code 93544	General	Llano	1,259	Pacific	661/760
ZIP Code 93550	General	Palmdale	74,929	Pacific	661
ZIP Code 93551	General	Palmdale	50,798	Pacific	661
ZIP Code 93552	General	Palmdale	38,158	Pacific	661
ZIP Code 93553	General	Pearblossom	2,138	Pacific	661
ZIP Code 93563	General	Valyermo	388	Pacific	661/626
ZIP Code 93584	P.O. Box	Lancaster	0	Pacific	661
ZIP Code 93586	P.O. Box	Lancaster	0	Pacific	661
ZIP Code 93590	P.O. Box	Palmdale	0	Pacific	661
ZIP Code 93591	General	Palmdale	7,285	Pacific	661
ZIP Code 93599	Unique	Palmdale	0	Pacific	661"""
    )