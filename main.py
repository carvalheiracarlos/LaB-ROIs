from data_loader.audio_pre_load import AudioPreLoad
from utils.config import process_config
from utils.utils import get_args

def main():
    args = get_args()
    config = process_config(args.config)


    print('Create the data generator.')
    data_loader = AudioPreLoad(config)
    
    if args.gdown:
        print('Downloading data from google drive !!')
        data_loader.download_data_from_google()

    '''
    if args.preProcess:
        'Pre-Process Code'
        print('Pre-Process Code')
        exit(0)
    '''
    

if __name__ == '__main__':
    main()