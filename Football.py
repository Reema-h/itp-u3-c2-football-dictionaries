def convert_lists_to_dicts(players):
    player_dicts = []
    for player in players:
        player_dict = {
            'number': player[0],
            'position': player[1],
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8]
        }
        player_dicts.append(player_dict)
    return player_dicts


def group_by_pos(players):
    player_dict = {}
    for item in players:
        position = item['position']
        if position not in player_dict:
            player_dict[position] = []
        player_dict[position].append(item)
    return player_dict


def group_by_country(players):
    country_dict = {}

    for item in players:
        country = item['country']
        position = item['position']

        if country not in country_dict:
            country_dict[country] = {}
        if position not in country_dict[country]:
            country_dict[country][position] = []

        country_dict[country][position].append(item)

    return country_dict


if __name__ == '__main__':

    SQUADS_DATA = [
      [
        "1",                                     # Number
        "GK",                                    # Position
        "Juan Botasso",                          # Name
        "(1908-10-23)23 October 1908 (aged 21)", # Date of Birth
        "",                                      # Caps
        "Quilmes",                               # Club
        "Argentina",                             # Country (Players Country)
        "Argentina",                             # Club Country
        "1930"                                   # Year
      ],
      [
        "9",
        "FW",
        "Roberto Cherro",
        "(1907-02-23)23 February 1907 (aged 23)",
        "",
        "Boca Juniors",
        "Argentina",
        "Argentina",
        "1930"
      ]
      # More Players...
    ]
    list_to_dict = convert_lists_to_dicts(SQUADS_DATA)

    group_pos = group_by_pos(list_to_dict)

    group_country = group_by_country(list_to_dict)

    print("------Assignment 1---------")
    print(list_to_dict)
    print("\n------Assignment 2---------")
    print(group_pos)
    print("\n------Assignment 3---------")
    print(group_country)