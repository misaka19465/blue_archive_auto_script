stage_data = {
    '17-1-sss-present-task': {
        'start': {
            'burst1': (264, 101),
            'pierce1': (828, 388),
        },
        'action': [
            {'t': 'click', 'p': (578, 405), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (725, 482), 'ec': True, 'wait-over': True, 'desc': "2 lower left"},

            {'t': 'click', 'p': (602, 485), 'ec': True, 'desc': "1 lower right"},
            {'t': 'click', 'p': (780, 573), 'ec': True, 'wait-over': True, 'desc': "2 lower right"},

            {'t': 'click', 'p': (480, 491), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (822, 545), 'ec': True, 'wait-over': True, 'desc': "2 lower right"},

            {'t': 'exchange_and_click', 'p': (822, 542), 'wait-over': True, 'desc': "2 right left"},
            {'t': 'click', 'p': (449, 435), 'desc': "2 lower left"},
        ]
    },
    '17-2-sss-present-task': {
        'start': {
            'burst1': (434, 139),
            'pierce1': (729, 364),
        },
        'action': [
            {'t': 'click', 'p': (455, 415), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (681, 502), 'ec': True, 'wait-over': True, 'desc': "2 lower left"},

            {'t': 'click', 'p': (439, 496), 'ec': True, 'desc': "1 lower left"},
            {'t': 'click', 'p': (704, 546), 'ec': True, 'wait-over': True, 'desc': "2 lower left"},

            {'t': 'click', 'p': (564, 433), 'ec': True, 'desc': "1 lower right"},
            {'t': 'choose_and_change', 'p': (564, 433), 'desc': "swap 1 2"},
            {'t': 'click', 'p': (500, 517), 'ec': True, 'wait-over': True, 'desc': "2 lower left"},

            {'t': 'exchange_and_click', 'p': (592, 561), 'ec': True, 'desc': "2 lower right"},
            {'t': 'click', 'p': (851, 300), 'wait-over': True, 'desc': "1 right"},

            {'t': 'exchange_and_click', 'p': (607, 568), 'wait-over': True, 'desc': "2 lower right"},
            {'t': 'click', 'p': (788, 382), 'desc': "1 lower right"},
        ]
    },
    '17-3-sss-present-task': {
        'start': {
            'burst1': (455, 517),
            'pierce1': (782, 454),
            'burst2': (1064, 529),
        },
        'action': [
            {'t': 'exchange_twice_and_click', 'p': (722, 336), 'ec': True, 'desc': "3 upper left"},
            {'t': 'click', 'p': (439, 285), 'ec': True, 'desc': "1 upper left"},
            {'t': 'click', 'p': (728, 318), 'ec': True, 'wait-over': True, 'desc': "2 upper left"},

            {'t': 'click', 'p': (738, 374), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (722, 339), 'ec': True, 'desc': "2 upper left"},
            {'t': 'click', 'p': (839, 342), 'ec': True, 'wait-over': True, 'desc': "3 upper right"},

            {'t': 'exchange_and_click', 'p': (672, 238), 'ec': True, 'desc': "2 upper left"},
            {'t': 'exchange_twice_and_click', 'p': (726, 321), 'wait-over': True, 'desc': "3 upper left"},
            {'t': 'choose_and_change', 'p': (559, 279), 'desc': "swap 1 2"},
            {'t': 'click', 'p': (523, 200), 'wait-over': True, 'desc': "1 upper left left"},

            {'t': 'click', 'p': (576, 249), 'ec': True, 'desc': "1 upper right"},
            {'t': 'click', 'p': (454, 416), 'ec': True, 'desc': "2 lower left"},
            {'t': 'click', 'p': (710, 357), 'ec': True, 'wait-over': True, 'desc': "3 upper left"},

            {'t': 'exchange_and_click', 'p': (547, 591), 'ec': True, 'desc': "2 lower left"},
            {'t': 'exchange_twice_and_click', 'p': (666, 401), 'ec': True, 'desc': "3 left"},
            {'t': 'click', 'p': (514, 205), 'desc': "1 upper left"},
        ]
    },
}
