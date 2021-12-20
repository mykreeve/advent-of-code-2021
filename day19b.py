#!/usr/bin/env python3

import pathlib
import sys

from collections import defaultdict
from functools import total_ordering
from typing import List, Tuple

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / 'lib'))


@total_ordering
class Beacon:
    def __init__(self, ident: int, x: int, y: int, z: int) -> None:
        self.id = ident
        self.x, self.y, self.z = x, y, z

    def __str__(self) -> str:
        return f'{self.x},{self.y},{self.z}'

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        if self.x != other.x:
            return self.x < other.x

        if self.y != other.y:
            return self.y < other.y

        return self.z < other.z

    def coords(self) -> Tuple[int, int, int]:
        return self.x, self.y, self.z

    def delta(self, other) -> Tuple[int, int, int]:
        if self > other:
            self, other = other, self
        return other.x - self.x, other.y - self.y, other.z - self.z


class Scanner:
    def __init__(self, ident: int) -> None:
        self.id = ident
        self.beacons = []
        self.rotated = None
        self.distances = defaultdict(list)

    def __str__(self) -> str:
        return f'--- scanner {self.id} ---' + "".join(f"\n{beacon}" for beacon in self.beacons)

    def add_beacon(self, beacon: Beacon) -> None:
        for b in self.beacons:
            self.distances[b.delta(beacon)].append(
                (b, beacon) if b < beacon else (beacon, b))
        self.beacons.append(beacon)

    def rotations(self) -> List['Scanner']:
        if self.rotated:
            return self.rotated

        self.rotated = []
        scanner = self
        beacons = [Beacon(b.id, b.x, b.y, b.z) for b in self.beacons]

        for x_rot in range(2):
            for y_rot in range(4):
                for z_rot in range(4):
                    self.rotated.append(scanner)
                    scanner = Scanner(self.id)

                    for b in beacons:
                        b.x, b.y = b.y, -b.x
                        scanner.add_beacon(Beacon(b.id, b.x, b.y, b.z))

                for b in beacons:
                    b.x, b.z = b.z, -b.x

            for b in beacons:
                b.y, b.z = b.z, -b.y

        return self.rotated

    def find_overlapping(self, other: 'Scanner') -> Tuple[List[Tuple[Beacon]], 'Scanner']:
        for s in other.rotations():
            matching_beacons = {}
            for (dx, dy, dz) in self.distances.keys():
                if (dx, dy, dz) in s.distances:
                    for pair1, pair2 in zip(self.distances[dx, dy, dz], s.distances[dx, dy, dz]):
                        if pair1[0].coords() not in matching_beacons:
                            matching_beacons[pair1[0].coords()] = (
                                pair1[0], pair2[0])
                        if pair1[1].coords() not in matching_beacons:
                            matching_beacons[pair1[1].coords()] = (
                                pair1[1], pair2[1])

            if len(matching_beacons) >= 12:
                return list(matching_beacons.values()), s

        return ([], None)


def read_scanners(lines: List[str]) -> List[Scanner]:
    scanners = []
    scanner_indexes = [i for i in range(
        len(lines)) if lines[i].startswith("--- scanner")]

    for i, index in enumerate(scanner_indexes):
        scanner = Scanner(i)

        for j, line in enumerate(lines[index + 1:]):
            if line == "":
                break
            x, y, z = (int(p) for p in line.split(","))
            scanner.add_beacon(Beacon(j, x, y, z))

        scanners.append(scanner)

    return scanners


def run() -> None:

    filename = "input/day19input.txt"
    file = open(filename, "r")
    lines = [l.strip() for l in file.readlines()]
    scanners = read_scanners(lines)

    needs_scan = set(range(len(scanners)))
    pending = [0]
    relative_pos = {0: (0, 0, 0)}

    while len(pending):
        idx = pending.pop()
        if idx not in needs_scan:
            continue

        needs_scan.remove(idx)
        s = scanners[idx]

        for other_idx in needs_scan:
            other = scanners[other_idx]
            beacons, rotated_s = s.find_overlapping(other)
            if beacons:
                scanners[other_idx] = rotated_s
                relative_pos[other_idx] = (
                    relative_pos[idx][0] + beacons[0][0].x - beacons[0][1].x,
                    relative_pos[idx][1] + beacons[0][0].y - beacons[0][1].y,
                    relative_pos[idx][2] + beacons[0][0].z - beacons[0][1].z
                )
                pending.append(other_idx)

    beacons = set()
    for i, s in enumerate(scanners):
        for b in s.beacons:
            beacons.add((
                relative_pos[i][0] + b.x,
                relative_pos[i][1] + b.y,
                relative_pos[i][2] + b.z
            ))

    print(f'Beacons: {len(beacons)}')

    max_distance = 0
    for i in range(len(scanners)):
        for j in range(i + 1, len(scanners)):
            distance = abs(relative_pos[i][0] - relative_pos[j][0])
            distance += abs(relative_pos[i][1] - relative_pos[j][1])
            distance += abs(relative_pos[i][2] - relative_pos[j][2])

            max_distance = max(max_distance, distance)

    print(f'Maximum distance between scanners: {max_distance}')


if __name__ == '__main__':
    run()
    sys.exit(0)
