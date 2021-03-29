import tkinter as tk
import requests
from tqdm import tqdm
import shutil
import os.path
from os import path
import os
from tkinter import filedialog
from time import sleep

root = tk.Tk()
root.withdraw()

DEAFULT_GD_PATH = r'C:\Program Files (x86)\Steam\steamapps\common\Geometry Dash'
GD_FOLDER = ''
MHV6 = False
TO_INSTALL = []
DOWNLOAD_LIST = []
INSTALL_MESSAGE = ''

CHECKPOINT_FIX = r'https://cdn.discordapp.com/attachments/819517470091509761/825825710920302592/CheckpointFix.dll'
Y_ADVANCE = r'https://cdn.discordapp.com/attachments/819517470091509761/825825700048535642/yAdvance.dll'
NOCLIP_ACCURACY = r'https://cdn.discordapp.com/attachments/810593596143173722/817353567081594900/NoclipAcc.dll'
COCOS_EXPLORER = r'https://cdn.discordapp.com/attachments/810593596143173722/817353711650734090/CocosExplorer.dll'
START_POS_FIX = r'https://cdn.discordapp.com/attachments/810593596143173722/817854404383211550/StartposFix.dll'
PROFILE_BUTTON = r'https://cdn.discordapp.com/attachments/810593596143173722/823130011933868032/ProfileButton.dll'
FAST_TABOUT = r'https://cdn.discordapp.com/attachments/810593596143173722/825513106360893500/fast-tabout.dll'
GROUP_ID_FILTER = r'https://cdn.discordapp.com/attachments/810593596143173722/826151721692430346/GroupIDFilter.dll'

MODS_LIST = {
    CHECKPOINT_FIX : 'checkpoint fix',
    Y_ADVANCE : 'yAdvance',
    NOCLIP_ACCURACY : 'noclip accuracy',
    COCOS_EXPLORER : 'cocos explorer',
    START_POS_FIX : 'start pos fix',
    PROFILE_BUTTON : 'profile button',
    FAST_TABOUT : 'fast tabout',
    GROUP_ID_FILTER : 'group id filter'
}

MODIFY_LIBCURL = r'https://cdn.discordapp.com/attachments/819517470091509761/825825509572608080/libcurl.dll'
GDDLLoader = r'https://cdn.discordapp.com/attachments/819517470091509761/825774562083340298/GDDLLLoader.dll'
def download_url(url, file_name):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True, desc='downloading')
    with open(file_name, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
def main():
    print(r'''
   ________________    ___________           .__          
 /  _____/\______ \   \__    ___/___   ____ |  |   ______
/   \  ___ |    |  \    |    | /  _ \ /  _ \|  |  /  ___/
\    \_\  \|    `   \   |    |(  <_> |  <_> )  |__\___ \ 
 \______  /_______  /   |____| \____/ \____/|____/____  >
        \/        \/                                  \/ 
.___                 __         .__  .__                
|   | ____   _______/  |______  |  | |  |   ___________ 
|   |/    \ /  ___/\   __\__  \ |  | |  | _/ __ \_  __ \
|   |   |  \\___ \  |  |  / __ \|  |_|  |_\  ___/|  | \/
|___|___|  /____  > |__| (____  /____/____/\___  >__|   
         \/     \/            \/               \/       ''')
    print(r'join our server: https://discord.gg/PtWRs6B54j ')
    print('if you have any questions feel free to ask in the server')
    print('please make sure your antivirus is disabled')
    print('type 1 to proceed to the mods section: ')
    if int(input(' ')) == 1:
        sleep(1)
        os.system('cls')
        print('AVAIBLE MODS: ')
        for value in MODS_LIST.values():
            print(value)
        print('please type mods name and it will be installed, type DONE when you are done')
        x = input(' ')
        while x != 'DONE':
            if x in str(MODS_LIST.values()):
                TO_INSTALL.append(x)
                print('added')
                x = input('')
            else:
                print('this mod does not exist')
                x = input('')
        FILELIST = []
        INVERTED_MODS_LIST = {v: k for k, v in MODS_LIST.items()}
        LIST = [f'{file}.dll' for file in MODS_LIST.values()]

        for item in TO_INSTALL:
            download = INVERTED_MODS_LIST[str(item)]
            download_url(str(download), f'{item}.dll')
        for file in os.listdir(os.getcwd()):
            if file.endswith('dll') and file != 'libcurl.dll' and file != "GDLLLoader.dll" and file in LIST:
                try:
                    shutil.move(fr'{os.getcwd()}\{file}', GD_FOLDER)
                    print(f'moved {file} to {GD_FOLDER}')
                    FILELIST.append(file)
                except Exception as e:
                    print(f'[ERROR] {e}')
        if MHV6:
            ABSOLUTEDLLS = rf'{GD_FOLDER}\absolutedlls'
            print('INSTALLING MODS WITH MHV6 METHOD')
            os.rename(ABSOLUTEDLLS, fr'{ABSOLUTEDLLS}.txt')
            absolutedls = open(fr'{GD_FOLDER}\\absolutedlls.txt', 'w')
            absolutedls.write("hackpro.dll\n")
            for lol in FILELIST:
                absolutedls.write(f'{lol}\n')
            absolutedls.close()
            os.rename(fr'{GD_FOLDER}\\absolutedlls.txt', f"{GD_FOLDER}\\absolutedlls")
            print('SUCCESS!')

        else:
            print('INSTALLING MODS WITH LIBCURL AND GDLLLOADER METHOD (THIS WILL NOT WORK IF YOU HAVE YOUR AV ENABLED)')
            download_url(MODIFY_LIBCURL, 'libcurl.dll')
            download_url(GDDLLoader, 'GDLLLoader.dll')
            loader = rf'{os.getcwd()}\GDLLLoader.dll'
            modified = rf'{os.getcwd()}\libcurl.dll'
            libcurl = fr"{GD_FOLDER}\libcurl.dll"
            try:
                if os.path.exists(fr'{GD_FOLDER}\libcurl.OLD'):
                    os.remove(fr'{GD_FOLDER}\libcurl.OLD')
                os.rename(libcurl, rf'{GD_FOLDER}\libcurl.OLD')
            except:
                print('the backup is already there')
            try:
                os.mkdir(rf"{GD_FOLDER}\adaf-dll")
            except:
                print(f'\ncouldnt create adaf-dll in {GD_FOLDER}, its probably already there')
            try:
                shutil.move(modified, GD_FOLDER)
                shutil.move(loader, GD_FOLDER)
            except Exception as e:
                print(f'[ERROR] {e}')
            for file in FILELIST:
                shutil.move(rf'{GD_FOLDER}\{file}', rf"{GD_FOLDER}\adaf-dll")
                print(f'moved {file} to adaf-dll')

                print('SUCCESS')

    else:
        exit()
if __name__ == '__main__':
    from time import sleep
    if path.exists(DEAFULT_GD_PATH):
        print(f"gd path found on {DEAFULT_GD_PATH}")
        GD_FOLDER = DEAFULT_GD_PATH
    else:
        print('BASIC CONFIG')
        while not path.exists(GD_FOLDER):
            GD_FOLDER = filedialog.askdirectory(title='Select your geometry dash folder')
    if 'absolutedlls' in os.listdir(GD_FOLDER):
        MHV6 = True
        print("Mega Hack v6 detected!")
        INSTALL_MESSAGE = 'Installing using absolutedlls'
    else:
        print('no Mega Hack v6 detected')
        INSTALL_MESSAGE = 'installing using GDDLLLoader and modified libcurl, this will not work unless you disable your antivirus'
    main()
    sleep(5)








