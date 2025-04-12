from pathlib import Path
from datetime import datetime

# 取得.py檔案所在位置
script_dir = Path(__file__).parent

# 設定.txt檔案路徑跟.py同資料夾
txt_file_path = script_dir / "greeting_diary.txt"

name = input('請輸入你的名字: ')
mood = input('今天心情如何? (開心/累了/普通): ')

if mood == '開心':
    greeting = f'嗨，{name}！看來今天發生了什麼好事！'
elif mood == '累了':
    greeting = f'嗨，{name}！辛苦了，休息一下吧！'
elif mood == '普通':
    greeting = f'嗨，{name}！平凡的一天也很不錯！'
else:
    greeting = f'嗨！{name}，你要不要看看你在打什麼？'

print(greeting)

with open("greeting_diary.txt", 'a', encoding="utf-8") as file:
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'{time}: {greeting}\n')

print(script_dir)
print(txt_file_path)    