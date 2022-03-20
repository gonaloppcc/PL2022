from sys import argv

from stats.stats import get_stats

"""
Main function
"""

# pylint: disable=unused-argument


if __name__ == '__main__':
    get_stats(argv[1])
