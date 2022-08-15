akun = {"username":"valoran","password":"beliskin","coba":0}
user = {"saldo": 1000000, "valo":0,
        "skin":{
            "singularity" : "Belum Punya",
            "ruin" : "Belum Punya"
            },
        "battlepass":{
            "upgrade" : "belum upgrade",
            "level" : 0
            },
        "vouc":{"kode":"cutcut","chance": 3
                }
    }
from time import sleep
def waktu():
    import datetime
    waktu = datetime.datetime.now()
    sleep(0.5)
    jam = int(waktu.strftime("%H"))
    mnt = int(waktu.strftime("%M"))
    dtk = int(waktu.strftime("%S"))

    print("Anda masuk pada : ",jam,":",mnt,":",dtk)
#1
def sisa():
    print("Sisa saldo yang anda miliki adalah : ", user["saldo"])
#2
def valo():
    if user["saldo"] < 80000:
        print("Mohon maaf saldo anda tidak cukup")
    else :
        import datetime
        waktu = datetime.datetime.now()
        print("Anda masuk pada : ")
        sleep(0.5)
        jam = int(waktu.strftime("%H"))
        mnt = int(waktu.strftime("%M"))
        dtk = int(waktu.strftime("%S"))
        
        print(jam,":",mnt,":",dtk)
        print("Voucher akan hangus dalam 3 menit")
        batas_waktu = mnt + 3
        print("Hangus menit ke : ",batas_waktu)
        print("=====================================")
        print("1. 2500 valo = 80.000")
        print("2. 5000 valo = 150.000")
        print("3. 7500 valo = 220.000")
        print("=====================================")
        pilih = input("Pilih valo yang ingin anda beli : ")
        if int(pilih) == 1 and user["saldo"] >= 80000:
            pilih = input("Apakah anda mempunyai kode voucher (ya/tidak) : ")
            if pilih == "ya" or "Ya":
                while True :
                    x = input("Silahkan masukkan kode voucher anda : ")
                    waktu = datetime.datetime.now()
                    mnt = int(waktu.strftime("%M"))
                    if x == user["vouc"]["kode"] and user["vouc"]["chance"]>= 1 and mnt < batas_waktu :
                        (user["saldo"]) = (user["saldo"]) - (80000 -(80000 * 30/100))
                        (user["valo"]) = (user["valo"]) + 2500
                        print("Selamat pembelian valo anda berhasil")
                        print("Anda mendapat potongan 30%")
                        print("Valo anda sekarang sebanyak ",user["valo"])
                        print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
                        break
                    elif x != user["vouc"]["kode"]:
                        user["vouc"]["chance"] = user["vouc"]["chance"] -1
                        if user["vouc"]["chance"] == 0:
                            (user["saldo"]) = (user["saldo"]) - 80000
                            (user["valo"]) = (user["valo"]) + 2500
                            print("Selamat pembelian valo anda berhasil")
                            print("Kesempatan anda menggunakan voucher telah habis")
                            print("Valo anda sekarang sebanyak ",user["valo"])
                            print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
                            break               
                    else : 
                            (user["saldo"]) = (user["saldo"]) - 80000
                            (user["valo"]) = (user["valo"]) + 2500
                            print("Selamat pembelian valo anda berhasil")
                            print("Anda gagal mengaktifkan voucher")
                            print("Valo anda sekarang sebanyak ",user["valo"])
                            print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
                            break
            else : 
                (user["saldo"]) = (user["saldo"]) - 80000
                (user["valo"]) = (user["valo"]) + 2500
                print("Selamat pembelian valo anda berhasil")
                print("Valo anda sekarang sebanyak ",user["valo"])
                print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
        elif int(pilih) == 2 and user["saldo"] >= 150000:
            pilih = input("Apakah anda mempunyai kode voucher (ya/tidak) : ")
            if pilih == "ya" or "Ya":
                while True :
                    x = input("Silahkan masukkan kode voucher anda : ")
                    waktu = datetime.datetime.now()
                    mnt = int(waktu.strftime("%M"))
                    if x == user["vouc"]["kode"] and user["vouc"]["chance"]>= 1 and mnt < batas_waktu :
                        (user["saldo"]) = (user["saldo"]) - (150000 -(150000 * 30/100))
                        (user["valo"]) = (user["valo"]) + 5000
                        print("Selamat pembelian valo anda berhasil")
                        print("Anda mendapat potongan 30%")
                        print("Valo anda sekarang sebanyak ",user["valo"])
                        print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
                        break
                    elif x != user["vouc"]["kode"]:
                        user["vouc"]["chance"] = user["vouc"]["chance"] -1
                        if user["vouc"]["chance"] == 0:
                            (user["saldo"]) = (user["saldo"]) - 150000
                            (user["valo"]) = (user["valo"]) + 5000
                            print("Selamat pembelian valo anda berhasil")
                            print("Kesempatan anda menggunakan voucher telah habis")
                            print("Valo anda sekarang sebanyak ",user["valo"])
                            print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
                            break               
                    else : 
                            (user["saldo"]) = (user["saldo"]) - 150000
                            (user["valo"]) = (user["valo"]) + 5000
                            print("Selamat pembelian valo anda berhasil")
                            print("Anda gagal mengaktifkan voucher")
                            print("Valo anda sekarang sebanyak ",user["valo"])
                            print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
                            break
            else:
                (user["saldo"]) = (user["saldo"]) - 150000
                (user["valo"]) = (user["valo"]) + 5000
                print("Selamat pembelian valo anda berhasil")
                print("Valo anda sekarang sebanyak ",user["valo"])
                print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
        elif int(pilih) == 3 and user["saldo"] >= 220000:
            pilih = input("Apakah anda mempunyai kode voucher (ya/tidak) : ")
            if pilih == "ya" or "Ya":
                while True :
                    x = input("Silahkan masukkan kode voucher anda : ")
                    waktu = datetime.datetime.now()
                    mnt = int(waktu.strftime("%M"))
                    if x == user["vouc"]["kode"] and user["vouc"]["chance"]>= 1 and mnt < batas_waktu :
                        (user["saldo"]) = (user["saldo"]) - (220000 -(220000 * 30/100))
                        (user["valo"]) = (user["valo"]) + 7500
                        print("Selamat pembelian valo anda berhasil")
                        print("Anda mendapat potongan 30%")
                        print("Valo anda sekarang sebanyak ",user["valo"])
                        print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
                        break
                    elif x != user["vouc"]["kode"]:
                        user["vouc"]["chance"] = user["vouc"]["chance"] -1
                        if user["vouc"]["chance"] == 0:
                            (user["saldo"]) = (user["saldo"]) - 220000
                            (user["valo"]) = (user["valo"]) + 7500
                            print("Selamat pembelian valo anda berhasil")
                            print("Kesempatan anda menggunakan voucher telah habis")
                            print("Valo anda sekarang sebanyak ",user["valo"])
                            print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
                            break               
                    else : 
                            (user["saldo"]) = (user["saldo"]) - 220000
                            (user["valo"]) = (user["valo"]) + 7500
                            print("Selamat pembelian valo anda berhasil")
                            print("Anda gagal mengaktifkan voucher")
                            print("Valo anda sekarang sebanyak ",user["valo"])
                            print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
                            break
            else:
                (user["saldo"]) = (user["saldo"]) - 220000
                (user["valo"]) = (user["valo"]) + 7500
                print("Selamat pembelian valo anda berhasil")
                print("Valo anda sekarang sebanyak ",user["valo"])
                print("Sisa saldo yang anda miliki adalah : Rp", user["saldo"])
        else :
            print("Pilihan yang anda masukkan tidak tersedia")
