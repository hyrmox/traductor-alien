

texto_alien = ['miel, extraterrestre, al, automovil, auto, revestir, MIEL, EXTRATERRESTRE, AL, AUTOMOVIL, AUTO, REVESTIR']

def mensaje(texto_alien):
    alfabeto = u'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z '.split()
    alfa_reverso = u'Z Y X W V U T S R Q P O N M L K J I H G F E D C B A z y x w v u t s r q p o n m l k j i h g f e d c b a '.split()
    codigo = []
    
    for letra in texto_alien[0]:
        if letra in alfabeto:
            for i in range(len(alfabeto)):
                if alfabeto[i] == letra:
                    pos = i
            codigo.append(alfa_reverso[pos])
        else:
            codigo.append(letra)
        
        
    
    traduccion = ''.join(codigo)
    return traduccion

mensaje_traducido = mensaje(texto_alien)

print(mensaje_traducido)

texto_alien2 = input("\ningrese su texto: ")

def mensaje(texto_alien2):
    alfabeto = u'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'.split()
    alfa_reverso = u'Z Y X W V U T S R Q P O N M L K J I H G F E D C B A z y x w v u t s r q p o n m l k j i h g f e d c b a 9 8 7 6 5 4 3 2 1 0'.split()
    codigo = []
    
    for letra in texto_alien2:
        if letra in alfabeto:
            for i in range(len(alfabeto)):
                if alfabeto[i] == letra:
                    pos = i
            codigo.append(alfa_reverso[pos])
        else:
            codigo.append(letra)
        
        
    
    traduccion = ''.join(codigo)
    return traduccion

mensaje_traducido = mensaje(texto_alien2)

print(mensaje_traducido)