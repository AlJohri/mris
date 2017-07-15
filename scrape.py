#!/usr/bin/env python3

import json
import logging
import argparse
import requests
import itertools

# http://www.mrishomes.com/include/ajax/api.aspx?op=GetDmpApiKey
# http://m.mrishomes.com/mobile/listing/listingsearch.aspx
# http://m.mrishomes.com/include/ajax/api.aspx?op=GetListingPriceHistory&listingNumber=MC9833887&orgId=MDMRIS

sort_options = {
    "low_to_high": 29
}

# search for inidividual listing:
# Criteria/LocationJson:[[{"name":"Fx9921147 (MLS #)","type":"MLS #","value":"Fx9921147","isOr":true}]]
# Criteria/LocationBox:FX9921147
# Criteria/LocationBox:FX9921147

def search(per_page=10, sort="low_to_high"):

    sort_id = sort_options[sort]

    response = requests.get("http://www.mrishomes.com/Listing/ListingSearch.aspx")
    searchoverride = response.cookies['rBW-ListingSearch']
    payload = {
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
        "IgnoreMap": "false", # true ?
        "ListingSortID": sort_id,
        "view": "map",
        "first": "0",
        "Criteria/SearchType": "map",
        "SearchTab": "mapsearch-criteria-basicsearch",
        "CLSID": "-1",
        "ResultsPerPage": per_page,
    }

    response = requests.post(f"http://www.mrishomes.com/Include/AJAX/MapSearch/GetListingPins.aspx?searchoverride={searchoverride}&", data=payload)
    data = response.json()
    count = data['count']
    logging.debug(f"count: {count}")
    assert per_page == data['pageCount']
    yield from data['ListingResultSet']['Items'] # [0,per_page-1] of length per_page

    for offset in range(per_page, count+per_page, per_page):
        logging.debug(f"offset: {offset}")
        payload = {
            "view": "map",
            "first": offset,
            "count": per_page,
            "clsid": -1,
            "ListingSortID": sort_id,
            "priorSale": False
        }
        response = requests.post(f"http://www.mrishomes.com/Include/AJAX/MapSearch/GetListings.aspx?searchoverride={searchoverride}", data=payload)
        data = response.json()
        page = data['page']
        logging.debug(f"page: {page}")
        assert data['resultsPerPage'] == per_page
        yield from data['ListingResultSet']['Items'] # [offset, offset+per_page-1] of length per_page

if __name__ == '__main__':
    limit = 500
    for listing in itertools.islice(search(), limit):
        print(json.dumps(listing))
