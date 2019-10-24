import argparse


def get_argument():
    parser = argparse.ArgumentParser(description='YoutubeDownloader - mp3 or mp4', add_help=False)
    parser.add_argument(dest='ytbLink')
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 1.0',
        help="버전을 출력합니다."
    )
    parser.add_argument(
        '-h', '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='도움말을 출력합니다.'
    )
    parser.add_argument(
        '-t',
        choices=['mp3', 'mp4'],
        help='원하는 파일 형태를 고르세요. 선택하지않을 경우 mp3파일을 다운로드합니다.'
    )
    args = parser.parse_args()
    return args.ytbLink, args.t
