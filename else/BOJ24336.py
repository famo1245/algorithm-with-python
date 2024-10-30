import sys
from datetime import datetime, timedelta
input = sys.stdin.readline

distance = {'Seoul':0.0, 'Yeongdeungpo': 9.1, 'Anyang': 23.9, 'Suwon': 41.5, 'Osan': 56.5, 'Seojeongri': 66.5,
            'Pyeongtaek': 75.0, 'Seonghwan': 84.4, 'Cheonan': 96.6, 'Sojeongni': 107.4, 'Jeonui': 114.9,
            'Jochiwon': 129.3, 'Bugang': 139.8, 'Sintanjin': 151.9, 'Daejeon': 166.3, 'Okcheon': 182.5, 'Iwon': 190.8,
            'Jitan': 196.4, 'Simcheon': 200.8, 'Gakgye': 204.6, 'Yeongdong': 211.6, 'Hwanggan': 226.2,
            'Chupungnyeong': 234.7, 'Gimcheon': 253.8, 'Gumi': 276.7, 'Sagok': 281.3, 'Yangmok': 289.5, 'Waegwan': 296.0,
            'Sindong': 305.9, 'Daegu': 323.1, 'Dongdaegu': 326.3, 'Gyeongsan': 338.6, 'Namseonghyeon': 353.1,
            'Cheongdo': 361.8, 'Sangdong': 372.2, 'Miryang': 381.6, 'Samnangjin': 394.1, 'Wondong': 403.2,
            'Mulgeum': 412.4, 'Hwamyeong': 421.8, 'Gupo': 425.2, 'Sasang': 430.3, 'Busan': 441.7}

N, Q = map(int, input().split())
time_table = dict()

for _ in range(N):
    station, *times = input().split()
    for i in range(2):
        if times[i] == '-:-':
            times[i] = '00:00'

    time_table[station] = times

for _ in range(Q):
    start, end = input().split()
    time_diff = datetime.strptime(time_table[end][0], '%H:%M') - datetime.strptime(time_table[start][1], '%H:%M')

    if time_diff.total_seconds() < 0:
        time_diff += timedelta(days=1)

    hours = time_diff.total_seconds() / 3600
    diff_distance = abs(distance[start] - distance[end])
    print(diff_distance / hours)
