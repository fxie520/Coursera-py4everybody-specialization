import os


def notify(title, message):
    os.system(f''' osascript -e 'display notification "{message}" with title "{title}"' ''')


file_dir = "/Volumes/XFL-HDD/P/Pics/Nude 1"
nb_partition = 13
save_dirs = ["/Volumes/XFL-HDD/P/Pics/Nude " + str(i) for i in range(6, nb_partition + 6 - 1, 1)]
for save_dir in save_dirs:
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
print(f"Directories (apart from the original one) to save: {save_dirs}")

file_list = sorted(os.listdir(file_dir))
file_list = [file for file in file_list if file[:4] == "亚洲图片"]
partition_size = len(file_list) // (len(save_dirs) + 1) + 1
print(f"Partition files in {file_dir} to {len(save_dirs) + 1} directories of size {partition_size}")
print(f"File partition starts")
for i, file in enumerate(file_list[partition_size:]):
    dest_dir = save_dirs[i // partition_size]
    os.replace(os.path.join(file_dir, file), os.path.join(dest_dir, file))
    if i % 1000 == 0:
        print(i)

# Send banner
notify(title=f'{os.path.basename(__file__)} finished', message='')
