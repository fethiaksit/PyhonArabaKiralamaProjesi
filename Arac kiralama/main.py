from rent import CarRent,Customer
car = CarRent(100)
customer = Customer()

main_menu = True
while True:
    if main_menu:
        print("""
        *****Arac Seciniz*****
        A. Araba Menu
        B. Cikis
        """)
        main_menu=False
        choice = input("Seciniz:  ")
    if choice == "A" or "a":
       
        print("""
            ***Arac Menu***
            1. Bulunan Arac sayısı
            2. Saatlik fiyat 100₺
            3. Gunluk fiyat 1000₺
            4.Arac iade et
            5.Menuye Dön
            6.Cikis""")
        choice=input("Secim yapiniz: ")
        try:
                choice= int(choice)
        except ValueError:   
            print("Numeric secim yapınız")
            continue
        if choice ==1:
            car.displayStock()    
            choice="A"
        elif choice==2:
            customer.rentalTime = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis=1
            main_menu=True
            print("--------------------------------------")
        elif choice==3:
            customer.rentalTime = car.rentdaily(customer.requestVehicle("car"))
            customer.rentalBasis=2
            main_menu=True
            print("--------------------------------------")
        elif choice ==4:
            car.returnVehicle(customer.requestVehicle("car"),"car")
            customer.rentalBasis,customer.rentalTime,customer.cars=0,0,0
            main_menu=True
        elif choice==5:
            main_menu=True
            
        elif choice ==6:
            break    
        else:
            print("gecersiz")       

    elif choice == "B" or "b":
        break    

    else:
        print("Yanlis Giris Yaptınıza")    