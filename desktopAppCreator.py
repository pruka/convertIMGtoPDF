import os
import locale
import subprocess
# Kullanıcının işletim sistemi dilini al
language, encoding = locale.getdefaultlocale()

# Dil Türkçe ise "Masaüstü" kullan, değilse "Desktop" kullan
if 'tr' in language.lower():
    desktop_folder = 'Masaüstü'
else:
    desktop_folder = 'Desktop'

# Kullanıcıya özgü masaüstü yolunu oluşturma
home_dir = os.path.expanduser("~")
desktop_path = os.path.join(home_dir, desktop_folder)


resName = "ConvertApp"


# 'pwd' komutunu çalıştırarak çıktısını al
result = subprocess.run(['pwd'], capture_output=True, text=True)

# Çıktıyı alınan dizin yoluyla göster
if result.returncode == 0:
    current_dir = result.stdout.strip()
else:
    print("hata")

if " " in current_dir:
  current_dir = current_dir.replace(" ", "\\040")
  
#Create ConvertApp.sh file
os.system(f"touch {current_dir}/ConvertApp.sh")
with open(f"{current_dir}/ConvertApp.sh", "w") as f:
  f.write(f"python3 {current_dir}/guiMain.py")
os.system(f"chmod a+x {current_dir}/ConvertApp.sh")


txt = f"""[Desktop Entry]
Version=1.0
Name={resName}
Exec={current_dir}/ConvertApp.sh
Terminal=false
Icon={current_dir}/appicon/icon.png
Type=Application
"""

os.system(f"touch {desktop_path}/{resName}.desktop")
with open(f"{desktop_path}/{resName}.desktop", "w") as f:
    f.write(txt)

os.system(f"gio set {desktop_path}/{resName}.desktop metadata::trusted true")
os.system(f"chmod a+x {desktop_path}/{resName}.desktop")
print("Your app has been added successfully!✅")

