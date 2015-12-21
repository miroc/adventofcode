#!/usr/bin/env python
from collections import defaultdict

speeds = {}


def distances_in_time(time_seconds):
    distances = {}
    for reindeer in speeds:
        period_duration = speeds[reindeer]["fly_time"] + speeds[reindeer]["rest_time"]
        total_period_counts = time_seconds // period_duration

        leftover = time_seconds - total_period_counts * period_duration
        leftover_fly_duration = min(speeds[reindeer]["fly_time"], leftover)

        distance = total_period_counts * speeds[reindeer]["fly_speed"] * speeds[reindeer]["fly_time"]
        distance += leftover_fly_duration * speeds[reindeer]["fly_speed"]
        distances[reindeer] = distance
    return distances


def competition():
    duration = 2503

    dists1 = distances_in_time(duration)
    print("1. task:", max(dists1.values()))

    extra_points = defaultdict(lambda: 0)
    #
    for sec in range(1, duration + 1):
        distances = distances_in_time(sec)
        max_val = max(distances.values())
        round_winners = [name for name in distances if distances[name] == max_val]
        for round_winner in round_winners:
            extra_points[round_winner] += 1

    print("2. task:", max(extra_points.values()))


def main():
    with open("day_14_input") as f:
        lines = f.readlines()
        for line in lines:
            words = line.strip().split()
            name, fly_speed, fly_time, rest_time = words[0], words[3], words[6], words[-2]
            speeds[name] = {"fly_speed": int(fly_speed), "fly_time": int(fly_time), "rest_time": int(rest_time)}
        competition()


if __name__ == '__main__':
    main()
