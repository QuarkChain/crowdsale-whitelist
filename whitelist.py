#!/usr/bin/env python3

import argparse
import random

from os import path


WHITELIST_NUM = 5000
# In case we have bad actors.
WHITELSIT_SUBSTITUTE_NUM = 500


def get_user_keys_and_scores() -> [(str, float)]:
    """KYC-cleared users with score >= 60."""
    dir_path = path.dirname(path.realpath(__file__))

    with open(path.join(dir_path, 'applicants.csv')) as f:
        lines = f.readlines()
    ret = []
    # Skip header row.
    for line in lines[1:]:
        k, s = line.strip().split(',')
        ret.append((k, float(s)))
    return ret


def get_blacklisted_user_keys() -> [str]:
    """Get user keys who are blacklisted because of selling code, etc."""
    dir_path = path.join(path.dirname(path.realpath(__file__)))

    with open(path.join(dir_path, 'blacklist.txt')) as f:
        ret = [line.strip() for line in f.readlines()]
    return ret


class Candidate(object):
    """
    A candidate is identified by the accees code. The score is the sum of:

    1. Early supporter score. Max 30.
    2. Quiz score. Max 50.
    3. Contribution score. Max 20.
    """

    def __init__(self, key: str, score: float):
        self.key = key
        self.score = score


def main():
    parser = argparse.ArgumentParser()
    # Use a certain blockhash as the random seed.
    parser.add_argument(
        'seed', type=str, help='Use a certain blockhash as the random seed.')
    args = parser.parse_args()
    random.seed(args.seed)

    blacklisted_users = set(get_blacklisted_user_keys())
    # Get KYC-cleared users with scores >= 60.
    users_and_scores = get_user_keys_and_scores()
    candidates = [
        Candidate(k, s)
        for k, s in users_and_scores
        if k not in blacklisted_users
    ]
    whitelist = []

    assert len(candidates) > WHITELIST_NUM + WHITELSIT_SUBSTITUTE_NUM
    # Make sure the order is deterministic so it's reproducible.
    candidates.sort(key=lambda c: c.key)

    weights = [c.score for c in candidates]
    k = WHITELIST_NUM + WHITELSIT_SUBSTITUTE_NUM
    whitelist = random.choices(candidates, weights=weights, k=k)

    assert len(whitelist) == WHITELIST_NUM + WHITELSIT_SUBSTITUTE_NUM
    for i, c in enumerate(whitelist):
        if i == WHITELIST_NUM:
            print('=============Below are substitutes=============')
        print(c.key, c.score)


if __name__ == '__main__':
    main()
