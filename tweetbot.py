from concurrent.futures import thread
import tweepy
import time
import random


def get_lines(file_name, times):
    file = open(f"resources/files/{file_name}.txt", "r")
    text_block = file.read()
    all_lines = []
    all_lines = text_block.split('\n')
    file.close()
    final_lines = []
    for x in range(0, times):
        found_line = " "
        while found_line == " ":
            random_index = random.randint(0, len(all_lines) - 1)
            found_line = all_lines[random_index]
        final_lines.append(found_line)
        all_lines.pop(random_index)

    return final_lines


def batch_delete():
    print("Deleting all tweets from the account @%s." % api.verify_credentials().screen_name)
    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            # api.destroy_status(status.id)
            # print "Deleted:", status.id
            api.destroy_status(status.id)
        except:
            print("Failed to delete:", status.id)


def insert_beeps(beep_quantity, line):
    beeps = [" ..beep..", " ..boop.."]

    empty_spaces = []
    while len(empty_spaces) < beep_quantity:
        r = random.randint(0, len(line) - 1)
        if line[r] == ' ':
            empty_spaces.append(r)
    placed_beeps = 0
    for i in empty_spaces:
        if line[i] == ' ':
            line = line[:i] + beeps[random.randint(0, 1)] + line[i:]
            placed_beeps += 1
    if placed_beeps <= 0:
        line = line + beeps[random.randint(0, 1)]
    return line


CONSUMER_KEY = 'yDRjfJEW3cDPnEZN2HjMMO6xx'
CONSUMER_SECRET = 'VxOcmD1MBrWFehxas0S7N7IayqLKxwOiYxHPwcG3QpZego1qES'
ACCESS_KEY = '611329476-Ivi8Kl83lp8ZqPzaR4fAAhU9qpZNXOpzPFFlPhRn'
ACCESS_SECRET = '31SLhrMDY0QuKjDqaCnY176Oh4X0pDtOSp7LYmguUbPct'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
try:
    api.verify_credentials()
except Exception as e:
    print("ERROR")
    raise e

while True:
    # print(all_tweets[i])
    event_duration = random.randint(2, 4)
    print("New event with " + str(event_duration + 1) + " tweets.")
    detectors = get_lines("detectors", event_duration)
    adjectives = get_lines("adjectives", event_duration)
    places = get_lines("places", event_duration)
    celestial_bodies = get_lines("celestialBodies", event_duration)
    lines_put_together = []
    for x in range(0, event_duration):
        lines_put_together.append(detectors[x] + " " + adjectives[x] + " " + places[x] + " on the " + celestial_bodies[0])
    api.update_status(lines_put_together[0])
    time.sleep(15)
