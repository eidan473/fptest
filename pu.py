hotel=[
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],
    [[],[],[],[],[],[]],   
]





while True:
    print("agendar habitacion")
    print("ver estado del hotel")
    print("vaciar habitacion")
    print("monetizar")
    print("salir")
    op=int(input())
    if op==1:
        nom=input("cual es su nombre")
        print("su nombre es",nom)
        piso=int(input("en que piso quiere agendar"))
        hab=int(input("que habitacion quiere"))
        print("el piso que quiere es",piso,"y la hibatacion que quiere es",hab)
        
        if hotel[piso][hab]==[]:
           hotel[piso][hab]==nom
           print("se agedo su habitacion",nom)
           
        else:
            print("no esta disponible")
    if op==2:
        print("el hotal esta asi")
        for i in hotel:
            print(i)
    if op==3:
        
            
    
        
            