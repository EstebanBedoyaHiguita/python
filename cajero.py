contrasena = 123
intentos=3

while intentos != 0 : 
    num1 = int(input("Ingrese su contraseña"));
    if num1 == contrasena:
        print("Su contraseña es correcta")
        break
    else:
        intentos -= 1
        print("Contraseña incorrecta, le queda", intentos , "intentos");
if intentos == 0:
    print("Cuenta bloqueada")