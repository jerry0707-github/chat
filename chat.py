# 匯入 io 系統模組

import os # operating system

# 讀取檔案函數
def read_file(filename):
    chat =[] #聊天清單
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            data = line.strip() #strip():去除換行符,split():切割字串
            chat.append(data)
    return chat

# 格式轉換函數
def convert(chat):
    new = []
    person = None # None: 無
    for line in chat:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue       
        if person: # person 非 None,則執行以下程式
            new.append(person + ': ' + line)    
    return new

# 寫入檔案函數
def write_file(filename, chat):
    with open(filename, 'w') as f:
        for line in chat:
            f.write((line) + '\n')

def main():
    filename = 'input.txt'
    if os.path.isfile(filename): #檢查檔案是否存在
        print('找到檔案!')
        chat = read_file(filename)
        chat = convert(chat)
        write_file('output.txt', chat)
    else:
        print('找不到檔案......')        
    
main() #呼叫主函數