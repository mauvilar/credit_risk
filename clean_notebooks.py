#!/usr/bin/env python3
"""Script para limpiar outputs de notebooks Jupyter"""
import json
import sys
from pathlib import Path

def clean_notebook(notebook_path):
    """Limpia outputs de un notebook"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Limpiar outputs
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'code':
            cell['outputs'] = []
            cell['execution_count'] = None
    
    # Guardar
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    return notebook_path

if __name__ == '__main__':
    notebooks_dir = Path('notebooks')
    cleaned = []
    
    for nb_file in notebooks_dir.glob('*.ipynb'):
        clean_notebook(nb_file)
        cleaned.append(nb_file.name)
        print(f"✓ Cleaned: {nb_file.name}")
    
    print(f"\n✓ Total notebooks cleaned: {len(cleaned)}")
