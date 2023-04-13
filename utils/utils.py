import argparse


def get_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-c', '--config',
        dest='config',
        metavar='C',
        default='None',
        help='The Configuration file'
    )
    argparser.add_argument(
        '-d', '--debbug',
        help='Print Functions',
        action='store_true'
    )
    argparser.add_argument(
        '-k', '--preProcess',
        help='Pre Process Audio Files',
        action='store_true'
    )
    args = argparser.parse_args()
    return args
