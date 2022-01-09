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
    zip_code_parse(raw_zip_code_data="""ZIP Code 90620	General	Buena Park	45,113	Pacific	714/657
ZIP Code 90621	General	Buena Park	35,153	Pacific	714/657
ZIP Code 90622	P.O. Box	Buena Park	0	Pacific	714/657
ZIP Code 90623	General	La Palma	15,554	Pacific	714/657
ZIP Code 90624	P.O. Box	Buena Park	0	Pacific	714/657
ZIP Code 90630	General	Cypress	47,993	Pacific	714/657
ZIP Code 90631	General	La Habra	67,619	Pacific	562
ZIP Code 90632	P.O. Box	La Habra	0	Pacific	562
ZIP Code 90633	P.O. Box	La Habra	0	Pacific	562
ZIP Code 90680	General	Stanton	29,945	Pacific	657/714
ZIP Code 90720	General	Los Alamitos	21,751	Pacific	562/657/714
ZIP Code 90721	P.O. Box	Los Alamitos	0	Pacific	562/657/714
ZIP Code 90740	General	Seal Beach	23,729	Pacific	562/714
ZIP Code 90742	P.O. Box	Sunset Beach	831	Pacific	714/562
ZIP Code 90743	P.O. Box	Surfside	456	Pacific	714/562
ZIP Code 92602	General	Irvine	22,871	Pacific	949
ZIP Code 92603	General	Irvine	20,184	Pacific	949/714/657
ZIP Code 92604	General	Irvine	26,853	Pacific	949
ZIP Code 92605	P.O. Box	Huntington Beach	0	Pacific	657/714/562
ZIP Code 92606	General	Irvine	21,495	Pacific	949/714
ZIP Code 92607	P.O. Box	Laguna Niguel	0	Pacific	949/714
ZIP Code 92609	P.O. Box	El Toro	0	Pacific	949/714
ZIP Code 92610	General	Foothill Ranch	11,248	Pacific	949
ZIP Code 92612	General	Irvine	27,522	Pacific	949/714
ZIP Code 92614	General	Irvine	24,748	Pacific	949/714
ZIP Code 92615	P.O. Box	Huntington Beach	0	Pacific	657/714/562
ZIP Code 92616	P.O. Box	Irvine	0	Pacific	949/714
ZIP Code 92617	General	Irvine	14,044	Pacific	949/714
ZIP Code 92618	General	Irvine	16,366	Pacific	949/657
ZIP Code 92619	P.O. Box	Irvine	0	Pacific	949/714
ZIP Code 92620	General	Irvine	38,486	Pacific	949/657
ZIP Code 92623	P.O. Box	Irvine	0	Pacific	949/714
ZIP Code 92624	General	Capistrano Beach	7,248	Pacific	949/714
ZIP Code 92625	General	Corona Del Mar	12,478	Pacific	949
ZIP Code 92626	General	Costa Mesa	49,341	Pacific	714/657/949/562
ZIP Code 92627	General	Costa Mesa	61,510	Pacific	949
ZIP Code 92628	P.O. Box	Costa Mesa	0	Pacific	949
ZIP Code 92629	General	Dana Point	25,756	Pacific	949/714
ZIP Code 92630	General	Lake Forest	59,182	Pacific	949/714
ZIP Code 92637	General	Laguna Woods	16,012	Pacific	949/714
ZIP Code 92646	General	Huntington Beach	55,224	Pacific	657/714
ZIP Code 92647	General	Huntington Beach	57,245	Pacific	657/714/562
ZIP Code 92648	General	Huntington Beach	45,317	Pacific	657/714/562
ZIP Code 92649	General	Huntington Beach	32,463	Pacific	714/562
ZIP Code 92650	P.O. Box	East Irvine	0	Pacific	949/657
ZIP Code 92651	General	Laguna Beach	23,881	Pacific	949/714
ZIP Code 92652	P.O. Box	Laguna Beach	0	Pacific	949/714
ZIP Code 92653	General	Laguna Hills	29,291	Pacific	949/714
ZIP Code 92654	P.O. Box	Laguna Hills	0	Pacific	949/714
ZIP Code 92655	General	Midway City	8,337	Pacific	714
ZIP Code 92656	General	Aliso Viejo	49,046	Pacific	949/714
ZIP Code 92657	General	Newport Coast	9,741	Pacific	949
ZIP Code 92658	P.O. Box	Newport Beach	0	Pacific	949
ZIP Code 92659	P.O. Box	Newport Beach	0	Pacific	949
ZIP Code 92660	General	Newport Beach	34,797	Pacific	949
ZIP Code 92661	General	Newport Beach	3,744	Pacific	949
ZIP Code 92662	General	Newport Beach	2,756	Pacific	949
ZIP Code 92663	General	Newport Beach	21,649	Pacific	949
ZIP Code 92672	General	San Clemente	34,464	Pacific	949
ZIP Code 92673	General	San Clemente	29,309	Pacific	949
ZIP Code 92674	P.O. Box	San Clemente	0	Pacific	949
ZIP Code 92675	General	San Juan Capistrano	34,731	Pacific	949/714
ZIP Code 92676	General	Silverado	1,945	Pacific	657/714
ZIP Code 92677	General	Laguna Niguel	63,297	Pacific	949
ZIP Code 92678	P.O. Box	Trabuco Canyon	494	Pacific	949
ZIP Code 92679	General	Trabuco Canyon	32,611	Pacific	949
ZIP Code 92683	General	Westminster	89,747	Pacific	714/657
ZIP Code 92684	P.O. Box	Westminster	0	Pacific	714/657
ZIP Code 92685	P.O. Box	Westminster	0	Pacific	714/657
ZIP Code 92688	General	Rancho Santa Margarita	43,792	Pacific	949
ZIP Code 92690	P.O. Box	Mission Viejo	0	Pacific	949/714
ZIP Code 92691	General	Mission Viejo	47,582	Pacific	949/714
ZIP Code 92692	General	Mission Viejo	47,222	Pacific	949
ZIP Code 92693	P.O. Box	San Juan Capistrano	0	Pacific	949/714
ZIP Code 92694	General	Ladera Ranch	21,944	Pacific	949
ZIP Code 92697	Unique	Irvine	0	Pacific	949/714
ZIP Code 92698	Unique	Aliso Viejo	0	Pacific	949/714
ZIP Code 92701	General	Santa Ana	53,908	Pacific	714/949/657/562
ZIP Code 92702	P.O. Box	Santa Ana	0	Pacific	714/657/949/562
ZIP Code 92703	General	Santa Ana	65,445	Pacific	714/657
ZIP Code 92704	General	Santa Ana	88,123	Pacific	714/657
ZIP Code 92705	General	Santa Ana	44,706	Pacific	714/657
ZIP Code 92706	General	Santa Ana	36,457	Pacific	714/657/949
ZIP Code 92707	General	Santa Ana	59,492	Pacific	714/657/949/562
ZIP Code 92708	General	Fountain Valley	56,004	Pacific	714
ZIP Code 92711	P.O. Box	Santa Ana	0	Pacific	714/657/949/562
ZIP Code 92712	P.O. Box	Santa Ana	0	Pacific	714/657/949/562
ZIP Code 92728	P.O. Box	Fountain Valley	0	Pacific	714
ZIP Code 92735	P.O. Box	Santa Ana	0	Pacific	714/949/657/562
ZIP Code 92780	General	Tustin	57,741	Pacific	657
ZIP Code 92781	P.O. Box	Tustin	0	Pacific	657
ZIP Code 92782	General	Tustin	23,032	Pacific	657
ZIP Code 92799	General	Santa Ana	0	Pacific	714/657/949/562
ZIP Code 92801	General	Anaheim	62,068	Pacific	657/714/949
ZIP Code 92802	General	Anaheim	42,709	Pacific	714/657/949/562/909
ZIP Code 92803	P.O. Box	Anaheim	0	Pacific	714/562/949/626/909
ZIP Code 92804	General	Anaheim	85,914	Pacific	657/714
ZIP Code 92805	General	Anaheim	70,401	Pacific	714/657/949/562/909/626
ZIP Code 92806	General	Anaheim	37,173	Pacific	714/657/562/909/949/626
ZIP Code 92807	General	Anaheim	36,171	Pacific	714
ZIP Code 92808	General	Anaheim	20,039	Pacific	714/657
ZIP Code 92809	General	Anaheim	0	Pacific	657/714/949
ZIP Code 92811	P.O. Box	Atwood	0	Pacific	714/657
ZIP Code 92812	P.O. Box	Anaheim	0	Pacific	714/562/949/626/909
ZIP Code 92814	P.O. Box	Anaheim	0	Pacific	714/562/949/626/909
ZIP Code 92815	P.O. Box	Anaheim	0	Pacific	714/562/949/626/909
ZIP Code 92816	P.O. Box	Anaheim	0	Pacific	714/562/949/626/909
ZIP Code 92817	P.O. Box	Anaheim	0	Pacific	714/562/949/626/909
ZIP Code 92821	General	Brea	35,533	Pacific	714/657
ZIP Code 92822	P.O. Box	Brea	0	Pacific	714/657
ZIP Code 92823	General	Brea	3,613	Pacific	714/657
ZIP Code 92825	P.O. Box	Anaheim	0	Pacific	714/562/949/626/909
ZIP Code 92831	General	Fullerton	34,204	Pacific	714/657
ZIP Code 92832	General	Fullerton	24,752	Pacific	714/657
ZIP Code 92833	General	Fullerton	51,767	Pacific	657/714
ZIP Code 92834	P.O. Box	Fullerton	0	Pacific	714/657
ZIP Code 92835	General	Fullerton	24,010	Pacific	714/657
ZIP Code 92836	P.O. Box	Fullerton	0	Pacific	714/657
ZIP Code 92837	P.O. Box	Fullerton	0	Pacific	714/657
ZIP Code 92838	P.O. Box	Fullerton	0	Pacific	714/657
ZIP Code 92840	General	Garden Grove	54,083	Pacific	714/657
ZIP Code 92841	General	Garden Grove	32,845	Pacific	657/714
ZIP Code 92842	P.O. Box	Garden Grove	0	Pacific	714/657
ZIP Code 92843	General	Garden Grove	45,214	Pacific	714/657
ZIP Code 92844	General	Garden Grove	24,307	Pacific	714/657
ZIP Code 92845	General	Garden Grove	16,333	Pacific	657/714
ZIP Code 92846	P.O. Box	Garden Grove	0	Pacific	714/657
ZIP Code 92850	Unique	Anaheim	0	Pacific	714/562/949/626/909
ZIP Code 92856	P.O. Box	Orange	0	Pacific	714/657
ZIP Code 92857	P.O. Box	Orange	0	Pacific	714/657
ZIP Code 92859	P.O. Box	Orange	0	Pacific	714/657
ZIP Code 92861	General	Villa Park	5,781	Pacific	714
ZIP Code 92862	General	Orange	0	Pacific	714
ZIP Code 92863	P.O. Box	Orange	0	Pacific	714/657
ZIP Code 92864	P.O. Box	Orange	0	Pacific	714/657
ZIP Code 92865	General	Orange	19,704	Pacific	714
ZIP Code 92866	General	Orange	14,885	Pacific	714/657
ZIP Code 92867	General	Orange	44,515	Pacific	657/714
ZIP Code 92868	General	Orange	25,404	Pacific	714/657/949
ZIP Code 92869	General	Orange	37,184	Pacific	714
ZIP Code 92870	General	Placentia	52,033	Pacific	714/657
ZIP Code 92871	P.O. Box	Placentia	0	Pacific	714/657
ZIP Code 92885	P.O. Box	Yorba Linda	0	Pacific	714/657
ZIP Code 92886	General	Yorba Linda	46,564	Pacific	714/657
ZIP Code 92887	General	Yorba Linda	20,006	Pacific	714/657
ZIP Code 92899	General	Anaheim	0	Pacific	714/562/949/626/909"""
    )