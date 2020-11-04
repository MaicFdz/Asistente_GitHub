


import os

# Esta linea debe modificarse -> Colocar la ubicacion de nuestra carpeta. Nota: va todo separado con '\\'
os.chdir('C:\\Usuarios\\MiUsuario\\Escritorio\\MiCarpetaDeRepositorio')

os.system('git init')

os.system('git add .')

os.system('git commit --m "nuevoCommit"')

# Esta linea debe modificarse -> Colocar la ruta de nuestro repositorio
os.system('git remote add origin https://github.com/MiUsuario/MiRepositorio')

os.system('git pull origin main')

os.system('git push -f -u origin main')

os.system('pause>nul')