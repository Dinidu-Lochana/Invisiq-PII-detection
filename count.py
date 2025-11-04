def count_closing_braces(text):
    return text.count('}')

# Example usage:
sample_text = """
{
      "type": "date",
      "text": "Nov 2024",
      "start": 6460,
      "end": 6468,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Aug 2024",
      "start": 6596,
      "end": 6604,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Mar 2024",
      "start": 6767,
      "end": 6775,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Jan 2024",
      "start": 6938,
      "end": 6946,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Dec 2024",
      "start": 9937,
      "end": 9945,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Nov 2024",
      "start": 10068,
      "end": 10076,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Jan 2025",
      "start": 10186,
      "end": 10194,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Dec 2024",
      "start": 10304,
      "end": 10312,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Oct 2024",
      "start": 10422,
      "end": 10430,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "January 2025",
      "start": 14487,
      "end": 14499,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Nov 2024",
      "start": 22018,
      "end": 22026,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Oct 2021",
      "start": 33044,
      "end": 33052,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Mar 2022",
      "start": 33153,
      "end": 33161,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Sep 2023",
      "start": 33262,
      "end": 33270,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Feb 2024",
      "start": 33371,
      "end": 33379,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Jan 2025",
      "start": 36276,
      "end": 36284,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Jan 2025",
      "start": 49405,
      "end": 49413,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Nov 2024",
      "start": 63573,
      "end": 63581,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Aug 2024",
      "start": 63717,
      "end": 63725,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Mar 2024",
      "start": 63861,
      "end": 63869,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Jan 2024",
      "start": 64005,
      "end": 64013,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Oct 2023",
      "start": 64149,
      "end": 64157,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Jan 2025",
      "start": 65179,
      "end": 65187,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "April 2025",
      "start": 66836,
      "end": 66846,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Dec 2024",
      "start": 68641,
      "end": 68649,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Jan 2025",
      "start": 68652,
      "end": 68660,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Nov 2024",
      "start": 68994,
      "end": 69002,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Dec 2024",
      "start": 69516,
      "end": 69524,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Jan 2025",
      "start": 69649,
      "end": 69657,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "29 January 2025",
      "start": 72450,
      "end": 72465,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "29 April 2025",
      "start": 72680,
      "end": 72693,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "29 January 2025",
      "start": 72824,
      "end": 72839,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Oct 2023",
      "start": 72885,
      "end": 72893,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Nov 2024",
      "start": 72896,
      "end": 72904,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Nov 2024",
      "start": 72940,
      "end": 72948,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "Jan 2025",
      "start": 72951,
      "end": 72959,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "November 2024",
      "start": 73036,
      "end": 73049,
      "score": null,
      "source": "regex"
    },
    {
      "type": "date",
      "text": "29 January 2025",
      "start": 73742,
      "end": 73757,
      "score": null,
      "source": "regex"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 19,
      "end": 31,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 33,
      "end": 42,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 44,
      "end": 51,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 106,
      "end": 118,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 120,
      "end": 129,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 131,
      "end": 138,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "|\\n| B+                  ",
      "start": 1493,
      "end": 1518,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 1711,
      "end": 1720,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 1722,
      "end": 1731,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Castle",
      "start": 1761,
      "end": 1777,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 1938,
      "end": 1950,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 1982,
      "end": 1989,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "West Berkshire",
      "start": 2155,
      "end": 2169,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "North Hampshire",
      "start": 2174,
      "end": 2189,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 2315,
      "end": 2324,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 2677,
      "end": 2684,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 2686,
      "end": 2697,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 3286,
      "end": 3298,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 3300,
      "end": 3309,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "|\\n| Year Built",
      "start": 3928,
      "end": 3943,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "|\\n| Garden",
      "start": 4094,
      "end": 4105,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 4499,
      "end": 4511,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 4623,
      "end": 4632,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 4668,
      "end": 4677,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Castle",
      "start": 4725,
      "end": 4741,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Downton Abbey",
      "start": 4759,
      "end": 4772,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 4926,
      "end": 4933,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 4945,
      "end": 4956,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "North Hampshire",
      "start": 5907,
      "end": 5922,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2023-2024",
      "start": 5940,
      "end": 5949,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Sqft",
      "start": 6181,
      "end": 6185,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere       ",
      "start": 6442,
      "end": 6458,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Aug 2024                         ",
      "start": 6596,
      "end": 6629,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Mar 2024                         ",
      "start": 6767,
      "end": 6800,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 6906,
      "end": 6918,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 6920,
      "end": 6929,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Beacon Hill Road",
      "start": 7109,
      "end": 7125,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Burghclere",
      "start": 7127,
      "end": 7137,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 7566,
      "end": 7575,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Hollington Lane",
      "start": 7577,
      "end": 7592,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Burghclere",
      "start": 7779,
      "end": 7789,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "West Berkshire",
      "start": 8121,
      "end": 8135,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "North Hampshire",
      "start": 8136,
      "end": 8151,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "annual",
      "start": 8179,
      "end": 8185,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 8288,
      "end": 8297,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "-->\\n\\n| Rental Metric                         ",
      "start": 8782,
      "end": 8829,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Monthly",
      "start": 8831,
      "end": 8838,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "|\\n| Gross -                               ",
      "start": 9070,
      "end": 9113,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 9259,
      "end": 9266,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 9365,
      "end": 9371,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 9950,
      "end": 9959,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Ecchinswell",
      "start": 10091,
      "end": 10102,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "|\\n| Newbury",
      "start": 10204,
      "end": 10216,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Whitway",
      "start": 10327,
      "end": 10334,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Annual",
      "start": 10455,
      "end": 10461,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Annual",
      "start": 10553,
      "end": 10559,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 11282,
      "end": 11291,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "St. Michael's",
      "start": 11605,
      "end": 11618,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury Station",
      "start": 11723,
      "end": 11738,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "15 mins",
      "start": 11739,
      "end": 11746,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "M4",
      "start": 11748,
      "end": 11750,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Aldermaston",
      "start": 11821,
      "end": 11832,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 11972,
      "end": 11979,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Area",
      "start": 12114,
      "end": 12128,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "West Berkshire",
      "start": 12133,
      "end": 12147,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 12152,
      "end": 12161,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "UK",
      "start": 12176,
      "end": 12178,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "1-Year Change",
      "start": 12344,
      "end": 12357,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "3-Year Change",
      "start": 12433,
      "end": 12446,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-Year Change   |\\n\\nSources",
      "start": 12522,
      "end": 12550,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 12615,
      "end": 12624,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2023-2024",
      "start": 12691,
      "end": 12700,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "West Berkshire",
      "start": 12705,
      "end": 12719,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "North Hampshire",
      "start": 12772,
      "end": 12787,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2022",
      "start": 12949,
      "end": 12953,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Q4 2024 - Q1",
      "start": 13091,
      "end": 13103,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Area",
      "start": 13173,
      "end": 13187,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "68 days",
      "start": 13308,
      "end": 13315,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "82 days",
      "start": 13329,
      "end": 13336,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "12 months",
      "start": 13602,
      "end": 13611,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 13749,
      "end": 13758,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "annually",
      "start": 13829,
      "end": 13837,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 13924,
      "end": 13930,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "post-2020",
      "start": 13946,
      "end": 13955,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 13986,
      "end": 13993,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Abbey",
      "start": 14073,
      "end": 14078,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Aldermaston",
      "start": 14167,
      "end": 14178,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "3-6 month",
      "start": 14321,
      "end": 14330,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "6-12 month",
      "start": 14374,
      "end": 14384,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "January 2025):\\n\\n|",
      "start": 14487,
      "end": 14506,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "25yr",
      "start": 14571,
      "end": 14575,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2-Year",
      "start": 14692,
      "end": 14698,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-Year",
      "start": 14769,
      "end": 14775,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 15193,
      "end": 15202,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2021",
      "start": 15382,
      "end": 15386,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Monthly",
      "start": 15398,
      "end": 15405,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "/month",
      "start": 15438,
      "end": 15444,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 15655,
      "end": 15661,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "South East",
      "start": 15662,
      "end": 15672,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 16022,
      "end": 16031,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 16033,
      "end": 16044,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Deane district",
      "start": 16049,
      "end": 16063,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "West Berkshire",
      "start": 16094,
      "end": 16108,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Castle",
      "start": 16156,
      "end": 16172,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 16402,
      "end": 16411,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Berkshire",
      "start": 16426,
      "end": 16435,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "1974",
      "start": 16442,
      "end": 16446,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 16459,
      "end": 16470,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Burghclere",
      "start": 16561,
      "end": 16571,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "-->\\n\\n| Demographic Metric",
      "start": 16683,
      "end": 16710,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 16736,
      "end": 16745,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "England",
      "start": 16750,
      "end": 16757,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "47 years",
      "start": 17117,
      "end": 17125,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "42 years           |",
      "start": 17140,
      "end": 17160,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 17646,
      "end": 17655,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Area (est",
      "start": 18462,
      "end": 18481,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 18488,
      "end": 18497,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "UK",
      "start": 18502,
      "end": 18504,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Aldermaston",
      "start": 18933,
      "end": 18944,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 19118,
      "end": 19129,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 19257,
      "end": 19263,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 19299,
      "end": 19306,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Birmingham",
      "start": 19495,
      "end": 19505,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 19690,
      "end": 19696,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "55-65 mins",
      "start": 19834,
      "end": 19844,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Kingsclere -         ",
      "start": 19941,
      "end": 19962,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "45-50 mins",
      "start": 19979,
      "end": 19989,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Waterloo",
      "start": 19995,
      "end": 20003,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 20021,
      "end": 20032,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Newbury",
      "start": 20071,
      "end": 20078,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "15 minutes",
      "start": 20081,
      "end": 20091,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 20102,
      "end": 20113,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "20 minutes",
      "start": 20116,
      "end": 20126,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "35 minutes",
      "start": 20140,
      "end": 20150,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 20154,
      "end": 20160,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Paddington",
      "start": 20162,
      "end": 20172,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "90 minutes",
      "start": 20176,
      "end": 20186,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Southampton Airport",
      "start": 20304,
      "end": 20323,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Michael",
      "start": 20419,
      "end": 20426,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "seasonally",
      "start": 20502,
      "end": 20512,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Burghclere",
      "start": 20613,
      "end": 20623,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 20839,
      "end": 20846,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Kingsclere",
      "start": 21068,
      "end": 21078,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury Racecourse",
      "start": 21194,
      "end": 21212,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Castle",
      "start": 21431,
      "end": 21447,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Sandham Memorial",
      "start": 21449,
      "end": 21465,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 21558,
      "end": 21567,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "estimated):\\n\\n<!--",
      "start": 21579,
      "end": 21598,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "12 months to Nov 2024):\\n\\n|",
      "start": 22005,
      "end": 22033,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "NRP",
      "text": "Hampshire Avg",
      "start": 22091,
      "end": 22104,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "4            ",
      "start": 22594,
      "end": 22607,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Vehicle Crime",
      "start": 22669,
      "end": 22682,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "|\\n| 5",
      "start": 22925,
      "end": 22931,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 23228,
      "end": 23237,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 23431,
      "end": 23440,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 23514,
      "end": 23523,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Wales",
      "start": 23571,
      "end": 23576,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 23929,
      "end": 23936,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "St. Michael's",
      "start": 24337,
      "end": 24350,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 24363,
      "end": 24372,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2019",
      "start": 24768,
      "end": 24772,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 24969,
      "end": 24978,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Pupil Nos",
      "start": 25233,
      "end": 25242,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 25473,
      "end": 25480,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2024",
      "start": 25750,
      "end": 25754,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "English &",
      "start": 25783,
      "end": 25792,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 25979,
      "end": 25988,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Burghclere",
      "start": 25990,
      "end": 26000,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Bartholomew",
      "start": 26082,
      "end": 26093,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2018",
      "start": 26165,
      "end": 26169,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2023",
      "start": 26171,
      "end": 26175,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Berkshire",
      "start": 26200,
      "end": 26209,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "English &",
      "start": 26267,
      "end": 26276,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Headley",
      "start": 26530,
      "end": 26537,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Cold Ash",
      "start": 26664,
      "end": 26672,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "St. Gabriel's",
      "start": 26716,
      "end": 26729,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 26740,
      "end": 26747,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "St. Michael's",
      "start": 26880,
      "end": 26893,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "NRP",
      "text": "Victorian",
      "start": 27361,
      "end": 27370,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "NRP",
      "text": "Edwardian",
      "start": 27372,
      "end": 27381,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Downton Abbey",
      "start": 27672,
      "end": 27685,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Stanley Spencer",
      "start": 27753,
      "end": 27768,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Stud",
      "start": 28093,
      "end": 28107,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Sandford Springs",
      "start": 28123,
      "end": 28139,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 28290,
      "end": 28297,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Kingsclere",
      "start": 28371,
      "end": 28381,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 28539,
      "end": 28546,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "weekly",
      "start": 28548,
      "end": 28554,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Village Hall",
      "start": 28586,
      "end": 28608,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "annual",
      "start": 29385,
      "end": 29391,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Flood Zone 1",
      "start": 29766,
      "end": 29778,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "&lt;0.1%",
      "start": 29808,
      "end": 29816,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "annual",
      "start": 29817,
      "end": 29823,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 29885,
      "end": 29897,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 31001,
      "end": 31013,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "England",
      "start": 31268,
      "end": 31275,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "fort",
      "start": 31668,
      "end": 31672,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere Castle",
      "start": 31759,
      "end": 31775,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "arboretum Ancient",
      "start": 31811,
      "end": 31828,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2016",
      "start": 32154,
      "end": 32158,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 32253,
      "end": 32262,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Limit",
      "start": 32461,
      "end": 32466,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 32549,
      "end": 32558,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2016-2029",
      "start": 32579,
      "end": 32588,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 32615,
      "end": 32626,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "21/03247/HSE      ",
      "start": 32949,
      "end": 32967,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road Single-storey",
      "start": 32969,
      "end": 32995,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hollington Lane            ",
      "start": 33187,
      "end": 33214,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Conservation",
      "start": 33585,
      "end": 33597,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2025-2029)\\n- Impact: Neutral",
      "start": 34349,
      "end": 34378,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "-->\\n\\n| Input Parameter",
      "start": 35783,
      "end": 35807,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2-year",
      "start": 36257,
      "end": 36263,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "25 years",
      "start": 36326,
      "end": 36334,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Annual",
      "start": 36470,
      "end": 36476,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "0.6 months",
      "start": 36804,
      "end": 36814,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "25 years\\n\\n(300 months",
      "start": 37137,
      "end": 37160,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Annual",
      "start": 37297,
      "end": 37303,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Year 1",
      "start": 37791,
      "end": 37797,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Annual",
      "start": 37826,
      "end": 37832,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Year 1",
      "start": 38034,
      "end": 38040,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Year 1",
      "start": 38346,
      "end": 38352,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Year 1)\\n\\nTotal Return",
      "start": 38425,
      "end": 38448,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-year",
      "start": 38464,
      "end": 38470,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "p.a.",
      "start": 38510,
      "end": 38514,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "(5 years",
      "start": 38571,
      "end": 38579,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "-5-Year",
      "start": 38678,
      "end": 38685,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 39381,
      "end": 39390,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "1,236/month",
      "start": 40020,
      "end": 40031,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Annual",
      "start": 40220,
      "end": 40226,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "7-8 years",
      "start": 40336,
      "end": 40345,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-Yr",
      "start": 40554,
      "end": 40558,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-Yr",
      "start": 40818,
      "end": 40822,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "UK",
      "start": 41769,
      "end": 41771,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Monthly",
      "start": 42092,
      "end": 42099,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-Year",
      "start": 42776,
      "end": 42782,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-Yr Total",
      "start": 43173,
      "end": 43183,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "early years",
      "start": 43651,
      "end": 43662,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "3-6 month",
      "start": 43784,
      "end": 43793,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Grade",
      "start": 43869,
      "end": 43874,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Flood Zone 1",
      "start": 45305,
      "end": 45317,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "next 2-3",
      "start": 45976,
      "end": 45984,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "6-9 months",
      "start": 46086,
      "end": 46096,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "3-4 months",
      "start": 46100,
      "end": 46110,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "years",
      "start": 46229,
      "end": 46234,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "West Berkshire",
      "start": 46514,
      "end": 46528,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 46529,
      "end": 46538,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "3-6 months",
      "start": 47011,
      "end": 47021,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "82 days",
      "start": 47443,
      "end": 47450,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "62 days",
      "start": 47455,
      "end": 47462,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Knight Frank",
      "start": 47679,
      "end": 47691,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "6-12 months",
      "start": 47795,
      "end": 47806,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 47849,
      "end": 47855,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 47868,
      "end": 47875,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "BoE",
      "start": 48243,
      "end": 48246,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2025-2026)\\n\\n",
      "start": 48285,
      "end": 48299,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "month",
      "start": 48802,
      "end": 48807,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-year",
      "start": 49145,
      "end": 49151,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "BoE",
      "start": 49377,
      "end": 49380,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "next 2 years",
      "start": 49523,
      "end": 49535,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "1-2 months",
      "start": 49880,
      "end": 49890,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "quarterly",
      "start": 50368,
      "end": 50377,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2-3 year",
      "start": 50683,
      "end": 50691,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2025",
      "start": 53031,
      "end": 53035,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "UK",
      "start": 53040,
      "end": 53042,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Aldermaston",
      "start": 53278,
      "end": 53289,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 53291,
      "end": 53298,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 53470,
      "end": 53476,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 53514,
      "end": 53520,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2008-2009",
      "start": 54035,
      "end": 54044,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "West Berkshire",
      "start": 54056,
      "end": 54070,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "18 months",
      "start": 54117,
      "end": 54126,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "24 months",
      "start": 54155,
      "end": 54164,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2020",
      "start": 54187,
      "end": 54191,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "10+ years",
      "start": 54300,
      "end": 54309,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 55165,
      "end": 55174,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "6-12 months",
      "start": 55340,
      "end": 55351,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Rationale\\n\\nBlackford Cottage",
      "start": 55625,
      "end": 55655,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 55720,
      "end": 55729,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "annually",
      "start": 56478,
      "end": 56486,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 56508,
      "end": 56514,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 56527,
      "end": 56534,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-year",
      "start": 56601,
      "end": 56607,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Year 1-3",
      "start": 57096,
      "end": 57104,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "10-Year Projection",
      "start": 57651,
      "end": 57669,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Annual",
      "start": 57846,
      "end": 57852,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-Year",
      "start": 58109,
      "end": 58115,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "10-Year",
      "start": 58148,
      "end": 58155,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2025 - Q4 2026):\\n\\n<!--",
      "start": 58266,
      "end": 58290,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2024",
      "start": 58461,
      "end": 58465,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "London",
      "start": 58543,
      "end": 58549,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "BoE",
      "start": 58782,
      "end": 58785,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Typical Comparables   |\\n|-------------------------------------|----------------------------|-----------------------|\\n|",
      "start": 59262,
      "end": 59382,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 59390,
      "end": 59399,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "sqft",
      "start": 59483,
      "end": 59487,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5-year",
      "start": 60937,
      "end": 60943,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 61213,
      "end": 61222,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "weekday/weekend",
      "start": 61247,
      "end": 61262,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "St. Michael's",
      "start": 61324,
      "end": 61337,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Hurst",
      "start": 61343,
      "end": 61348,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 61390,
      "end": 61397,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 61399,
      "end": 61410,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "8-12 weeks",
      "start": 61797,
      "end": 61807,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "10+ year",
      "start": 62147,
      "end": 62155,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Year 1 - You",
      "start": 62321,
      "end": 62333,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "3 years",
      "start": 62463,
      "end": 62470,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Savills Newbury",
      "start": 62874,
      "end": 62889,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Knight Frank",
      "start": 62891,
      "end": 62903,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Address                      | Sale Date",
      "start": 63254,
      "end": 63294,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hollington Lane",
      "start": 63542,
      "end": 63557,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 63559,
      "end": 63568,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Burghclere",
      "start": 63702,
      "end": 63712,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 63830,
      "end": 63842,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Highclere      ",
      "start": 63844,
      "end": 63859,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Beacon Hill Road",
      "start": 64118,
      "end": 64134,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Burghclere",
      "start": 64136,
      "end": 64146,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2-year",
      "start": 65160,
      "end": 65166,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "25 years",
      "start": 65226,
      "end": 65234,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "UK",
      "start": 65261,
      "end": 65263,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Annual",
      "start": 65435,
      "end": 65441,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "p.a",
      "start": 65519,
      "end": 65522,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 66034,
      "end": 66043,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "25 years",
      "start": 67430,
      "end": 67438,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "300 months",
      "start": 67440,
      "end": 67450,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Year 1",
      "start": 67536,
      "end": 67542,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Monthly",
      "start": 67574,
      "end": 67581,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Annual",
      "start": 67586,
      "end": 67592,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Year",
      "start": 67800,
      "end": 67804,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2023-2024",
      "start": 68424,
      "end": 68433,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 68467,
      "end": 68476,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Dec 2024 - Jan 2025",
      "start": 68641,
      "end": 68660,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "West Berkshire/Hampshire",
      "start": 68686,
      "end": 68710,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2021",
      "start": 68781,
      "end": 68785,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Deane MSOA",
      "start": 68823,
      "end": 68833,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "12 months to Nov 2024",
      "start": 68981,
      "end": 69002,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2022-2024",
      "start": 69128,
      "end": 69137,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2024",
      "start": 69200,
      "end": 69204,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "UK",
      "start": 69471,
      "end": 69473,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Moneyfacts",
      "start": 69637,
      "end": 69647,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 71406,
      "end": 71415,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 71416,
      "end": 71423,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "01635 555444",
      "start": 71459,
      "end": 71471,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Knight Frank",
      "start": 71472,
      "end": 71484,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Parker Newbury",
      "start": 71520,
      "end": 71534,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "0800 373300",
      "start": 71663,
      "end": 71674,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 71730,
      "end": 71737,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Thackray Williams",
      "start": 71858,
      "end": 71875,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Newbury",
      "start": 71928,
      "end": 71935,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "01635",
      "start": 71938,
      "end": 71943,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 72011,
      "end": 72020,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Homewise Surveying",
      "start": 72037,
      "end": 72055,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Basingstoke",
      "start": 72104,
      "end": 72115,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "January 2025                          | Valuation Date      ",
      "start": 72453,
      "end": 72513,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "Version      ",
      "start": 72568,
      "end": 72581,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "3 months",
      "start": 72664,
      "end": 72672,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "PERSON",
      "text": "|\\n\\nAudit Trail",
      "start": 72785,
      "end": 72801,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Oct 2023 - Nov 2024",
      "start": 72885,
      "end": 72904,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "Nov 2024 - Jan 2025",
      "start": 72940,
      "end": 72959,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "12 months to November 2024",
      "start": 73023,
      "end": 73049,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Andover Road",
      "start": 73169,
      "end": 73181,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Highclere",
      "start": 73183,
      "end": 73192,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "LOCATION",
      "text": "Hampshire",
      "start": 73468,
      "end": 73477,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2025",
      "start": 73872,
      "end": 73876,
      "score": 0.85,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "4.04.25",
      "start": 49458,
      "end": 49465,
      "score": 0.6,
      "source": "presidio"
    },
    {
      "type": "URL",
      "text": "Police.uk",
      "start": 23198,
      "end": 23207,
      "score": 0.5,
      "source": "presidio"
    },
    {
      "type": "URL",
      "text": "www.gov.uk/land-registry",
      "start": 62653,
      "end": 62677,
      "score": 0.5,
      "source": "presidio"
    },
    {
      "type": "URL",
      "text": "www.basingstoke.gov.uk/planning",
      "start": 62731,
      "end": 62762,
      "score": 0.5,
      "source": "presidio"
    },
    {
      "type": "URL",
      "text": "www.northwessexdowns.org.uk",
      "start": 62805,
      "end": 62832,
      "score": 0.5,
      "source": "presidio"
    },
    {
      "type": "URL",
      "text": "Police.uk",
      "start": 68955,
      "end": 68964,
      "score": 0.5,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "9/10",
      "start": 51542,
      "end": 51546,
      "score": 0.44999999999999996,
      "source": "presidio"
    },
    {
      "type": "PHONE_NUMBER",
      "text": "43820 60050",
      "start": 16607,
      "end": 16618,
      "score": 0.4,
      "source": "presidio"
    },
    {
      "type": "PHONE_NUMBER",
      "text": "01635 555055",
      "start": 71494,
      "end": 71506,
      "score": 0.4,
      "source": "presidio"
    },
    {
      "type": "PHONE_NUMBER",
      "text": "01635 521707",
      "start": 71536,
      "end": 71548,
      "score": 0.4,
      "source": "presidio"
    },
    {
      "type": "PHONE_NUMBER",
      "text": "01635 555033",
      "start": 71938,
      "end": 71950,
      "score": 0.4,
      "source": "presidio"
    },
    {
      "type": "PHONE_NUMBER",
      "text": "01635 555123",
      "start": 72067,
      "end": 72079,
      "score": 0.4,
      "source": "presidio"
    },
    {
      "type": "PHONE_NUMBER",
      "text": "01256 883883",
      "start": 72118,
      "end": 72130,
      "score": 0.4,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n1",
      "start": 365,
      "end": 367,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n2",
      "start": 388,
      "end": 390,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n3",
      "start": 411,
      "end": 413,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n4",
      "start": 434,
      "end": 436,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n5",
      "start": 462,
      "end": 464,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n6",
      "start": 502,
      "end": 504,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n7",
      "start": 540,
      "end": 542,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n8",
      "start": 576,
      "end": 578,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n9",
      "start": 618,
      "end": 620,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n10",
      "start": 660,
      "end": 663,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n11",
      "start": 679,
      "end": 682,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n12",
      "start": 708,
      "end": 711,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A34",
      "start": 2018,
      "end": 2021,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A343",
      "start": 4522,
      "end": 4526,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A34",
      "start": 4997,
      "end": 5000,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "M4",
      "start": 5068,
      "end": 5070,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "M3",
      "start": 5075,
      "end": 5077,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n2",
      "start": 7378,
      "end": 7380,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n1",
      "start": 7518,
      "end": 7520,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n2",
      "start": 7698,
      "end": 7700,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n3",
      "start": 7813,
      "end": 7815,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n4",
      "start": 7866,
      "end": 7868,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n5",
      "start": 7913,
      "end": 7915,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n6",
      "start": 7948,
      "end": 7950,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n3",
      "start": 7995,
      "end": 7997,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n4",
      "start": 8099,
      "end": 8101,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Q4",
      "start": 13091,
      "end": 13093,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Q1",
      "start": 13101,
      "end": 13103,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n1",
      "start": 13728,
      "end": 13730,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n1",
      "start": 18925,
      "end": 18927,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n2",
      "start": 18992,
      "end": 18994,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n3",
      "start": 19058,
      "end": 19060,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n4",
      "start": 19114,
      "end": 19116,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n5",
      "start": 19191,
      "end": 19193,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n6",
      "start": 19253,
      "end": 19255,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A343",
      "start": 19385,
      "end": 19389,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A34",
      "start": 19448,
      "end": 19451,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A34",
      "start": 19452,
      "end": 19455,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "M4",
      "start": 19528,
      "end": 19530,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "M3",
      "start": 19573,
      "end": 19575,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "M4",
      "start": 20219,
      "end": 20221,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A34",
      "start": 21741,
      "end": 21744,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "M4",
      "start": 21746,
      "end": 21748,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "M3",
      "start": 21750,
      "end": 21752,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A343",
      "start": 30987,
      "end": 30991,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A34",
      "start": 34039,
      "end": 34042,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "A34",
      "start": 35503,
      "end": 35506,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Y1",
      "start": 42913,
      "end": 42915,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Y2",
      "start": 42977,
      "end": 42979,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Y3",
      "start": 43026,
      "end": 43028,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Y4",
      "start": 43075,
      "end": 43077,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Y5",
      "start": 43124,
      "end": 43126,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "M4",
      "start": 56132,
      "end": 56134,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "M3",
      "start": 56135,
      "end": 56137,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Q1",
      "start": 58263,
      "end": 58265,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Q4",
      "start": 58273,
      "end": 58275,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Q1",
      "start": 58617,
      "end": 58619,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "Q2",
      "start": 58620,
      "end": 58622,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n1",
      "start": 60255,
      "end": 60257,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n2",
      "start": 60538,
      "end": 60540,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n3",
      "start": 60859,
      "end": 60861,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n4",
      "start": 61162,
      "end": 61164,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "n5",
      "start": 61547,
      "end": 61549,
      "score": 0.3,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "7/10",
      "start": 21681,
      "end": 21685,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "9/10",
      "start": 21735,
      "end": 21739,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "2/10",
      "start": 21774,
      "end": 21778,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "6/10",
      "start": 21815,
      "end": 21819,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5/10",
      "start": 26808,
      "end": 26812,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5/10",
      "start": 31923,
      "end": 31927,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "6/10",
      "start": 47918,
      "end": 47922,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5/10",
      "start": 52793,
      "end": 52797,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5/10",
      "start": 54450,
      "end": 54454,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5/10",
      "start": 54658,
      "end": 54662,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "DATE_TIME",
      "text": "5/10",
      "start": 73383,
      "end": 73387,
      "score": 0.1,
      "source": "presidio"
    },
    {
      "type": "US_BANK_NUMBER",
      "text": "20250129",
      "start": 72326,
      "end": 72334,
      "score": 0.05,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "555444",
      "start": 71465,
      "end": 71471,
      "score": 0.01,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "555055",
      "start": 71500,
      "end": 71506,
      "score": 0.01,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "521707",
      "start": 71542,
      "end": 71548,
      "score": 0.01,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "373300",
      "start": 71668,
      "end": 71674,
      "score": 0.01,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "9589191",
      "start": 71892,
      "end": 71899,
      "score": 0.01,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "555033",
      "start": 71944,
      "end": 71950,
      "score": 0.01,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "555123",
      "start": 72073,
      "end": 72079,
      "score": 0.01,
      "source": "presidio"
    },
    {
      "type": "US_DRIVER_LICENSE",
      "text": "883883",
      "start": 72124,
      "end": 72130,
      "score": 0.01,
      "source": "presidio"
    },
    {
      "type": "LOC",
      "text": "Blackford Cottage",
      "start": 0,
      "end": 17,
      "score": 0.9558051228523254,
      "source": "deberta"
    },
    {
      "type": "LOC",
      "text": "Blackford Cottage",
      "start": 87,
      "end": 104,
      "score": 0.9785680770874023,
      "source": "deberta"
    },
    {
      "type": "ORG",
      "text": "##ti",
      "start": 264,
      "end": 266,
      "score": 0.4820546507835388,
      "source": "deberta"
    },
    {
      "type": "ORG",
      "text": "UK",
      "start": 272,
      "end": 274,
      "score": 0.9131453633308411,
      "source": "deberta"
    },
    {
      "type": "ORG",
      "text": "Ana",
      "start": 287,
      "end": 290,
      "score": 0.6834108233451843,
      "source": "deberta"
    },
    {
      "type": "ORG",
      "text": "##tics",
      "start": 292,
      "end": 296,
      "score": 0.7165608406066895,
      "source": "deberta"
    },
    {
      "type": "ORG",
      "text": "Blackford Cottage, Andover Road,",
      "start": 0,
      "end": 32,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Blackford Cottage, Andover Road, Highclere,",
      "start": 84,
      "end": 130,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "RG20",
      "start": 140,
      "end": 144,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Date:\\n\\nJanuary 2025\\n\\nReport Type:\\n\\nDesktop Automated Valuation Model",
      "start": 159,
      "end": 233,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "EVENT",
      "text": "AI - UK Real Estate Analytics\\n\\nConfidence Level:\\n\\nMedium-High",
      "start": 267,
      "end": 332,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "72%)\\n\\n## Table",
      "start": 334,
      "end": 350,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Local Market &amp",
      "start": 467,
      "end": 484,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Neighbourhood &",
      "start": 507,
      "end": 522,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Crime,",
      "start": 545,
      "end": 551,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Schools &",
      "start": 552,
      "end": 561,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Lifestyle\\n8.  ",
      "start": 566,
      "end": 581,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Environmental &",
      "start": 581,
      "end": 596,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Financial &",
      "start": 623,
      "end": 634,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Investment Modelling\\n10",
      "start": 639,
      "end": 663,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Key Investment",
      "start": 771,
      "end": 788,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Value                              ",
      "start": 824,
      "end": 859,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 1064,
      "end": 1071,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "364",
      "start": 1151,
      "end": 1154,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.1%",
      "start": 1237,
      "end": 1241,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Gross Rental",
      "start": 1296,
      "end": 1308,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.8%",
      "start": 1324,
      "end": 1328,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "|\\n| 72%",
      "start": 1406,
      "end": 1414,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "B+                  ",
      "start": 1498,
      "end": 1518,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "|\\n\\n",
      "start": 1580,
      "end": 1585,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "the North Wessex Downs Area",
      "start": 1782,
      "end": 1809,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,402",
      "start": 1861,
      "end": 1866,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "4",
      "start": 1896,
      "end": 1897,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2",
      "start": 1911,
      "end": 1912,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 1991,
      "end": 1998,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "£825,000 - £925,000",
      "start": 2071,
      "end": 2090,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 2102,
      "end": 2109,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Burghclere",
      "start": 2326,
      "end": 2336,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "340-£385",
      "start": 2421,
      "end": 2429,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury, Basingstoke",
      "start": 2677,
      "end": 2697,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Property Specifications\\n\\n| Feature",
      "start": 3071,
      "end": 3110,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Blackford        |\\n|",
      "start": 3330,
      "end": 3351,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "House",
      "start": 3361,
      "end": 3366,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Bedrooms         |\\n| 2",
      "start": 3496,
      "end": 3519,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Bathrooms        |\\n|",
      "start": 3579,
      "end": 3600,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,402",
      "start": 3601,
      "end": 3606,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "223",
      "start": 3614,
      "end": 3617,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Floor Area       |\\n|",
      "start": 3662,
      "end": 3683,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Freehold         |\\n|",
      "start": 3745,
      "end": 3766,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "2,800-£3,200",
      "start": 3786,
      "end": 3798,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Council Tax Band",
      "start": 3828,
      "end": 3844,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Private          |\\n\\nProperty Features &amp",
      "start": 4160,
      "end": 4204,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,402",
      "start": 4366,
      "end": 4371,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "4",
      "start": 4399,
      "end": 4400,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2",
      "start": 4433,
      "end": 4434,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "the North Wessex Downs AONB",
      "start": 4799,
      "end": 4826,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 4935,
      "end": 4942,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "12 miles",
      "start": 4958,
      "end": 4966,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "20 miles",
      "start": 4982,
      "end": 4990,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Value                      ",
      "start": 5199,
      "end": 5226,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "825,000",
      "start": 5295,
      "end": 5302,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Lower Estimate             |\\n|",
      "start": 5325,
      "end": 5356,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 5358,
      "end": 5365,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Midpoint Valuation         |\\n|",
      "start": 5388,
      "end": 5419,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "925,000",
      "start": 5421,
      "end": 5428,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Upper Estimate             |\\n|",
      "start": 5451,
      "end": 5482,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "364",
      "start": 5484,
      "end": 5487,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "72%",
      "start": 5557,
      "end": 5560,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "#",
      "start": 5610,
      "end": 5611,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1",
      "start": 5688,
      "end": 5689,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3-mile",
      "start": 5768,
      "end": 5774,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2",
      "start": 5782,
      "end": 5783,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "3",
      "start": 5867,
      "end": 5868,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "4",
      "start": 5951,
      "end": 5952,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "AONB",
      "start": 6015,
      "end": 6019,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 6049,
      "end": 6051,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Sale Date         ",
      "start": 6118,
      "end": 6136,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Distance",
      "start": 6150,
      "end": 6158,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Hollington Lane",
      "start": 6425,
      "end": 6440,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "885,000",
      "start": 6470,
      "end": 6477,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.6 miles",
      "start": 6480,
      "end": 6489,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "377",
      "start": 6524,
      "end": 6527,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "0%",
      "start": 6532,
      "end": 6534,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2024                         | £",
      "start": 6600,
      "end": 6632,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "725,000",
      "start": 6632,
      "end": 6639,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2.1 miles",
      "start": 6651,
      "end": 6660,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "345",
      "start": 6695,
      "end": 6698,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Grotto Cottage",
      "start": 6735,
      "end": 6749,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Burghclere |\\n|",
      "start": 6751,
      "end": 6766,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2024                         | £",
      "start": 6771,
      "end": 6803,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "795,000",
      "start": 6803,
      "end": 6810,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.3 miles",
      "start": 6822,
      "end": 6831,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3 | 2,000  | £",
      "start": 6852,
      "end": 6866,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "398",
      "start": 6866,
      "end": 6869,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "925,000",
      "start": 6974,
      "end": 6981,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.8 miles",
      "start": 6993,
      "end": 7002,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "356",
      "start": 7037,
      "end": 7040,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Burghclere Oct",
      "start": 7127,
      "end": 7141,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "815,000",
      "start": 7150,
      "end": 7157,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2.5 miles",
      "start": 7164,
      "end": 7173,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "362",
      "start": 7208,
      "end": 7211,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "NORP",
      "text": "|\\n\\nMedian",
      "start": 7275,
      "end": 7286,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Calculation:\\n\\n2,402",
      "start": 7363,
      "end": 7384,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "364",
      "start": 7393,
      "end": 7396,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "874,328",
      "start": 7405,
      "end": 7412,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "£875,000)\\n\\n## Valuation",
      "start": 7425,
      "end": 7450,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 7491,
      "end": 7498,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Strong Comparable Support",
      "start": 7522,
      "end": 7547,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "885k",
      "start": 7597,
      "end": 7601,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "925k",
      "start": 7617,
      "end": 7621,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "850k+",
      "start": 7645,
      "end": 7650,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "4",
      "start": 7655,
      "end": 7656,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,300",
      "start": 7686,
      "end": 7691,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "10-15%",
      "start": 7742,
      "end": 7748,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "WORK_OF_ART",
      "text": "Burghclere, Ashmansworth",
      "start": 7779,
      "end": 7803,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "to:\\n3",
      "start": 7809,
      "end": 7815,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Highclere Castle association",
      "start": 7817,
      "end": 7845,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Floor Area Advantage",
      "start": 7999,
      "end": 8019,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,402",
      "start": 8025,
      "end": 8030,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "sqft",
      "start": 8031,
      "end": 8035,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "4",
      "start": 8087,
      "end": 8088,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "West Berkshire/",
      "start": 8121,
      "end": 8136,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2024)\\n\\n<!--",
      "start": 8194,
      "end": 8207,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "72%",
      "start": 8249,
      "end": 8252,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "last 12 months",
      "start": 8307,
      "end": 8321,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "345-£398",
      "start": 8349,
      "end": 8357,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Limited",
      "start": 8387,
      "end": 8394,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 8635,
      "end": 8637,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## £",
      "start": 8696,
      "end": 8700,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "2,950 - £3,250 | £35,400 - £39,000",
      "start": 8956,
      "end": 8990,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Midpoint Rental Value",
      "start": 9004,
      "end": 9025,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "37,200",
      "start": 9058,
      "end": 9064,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Rental",
      "start": 9115,
      "end": 9121,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.25%",
      "start": 9128,
      "end": 9133,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.81%",
      "start": 9186,
      "end": 9191,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "|\\n\\n",
      "start": 9212,
      "end": 9217,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Highclere/Newbury",
      "start": 9249,
      "end": 9266,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "London/Reading Limited",
      "start": 9365,
      "end": 9387,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "4+",
      "start": 9406,
      "end": 9408,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Rental Comparables:\\n\\n| Address",
      "start": 9591,
      "end": 9626,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Distance",
      "start": 9701,
      "end": 9709,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Listed Date       ",
      "start": 9714,
      "end": 9732,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "4      | £",
      "start": 9886,
      "end": 9896,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "16.50",
      "start": 9905,
      "end": 9910,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.5 miles",
      "start": 9921,
      "end": 9930,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "4      |        |",
      "start": 10004,
      "end": 10021,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "15.20",
      "start": 10040,
      "end": 10045,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2.0 miles  | Nov",
      "start": 10055,
      "end": 10071,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "4      |        | £3,000         | £",
      "start": 10122,
      "end": 10158,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "14.80",
      "start": 10158,
      "end": 10163,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3.5 miles  |",
      "start": 10173,
      "end": 10185,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury",
      "start": 10209,
      "end": 10216,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "4      | £",
      "start": 10249,
      "end": 10259,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "17.00",
      "start": 10276,
      "end": 10281,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6.0 miles",
      "start": 10291,
      "end": 10300,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2024",
      "start": 10308,
      "end": 10312,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury",
      "start": 10336,
      "end": 10343,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "3",
      "start": 10358,
      "end": 10359,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "16.50",
      "start": 10394,
      "end": 10399,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "7.0 miles",
      "start": 10409,
      "end": 10418,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2024",
      "start": 10426,
      "end": 10430,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,100",
      "start": 10481,
      "end": 10486,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "37,200",
      "start": 10606,
      "end": 10612,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 10616,
      "end": 10623,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "100",
      "start": 10627,
      "end": 10630,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "37,200",
      "start": 10681,
      "end": 10687,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "10%",
      "start": 10737,
      "end": 10740,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "3,720",
      "start": 10744,
      "end": 10749,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "1.5%",
      "start": 10773,
      "end": 10777,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "13,125",
      "start": 10790,
      "end": 10796,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "500",
      "start": 10811,
      "end": 10814,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5%",
      "start": 10831,
      "end": 10833,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "1,860",
      "start": 10842,
      "end": 10847,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "19,205",
      "start": 10861,
      "end": 10867,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "17,995",
      "start": 10890,
      "end": 10896,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "17,995",
      "start": 10912,
      "end": 10918,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 10922,
      "end": 10929,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "100",
      "start": 10933,
      "end": 10936,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2.06%\\n\\n*Note",
      "start": 10939,
      "end": 10953,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.81%",
      "start": 10976,
      "end": 10981,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "8,750",
      "start": 11017,
      "end": 11022,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Yield Comparison",
      "start": 11111,
      "end": 11127,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Subject vs Regional",
      "start": 11129,
      "end": 11148,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.25%",
      "start": 11226,
      "end": 11231,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3.5-4.0%",
      "start": 11328,
      "end": 11336,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.81%",
      "start": 11351,
      "end": 11356,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "CE Primary",
      "start": 11619,
      "end": 11629,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "NORP",
      "text": "Hurst",
      "start": 11635,
      "end": 11640,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "15",
      "start": 11739,
      "end": 11741,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "AWE Aldermaston",
      "start": 11817,
      "end": 11832,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Vodafone Newbury",
      "start": 11834,
      "end": 11850,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Greenham Business Park",
      "start": 11852,
      "end": 11874,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,100+/month",
      "start": 11933,
      "end": 11945,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## 5",
      "start": 11999,
      "end": 12003,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Local Market &amp",
      "start": 12005,
      "end": 12022,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "|\\n|---------------|------------------|------------------|-------------|-----------------|\\n| +2.8%",
      "start": 12182,
      "end": 12281,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "1-Year",
      "start": 12344,
      "end": 12350,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "+9.8%",
      "start": 12400,
      "end": 12405,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3-Year",
      "start": 12433,
      "end": 12439,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "5-Year",
      "start": 12522,
      "end": 12528,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "HM Land Registry",
      "start": 12552,
      "end": 12568,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "UK",
      "start": 12570,
      "end": 12572,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "625,000",
      "start": 12750,
      "end": 12757,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "YoY",
      "start": 12765,
      "end": 12768,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "585,000",
      "start": 12809,
      "end": 12816,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-12%",
      "start": 12941,
      "end": 12945,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Supply &",
      "start": 13029,
      "end": 13040,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Demand Dynamics\\n\\nCurrent Market Conditions",
      "start": 13045,
      "end": 13089,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2024 - Q1",
      "start": 13094,
      "end": 13103,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2025):\\n\\n<!--",
      "start": 13104,
      "end": 13118,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "-->\\n\\n| Metric",
      "start": 13143,
      "end": 13158,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "|\\n|--------------------|------------------|----------------------------------|\\n| 68 days",
      "start": 13225,
      "end": 13315,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "97.2%",
      "start": 13386,
      "end": 13391,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "95.8%",
      "start": 13407,
      "end": 13412,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Sale Price",
      "start": 13426,
      "end": 13436,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "3",
      "start": 13464,
      "end": 13465,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "4",
      "start": 13521,
      "end": 13522,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "8-12",
      "start": 13542,
      "end": 13546,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Transaction Volume",
      "start": 13582,
      "end": 13600,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "approximately 350",
      "start": 13763,
      "end": 13780,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "only 2",
      "start": 13810,
      "end": 13816,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Crossrail",
      "start": 14011,
      "end": 14020,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Reading-Paddington",
      "start": 14031,
      "end": 14049,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "\\\"Downton Abbey",
      "start": 14063,
      "end": 14078,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "Strong",
      "start": 14133,
      "end": 14139,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "AWE Aldermaston",
      "start": 14163,
      "end": 14178,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury Business Parks)\\n\\n",
      "start": 14180,
      "end": 14207,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "600k-£850k",
      "start": 14241,
      "end": 14251,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "850k-£1.2",
      "start": 14292,
      "end": 14301,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Interest Rate Environment &amp",
      "start": 14409,
      "end": 14439,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "Monthly",
      "start": 14538,
      "end": 14545,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875k",
      "start": 14556,
      "end": 14560,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "75%",
      "start": 14562,
      "end": 14565,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 14566,
      "end": 14569,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5.15%",
      "start": 14661,
      "end": 14666,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.85%",
      "start": 14738,
      "end": 14743,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5.50%",
      "start": 14815,
      "end": 14820,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "4,002",
      "start": 14830,
      "end": 14835,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5.75%",
      "start": 14892,
      "end": 14897,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "4,109",
      "start": 14907,
      "end": 14912,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Tracker                                  |\\n\\nAffordability Analysis: - Property Value",
      "start": 14923,
      "end": 15009,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 15012,
      "end": 15019,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "25%",
      "start": 15039,
      "end": 15042,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "218,750",
      "start": 15046,
      "end": 15053,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "75%",
      "start": 15075,
      "end": 15078,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 15079,
      "end": 15082,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "656,250",
      "start": 15086,
      "end": 15093,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "4.5x",
      "start": 15121,
      "end": 15125,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "145,833",
      "start": 15138,
      "end": 15145,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "55,000",
      "start": 15185,
      "end": 15191,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5%",
      "start": 15332,
      "end": 15334,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "130",
      "start": 15362,
      "end": 15365,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3.7%",
      "start": 15388,
      "end": 15392,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "sub£600k",
      "start": 15497,
      "end": 15505,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4050%",
      "start": 15601,
      "end": 15606,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Transaction Volume Trends:\\n\\n<!--",
      "start": 15755,
      "end": 15792,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Neighbourhood &amp",
      "start": 15875,
      "end": 15893,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 15929,
      "end": 15931,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "\\\"Downton Abbey.\\",
      "start": 16234,
      "end": 16251,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "the North Wessex Downs Area",
      "start": 16274,
      "end": 16301,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Context",
      "start": 16383,
      "end": 16390,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "9",
      "start": 16546,
      "end": 16547,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Burghclere, Ashmansworth)",
      "start": 16561,
      "end": 16586,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "SU 43820",
      "start": 16604,
      "end": 16612,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 16636,
      "end": 16638,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Demographics &",
      "start": 16639,
      "end": 16653,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Demographic Metric",
      "start": 16692,
      "end": 16710,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "NORP",
      "text": "Parish",
      "start": 16725,
      "end": 16731,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1,844,000",
      "start": 16885,
      "end": 16894,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "774,000            | -           | Households            |\\n| 67/km ²              ",
      "start": 16970,
      "end": 17053,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "460/km ²           | 432/km ²    | Population Density",
      "start": 17055,
      "end": 17108,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "42 years           | 40 years",
      "start": 17140,
      "end": 17169,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "78%",
      "start": 17202,
      "end": 17205,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "68%",
      "start": 17225,
      "end": 17228,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "63%",
      "start": 17246,
      "end": 17249,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Owner-Occupation Rate",
      "start": 17260,
      "end": 17281,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "62%",
      "start": 17287,
      "end": 17290,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "28%",
      "start": 17310,
      "end": 17313,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "22%",
      "start": 17331,
      "end": 17334,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Homes        |\\n\\nHousehold Composition",
      "start": 17354,
      "end": 17393,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "35%",
      "start": 17433,
      "end": 17436,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "28%",
      "start": 17462,
      "end": 17465,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "18%",
      "start": 17493,
      "end": 17496,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "19%\\n\\n##",
      "start": 17509,
      "end": 17518,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Employment &",
      "start": 17576,
      "end": 17591,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Occupation Types",
      "start": 17614,
      "end": 17633,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Working Population                     |\\n|--------------------------------------------|--------------------------------------------|\\n| Managers,",
      "start": 17722,
      "end": 17868,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Directors & Senior",
      "start": 17869,
      "end": 17887,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "24%",
      "start": 17898,
      "end": 17901,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Directors & Senior",
      "start": 17914,
      "end": 17932,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "24%",
      "start": 17943,
      "end": 17946,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Professional Occupations",
      "start": 17952,
      "end": 17976,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "32%",
      "start": 17977,
      "end": 17980,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Professional Occupations",
      "start": 17997,
      "end": 18021,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "32%",
      "start": 18022,
      "end": 18025,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Associate Professional & Technical",
      "start": 18045,
      "end": 18079,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "18%",
      "start": 18080,
      "end": 18083,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Associate Professional & Technical",
      "start": 18090,
      "end": 18124,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "18%",
      "start": 18125,
      "end": 18128,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "11%",
      "start": 18167,
      "end": 18170,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Administrative & Secretarial",
      "start": 18183,
      "end": 18211,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "11%",
      "start": 18212,
      "end": 18215,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "8%",
      "start": 18246,
      "end": 18248,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "8%",
      "start": 18291,
      "end": 18293,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "7%",
      "start": 18330,
      "end": 18332,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "7%",
      "start": 18375,
      "end": 18377,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "55,000",
      "start": 18637,
      "end": 18643,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "51,000",
      "start": 18663,
      "end": 18669,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "89,000",
      "start": 18706,
      "end": 18712,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "68,500",
      "start": 18724,
      "end": 18730,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "62,000",
      "start": 18750,
      "end": 18756,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "18%",
      "start": 18792,
      "end": 18795,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "9%",
      "start": 18810,
      "end": 18812,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "6%",
      "start": 18836,
      "end": 18838,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "100k",
      "start": 18861,
      "end": 18865,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Employment Hubs",
      "start": 18888,
      "end": 18903,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "15",
      "start": 18912,
      "end": 18914,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "AWE Aldermaston",
      "start": 18929,
      "end": 18944,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "5 miles",
      "start": 18946,
      "end": 18953,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "5,000",
      "start": 18975,
      "end": 18980,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury Business Park",
      "start": 18996,
      "end": 19017,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 19019,
      "end": 19026,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "UK",
      "start": 19039,
      "end": 19041,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Greenham Business Park",
      "start": 19062,
      "end": 19084,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "7 miles",
      "start": 19086,
      "end": 19093,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "12 miles",
      "start": 19131,
      "end": 19139,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "20 miles",
      "start": 19204,
      "end": 19212,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "65 miles",
      "start": 19265,
      "end": 19273,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Transport &",
      "start": 19336,
      "end": 19350,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "FAC",
      "text": "Andover Road",
      "start": 19391,
      "end": 19403,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "WORK_OF_ART",
      "text": "A34 A34",
      "start": 19448,
      "end": 19455,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2 miles",
      "start": 19458,
      "end": 19465,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "FAC",
      "text": "Birmingham-Southampton",
      "start": 19495,
      "end": 19517,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "14 miles",
      "start": 19533,
      "end": 19541,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "LAW",
      "text": "Junction 13",
      "start": 19549,
      "end": 19560,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Chieveley",
      "start": 19562,
      "end": 19571,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "12 miles",
      "start": 19578,
      "end": 19586,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Rail",
      "start": 19621,
      "end": 19628,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Frequency            |\\n|-----------|--------------|--------------------------|----------------------|\\n| 6 miles",
      "start": 19701,
      "end": 19814,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "55-65",
      "start": 19834,
      "end": 19839,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Paddington",
      "start": 19846,
      "end": 19856,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury 2-3/hour",
      "start": 19861,
      "end": 19877,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "|\\n| 8 miles",
      "start": 19882,
      "end": 19894,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Kingsclere -         |\\n|",
      "start": 19941,
      "end": 19966,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "12 miles",
      "start": 19967,
      "end": 19975,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "45-50",
      "start": 19979,
      "end": 19984,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Basingstoke 4-6/hour",
      "start": 20021,
      "end": 20041,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "LAW",
      "text": "Jct 13",
      "start": 20223,
      "end": 20229,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "10",
      "start": 20233,
      "end": 20235,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "50 miles",
      "start": 20283,
      "end": 20291,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "60",
      "start": 20293,
      "end": 20295,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "35 miles",
      "start": 20326,
      "end": 20334,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "45",
      "start": 20336,
      "end": 20338,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "mins)\\n\\n<!--",
      "start": 20339,
      "end": 20352,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "All Angels Church",
      "start": 20431,
      "end": 20448,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Yew Tree",
      "start": 20518,
      "end": 20526,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2 miles",
      "start": 20625,
      "end": 20632,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3 miles",
      "start": 20759,
      "end": 20766,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2 miles",
      "start": 20782,
      "end": 20789,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 20848,
      "end": 20855,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "-Newbury Hospital",
      "start": 20929,
      "end": 20946,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 20949,
      "end": 20956,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Basingstoke Hospital",
      "start": 20979,
      "end": 20999,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "12 miles",
      "start": 21002,
      "end": 21010,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "major acute hospital",
      "start": 21012,
      "end": 21032,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "GP Surgeries",
      "start": 21034,
      "end": 21046,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury",
      "start": 21049,
      "end": 21056,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 21058,
      "end": 21065,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "8",
      "start": 21080,
      "end": 21081,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "miles)\\n\\nLifestyle &amp",
      "start": 21082,
      "end": 21106,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "8 miles",
      "start": 21214,
      "end": 21221,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Sandford Springs Golf Club",
      "start": 21232,
      "end": 21258,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3 miles",
      "start": 21260,
      "end": 21267,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury &amp",
      "start": 21270,
      "end": 21282,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Crookham",
      "start": 21284,
      "end": 21292,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 21294,
      "end": 21301,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Wayfarer's Walk, Test Way",
      "start": 21363,
      "end": 21388,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Sandham Memorial Chapel\\n\\n<!--",
      "start": 21449,
      "end": 21480,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 21612,
      "end": 21614,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury",
      "start": 21687,
      "end": 21694,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 21695,
      "end": 21702,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Road Network",
      "start": 21704,
      "end": 21716,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "50 miles",
      "start": 21830,
      "end": 21838,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "6.0/10\\n```\\n\\n#",
      "start": 21866,
      "end": 21882,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Schools &",
      "start": 21894,
      "end": 21903,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "12 months",
      "start": 22005,
      "end": 22014,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Rate",
      "start": 22069,
      "end": 22073,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "1,000   |",
      "start": 22078,
      "end": 22087,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Hampshire Avg   |",
      "start": 22091,
      "end": 22108,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "National Avg                 |\\n|--------------|-------------------|------------------|--------------------|---------------------------------|\\n| Total Crime",
      "start": 22112,
      "end": 22269,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "42",
      "start": 22273,
      "end": 22275,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "11.2",
      "start": 22283,
      "end": 22287,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-67%",
      "start": 22293,
      "end": 22297,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-73%",
      "start": 22333,
      "end": 22337,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "8            |",
      "start": 22370,
      "end": 22384,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2.1",
      "start": 22385,
      "end": 22388,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-76%",
      "start": 22467,
      "end": 22471,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3            |",
      "start": 22482,
      "end": 22496,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.8               |                  ",
      "start": 22497,
      "end": 22534,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-60%",
      "start": 22536,
      "end": 22540,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "Burglary -68%",
      "start": 22557,
      "end": 22570,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1.1",
      "start": 22609,
      "end": 22612,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-58%",
      "start": 22648,
      "end": 22652,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-64%",
      "start": 22683,
      "end": 22687,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "12",
      "start": 22706,
      "end": 22708,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "3.2",
      "start": 22721,
      "end": 22724,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Violence & Sexual Offences",
      "start": 22781,
      "end": 22807,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6            |                   ",
      "start": 22818,
      "end": 22851,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1.6              ",
      "start": 22853,
      "end": 22870,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-72%",
      "start": 22872,
      "end": 22876,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "Theft -78%",
      "start": 22893,
      "end": 22903,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1.3",
      "start": 22965,
      "end": 22968,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Criminal Damage -69%",
      "start": 23005,
      "end": 23025,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1.1              ",
      "start": 23077,
      "end": 23094,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-68%",
      "start": 23096,
      "end": 23100,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "9",
      "start": 23281,
      "end": 23282,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "11.2",
      "start": 23475,
      "end": 23479,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1,000",
      "start": 23484,
      "end": 23489,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "67%",
      "start": 23504,
      "end": 23507,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "34",
      "start": 23533,
      "end": 23535,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1,000",
      "start": 23540,
      "end": 23545,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "73%",
      "start": 23547,
      "end": 23550,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "England &",
      "start": 23557,
      "end": 23566,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "42",
      "start": 23586,
      "end": 23588,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "ASB",
      "start": 23651,
      "end": 23654,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "0.8",
      "start": 23704,
      "end": 23707,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1,000",
      "start": 23712,
      "end": 23717,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2.5",
      "start": 23721,
      "end": 23724,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Hampshire Constabulary",
      "start": 23905,
      "end": 23927,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 24028,
      "end": 24030,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Schools &amp",
      "start": 24031,
      "end": 24043,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 24058,
      "end": 24060,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Distance",
      "start": 24153,
      "end": 24161,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Ofsted Rating",
      "start": 24178,
      "end": 24191,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Pupil Nos",
      "start": 24211,
      "end": 24220,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "|\\n|-------------------------------------|------------|-----------|-----------------|------------|-------------|\\n| St. Michael's",
      "start": 24221,
      "end": 24350,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "CE Primary",
      "start": 24351,
      "end": 24361,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.5 miles",
      "start": 24375,
      "end": 24384,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "C of E VA",
      "start": 24388,
      "end": 24397,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "105",
      "start": 24425,
      "end": 24428,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "98",
      "start": 24440,
      "end": 24442,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Burghclere Primary School",
      "start": 24448,
      "end": 24473,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2.1 miles",
      "start": 24486,
      "end": 24495,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Community",
      "start": 24499,
      "end": 24508,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "140 |         128",
      "start": 24536,
      "end": 24553,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Woolton Hill Junior School",
      "start": 24559,
      "end": 24585,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "4.2 miles",
      "start": 24597,
      "end": 24606,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Community",
      "start": 24610,
      "end": 24619,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "180 |         172",
      "start": 24647,
      "end": 24664,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Michael",
      "start": 24674,
      "end": 24681,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "CE Primary School",
      "start": 24684,
      "end": 24701,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "Year 6",
      "start": 24808,
      "end": 24814,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "92%",
      "start": 25037,
      "end": 25040,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "65%",
      "start": 25105,
      "end": 25108,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Distance",
      "start": 25178,
      "end": 25186,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "The Hurst Community College",
      "start": 25352,
      "end": 25379,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6.5 miles",
      "start": 25382,
      "end": 25391,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Academy",
      "start": 25395,
      "end": 25402,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1,250",
      "start": 25437,
      "end": 25442,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Park House School",
      "start": 25454,
      "end": 25471,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "7 miles",
      "start": 25484,
      "end": 25491,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Academy",
      "start": 25497,
      "end": 25504,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1,650",
      "start": 25539,
      "end": 25544,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "St. Bartholomew's School",
      "start": 25556,
      "end": 25580,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "8 miles",
      "start": 25586,
      "end": 25593,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Academy",
      "start": 25599,
      "end": 25606,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "11-18",
      "start": 25627,
      "end": 25632,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,150",
      "start": 25641,
      "end": 25646,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Hurst Community College - Key Details",
      "start": 25662,
      "end": 25699,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2022",
      "start": 25717,
      "end": 25721,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "68%",
      "start": 25757,
      "end": 25760,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "Grade 5+",
      "start": 25771,
      "end": 25779,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "NORP",
      "text": "English",
      "start": 25783,
      "end": 25790,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Maths",
      "start": 25797,
      "end": 25802,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "51%",
      "start": 25818,
      "end": 25821,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "8",
      "start": 25867,
      "end": 25868,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Bartholomew's School (Newbury) - Highly Sought Alternative",
      "start": 26082,
      "end": 26140,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "FAC",
      "text": "Berkshire for Progress",
      "start": 26200,
      "end": 26222,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "85%",
      "start": 26241,
      "end": 26244,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "Grade 5+",
      "start": 26255,
      "end": 26263,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "NORP",
      "text": "English",
      "start": 26267,
      "end": 26274,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Maths - A-Level: Average",
      "start": 26281,
      "end": 26305,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "B+",
      "start": 26312,
      "end": 26314,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "42%",
      "start": 26316,
      "end": 26319,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 26393,
      "end": 26395,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Independent Schools",
      "start": 26396,
      "end": 26415,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "15",
      "start": 26424,
      "end": 26426,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Highclere School",
      "start": 26439,
      "end": 26455,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "4 miles",
      "start": 26521,
      "end": 26528,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Co-ed",
      "start": 26540,
      "end": 26545,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Horris Hill",
      "start": 26582,
      "end": 26593,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "10 miles",
      "start": 26595,
      "end": 26603,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "12 miles",
      "start": 26654,
      "end": 26662,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "11-18",
      "start": 26692,
      "end": 26697,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 26731,
      "end": 26738,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 26778,
      "end": 26780,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "St. Bartholomew's",
      "start": 27030,
      "end": 27047,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Lifestyle &",
      "start": 27184,
      "end": 27198,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "WORK_OF_ART",
      "text": "Community\\n\\nVillage Character: -Population : ~850",
      "start": 27203,
      "end": 27253,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Lifestyle Attractions:\\n\\n<!--",
      "start": 27565,
      "end": 27595,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "5,000-acre",
      "start": 27653,
      "end": 27663,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Sandham Memorial Chapel",
      "start": 27718,
      "end": 27741,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3 miles",
      "start": 27743,
      "end": 27750,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "National Trust Newbury",
      "start": 27777,
      "end": 27799,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "1,738 km ²",
      "start": 27883,
      "end": 27893,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Wayfarer",
      "start": 27948,
      "end": 27956,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "NORP",
      "text": "Equestrian",
      "start": 28051,
      "end": 28061,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3 miles",
      "start": 28141,
      "end": 28148,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury &amp",
      "start": 28151,
      "end": 28163,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Crookham",
      "start": 28165,
      "end": 28173,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "6 miles)\\n\\n<!--",
      "start": 28175,
      "end": 28191,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "30",
      "start": 28300,
      "end": 28302,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 28494,
      "end": 28501,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "St. Michael's Church",
      "start": 28640,
      "end": 28660,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2 miles",
      "start": 28725,
      "end": 28732,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 28794,
      "end": 28796,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Lifestyle Factor Ratings",
      "start": 28833,
      "end": 28857,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "7.0/10 - Excellent",
      "start": 28917,
      "end": 28935,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Environmental &amp",
      "start": 29066,
      "end": 29084,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Planning",
      "start": 29086,
      "end": 29094,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Environmental Risk",
      "start": 29124,
      "end": 29145,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Flood Risk\\n\\n| Flood",
      "start": 29160,
      "end": 29184,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Flood Zone 1",
      "start": 29365,
      "end": 29377,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "0.1%",
      "start": 29380,
      "end": 29384,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "NORP",
      "text": "Minimal",
      "start": 29442,
      "end": 29449,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Groundwater    ",
      "start": 29487,
      "end": 29502,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "lt;0.1%",
      "start": 29809,
      "end": 29816,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Air Quality\\n\\n|",
      "start": 30117,
      "end": 30136,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Value vs National",
      "start": 30152,
      "end": 30169,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "6.2",
      "start": 30289,
      "end": 30292,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "50%",
      "start": 30304,
      "end": 30307,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "11.8",
      "start": 30365,
      "end": 30369,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "³ | 30%",
      "start": 30376,
      "end": 30383,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Excellent                    |\\n|",
      "start": 30407,
      "end": 30440,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "14.3",
      "start": 30441,
      "end": 30445,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "³ | 36%",
      "start": 30452,
      "end": 30459,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "LAW",
      "text": "NO ₂",
      "start": 30478,
      "end": 30482,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "9",
      "start": 30703,
      "end": 30704,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2024",
      "start": 30722,
      "end": 30726,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Green Space &",
      "start": 31074,
      "end": 31087,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "#",
      "start": 31134,
      "end": 31135,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Designation:\\n\\nNorth",
      "start": 31136,
      "end": 31157,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "FAC",
      "text": "the North Wessex Downs AONB",
      "start": 31239,
      "end": 31266,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORDINAL",
      "text": "third",
      "start": 31278,
      "end": 31283,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "1,738 km ²",
      "start": 31313,
      "end": 31323,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "1,200+ miles",
      "start": 31567,
      "end": 31579,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "1.5 miles",
      "start": 31642,
      "end": 31651,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "National Trust Sidown Hill",
      "start": 31691,
      "end": 31717,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2 miles",
      "start": 31719,
      "end": 31726,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.6 miles",
      "start": 31786,
      "end": 31795,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "5,000 acres",
      "start": 31798,
      "end": 31809,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Ancient",
      "start": 31821,
      "end": 31828,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "3",
      "start": 31863,
      "end": 31864,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Planning &",
      "start": 32022,
      "end": 32035,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Development",
      "start": 32040,
      "end": 32051,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Deane Borough Council - Local Plan",
      "start": 32110,
      "end": 32144,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2029",
      "start": 32166,
      "end": 32170,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Restrict",
      "start": 32425,
      "end": 32433,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Basingstoke, Tadley",
      "start": 32615,
      "end": 32634,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.5 miles",
      "start": 32695,
      "end": 32704,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Proposal",
      "start": 32780,
      "end": 32788,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "HSE      ",
      "start": 32958,
      "end": 32967,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "FAC",
      "text": "Andover Road Single",
      "start": 32969,
      "end": 32988,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Conversion",
      "start": 33107,
      "end": 33117,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2022",
      "start": 33157,
      "end": 33161,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "HSE      ",
      "start": 33176,
      "end": 33185,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "FAC",
      "text": "Hollington Lane",
      "start": 33187,
      "end": 33202,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "Two",
      "start": 33216,
      "end": 33219,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Tree",
      "start": 33325,
      "end": 33329,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "90%+",
      "start": 33434,
      "end": 33438,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Infrastructure Projects &amp",
      "start": 33692,
      "end": 33720,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Confirmed/Proposed Developments",
      "start": 33738,
      "end": 33772,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "10 miles):\\n\\n#",
      "start": 33781,
      "end": 33796,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury Town Centre Regeneration\\n\\n- Location",
      "start": 33801,
      "end": 33847,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 33849,
      "end": 33856,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "WORK_OF_ART",
      "text": "Scope: Mixed",
      "start": 33865,
      "end": 33877,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Status",
      "start": 33930,
      "end": 33936,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2023",
      "start": 33956,
      "end": 33960,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Phase 2",
      "start": 33963,
      "end": 33970,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "A34 Chieveley Junction Improvements\\n\\n- Location",
      "start": 34039,
      "end": 34088,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "8 miles",
      "start": 34090,
      "end": 34097,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Scope: Junction",
      "start": 34111,
      "end": 34126,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "National Highways)\\n- Status: Consultation",
      "start": 34145,
      "end": 34187,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Kingsclere Housing Allocation\\n\\n- Location",
      "start": 34265,
      "end": 34308,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "8 miles",
      "start": 34310,
      "end": 34317,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "Scope",
      "start": 34327,
      "end": 34332,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "150",
      "start": 34334,
      "end": 34337,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2025-2029)\\n-",
      "start": 34349,
      "end": 34362,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Burghclere Neighbourhood",
      "start": 34444,
      "end": 34468,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "2 miles",
      "start": 34489,
      "end": 34496,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "20-30",
      "start": 34519,
      "end": 34524,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2022\\n\\n-",
      "start": 34576,
      "end": 34585,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Major Negative Developments Identified",
      "start": 34656,
      "end": 34694,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Environmental Risk",
      "start": 34894,
      "end": 34915,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "Strong",
      "start": 35137,
      "end": 35143,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Financial &",
      "start": 35650,
      "end": 35661,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Investment",
      "start": 35710,
      "end": 35720,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 35971,
      "end": 35978,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Midpoint",
      "start": 35990,
      "end": 35998,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "218,750",
      "start": 36060,
      "end": 36067,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "25%",
      "start": 36069,
      "end": 36072,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Deposit",
      "start": 36114,
      "end": 36121,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 36123,
      "end": 36126,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "656,250",
      "start": 36149,
      "end": 36156,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "75%",
      "start": 36168,
      "end": 36171,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 36172,
      "end": 36175,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5.15%",
      "start": 36237,
      "end": 36242,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "37,200",
      "start": 36416,
      "end": 36422,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "10%",
      "start": 36504,
      "end": 36507,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "1%",
      "start": 36593,
      "end": 36595,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "8,750",
      "start": 36614,
      "end": 36619,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Maintenance Reserve",
      "start": 36648,
      "end": 36667,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "500/year         |",
      "start": 36683,
      "end": 36701,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5%",
      "start": 36771,
      "end": 36773,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "1,860/year",
      "start": 36792,
      "end": 36802,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.5%",
      "start": 36860,
      "end": 36864,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "Annual",
      "start": 36915,
      "end": 36921,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Property Appreciation",
      "start": 36922,
      "end": 36943,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "656,250",
      "start": 37088,
      "end": 37095,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5.15%",
      "start": 37113,
      "end": 37118,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,842\\n\\nAnnual",
      "start": 37182,
      "end": 37197,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "£46,104\\n\\n##",
      "start": 37213,
      "end": 37226,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Property Management",
      "start": 37486,
      "end": 37505,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "10%",
      "start": 37507,
      "end": 37510,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Maintenance Reserve",
      "start": 37542,
      "end": 37561,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "1%",
      "start": 37563,
      "end": 37565,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5%",
      "start": 37668,
      "end": 37670,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "22,370",
      "start": 37746,
      "end": 37752,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "12,297",
      "start": 38051,
      "end": 38057,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 38098,
      "end": 38100,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "218,750",
      "start": 38210,
      "end": 38217,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "26,250",
      "start": 38231,
      "end": 38237,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "5,000",
      "start": 38248,
      "end": 38253,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "250,000",
      "start": 38270,
      "end": 38277,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "22,370",
      "start": 38300,
      "end": 38306,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "33,807",
      "start": 38356,
      "end": 38362,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "Year 1)\\n\\nTotal Return on Investment",
      "start": 38425,
      "end": 38462,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.5%",
      "start": 38505,
      "end": 38509,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875k",
      "start": 38518,
      "end": 38522,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "986k",
      "start": 38526,
      "end": 38530,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "111,250",
      "start": 38534,
      "end": 38541,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "5 years",
      "start": 38572,
      "end": 38579,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "65,000",
      "start": 38647,
      "end": 38653,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "141,250",
      "start": 38670,
      "end": 38677,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "56.5%",
      "start": 38691,
      "end": 38696,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "11.3%",
      "start": 38698,
      "end": 38703,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "37,200",
      "start": 38904,
      "end": 38910,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 38914,
      "end": 38921,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "100",
      "start": 38925,
      "end": 38928,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.25%",
      "start": 38941,
      "end": 38946,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "22,370",
      "start": 38975,
      "end": 38981,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 38985,
      "end": 38992,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "100",
      "start": 38996,
      "end": 38999,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.56%",
      "start": 39012,
      "end": 39017,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "100",
      "start": 39077,
      "end": 39080,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "8.95%",
      "start": 39083,
      "end": 39088,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.25%",
      "start": 39132,
      "end": 39137,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.56%",
      "start": 39197,
      "end": 39202,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3.5-4.5%",
      "start": 39359,
      "end": 39367,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "FAC",
      "text": "Hampshire/West Berks)\\n\\n",
      "start": 39381,
      "end": 39406,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Capitalization Rate",
      "start": 39406,
      "end": 39428,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Cap",
      "start": 39430,
      "end": 39433,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "22,370",
      "start": 39537,
      "end": 39543,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 39563,
      "end": 39570,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2.56%\\n\\nInterpretation",
      "start": 39583,
      "end": 39606,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.5-3%",
      "start": 39622,
      "end": 39628,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "4,220",
      "start": 39875,
      "end": 39880,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "10,610",
      "start": 39925,
      "end": 39931,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "14,830",
      "start": 39966,
      "end": 39972,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "14,830",
      "start": 40005,
      "end": 40011,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "12",
      "start": 40014,
      "end": 40016,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "1,236",
      "start": 40020,
      "end": 40025,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,100",
      "start": 40048,
      "end": 40053,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "60%",
      "start": 40075,
      "end": 40078,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.5%",
      "start": 40167,
      "end": 40171,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "annual",
      "start": 40172,
      "end": 40178,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "250,000",
      "start": 40212,
      "end": 40219,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "~£22,000 - Plus",
      "start": 40257,
      "end": 40272,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "~£12,000/year",
      "start": 40303,
      "end": 40316,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Sensitivity",
      "start": 40410,
      "end": 40424,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 40504,
      "end": 40511,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,100",
      "start": 40521,
      "end": 40526,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.56%",
      "start": 40546,
      "end": 40551,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "56.5%\\n\\nOptimistic",
      "start": 40564,
      "end": 40583,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "+5%",
      "start": 40605,
      "end": 40608,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "918,750",
      "start": 40627,
      "end": 40634,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "3,410/month",
      "start": 40644,
      "end": 40655,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.84%",
      "start": 40669,
      "end": 40674,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "5Yr",
      "start": 40677,
      "end": 40680,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "68.2%\\n\\n<!--",
      "start": 40686,
      "end": 40699,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-10%",
      "start": 40735,
      "end": 40739,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "831,250",
      "start": 40768,
      "end": 40775,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2,790/month",
      "start": 40785,
      "end": 40796,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "1.92%",
      "start": 40810,
      "end": 40815,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "42.1%\\n\\n<!--",
      "start": 40828,
      "end": 40841,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 40855,
      "end": 40857,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "-->\\n\\n| Rental Income",
      "start": 40945,
      "end": 40967,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "825k",
      "start": 40989,
      "end": 40993,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875k",
      "start": 40999,
      "end": 41003,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "925k",
      "start": 41016,
      "end": 41020,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "2,790",
      "start": 41103,
      "end": 41108,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-10%",
      "start": 41110,
      "end": 41114,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.03%",
      "start": 41120,
      "end": 41125,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "1.92%",
      "start": 41146,
      "end": 41151,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "1.81%",
      "start": 41163,
      "end": 41168,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,100",
      "start": 41177,
      "end": 41182,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.71%",
      "start": 41194,
      "end": 41199,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.56%",
      "start": 41220,
      "end": 41225,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.42%",
      "start": 41237,
      "end": 41242,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,410",
      "start": 41251,
      "end": 41256,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3.39%",
      "start": 41268,
      "end": 41273,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3.20%",
      "start": 41294,
      "end": 41299,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3.03%",
      "start": 41311,
      "end": 41316,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 41738,
      "end": 41740,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Pass/Fail",
      "start": 41874,
      "end": 41883,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "656,250",
      "start": 41996,
      "end": 42003,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "4.5           | £",
      "start": 42006,
      "end": 42023,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "145,833",
      "start": 42023,
      "end": 42030,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "150k",
      "start": 42059,
      "end": 42063,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "26%",
      "start": 42119,
      "end": 42122,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "12,153",
      "start": 42127,
      "end": 42133,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "35%",
      "start": 42141,
      "end": 42144,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Affordability Test |\\n|",
      "start": 42165,
      "end": 42188,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "125%",
      "start": 42216,
      "end": 42220,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "125%",
      "start": 42238,
      "end": 42242,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Rental Coverage    |\\n| Payment",
      "start": 42262,
      "end": 42293,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "8.15%",
      "start": 42297,
      "end": 42302,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "5,124/month      |",
      "start": 42314,
      "end": 42332,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Stress Rate        |\\n\\n<!--",
      "start": 42359,
      "end": 42387,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Buyer",
      "start": 42462,
      "end": 42467,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "150,000",
      "start": 42507,
      "end": 42514,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "220,000",
      "start": 42577,
      "end": 42584,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "25%",
      "start": 42587,
      "end": 42590,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 42591,
      "end": 42594,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "30,000",
      "start": 42622,
      "end": 42628,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Rental  Opex   Mortgage  Net CF   Equity",
      "start": 42867,
      "end": 42907,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "38.5k",
      "start": 42984,
      "end": 42989,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "39.8k",
      "start": 43033,
      "end": 43038,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "41.2k",
      "start": 43082,
      "end": 43087,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "+£23.7k",
      "start": 43116,
      "end": 43123,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "42.6k",
      "start": 43131,
      "end": 43136,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "5",
      "start": 43173,
      "end": 43174,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "+£77.7k\\n```\\n\\n## Investment Analysis",
      "start": 43226,
      "end": 43264,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "70%+",
      "start": 43560,
      "end": 43564,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.56%",
      "start": 43716,
      "end": 43721,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "250k+",
      "start": 43839,
      "end": 43844,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "B+",
      "start": 43876,
      "end": 43878,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 44233,
      "end": 44236,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Risk Assessment",
      "start": 44318,
      "end": 44336,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "-->\\n\\n| Risk Category",
      "start": 44484,
      "end": 44506,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Mitigation         |\\n|-----------------|----------------------|-----------------------------------------------------------|--------------------|\\n| Medium",
      "start": 44594,
      "end": 44749,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Price",
      "start": 44909,
      "end": 44914,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Rental               ",
      "start": 45136,
      "end": 45157,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Quality",
      "start": 45165,
      "end": 45172,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Tenant Risk        ",
      "start": 45219,
      "end": 45238,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Flood",
      "start": 45284,
      "end": 45289,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "EPC",
      "start": 45419,
      "end": 45422,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "30-40%",
      "start": 45934,
      "end": 45940,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5-10%",
      "start": 45956,
      "end": 45961,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "10%",
      "start": 46005,
      "end": 46008,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875k",
      "start": 46025,
      "end": 46029,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "787k",
      "start": 46033,
      "end": 46037,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "88k",
      "start": 46040,
      "end": 46043,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "YoY",
      "start": 46552,
      "end": 46555,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2023",
      "start": 46667,
      "end": 46671,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## 2",
      "start": 46728,
      "end": 46732,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "850k+",
      "start": 46814,
      "end": 46819,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "9",
      "start": 47040,
      "end": 47041,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "10-15%",
      "start": 47129,
      "end": 47135,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "8-12",
      "start": 47267,
      "end": 47271,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "/year",
      "start": 47277,
      "end": 47282,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2-3",
      "start": 47380,
      "end": 47383,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "15-20%",
      "start": 47505,
      "end": 47511,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "6/10 - Manageable",
      "start": 47918,
      "end": 47935,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "5%+",
      "start": 48069,
      "end": 48072,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2025",
      "start": 48285,
      "end": 48289,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Analysis:\\n\\n| Interest Rate",
      "start": 48311,
      "end": 48339,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "656k",
      "start": 48362,
      "end": 48366,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.15%",
      "start": 48492,
      "end": 48497,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,545",
      "start": 48511,
      "end": 48516,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5.15%",
      "start": 48575,
      "end": 48580,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,842",
      "start": 48594,
      "end": 48599,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "6.15%",
      "start": 48658,
      "end": 48663,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "4,155",
      "start": 48677,
      "end": 48682,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "/month",
      "start": 48718,
      "end": 48724,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "|\\n|",
      "start": 48736,
      "end": 48740,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "7.15%",
      "start": 48741,
      "end": 48746,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "4,485",
      "start": 48760,
      "end": 48765,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "/month",
      "start": 48801,
      "end": 48807,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "~10",
      "start": 48911,
      "end": 48914,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "15%",
      "start": 48915,
      "end": 48918,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "58%",
      "start": 48961,
      "end": 48964,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "8.15%",
      "start": 49185,
      "end": 49190,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Monitor BoE",
      "start": 49305,
      "end": 49316,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.75%",
      "start": 49392,
      "end": 49397,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.04.25%",
      "start": 49458,
      "end": 49466,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.5-5.5%",
      "start": 49510,
      "end": 49518,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## 4",
      "start": 49602,
      "end": 49606,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Tenant Risk LOW\\n\\n<!--",
      "start": 49608,
      "end": 49631,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5-8%",
      "start": 49910,
      "end": 49914,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "10%",
      "start": 50234,
      "end": 50237,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "10-15",
      "start": 50497,
      "end": 50502,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Highclere/Newbury",
      "start": 50525,
      "end": 50542,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## 5",
      "start": 50748,
      "end": 50752,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "EPC",
      "start": 51399,
      "end": 51402,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "15",
      "start": 51449,
      "end": 51451,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "- Monitor Environment Agency",
      "start": 51465,
      "end": 51493,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## 6",
      "start": 51562,
      "end": 51566,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "24-28%",
      "start": 51883,
      "end": 51889,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "EPC",
      "start": 52012,
      "end": 52015,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Crating",
      "start": 52076,
      "end": 52083,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2028",
      "start": 52094,
      "end": 52098,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "LAW",
      "text": "Section 21",
      "start": 52168,
      "end": 52178,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "500",
      "start": 52271,
      "end": 52274,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Budget for EPC",
      "start": 52594,
      "end": 52608,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "20k",
      "start": 52624,
      "end": 52627,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## 7",
      "start": 52831,
      "end": 52835,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Context",
      "start": 53022,
      "end": 53029,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "+1.0%",
      "start": 53064,
      "end": 53069,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.5-3.0%",
      "start": 53093,
      "end": 53101,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.3%",
      "start": 53133,
      "end": 53137,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "AWE Aldermaston",
      "start": 53274,
      "end": 53289,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "68k",
      "start": 53357,
      "end": 53360,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "20%",
      "start": 53485,
      "end": 53488,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Mild Recession",
      "start": 53812,
      "end": 53826,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-10% to -15%",
      "start": 53868,
      "end": 53880,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Moderate Recession",
      "start": 53894,
      "end": 53912,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-15%",
      "start": 53928,
      "end": 53932,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-15%",
      "start": 53950,
      "end": 53954,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Severe Recession",
      "start": 53976,
      "end": 53992,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "|\\n\\nHistorical Resilience",
      "start": 54005,
      "end": 54031,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2009",
      "start": 54040,
      "end": 54044,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-12%",
      "start": 54083,
      "end": 54087,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "-18%",
      "start": 54092,
      "end": 54096,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 54355,
      "end": 54358,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "view)\\n\\n<!--",
      "start": 54482,
      "end": 54495,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Radar",
      "start": 54514,
      "end": 54519,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Overall Risk",
      "start": 54601,
      "end": 54616,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "horizon - Adequate",
      "start": 55306,
      "end": 55324,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "B+",
      "start": 55600,
      "end": 55602,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "##",
      "start": 55612,
      "end": 55614,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "one",
      "start": 55713,
      "end": 55716,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,402",
      "start": 55905,
      "end": 55910,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury",
      "start": 56115,
      "end": 56122,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 56123,
      "end": 56130,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "M4/M3",
      "start": 56132,
      "end": 56137,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 56202,
      "end": 56209,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "725k-£925k",
      "start": 56244,
      "end": 56254,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "364",
      "start": 56263,
      "end": 56266,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "72%",
      "start": 56330,
      "end": 56333,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1",
      "start": 56760,
      "end": 56761,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Key",
      "start": 56942,
      "end": 56948,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "Year 1-3 Highly",
      "start": 57096,
      "end": 57111,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 57138,
      "end": 57141,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "NORP",
      "text": "Urban",
      "start": 57173,
      "end": 57178,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "5-10+ years",
      "start": 57300,
      "end": 57311,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Owner",
      "start": 57341,
      "end": 57346,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Families",
      "start": 57498,
      "end": 57506,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "10-Year",
      "start": 57651,
      "end": 57658,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 57743,
      "end": 57750,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "1,120,000",
      "start": 57765,
      "end": 57774,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "22,370",
      "start": 57808,
      "end": 57814,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "26,500",
      "start": 57819,
      "end": 57825,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "32,000",
      "start": 57830,
      "end": 57836,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "670,000",
      "start": 57895,
      "end": 57902,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Cumulative Return",
      "start": 57976,
      "end": 57993,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.25%",
      "start": 58030,
      "end": 58035,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.56%",
      "start": 58071,
      "end": 58076,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "56.5%",
      "start": 58121,
      "end": 58126,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "11.3%",
      "start": 58128,
      "end": 58133,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "168%",
      "start": 58161,
      "end": 58165,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "10.4%",
      "start": 58178,
      "end": 58183,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2025",
      "start": 58266,
      "end": 58270,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2026):\\n\\n<!--",
      "start": 58276,
      "end": 58290,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5.15%",
      "start": 58399,
      "end": 58404,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "4.5-4.75%",
      "start": 58407,
      "end": 58416,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "15%",
      "start": 58454,
      "end": 58457,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2025",
      "start": 58623,
      "end": 58627,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3-5%",
      "start": 58834,
      "end": 58838,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "+£5-10k",
      "start": 59005,
      "end": 59012,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,402",
      "start": 59477,
      "end": 59482,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,000-2,200",
      "start": 59515,
      "end": 59526,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Property Size         |\\n|",
      "start": 59544,
      "end": 59570,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "364",
      "start": 59666,
      "end": 59669,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "340",
      "start": 59704,
      "end": 59707,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "|\\n|",
      "start": 59754,
      "end": 59758,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Environmental Quality",
      "start": 59826,
      "end": 59847,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "|\\n|",
      "start": 59848,
      "end": 59852,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury",
      "start": 59854,
      "end": 59861,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "6 miles",
      "start": 59862,
      "end": 59869,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Downton Abbey",
      "start": 59993,
      "end": 60006,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,402",
      "start": 60117,
      "end": 60122,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "sqft",
      "start": 60123,
      "end": 60127,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,100",
      "start": 60131,
      "end": 60136,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "sqft",
      "start": 60137,
      "end": 60141,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## Action Plan",
      "start": 60171,
      "end": 60185,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Property Inspection &amp",
      "start": 60259,
      "end": 60283,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "1,200",
      "start": 60345,
      "end": 60350,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Request EPC",
      "start": 60364,
      "end": 60375,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Legal &amp",
      "start": 60542,
      "end": 60552,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Title Checks - [",
      "start": 60554,
      "end": 60570,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "2,500",
      "start": 60618,
      "end": 60623,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Financial Planning - [",
      "start": 60863,
      "end": 60885,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "WORK_OF_ART",
      "text": "Obtain mortgage Agreement in Principle",
      "start": 60888,
      "end": 60926,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "75%",
      "start": 60928,
      "end": 60931,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 60932,
      "end": 60935,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "41,250",
      "start": 60975,
      "end": 60981,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "51,250",
      "start": 61000,
      "end": 61006,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Reserve",
      "start": 61036,
      "end": 61043,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Location &amp",
      "start": 61166,
      "end": 61179,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury, Basingstoke, Reading",
      "start": 61390,
      "end": 61419,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "HM Land Registry",
      "start": 61510,
      "end": 61526,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "850,000-£860,000",
      "start": 61588,
      "end": 61604,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3-5%",
      "start": 61616,
      "end": 61620,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875k+",
      "start": 61649,
      "end": 61654,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "Agree",
      "start": 61760,
      "end": 61765,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "25%+",
      "start": 62106,
      "end": 62110,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV",
      "start": 62111,
      "end": 62114,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "B+",
      "start": 62506,
      "end": 62508,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Strong Buy",
      "start": 62510,
      "end": 62520,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "78%\\n\\n## Contact &amp",
      "start": 62571,
      "end": 62593,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Next Steps\\n\\nFor Further Information: -HM Land Registry",
      "start": 62595,
      "end": 62651,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Deane Planning",
      "start": 62715,
      "end": 62729,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "WORK_OF_ART",
      "text": "North Wessex Downs",
      "start": 62780,
      "end": 62798,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Strutt &",
      "start": 62905,
      "end": 62913,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Sale Date",
      "start": 63285,
      "end": 63294,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Distance",
      "start": 63339,
      "end": 63347,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "885,000",
      "start": 63588,
      "end": 63595,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "377",
      "start": 63617,
      "end": 63620,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.6 mi     ",
      "start": 63627,
      "end": 63638,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "0%",
      "start": 63640,
      "end": 63642,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "885,000",
      "start": 63650,
      "end": 63657,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Grotto Cottage",
      "start": 63686,
      "end": 63700,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2024",
      "start": 63721,
      "end": 63725,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "725,000",
      "start": 63732,
      "end": 63739,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "345",
      "start": 63761,
      "end": 63764,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2.1",
      "start": 63771,
      "end": 63774,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2024",
      "start": 63865,
      "end": 63869,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "795,000",
      "start": 63876,
      "end": 63883,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3 | 2,000  | £",
      "start": 63891,
      "end": 63905,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "398",
      "start": 63905,
      "end": 63908,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.3 mi     ",
      "start": 63915,
      "end": 63926,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "818,850",
      "start": 63938,
      "end": 63945,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "356",
      "start": 64049,
      "end": 64052,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "0.8 mi     ",
      "start": 64059,
      "end": 64070,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "971,250",
      "start": 64082,
      "end": 64089,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "815,000",
      "start": 64164,
      "end": 64171,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "362",
      "start": 64193,
      "end": 64196,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2.5",
      "start": 64203,
      "end": 64206,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "774,250",
      "start": 64226,
      "end": 64233,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "815,000",
      "start": 64308,
      "end": 64315,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "362",
      "start": 64337,
      "end": 64340,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "818,850",
      "start": 64370,
      "end": 64377,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "2,402",
      "start": 64436,
      "end": 64441,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "362",
      "start": 64465,
      "end": 64468,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "2,402 × £362",
      "start": 64487,
      "end": 64499,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "£875,000\\n\\n##",
      "start": 64567,
      "end": 64581,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Source/Rationale                             |\\n|----------------------------|----------------|----------------------------------------------|\\n|",
      "start": 64667,
      "end": 64812,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 64843,
      "end": 64850,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "25%",
      "start": 64938,
      "end": 64941,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "218,750",
      "start": 64944,
      "end": 64951,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV         |\\n|",
      "start": 64988,
      "end": 65004,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "656,250",
      "start": 65035,
      "end": 65042,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "75%",
      "start": 65060,
      "end": 65063,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV                             |\\n|",
      "start": 65064,
      "end": 65100,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5.15%",
      "start": 65130,
      "end": 65135,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "|\\n|                            | £",
      "start": 65288,
      "end": 65323,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "999",
      "start": 65323,
      "end": 65326,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "37,200",
      "start": 65419,
      "end": 65425,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "3,100/month",
      "start": 65443,
      "end": 65454,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3.5%",
      "start": 65514,
      "end": 65518,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "10%",
      "start": 65610,
      "end": 65613,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1",
      "start": 65658,
      "end": 65659,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Maintenance                |",
      "start": 65677,
      "end": 65705,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "1%",
      "start": 65706,
      "end": 65708,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "8,750",
      "start": 65746,
      "end": 65751,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "1",
      "start": 65757,
      "end": 65758,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Buildings & contents",
      "start": 65819,
      "end": 65839,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5%",
      "start": 65898,
      "end": 65900,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "0.6 months/year",
      "start": 65915,
      "end": 65930,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "1,860",
      "start": 65933,
      "end": 65938,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "Year 1",
      "start": 65939,
      "end": 65945,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "2.5%",
      "start": 65994,
      "end": 65998,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "41,250",
      "start": 66091,
      "end": 66097,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5%",
      "start": 66107,
      "end": 66109,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875k",
      "start": 66114,
      "end": 66118,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "51,250",
      "start": 66187,
      "end": 66193,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "8%",
      "start": 66203,
      "end": 66205,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875k",
      "start": 66210,
      "end": 66214,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORDINAL",
      "text": "second",
      "start": 66225,
      "end": 66231,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "1,200-£1,500",
      "start": 66379,
      "end": 66391,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Standard Rate",
      "start": 66474,
      "end": 66487,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Rate",
      "start": 66547,
      "end": 66551,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "0 - £250,000",
      "start": 66634,
      "end": 66646,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "250,000",
      "start": 66656,
      "end": 66663,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "0%",
      "start": 66669,
      "end": 66671,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "250,001 - £925,000 | £625,000",
      "start": 66695,
      "end": 66724,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5%",
      "start": 66730,
      "end": 66732,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "31,250",
      "start": 66740,
      "end": 66746,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 66778,
      "end": 66785,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "31,250",
      "start": 66801,
      "end": 66807,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Property Supplement",
      "start": 66889,
      "end": 66908,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Rate",
      "start": 66957,
      "end": 66961,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "0 - £250,000",
      "start": 67044,
      "end": 67056,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "250,000",
      "start": 67066,
      "end": 67073,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "3%",
      "start": 67079,
      "end": 67081,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "7,500",
      "start": 67089,
      "end": 67094,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "250,001 - £925,000 | £625,000",
      "start": 67105,
      "end": 67134,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "8%",
      "start": 67140,
      "end": 67142,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "50,000",
      "start": 67150,
      "end": 67156,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 67188,
      "end": 67195,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "57,500",
      "start": 67211,
      "end": 67217,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "|\\n\\nFirst-Time Buyer",
      "start": 67221,
      "end": 67242,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## D. Mortgage",
      "start": 67309,
      "end": 67323,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "Year 1)\\n\\nLoan",
      "start": 67342,
      "end": 67357,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "656,250",
      "start": 67381,
      "end": 67388,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "5.15%",
      "start": 67406,
      "end": 67411,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Capital &amp",
      "start": 67468,
      "end": 67480,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Breakdown",
      "start": 67525,
      "end": 67534,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "Year 1 average):\\n\\n| Component",
      "start": 67536,
      "end": 67567,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "2,817",
      "start": 67659,
      "end": 67664,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "33,807",
      "start": 67671,
      "end": 67677,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "1,025",
      "start": 67701,
      "end": 67706,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "12,297",
      "start": 67713,
      "end": 67719,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "3,842",
      "start": 67743,
      "end": 67748,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "46,104",
      "start": 67755,
      "end": 67761,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Principal Paid",
      "start": 67845,
      "end": 67859,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Closing Balance",
      "start": 67864,
      "end": 67879,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "1 | £",
      "start": 67981,
      "end": 67986,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "656,250",
      "start": 67986,
      "end": 67993,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "12,297",
      "start": 68024,
      "end": 68030,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "643,953",
      "start": 68043,
      "end": 68050,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "5 | £",
      "start": 68070,
      "end": 68075,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "599,438",
      "start": 68075,
      "end": 68082,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "30,854",
      "start": 68095,
      "end": 68101,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "15,250",
      "start": 68113,
      "end": 68119,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "584,188",
      "start": 68132,
      "end": 68139,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "10 | £",
      "start": 68158,
      "end": 68164,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "518,742",
      "start": 68164,
      "end": 68171,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "19,413",
      "start": 68202,
      "end": 68208,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "499,329",
      "start": 68221,
      "end": 68228,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "25 | £45,263",
      "start": 68247,
      "end": 68259,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "2,331",
      "start": 68273,
      "end": 68278,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "43,773",
      "start": 68291,
      "end": 68297,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "E. Data Sources &amp",
      "start": 68335,
      "end": 68355,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Paid Data",
      "start": 68413,
      "end": 68422,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Burghclere",
      "start": 68478,
      "end": 68488,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "QUANTITY",
      "text": "3-mile",
      "start": 68490,
      "end": 68496,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Knight Frank",
      "start": 68553,
      "end": 68565,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "VOA Private Rental Market Statistics\\n\\nDemographics: - ONS Census",
      "start": 68714,
      "end": 68780,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Basingstoke &",
      "start": 68805,
      "end": 68818,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2023",
      "start": 68883,
      "end": 68887,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "9",
      "start": 69009,
      "end": 69010,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Hampshire Constabulary Community Safety Partnership",
      "start": 69030,
      "end": 69081,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "GCSE",
      "start": 69178,
      "end": 69182,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Highclere CE Primary",
      "start": 69232,
      "end": 69252,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "St. Bart's",
      "start": 69265,
      "end": 69275,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2024",
      "start": 69333,
      "end": 69337,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2024",
      "start": 69371,
      "end": 69375,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "House",
      "start": 69474,
      "end": 69479,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "HM Land Registry",
      "start": 69493,
      "end": 69509,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "ONS",
      "start": 69511,
      "end": 69514,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "Moneyfacts, Jan 2025",
      "start": 69637,
      "end": 69657,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Deane Borough Council Planning Portal - HM Land Registry",
      "start": 69689,
      "end": 69745,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Estimates &",
      "start": 70147,
      "end": 70158,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "72%",
      "start": 70493,
      "end": 70496,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "HM Land Registry",
      "start": 70550,
      "end": 70566,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "FAC",
      "text": "Tekniti AI",
      "start": 70817,
      "end": 70827,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "AVM         |\\n|",
      "start": 71082,
      "end": 71098,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Cap Rate",
      "start": 71116,
      "end": 71124,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "EPC         |\\n|",
      "start": 71133,
      "end": 71149,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "HPI         |\\n|",
      "start": 71167,
      "end": 71183,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "LTV         |\\n| Net",
      "start": 71184,
      "end": 71204,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "|\\n|",
      "start": 71213,
      "end": 71217,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "RICS        |\\n|",
      "start": 71235,
      "end": 71251,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "|\\n\\n",
      "start": 71281,
      "end": 71286,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Property Viewing &amp",
      "start": 71319,
      "end": 71340,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Purchase Enquiries:",
      "start": 71342,
      "end": 71361,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Highclere/Newbury",
      "start": 71406,
      "end": 71423,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Savills Newbury",
      "start": 71442,
      "end": 71457,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "01635",
      "start": 71459,
      "end": 71464,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Knight Frank Newbury",
      "start": 71472,
      "end": 71492,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "01635",
      "start": 71494,
      "end": 71499,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Strutt &amp",
      "start": 71507,
      "end": 71518,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "01635",
      "start": 71536,
      "end": 71541,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "521707\\n\\nFor Mortgage Advice",
      "start": 71542,
      "end": 71571,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "London &",
      "start": 71641,
      "end": 71649,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "0800",
      "start": 71663,
      "end": 71667,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Habito",
      "start": 71675,
      "end": 71681,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury/Basingstokebased advisors\\n\\nFor",
      "start": 71730,
      "end": 71770,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "0118 9589191",
      "start": 71887,
      "end": 71899,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Hampshire/West Berkshire: Homewise Surveying",
      "start": 72011,
      "end": 72055,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Newbury",
      "start": 72057,
      "end": 72064,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "01635",
      "start": 72067,
      "end": 72072,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Stocker &",
      "start": 72080,
      "end": 72089,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Partners (Basingstoke",
      "start": 72094,
      "end": 72115,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "01256",
      "start": 72118,
      "end": 72123,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "## I. Report Version &amp",
      "start": 72134,
      "end": 72159,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "AVM-RG209PF-20250129                     ",
      "start": 72314,
      "end": 72355,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "UPRN",
      "start": 72434,
      "end": 72438,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "|\\n| 29 January 2025",
      "start": 72445,
      "end": 72465,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PRODUCT",
      "text": "Version      |\\n|",
      "start": 72568,
      "end": 72585,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "AI -",
      "start": 72593,
      "end": 72597,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Tekniti             |\\n| Valid",
      "start": 72629,
      "end": 72659,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Review Date         |\\n|",
      "start": 72697,
      "end": 72721,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Next Review",
      "start": 72722,
      "end": 72733,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "28-29",
      "start": 72821,
      "end": 72826,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "January 2025 - Comparable",
      "start": 72827,
      "end": 72852,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "5",
      "start": 72869,
      "end": 72870,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "CARDINAL",
      "text": "5",
      "start": 72928,
      "end": 72929,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "ONS Census",
      "start": 72981,
      "end": 72991,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2021 +",
      "start": 72992,
      "end": 72998,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "2023",
      "start": 73004,
      "end": 73008,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "12 months to November 2024 - School",
      "start": 73023,
      "end": 73058,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Ofsted/DfE",
      "start": 73065,
      "end": 73075,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "2024)\\n\\n## End",
      "start": 73094,
      "end": 73109,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "875,000",
      "start": 73221,
      "end": 73228,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "825k",
      "start": 73238,
      "end": 73242,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "MONEY",
      "text": "925k",
      "start": 73246,
      "end": 73250,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "BUY",
      "start": 73268,
      "end": 73271,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERSON",
      "text": "Grade B+",
      "start": 73273,
      "end": 73281,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "PERCENT",
      "text": "72%",
      "start": 73296,
      "end": 73299,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "MediumHigh",
      "start": 73301,
      "end": 73311,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "DATE",
      "text": "5-10+ years",
      "start": 73333,
      "end": 73344,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "GPE",
      "text": "Hampshire village",
      "start": 73468,
      "end": 73485,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "ORG",
      "text": "Tekniti AI",
      "start": 73728,
      "end": 73738,
      "score": null,
      "source": "spacy"
    },
    {
      "type": "FAC",
      "text": "Tekniti AI - UK Real Estate Analytics",
      "start": 73877,
      "end": 73914,
      "score": null,
      "source": "spacy"
    }

"""

count = count_closing_braces(sample_text)
print(f"Number of '}}' in text: {count}")
