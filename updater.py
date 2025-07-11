import requests
import os
import sys
import tkinter as tk
from tkinter import messagebox

def check_for_updates():
    CURRENT_VERSION = "1.0.0"  # Cambiar en cada release
    REPO = "tuusuario/calculadora-actualizable"  # Reemplaza con tu repo

    try:
        # Obtener última versión desde GitHub API
        response = requests.get(
            f"https://api.github.com/repos/{REPO}/releases/latest"
        )
        data = response.json()
        latest_version = data["tag_name"]
        download_url = data["assets"][0]["browser_download_url"]  # URL del .exe

        if latest_version > CURRENT_VERSION:
            if messagebox.askyesno(
                "Actualización Disponible",
                f"Versión {latest_version} disponible. ¿Descargar ahora?"
            ):
                download_update(download_url)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo verificar actualizaciones: {str(e)}")

def download_update(url):
    try:
        # Descarga en carpeta temporal
        temp_path = os.path.join(os.environ["TEMP"], "calculadora_update.exe")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(temp_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        # Ejecuta el instalador y cierra la app
        os.startfile(temp_path)
        sys.exit()
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al descargar: {str(e)}")
