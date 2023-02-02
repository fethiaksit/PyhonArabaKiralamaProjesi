import datetime


class VehicleRent:

    def __init__(self, stock):
        self.stock = stock  # tum stokaları 'self.stock' ile tum classta kullanılır yaptım
        self.now = 0  # kiralama süresine göre fiyatlandırmak için kullanılacak

    def displayStock(self):
        "display stok"  # stok adedi
        print("{} vehicle avaliable to rent".format(
            self.stock))  # kiralamaya uygun araç sayısı
        return self.stock

    def rentHourly(self, n):  # n kiralanabilir arac sayısı
        "rent hourly"  # saatlik kiralama secenegi
        if n <=1:
            # hatalı giris yapıldıgını yazdırıyoruz
            print("Number should positive")
            return None  # arac kiralanmadıgını soyluyoruz
        elif n > self.stock:  # istenen arac sayısı stoktan fazla oldugunu belirtiyruz
            print("{} vehicle avaliable to rent".format(
                self.stock))  # uyarı veriyor
            return None
        else:                                     # her seyin uygun oldugu kosulda ise
            self.now = datetime.datatime.now()  # simdiki zamanı alıyoruz
            # hangi saatte , kac arac kiralandıgını belirtiyoruz
            print("rented a {} vehicle for hourly at {} hours".format(
                n, self.now.hour))
            self.stock -= n  # kiralanan arac sayısını stoktan dusuyoruz
            return self.now  # fiyatı zamana gore ayarlıcaz

    def rentdaily(self, n):
        "rent daily"  # gunluk kiralama secenegi
        if n <= 1:
            # hatalı giris yapıldıgını yazdırıyoruz
            print("Number should positive")
            return None  # arac kiralanmadıgını soyluyoruz
        elif n > self.stock:  # istenen arac sayısı stoktan fazla oldugunu belirtiyruz
            print("{} vehicle avaliable to rent".format(
                self.stock))  # uyarı veriyor
            return None
        else:  # her seyin uygun oldugu kosulda ise
            self.now = datetime.datatime.now()  # simdiki zamanı alıyoruz
            # hangi saatte , kac arac kiralandıgını belirtiyoruz
            print("rented a {} vehicle for dayily at {} hourly".format(
                n, self.now.hour))
            self.stock -= n  # kiralanan arac sayısını stoktan dusuyoruz
            return self.now  # fiyatı zamana gore ayarlıcaz

    def Monthly(self, n):
        "rent monthly"  # aylık kiralama seceneği
        if n <= 0:
            # hatalı giris yapıldıgını yazdırıyoruz
            print("Number should positive")
            return None  # arac kiralanmadıgını soyluyoruz
        elif n > self.stock:  # istenen arac sayısı stoktan fazla oldugunu belirtiyruz
            print("{} vehicle avaliable to rent".format(
                self.stock))  # uyarı veriyor
            return None
        else:  # her seyin uygun oldugu kosulda ise
            self.now = datetime.datatime.now()  # simdiki zamanı alıyoruz
            # hangi saatte , kac arac kiralandıgını belirtiyoruz
            print("rented a {} vehicle for monthly at {} hourly".format(
                n, self.now.hour))
            self.stock -= n  # kiralanan arac sayısını stoktan dusuyoruz
            return self.now  # fiyatı zamana gore ayarlıcaz

    def returnVehicle(self, request, brand):  # geri gelen araclar fiyat hesaplaması
        "retun a bill"  # secilen kiralamaya gore odenecek para birimini ayarlama
        car_h_price = 50  # saatlik fiyat
        car_d_price = 1000  # gunluk fiyat
        car_m_price = 20000  # aylık fiyat

        # ne zaman , ne kadar sureyle(saat,gun,ay) ,arac sayısı
        rentalTime, rentalBasis, numberOfVehicle = request
        bill = 0

        if brand == "car":
            # kiralanan aracın zamanı , saatlik veya gunluk kiralama turu , arac sayısı varsa islem devam eder
            if rentalTime and rentalBasis and numberOfVehicle:
                self.stock += numberOfVehicle  # aracı stoklara ekledik
                now = datetime.datetime.now()  # bu metot aracın ne zaman gittiğini tutar
                rentalPeriod = now - rentalTime  # musteride kalan zamanı alıyoz

                if rentalBasis == 1:  # daily #gunluk
                    bill = rentalPeriod.second/3600 * car_h_price * \
                        numberOfVehicle  # fiyat hesaplanıyor

                elif rentalBasis == 2:
                    bill = rentalPeriod.second / \
                        (3600*24)*car_d_price * \
                        numberOfVehicle  # fiyat hesaplanıyor

                else:
                    bill = rentalPeriod.second / \
                        ((3600*24)*30) * car_m_price * \
                        numberOfVehicle  # fiyat hesaplanıyor

                if (5 <= numberOfVehicle):
                    print("%20 indirim uygulandı")
                    bill = bill*0.8
                print("Araci getirdiginiz icin tesekkurler")
                print("ucret: {} ₺".format(bill))
                return bill
        else:
            print("Araç geri alinamadi")
            return None


class CarRent(VehicleRent):
    global discount_rate

    def __init__(self, stock):
        super().__init__(stock)

    def discount(self, b):  # indirim
        bill = b - (b*discount_rate)/100
        return bill


class Customer:
    def __init__(self):
        self.cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0

    def requestVehicle(self, brand):  # arac talepleri
        if brand == "car":
            cars = input("Kac tane arac kiralamak istersin? ")
            try:
                cars = int(cars)
            except ValueError:
                print("numeric deger giriniz")
                return -1
            if cars < 1:
                print("0 haric sayi giriniz")
                return -1
            else:
                self.cars = cars
            return self.cars
        else:
            print("Hatalı giriş yaptınız")

    def requestVehicle(self, brand):  # geri gelen araclar
        if brand == "car":
            if self.rentalTime and self.rentalBasis and self.cars:
                return self.rentalTime and self.rentalBasis and self.cars
            else:
                return 0, 0, 0
        else:
            print("hatalı giris yaptınız")
