from calculos import operaciones

# division = operaciones.division(10, 2)

import sys
import os

print("📂 Archivo main.py ejecutándose desde:", os.getcwd())
print("🔍 Rutas que Python está usando para buscar módulos:")
for p in sys.path:
    print("   ", p)