#3

def skin():
    if user["skin"]["singularity"] == "Sudah punya" and user["skin"]["ruin"] == "Sudah punya":
        print("Anda sudah memiliki semua skin")
        print("Anda tidak dapat membeli lagi")
    else :
        print("=====================================")
        print("1. Singularity Bundle = 8750 valo")
        print("2. Ruin Bundle        = 2875 valo")
        print("=====================================")
        pilih = input("Pilih skin yang ingin anda beli : ")
        if int(pilih) == 1 and user["skin"]["singularity"] == "Belum Punya" and user["valo"] >=8750 :
            user["valo"] = user["valo"] - 8750
            user["skin"]["singularity"] = "Sudah punya"
            print("Selamat Singularity Bundle telah masuk ke inventary anda")
            print("Sisa valo yang anda miliki adalah : ", user["valo"])
        elif int(pilih) == 2 and user["skin"]["ruin"] == "Belum Punya" and user["valo"] >= 2875 :
            user["valo"] = user["valo"] - 2875
            user["skin"]["ruin"] = "Sudah punya"
            print("Selamat Ruin Bundle telah masuk ke inventary anda")
            print("Sisa valo yang anda miliki adalah : ", user["valo"])
        elif int(pilih) == 1 and user["skin"]["singularity"] == "Sudah punya":
            print("Anda sudah memiliki Singulary Bundle")
        elif int(pilih) == 2 and user["skin"]["ruin"] == "Sudah punya":
            print("Anda sudah memiliki Ruin Bundle")
        else :
            print("Pilihan yang anda masukkan tidak tersedia atau valo tidak mencukupi")
