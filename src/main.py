from bs4 import BeautifulSoup as BS
import requests
import pyfiglet
  
result = pyfiglet.figlet_format("Monitorings Parser")
result1 = pyfiglet.figlet_format("by Swenly")
print(f'{result}\n{result1}')

r = requests.get('https://monitoringminecraft.ru/novie-servera')
soup = BS(r.content, 'html.parser')

_need_ver = input('Какая версия? ')
if _need_ver == '' or _need_ver == '\n': need_ver = 'all'
else: need_ver = _need_ver
#_need_no_online = input('Нужно ли убирать серваки c 0 онлайном? ')
#if _need_no_online.lower() == 'да' or _need_no_online == '': need_no_online = 'да'
#else: need_no_online = 'нет'
_aternos = input('Убирать атерносы? ')
if _aternos.lower() == 'да' or _aternos == '': aternos = 'да'
else: aternos = _aternos
_min_online = input('Минимальный онлайн? ')
if _min_online == '' or _min_online == '\n': min_online = 'all'
else: min_online = _min_online
print()

#!monitoring-minecraft
mm_servers = soup.find_all('tr', class_='server')
for i in mm_servers:
    if 'Offline' in i.text: continue
    name = i.find(class_='name')
    ip = i.find('td', class_='ip').find('span', class_='ip_serv')
    try: a = ip.text
    except: continue
    if aternos == 'да':
        if 'aternos' in ip.text: continue
        if ip.text.startswith('185') or ip.text.startswith('193') or ip.text.startswith('194'): continue
    version = i.find('td', class_='ver')
    if need_ver != 'all':
        if str(version.text) != need_ver: continue
    online = i.find('td', class_='status').find('div', class_='wrap')
    list = online.text.split(' ')
    list.remove('')
    list.remove('')
    if min_online != 'all':
        if int(list[0]) < int(min_online):
            continue
    cur_online = f'{list[0]} {list[1]} {list[2]}'
#    if need_no_online == 'да':
#        if list[0] == '0': continue
    print('Сервер')
    print('-' * len(f' Название сервера: "{name.text}"'))
    print(f' Название сервера: {name.text}')
    print(f' Версия: {version.text} ')
    print(f' Онлайн: {cur_online} ')
    print(f' Айпи: {ip.text} ')
    print('-' * len(f' Название сервера: "{name.text}"'))

#*MinecraftRating
r = requests.get('https://minecraftrating.ru/new-servers/')
soup = BS(r.content, 'html.parser')

mr_servers = soup.find_all('tr', class_='server-new')
for i in mr_servers:
    if 'Offline' in i.text or 'block ip has-launch' in i.text: continue
    if i.find('td', class_='block ip has-launch'): continue
    name = i.find('h3', class_='name')
    ip = i.find('var', class_='tooltip')
    try: a = ip.text
    except: continue
    if ip.text in mm_servers: continue
    if aternos == 'да':
        if 'aternos' in ip.text: continue
        if ip.text.startswith('185') or ip.text.startswith('193') or ip.text.startswith('194'): continue
    version = i.find('i', class_='fal fa-check-circle').find_parent()
    if need_ver != 'all':
        if str(version.text) != need_ver: continue
    online = i.find('i', class_='fal fa-user').find_parent().text.split('онлайн')[0]
    if min_online != 'all':
        if int(online) < int(min_online):
            continue
#    if need_no_online == 'да':
        if str(online) == '0': continue
#    if 'Offline' in name.text or 'License only' in name.text: continue
    print('Сервер')
    print('-' * len(f'Название сервера: "{name.text}"'))
    print(f' Название сервера: "{name.text}"')
    print(f' Версия: {version.text}')
    print(f' Онлайн: {online}')
    print(f' Айпи: {ip.text}')
    print('-' * len(f'Название сервера: "{name.text}"'))

#*Misterlauncher
r = requests.get('https://misterlauncher.org/servera-novye/')
soup = BS(r.content, 'html.parser')

ml_servers = soup.find('div', class_='servers-list').find_all('div', class_='server')
for i in ml_servers:
    name = i.find('h3', class_='name')
    ip = i.find('kbd')
    try: a = ip.text
    except: continue
    if ip.text in mm_servers or ip.text in mr_servers: continue
    if aternos == 'да':
        if 'aternos' in ip.text: continue
        if ip.text.startswith('185') or ip.text.startswith('193') or ip.text.startswith('194'): continue
    version = i.find('i', class_='far fa-check-circle').find_parent().text.split('версия')[0]
    if need_ver != 'all':
        if str(version) != need_ver: continue
    online = i.find('em', itemprop='playersOnline').text
    if min_online != 'all':
        if int(online) < int(min_online):
            continue
#    if need_no_online == 'да':
#        if str(online) == '0': continue
    print('Сервер')
    print('-' * len(f'Название сервера: "{name.text}"'))
    print(f' Название сервера: "{name.text}"')
    print(f' Версия: {version}')
    print(f' Онлайн: {online}')
    print(f' Айпи: {ip.text}')
    print('-' * len(f'Название сервера: "{name.text}"'))

input('Нажмите Enter для выхода\n')