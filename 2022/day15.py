from utils.utils import readlines

FILENAME = 'data/day15.txt'


def manhatten_distance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def parse_location(s):
    x_str, y_str = s.split(',')

    return int(x_str[2:]), int(y_str[2:])


class Sensor:
    def __init__(self, sensor_loc, beacon_loc):
        self.sensor_loc = sensor_loc
        self.beacon_loc = beacon_loc

        self.max_distance = manhatten_distance(sensor_loc, beacon_loc)

    def reach(self, location):
        return manhatten_distance(self.sensor_loc, location) <= self.max_distance

    def reachable_locations_on_row(self, row):
        col_loc = self.sensor_loc[0]

        distance_to_row = manhatten_distance(self.sensor_loc, (col_loc, row))
        slack = self.max_distance - distance_to_row

        if slack >= 0:
            return Interval(col_loc - slack, col_loc + slack)

        return Empty()


class Map:
    def __init__(self, sensors):
        self.sensors = sensors

        self.sensor_locations = set([s.sensor_loc for s in sensors])
        self.beacon_locations = set([s.beacon_loc for s in sensors])

        self.occupied_locations = self.sensor_locations.union(self.beacon_locations)

    def reachable_locations_on_row(self, row):
        reachable_locations = Empty()
        for sensor in self.sensors:
            interval = sensor.reachable_locations_on_row(row)
            reachable_locations = reachable_locations.union(interval)

        return reachable_locations


class Interval:
    def __init__(self, start, end):
        assert start <= end

        self.start = start
        self.end = end

    def union(self, interval):
        if isinstance(interval, Empty):
            return self

        min_start, max_start = sorted([self.start, interval.start])
        min_end, max_end = sorted([self.end, interval.end])

        if max_start <= min_end:
            return Interval(min_start, max_end)
        return DisjointInterval([self, interval], simplify=False)

    def __len__(self):
        return self.end - self.start + 1

    def contains(self, interval):
        return self.start <= interval.start and self.end >= interval.end


class Empty:
    def __init__(self):
        self.start = None
        self.end = None

    def __len__(self):
        return 0

    def union(self, interval):
        return interval

    def contains(self, interval):
        return False


class DisjointInterval:
    def __init__(self, intervals, simplify=True):
        if simplify:
            self.intervals = self._simplify_intervals(intervals)
        else:
            self.intervals = intervals

    @staticmethod
    def _simplify_intervals(intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        final_intervals = []

        working_interval = sorted_intervals[0]
        for interval in sorted_intervals[1:]:
            combined_interval = working_interval.union(interval)

            if isinstance(combined_interval, DisjointInterval):
                final_intervals.append(combined_interval.intervals[0])

                working_interval = combined_interval.intervals[1]
            else:
                working_interval = combined_interval
        final_intervals.append(working_interval)

        return final_intervals

    def __len__(self):
        return sum([len(interval) for interval in self.intervals])

    def union(self, interval):
        if isinstance(interval, Empty):
            return self

        elif isinstance(interval, Interval):
            return DisjointInterval(self.intervals + [interval])

        return DisjointInterval(self.intervals + interval.intervals)

    def contains(self, interval):
        return any([i.contains(interval) for i in self.intervals])


def part1():
    lines = readlines(FILENAME)

    sensors = []

    for line in lines:
        cleaned_line = line.replace('\n', '')
        cleaned_line = cleaned_line.replace(' ', '')

        sensor_str, beacon_str = cleaned_line.split(':')

        sensor_loc = parse_location(sensor_str[8:])
        beacon_loc = parse_location(beacon_str[17:])

        sensors.append(Sensor(sensor_loc, beacon_loc))

    row = 2000000

    map_ = Map(sensors)
    reachable_locations = map_.reachable_locations_on_row(row)

    occupied_locations = 0
    unique_beacons = set([sensor.beacon_loc for sensor in map_.sensors])

    for beacon in unique_beacons:
        beacon_col, beacon_row = beacon
        if beacon_row == row:
            interval = Interval(beacon_col, beacon_col)
            occupied_locations += reachable_locations.contains(interval)

    return len(reachable_locations) - occupied_locations


def part2():
    lines = readlines(FILENAME)
    return None


if __name__ == '__main__':
    print("Advent of Code 2022 Day 13")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