#4           
def bp():
    if user["battlepass"]["upgrade"] == "belum upgrade" :
        pilih=input ("Anda ingin upgrade Battle Pass seharga 1000 valo? (ya/tidak) : ")
        if pilih == "ya" and user["valo"] >= 1000 :
            user["valo"] = user["valo"] - 1000
            user["battlepass"]["upgrade"] = "sudah upgrade"
            user["battlepass"]["level"] = user["battlepass"]["level"] + 1
            print("=====================================")
            print("Battle Pass anda berhasil di upgrade")
            print("Sisa valo yang anda miliki adalah : ", user["valo"])
            print("Battle pass anda sekarang level ", user["battlepass"]["level"])
            print("=====================================")
        elif pilih == "ya" and user["valo"] < 1000 :
            print("=====================================")
            print("Mohon maaf valo anda tidak mencukupi")
            print("=====================================")
        else:
            print("Terima kasih")
    else :
        print("Battle Pass anda telah diaktifkan")
        print("Anda tidak dapat membeli lagi")
        
#5
def lvl():
    if user["battlepass"]["upgrade"] == "belum upgrade" :
        print("Mohon maaf Battle Pass anda belum terupgrade")
        print("Silahkan upgrade Battle Pass anda")
    elif user["battlepass"]["upgrade"] == "sudah upgrade" and user["valo"] < 500:
        print("Mohon maaf valo anda tidak cukup untuk membeli level")
        print("Silahkan beli valo terlebih dahulu")
    else :
        print("=====================================")
        print("1. 5 level       = 500 valo")
        print("2. 10 level      = 900 valo")
        print("=====================================")
        pilih = input ("Berapa level yang ingin anda beli ?(1/2) : ")
        if pilih == "1" and user["valo"] >= 500 :
            user["valo"] = user["valo"] - 500
            user["battlepass"]["level"] = user["battlepass"]["level"] + 5
            print("Battle pass anda sekarang level ", user["battlepass"]["level"])
            print("Sisa valo yang anda miliki adalah : ", user["valo"])
        elif pilih == "2" and user["valo"] >= 900 :
            user["valo"] = user["valo"] - 900
            user["battlepass"]["level"] = user["battlepass"]["level"] + 10
            print("Battle pass anda sekarang level ", user["battlepass"]["level"])
            print("Sisa valo yang anda miliki adalah : ", user["valo"])
        elif pilih == "2" and user["valo"] < 900 :
            print("Mohon maaf valo anda tidak mencukupi")
            print("Silahkan membeli valo terlebih dahulu")
            print("Atau anda bisa membeli pilihan 1")            
        else :
            print("Pilihan yang anda masukkan tidak tersedia")
            
