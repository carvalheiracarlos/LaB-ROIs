from utils.config import process_config
from utils.utils import get_args

def main():
    try:
        args = get_args()
        config = process_config(args.config)
    except:
        print("missing or invalid arguments")
        exit(0)

    if args.debbug:
        'Debbug Code'
        print('Debbug Code')
        exit(0)

    if args.preProcess:
        'Pre-Process Code'
        print('Pre-Process Code')
        exit(0)


if __name__ == '__main__':
    main()