hotels = [
    {'title': '5-звездочные отели', 'id': 1},
    {'title': '4-звездочные отели', 'id': 2},
    {'title': '3-звездочные отели', 'id': 3},
    {'title': '2-звездочные отели', 'id': 4}
    ]


hotels_dict = {val.get('id'): val for val in hotels}
