from bs4 import BeautifulSoup
import requests
import time

urls = ['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,300,30)]

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(5)
    #print(wb_data)
    Soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = Soup.select('div.property_title > a[target="_blank"]')
    images = Soup.select('img[width="160"]')
    #cates = Soup.select('div.p13n_reasoning_v2')
    if data == None:
        for title, image in zip(titles, images):
            data = {
                'title' : title.get_text(),
                'image' : image.get('src'),
                #'cate'  : cate.get_text()
            }
            print(data)

for single_url in urls:
    get_attractions(single_url)

'''
headers ={
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Cookie' : 'TAUnique=%1%enc%3AE9tEvZC3lWs4bVUX6Sk345EDWocUgHxHVJ5HZiWr%2BWzEdwUztdq5rA%3D%3D; TACds=C.2.14348.2.2016-10-18; ServerPool=C; TASSK=enc%3AAE4jiDoTSgq1Stg8QfK8p9zO1ZxcbwZcI2AZBUvUzOw19Sfq%2BVLaiWO050OHb8iMYHevv46NsU0ewLbmw6VeYgan9T1gsD4BS3NGYGbHD8%2BAaZulkjQymF0LncCW%2FtcapA%3D%3D; TART=%1%enc%3AOG1VF%2BkpN%2BO0uuKa7u6AYCAyBl06XEfyqQvnVa%2B170cWiKhgj14VpwzatuslqTxnlM5jTnIK0sY%3D; PAC=ABkKsrV6Y0Wi3uxL3wfBjVxWICJGTCN_kRPNlFwQ64rjthZGV8YWYiHned4qYZrfzJBIAl-VAWRGakDO520d1K2rBTacRaR5A7MhVrXmYrli; __gads=ID=db97948212ebb9f1:T=1478660882:S=ALNI_MZTUMp_-gLmCWHovOEX4dWoedBM7g; BEPIN=%1%158470ebe16%3Bhac01a%3A10023%3B; CommercePopunder=SuppressAll*1478664538518; TATravelInfo=V2*AC.LAX*A.2*MG.-1*HP.2*FL.3*RVL.60763_313l105125_313l136072_313l105127_314*RS.1; fbm_162729813767876=base_domain=.tripadvisor.com; SecureLogin2=3.4%3AAOq9KIb6CBqA9GvlNj4IMrzdfihD7M5BnWdBkfP%2FrtPvvOkDpsv4wz9m8N2KKN%2B0b7COJWZEtaVgnZRFumHRE%2B%2FnWStDhreSmrkil6HvNDvxXf76TCdaz5DJMGCcBaQyOzsiR1jZynHDSk7PNFXwA4ptSg%2Bk3LjFJmeC31URO0A186KXGIhzPUcA4oX2EAVw30Y%2BUb6HDXHEK1%2F6imVHIi4%3D; TAAuth3=3%3A2dc1fd4b9158c27004e69fb3773f55d7%3AAHXQAaS%2FoubH0UMUWIjtiTXdZpxg8YdcCU5U8bKg6wEeBQxn8R4iBgYGM1IGOuMTOocVTNOgRdvg2b6BZhZcWcsd8DM8l89iInTYZJnQyj7%2F0DAmS4wCZXqt%2FcO64nL37w3Zdv8sGHCBvnD3wPLOe%2FMvch0xGp1YuxMyhGJnjp47PdIaxtRyRPl7vZEX7OwMdj6CQA%2BsOxJ%2Fyiy6FCZxZiM%3D; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C1%2C-1%7Cpv%2C12%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C4%2C-1%7CPremiumSURPers%2C%2C-1%7CAWPUPers%2C%2C-1%7CPCBSess%2C-1%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C8%2C-1%7Cbrandsess%2C1%2C-1%7Csesscoestorem%2C%2C-1%7CCpmPopunder_1%2C1%2C1478750363%7CCCSess%2C2%2C-1%7CCpmPopunder_2%2C1%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C2%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7Chac_ua_rd%2C%2C-1%7CSaveFtrPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1479265681%7CPCBPers%2C1%2C1481255904%7CLaFourchette+MC+Banners%2C%2C-1%7CAWPUSess%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2CRuleBasedPopup%2C1478750304%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTakeOver%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html; roybatty=TNI1625!ANANRHkmAnX6yZFnDVhUSh%2BZZeqv19d5Jm6fHrt1fatB4324W%2BOKEyNzNyEnpsnDMDPIUhpgB8M1Nj9l6iUuPUPKRVrk84n6A%2FltY1sNUhXeEn8b8aMCVwYJGrIwpZslEXuMfL4p%2BmXPC0LvphrRN%2Bg8eCugxFhV1hFeGu0gte84%2C1; fbsr_162729813767876=Mh42OjaoeaA2MneooqgdQy3Yq2DRY7518q9LXtGG4nY.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUFTM1BGNml1Q3NxX3lRZ1dvOHVoQ1ZTTmYtVVZNQjNaM09wamVad1BqcERzazVsS3FWRkhmbGhaTmN0R1lELWhuWDlscVMtU0xMdVhRaEM4SXlZTkxOQ1c1Z0RZRllCbDl4N2dydy00U0lWdlBjSHpiZzBScldaVVBtWmpOVnNRT1pzR1Z3OWh3TVRRbFItQ2dOMWU1Yi1SUUNBdmRtdXZidGNWbUpFdFd3MXcyTWwyb0YyalNRZmJ4WVYxcVpLTXNBdE9aa2xFQzdxZVZDWlBFM3AwVEoxZTlPN0FhWm1PbEZySFgybWpyV3Y5akNTSWJhSk1NTUNua2xfLWJtRUdtbG52Yk9oVEZ6VzE3aWRQMDdLcmZNSTZXc2c2d1BSOVFhNGZSYzIwczY4RGZuVGZXQzUtRURXcVdVZXAxalktdnAwbzNteWlSN0tEb3J3dWRVWkZNSCIsImlzc3VlZF9hdCI6MTQ3ODY3MTI1OSwidXNlcl9pZCI6IjE3OTYyOTM5NzM5NjE3NTEifQ; NPID=; TASession=%1%V2ID.C43CE9EDEE93D125894CE19EA9AFED91*SQ.104*MC.26961*LR.https%3A%2F%2Fwww%5C.google%5C.com%2F*LP.%2F-a_supli%5C.-a_supti%5C.kwd__2D__119671122-a_supdv%5C.c-m26961-a_supsc%5C.s-a_supap%5C.1t1-a_suplp%5C.9030933-a_supbk%5C.1-a_supai%5C.69761355735-a_supci%5C.1071146368-a_supnt%5C.g*LS.MetaPlacementAjax*GR.11*TCPAR.86*TBR.79*EXEX.93*ABTR.9*PPRP.41*PHTB.0*FS.15*CPU.3*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.0A6D2712D8082344878BC85304B0755E*LF.zhCN*FA.1*DF.0*FBH.2*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105127*BG.60763*BT.hmh7o1*FBC.1; TAUD=LA-1478660876176-1*LG-10386227-2.1.F.*LD-10386228-.....'
}

url_saves = 'https://cn.tripadvisor.com/Saves#56346156'
wb_data = requests.get(url_saves, headers = headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
print(soup)
titles = soup.select('div.title')
for title in zip(titles):
    data = {
        'title': title.get_text()
    }
    print(data)
'''

'''
#taplc_attraction_coverpage_0 > div:nth-child(1) > div > div > div.shelf_item_container > div:nth-child(1) > div > div > div.item.name > a
#taplc_attraction_coverpage_0 > div:nth-child(1) > div > div > div.shelf_item_container > div:nth-child(2) > div > div > div.item.name
#taplc_attraction_coverpage_0 > div:nth-child(1) > div > div > div.shelf_item_container > div:nth-child(2) > div > a > div > div > div > img
#taplc_attraction_coverpage_0 > div:nth-child(1) > div > div > div.shelf_item_container > div:nth-child(1) > div > div > div:nth-child(3)
#taplc_attraction_coverpage_0 > div:nth-child(1) > div > div > div.shelf_item_container > div:nth-child(1) > div > div > div:nth-child(3)
#taplc_attraction_coverpage_0 > div:nth-child(2) > div > div > div.shelf_item_container > div:nth-child(3) > div > div > div:nth-child(2)
#BODYCON > div.modules-saves-single-trip-view > div > div.trip_content > div.items > div > div.info > div.location_summary > div.title
#BODYCON > div.modules-saves-single-trip-view > div > div.trip_content > div.items > div > div.info > div.location_summary > div.poi_type_tags > a > span.tags
'''