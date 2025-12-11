import subprocess

vol = subprocess.run('pamixer --get-volume', capture_output=True, text=True, shell=True)
current_volume=int((vol.stdout.strip()))

if current_volume == 100:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:100 -t 1000 -u low', shell=True)
elif current_volume == 95:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:95 -t 1000 -u low', shell=True)
elif current_volume == 90:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:90 -t 1000 -u low', shell=True)
elif current_volume == 85:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:85 -t 1000 -u low', shell=True)
elif current_volume == 80:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:80 -t 1000 -u low', shell=True)
elif current_volume == 75:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:75 -t 1000 -u low', shell=True)
elif current_volume == 70:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:70 -t 1000 -u low', shell=True)
elif current_volume == 65:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:65 -t 1000 -u low', shell=True)
elif current_volume == 60:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:60 -t 1000 -u low', shell=True)
elif current_volume == 55:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:55 -t 1000 -u low', shell=True)
elif current_volume == 50:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:50 -t 1000 -u low', shell=True)
elif current_volume == 45:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:45 -t 1000 -u low', shell=True)
elif current_volume == 40:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:40 -t 1000 -u low', shell=True)
elif current_volume == 35:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:35 -t 1000 -u low', shell=True)
elif current_volume == 30:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:30 -t 1000 -u low', shell=True)
elif current_volume == 25:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:25 -t 1000 -u low', shell=True)
elif current_volume == 20:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:20 -t 1000 -u low', shell=True)
elif current_volume == 15:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:15 -t 1000 -u low', shell=True)
elif current_volume == 10:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:10 -t 1000 -u low', shell=True)
elif current_volume == 5:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:5 -t 1000 -u low', shell=True)
elif current_volume == 0:
    subprocess.run('notify-send -e "volume changed by 5" -r 1 -h int:value:0 -t 1000 -u low', shell=True)
