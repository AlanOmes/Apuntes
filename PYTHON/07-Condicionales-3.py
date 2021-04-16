# Operadores and y or

# and -> revisa que se cumplan todas las condiciones // or -> revisa que al menos se cumpla una

usuario_logueado = True
usuario_admin = True

if usuario_logueado and usuario_admin:
    print('Administrador')
elif usuario_logueado:
    print ('Acceso al sistema')
else:
    print ('Debes iniciar sesión')