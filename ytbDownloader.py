import youtube_dl as yd
import os

import ydlOpts
import argParser

downloads_path = 'downloads/'
if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)


def supported(url):
    ies = yd.extractor.gen_extractors()
    for ie in ies:
        if ie.suitable(url) and ie.IE_NAME != 'generic':
            return True
    return False


def ytb_download():
    if not supported(ytb_link):
        print('해당 링크를 찾을 수 없습니다. 올바른 링크인지 확인해주세요.')
        return

    if format_type == 'mp3':
        ydl_opts = ydlOpts.get_ydl_opts_for_mp3(downloads_path)
        with yd.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytb_link])

    if format_type == 'mp4':
        ydl_opts = ydlOpts.get_ydl_opts_for_mp4(downloads_path)
        with yd.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytb_link])


if __name__ == '__main__':
    ytb_link, format_type = argParser.get_argument()
    if format_type is None:
        format_type = 'mp3'

    try:
        ytb_download()
    except KeyboardInterrupt:
        print('사용자에 의해 작업이 취소 됐습니다.')
