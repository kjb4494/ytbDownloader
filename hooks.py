
def finished_hook_for_mp3(d):
    if d['status'] == 'finished':
        print('다운로드가 완료되었습니다. 컨버팅을 시작합니다.')


def finished_hook_for_mp4(d):
    if d['status'] == 'finished':
        print('다운로드가 완료되었습니다.')
