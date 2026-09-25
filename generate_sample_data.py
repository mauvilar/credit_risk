#!/usr/bin/env python3
"""
Script para crear datos de ejemplo anonimizados a partir del dataset completo.
Genera una muestra pequeña (1000 registros) con datos sensibles anonimizados.
"""
import pandas as pd
import numpy as np
from pathlib import Path

# Muestra procesada completa: vive en data/processed/, ignorada por git
backup_path = Path(__file__).resolve().parent / 'data/processed/df_sample.csv'
output_path = Path('data/sample_data.csv')

print("📊 Generando datos de ejemplo anonimizados...")

# Cargar muestra pequeña
df = pd.read_csv(backup_path, nrows=1000)

print(f"✓ Cargadas {len(df)} filas")

# Anonimizar campos sensibles
print("🔒 Anonimizando datos sensibles...")

# IDs aleatorios
df['id'] = np.random.randint(1000000, 9999999, len(df))
df['member_id'] = np.random.randint(1000000, 9999999, len(df))

# Redactar información personal
if 'emp_title' in df.columns:
    df['emp_title'] = 'REDACTED'
if 'desc' in df.columns:
    df['desc'] = ''
if 'url' in df.columns:
    df['url'] = ''
if 'title' in df.columns:
    df['title'] = 'Loan Application'

# Anonimizar códigos postales (solo primeros 2 dígitos)
if 'zip_code' in df.columns:
    df['zip_code'] = df['zip_code'].astype(str).str[:2] + 'xxx'

print(f"✓ Datos anonimizados")

# Guardar
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

file_size = output_path.stat().st_size / (1024 * 1024)
print(f"✓ Archivo guardado: {output_path} ({file_size:.2f} MB)")
print(f"✓ Total de columnas: {len(df.columns)}")
print(f"✓ Total de filas: {len(df)}")

print("\n✅ Datos de ejemplo listos para el repositorio público")
