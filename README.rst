mris
==========================

Python wrapper for `mris`_. Requires Python 3.6+.

Install
-------

::

    pip3 install --upgrade git+https://github.com/AlJohri/mris.git


CLI
---

::

    $ mris search
    {"url": "http://www.mrishomes.com/homes-for-sale/x-157544018", "ListingID": 157544018, "ListingNumber": "MC8737879", "PostalCode": "20850", "ListPriceLow": 999999999, "NumberBedrooms": "1", "NumberBaths": "1", "MLSShortName": "MDMRIS"}
    {"url": "http://www.mrishomes.com/homes-for-sale/x-157537449", "ListingID": 157537449, "ListingNumber": "MC9009366", "PostalCode": "20850", "ListPriceLow": 999999999, "NumberBedrooms": "1", "NumberBaths": "1", "MLSShortName": "MDMRIS"}
    {"url": "http://www.mrishomes.com/homes-for-sale/x-206530264", "ListingID": 206530264, "ListingNumber": "FX9978626", "PostalCode": "22101", "ListPriceLow": 29900000, "NumberBedrooms": "12", "NumberBaths": "21", "MLSShortName": "MDMRIS"}
    ...

Development
-----------

Setup
~~~~~

::

    mkvirtualenv mris -p python3.6
    make install

Test
~~~~

::

    workon mris
    make test

.. _mris: http://www.mrishomes.com/
