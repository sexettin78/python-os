import os

os.name #işletim sistemi bilgisini verir. nt: Windows, posix:Linux

os.sep #işletim sistemi dizin ayracını öğreniriz. windows için \\, linux için /

os.getcwd #içinde bulunduğumuz dizini görebiliriz

os.chdir("C:\\") #bu fonksiyon ile istediğimiz dizine geçebiliriz. hangi dizini istersek parametrede belirtmemiz lazım

os.listdir("C:\\") #belirttiğimiz yerdeki dosya ve klasörleri listeler

os.curdir #bulunduğumuz dizini göstermektedir. os.listdir(os.curdir) yaparak bulunduğumuz dizindeki dosya ve klasörlere bakabiliriz

os.pardir #bir üstteki dizini gösterir. listdir'e parametre olarak atarsak üst dizindeki verileri görebiliriz.

#os.startfile("") #belirtilen parametrede yer alan dosyayı açar. sadece windowsda geçerli

os.mkdir("klasör_adı") #belirtilen parametreye ait isimde bir klasör oluşturur. klasör zaten varsa hata verir

os.makedirs("dizin\\altdizin") #eğer dizin yoksa kendisi oluşturur. mkdirde hata verir

os.rename("eskiad","yeniad") #eskiad isimdeki klasörün adını yeniad yapar

#os.replace #os.rename ile aynıdır

os.remove("klasör_adı") #belirtilen parametredeki klasörü siler. klasör içinin boş olması gerekir.

os.remove("dosya") #belirtilen dosyayı siler

os.removedirs("dizin\\altdizin") #içi boş ise dizin ve alt dizini siler

f = os.stat() #belirtilen dosya hakkında bilgi verir. çekmek istediğimiz bilgiyi (örneğin st_size=10 bilgisini) f.st_size yaparak çekebiliriz

#os.system("") #parametre içerisinde yer alan sistem komutunu çalıştırır

os.urandom(10) #rastgele byte türünde dizi üretir

os.environ #işletim sisteminin çeşitli çevre değişkenleri hakkında bilgi verir

os.path.abspath("1os.py") #belirtilen dosyanın tam yolunu verir.

os.path.dirname("1os.py") #belirtilen dosyanın sadece dizin yolunu verir

os.path.exists("C:\\1os.py") #belirtilen klasör ya da dosya var mı diye kontrol eder. eğer varsa true, yoksa false çıktısını verir.

os.path.expanduser("~") #işletim sisteminin varsayılan kullanıcı dizisini gösterir.

