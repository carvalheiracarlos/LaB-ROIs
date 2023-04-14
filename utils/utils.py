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
    argparse.add_argument(
        '-d', '--driveDownload',
        help='Download Data from Gogle Drive',
        action='sotre_true'
    )
    argparser.add_argument(
        '-p', '--preProcess',
        help='Pre Process Audio Files',
        action='store_true'
    )
    args = argparser.parse_args()
    return args
