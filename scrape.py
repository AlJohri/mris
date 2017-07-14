#!/usr/bin/env python3

import json
import requests

# http://www.mrishomes.com/include/ajax/api.aspx?op=GetDmpApiKey
# http://m.mrishomes.com/mobile/listing/listingsearch.aspx
# http://m.mrishomes.com/include/ajax/api.aspx?op=GetListingPriceHistory&listingNumber=MC9833887&orgId=MDMRIS

response = requests.get("http://www.mrishomes.com/Listing/ListingSearch.aspx")
searchoverride = response.cookies['rBW-ListingSearch']
print(searchoverride)

print("page 1")

data = {
    "Criteria/FilterByAddress": "1",
    "Criteria/ListingTypeID": "1",
    "Criteria/Status": "1,0",
    "grp_rangetype": "A",
    "inrixDuration": "15",
    "inrixTod:8": "00",
    "Groups/Group_OwnershipType": "1",
    "HardCodedCriterion": "1899",
    "Groups/Group_AirCon": "1",
    "Groups/Group_Pool": "1",
    "Groups/Group_Style": "1",
    "Groups/Group_Level": "1",
    "Groups/Group_Room": "1",
    "Criteria/LocationJson": "[]",
    "Criteria/SearchMapNELat": "40.64740307947117",
    "Criteria/SearchMapNELong": "-75.46794128417963",
    "Criteria/SearchMapSWLat": "37.20418602461762",
    "Criteria/SearchMapSWLong": "-79.06596374511713",
    "Criteria/Zoom": "8",
    "Criteria/SearchMapStyle": "r",
    "IgnoreMap": "false",
    "ListingSortID": "29",
    "view": "map",
    "first": "0",
    "Criteria/SearchType": "map",
    "SearchTab": "mapsearch-criteria-basicsearch",
    "CLSID": "-1",
    "ResultsPerPage": "10",
}

response = requests.post(f"http://www.mrishomes.com/Include/AJAX/MapSearch/GetListingPins.aspx?searchoverride={searchoverride}&ts=1500001975909&", data=data)
page1 = response.json()
print(page1)

with open('page1.json', 'w') as f:
    json.dump(page1, f)

print("page 2")
data = {
    "view": "map",
    "first": 12,
    "count": 10,
    "clsid": -1,
    "ListingSortID": 29, # price low to high
    "priorSale": False
}
response = requests.post(f"http://www.mrishomes.com/Include/AJAX/MapSearch/GetListings.aspx?searchoverride={searchoverride}", data=data)
page2 = response.json()
print(page2)

with open('page2.json', 'w') as f:
    json.dump(page2, f)


print("page last?")
data = {
    "view": "map",
    "first": 190,
    "count": 10,
    "clsid": -1,
    "ListingSortID": 29, # price low to high
    "priorSale": False
}
response = requests.post(f"http://www.mrishomes.com/Include/AJAX/MapSearch/GetListings.aspx?searchoverride={searchoverride}", data=data)
pagelast = response.json()
print(pagelast)

with open('pagelast.json', 'w') as f:
    json.dump(pagelast, f)