#6        
def inven():
    if user["skin"]["singularity"] == "Sudah punya" and user["skin"]["ruin"] == "Sudah punya" :
        print("=====================================")
        print("Inventary kamu berisi : ")
        print("1. Singularity Bundle ")
        print("2. Ruin Bundle        ")
        print("=====================================")
    elif user["skin"]["singularity"] == "Sudah punya" and user["skin"]["ruin"] == "Belum Punya" :
        print("=====================================")
        print("Inventary kamu berisi : ")
        print("1. Singularity Bundle ")
        print("=====================================")
    elif user["skin"]["singularity"] == "Belum Punya" and user["skin"]["ruin"] == "Sudah punya" :
        print("=====================================")
        print("Inventary kamu berisi : ")
        print("1. Ruin Bundle        ")
        print("=====================================")
    else :
        print("=====================================")
        print("Kamu tidak memiliki skin apapun")
        print("=====================================")
        
#7    
def bp_info():
    if user["battlepass"]["upgrade"] == "belum upgrade" :
        print("Battle Pass anda belum terupgrade")
    else :
        print("Battle Pass anda telah diaktifkan")
        print("Battle pass anda sekarang level ", user["battlepass"]["level"])
#8       


def menu_utama():
    ulang = "ya"
    while ulang == "ya":
        print("=====================================")
        print("==============MENU UTAMA=============")
        print("=====================================")
        print("Silahkan pilih menu anda : ")
        print("1. Cek saldo ")
        print("2. Beli valo")
        print("3. Beli skin ")
        print("4. Upgrade Battle Pass ")
        print("5. Beli level Battle Pass ")
        print("6. Buka inventary ")
        print("7. Info Battle Pass ")
        print("8. Logout ")
        print("=====================================")
        pilih = int(input("Pilih menu : "))
        if (pilih) == 1 :
            sisa()
            ulang = input("Kembali ke menu utama ? (ya/tidak) : ")
            if ulang == "tidak":
                print("=====================================")
                print("============TERIMA KASIH=============")
                print("=========Sampai bertemu lagi=========")
                print("=====================================")
        elif (pilih) == 2 :
            valo()
            ulang = input("Kembali ke menu utama ? (ya/tidak) : ")
            if ulang == "tidak":
                print("=====================================")
                print("============TERIMA KASIH=============")
                print("=========Sampai bertemu lagi=========")
                print("=====================================")
        elif (pilih) == 3 :
            skin()
            ulang = input("Kembali ke menu utama ? (ya/tidak) : ")
            if ulang == "tidak":
                print("=====================================")
                print("============TERIMA KASIH=============")
                print("=========Sampai bertemu lagi=========")
                print("=====================================")
        elif (pilih) == 4 :
            bp()
            ulang = input("Kembali ke menu utama ? (ya/tidak) : ")
            if ulang == "tidak":
                print("=====================================")
                print("============TERIMA KASIH=============")
                print("=========Sampai bertemu lagi=========")
                print("=====================================")
        elif (pilih) == 5 :
            lvl()
            ulang = input("Kembali ke menu utama ? (ya/tidak) : ")
            if ulang == "tidak":
                print("=====================================")
                print("============TERIMA KASIH=============")
                print("=========Sampai bertemu lagi=========")
                print("=====================================")
        elif (pilih) == 6 :
            inven()
            ulang = input("Kembali ke menu utama ? (ya/tidak) : ")
            if ulang == "tidak":
                print("=====================================")
                print("============TERIMA KASIH=============")
                print("=========Sampai bertemu lagi=========")
                print("=====================================")
        elif (pilih) == 7 :
            bp_info()
            ulang = input("Kembali ke menu utama ? (ya/tidak) : ")
            if ulang == "tidak":
                print("=====================================")
                print("============TERIMA KASIH=============")
                print("=========Sampai bertemu lagi=========")
                print("=====================================")
        elif (pilih) == 8 :
            print("=====================================")
            print("============TERIMA KASIH=============")
            print("=========Sampai bertemu lagi=========")
            print("=====================================")
            break
#8
def launch():
    while True :
        if akun["coba"] <=3 :
            user = input("Masukkan Username : ")
            passw = input("Masukkan password : ")
            akun["coba"] = akun["coba"] + 1
            if user == akun["username"] and passw == akun["password"] :
                waktu()
                menu_utama()
                break
            else:
                print("Mohon maaf info login anda tidak sesuai")
        else:
            print("Mohon maaf anda tidak dapat login lagi")
            break
        
     
launch()
        
        