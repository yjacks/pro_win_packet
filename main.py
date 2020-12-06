import sys

import back

command = sys.argv.pop(0)

if command[0] == 'install':
    print(back.back.down(command[1]))

elif command[0] == 'uninstall':
    print(back.back.remove(command[1]))

elif command[0] == 'getlist':
    back.back.get_list()

else:
    print(
        '''
        command{
        'install':'从list.json获取软件包名称并下载'
        'uninstall':'从本地删除软件包'
        'getlist':'从服务器获取表单更新'
        ''')
