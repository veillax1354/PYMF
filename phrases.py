
#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import datetime, json, random, pytz, os

def compliment(tz):
    part = get_part_of_day(datetime.datetime.now(pytz.timezone(tz)).hour)
    if random.randint(1, 5) == 5:
        part = "anytime"
        with open(os.getcwd() + '/phrases.json') as phrases:
            data = json.load(phrases)
            c_list = data[part]
            n = random.randint(0, len(c_list) - 1)
            compliment = c_list[n]
            return compliment

def get_part_of_day(h):
    return (
        "morning" if 5 <= h <= 11
        else "afternoon" if 12 <= h <= 17
        else "evening" if 18 <= h <= 22
        else "night"
    )

if __name__ == "__main__":
    for hour in range(0, 24):
        part = get_part_of_day(hour)
        print(f"hour {hour} is {part}")
