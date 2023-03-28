import requests
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

user = input('Input player id or name: ')
player = 'null'
cls()
umode = int(input("\nModes:\n0 = vn!std\n4 = rx!std\n8 = ap!std\n1 = vn!taiko\n5 = rx!taiko\n2 = vn!catch\n6 = rx!catch\n3 = vn!mania\nInput mode: "))
cls()
limit = int(input("\nScores Limit (1-100): "))
cls()

def check_is_digit(input_str):
    global player
    if input_str.strip().isdigit():
        player = f'id={user}'
    else:
        player = f'name={user}'
check_is_digit(user)

url = f'https://api.okayu.me/get_player_scores?{player}&scope=best&mode={umode}&limit={limit}'
a = requests.get(url).json()

player_id = a['player']['id']
player_name = a['player']['name']

player = f'\nScores by: {player_name} ({player_id})'
print(player)

global abo
global message
abo = ' '
message = ' '

def minfo(number):
    scores_score = a['scores'][number]['score']
    scores_pp = a['scores'][number]['pp']
    scores_acc = a['scores'][number]['acc']
    scores_max_combo = a['scores'][number]['max_combo']
    scores_n300 = a['scores'][number]['n300']
    scores_n100 = a['scores'][number]['n100']
    scores_n50 = a['scores'][number]['n50']
    scores_nmiss = a['scores'][number]['nmiss']
    scores_grade = a['scores'][number]['grade']
    scores_mods = a['scores'][number]['mods_readable']

    scores_beatmap_artist = a['scores'][number]['beatmap']['artist']
    scores_beatmap_title = a['scores'][number]['beatmap']['title']
    scores_beatmap_version = a['scores'][number]['beatmap']['version']
    scores_beatmap_creator = a['scores'][number]['beatmap']['creator']
    scores_beatmap_max_combo = a['scores'][number]['beatmap']['max_combo']

    scores_beatmap_diff_info_bpm = a['scores'][number]['beatmap']['bpm']
    scores_beatmap_diff_info_cs = a['scores'][number]['beatmap']['cs']
    scores_beatmap_diff_info_od = a['scores'][number]['beatmap']['od']
    scores_beatmap_diff_info_ar = a['scores'][number]['beatmap']['ar']
    scores_beatmap_diff_info_hp = a['scores'][number]['beatmap']['hp']
    scores_beatmap_diff_info_diff = a['scores'][number]['beatmap']['diff']
    scores_beatmap_diff_info = f'{scores_beatmap_diff_info_bpm}bpm\nCS: {scores_beatmap_diff_info_cs} OD: {scores_beatmap_diff_info_od} AR: {scores_beatmap_diff_info_ar} HP: {scores_beatmap_diff_info_hp}\nStars: {scores_beatmap_diff_info_diff}*'
    
    scores = f'__Player score__\n{scores_score} PP: {scores_pp}\nGrade: {scores_grade}\n{scores_acc}% {scores_max_combo}/{scores_beatmap_max_combo}\n300\'s: {scores_n300} 100\'s: {scores_n100}\n50\'s: {scores_n50} X\'s: {scores_nmiss}\nMods: {scores_mods}'
    beatmap = f'__BeatMap__\n{scores_beatmap_artist} - {scores_beatmap_title} ({scores_beatmap_version}) [{scores_beatmap_creator}]\n{scores_beatmap_diff_info}'
    
    global message
    message = f'\n{beatmap}\n{scores}\n'
    abo = message

global count1
count1 = 0
while count1 < limit:
    minfo(count1)
    abo += message
    count1 = count1 + 1

print(abo)