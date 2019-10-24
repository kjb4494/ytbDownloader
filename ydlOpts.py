import hooks


def get_ydl_opts_for_mp3(download_path):
    prefix = 'mp3/'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': download_path + prefix + '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [
            hooks.finished_hook_for_mp3
        ]
    }
    return ydl_opts


def get_ydl_opts_for_mp4(download_path):
    prefix = 'mp4/'
    ydl_opts = {
        'format': 'best',
        'outtmpl': download_path + prefix + '%(title)s.%(ext)s',
        'progress_hooks': [
            hooks.finished_hook_for_mp4
        ]
    }
    return ydl_opts
