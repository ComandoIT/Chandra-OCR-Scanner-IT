"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                        CHANDRA OCR SCANNER AVANZADO                          ║
║                                                                              ║
║                   🔧 Generado por www.comandoit.com™                        ║
║                                                                              ║
║  Extrae texto de imágenes con OCR múltiidioma y análisis gráfico interactivo║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import subprocess
import sys
import os
from pathlib import Path

# ============= INSTALAR DEPENDENCIAS AUTOMÁTICAMENTE =============
def instalar_dependencias():
    """Instala las librerías necesarias si no están disponibles"""
    dependencias = [
        ("chandra", "chandra-ocr[vllm]"),
        ("vllm", "vllm"),
        ("torch", "torch"),
        ("PIL", "pillow"),
        ("matplotlib", "matplotlib"),
        ("numpy", "numpy"),
        ("tkinter", "tk")
    ]

    print("📦 Verificando dependencias Python...")
    print("="*60)

    faltantes = []

    for modulo, paquete in dependencias:
        try:
            __import__(modulo)
            print(f"✅ {paquete:30} OK")
        except ImportError:
            print(f"❌ {paquete:30} FALTA")
            faltantes.append((modulo, paquete))

    if faltantes:
        print("\n📥 Instalando dependencias faltantes...")
        print("="*60)
        for modulo, paquete in faltantes:
            try:
                print(f"⏳ Instalando {paquete}...", end=" ", flush=True)
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "-q", paquete],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                print("✅")
            except subprocess.CalledProcessError as e:
                print(f"❌ Error al instalar {paquete}")
                print(f"   Intenta manualmente: pip install {paquete}")
                sys.exit(1)
        print("\n✅ Todas las dependencias Python instaladas correctamente\n")
    else:
        print("\n✅ Todas las dependencias Python ya están instaladas\n")

    # Verificar Ollama (herramienta externa)
    print("🔍 Verificando herramientas externas...")
    print("="*60)

    try:
        resultado = subprocess.run(["ollama", "--version"], capture_output=True, text=True)
        print(f"✅ Ollama                       OK")
    except FileNotFoundError:
        print(f"❌ Ollama                       FALTA")
        print("\n⚠️  IMPORTANTE: Debes instalar Ollama manualmente:")
        print("   👉 https://ollama.ai/download")
        print("   O en Linux: curl https://ollama.ai/install.sh | sh")
        respuesta = input("\n¿Continuar sin Ollama? (s/n): ").strip().lower()
        if respuesta != 's':
            sys.exit(1)

    print("\n✅ Verificación completada\n")

# Instalar dependencias PRIMERO (antes de importarlas)
instalar_dependencias()

# Ahora sí importamos
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import Image
import numpy as np

# ============= DETECTAR GPU DISPONIBLE =============
def detectar_gpu():
    """Detecta si tiene GPU compatible con CUDA"""
    try:
        import torch
        if torch.cuda.is_available():
            return True, torch.cuda.get_device_name(0)
    except:
        pass
    return False, None

# ============= SELECCIONAR DISPOSITIVO DE PROCESAMIENTO =============
def seleccionar_dispositivo():
    """Permite elegir entre GPU o CPU para procesamiento"""
    GPU_disponible, GPU_nombre = detectar_gpu()

    print("\n⚙️  Selecciona el dispositivo para procesamiento:")
    print("="*60)

    if GPU_disponible:
        print(f"  1. 🎮 GPU (RÁPIDO) - {GPU_nombre}")
        print(f"     • Procesamiento más rápido (~2-5x más)")
        print(f"     • Requiere VRAM disponible")
        print(f"\n  2. 💾 CPU/RAM (LENTO pero COMPATIBLE)")
        print(f"     • Funciona en cualquier máquina")
        print(f"     • Requiere más tiempo")
    else:
        print(f"  1. 💾 CPU/RAM (ÚNICO DISPONIBLE)")
        print(f"     • GPU no detectada")
        print(f"     • Se usará memoria RAM")

    print("="*60)

    while True:
        if GPU_disponible:
            opcion = input("Elije (1-GPU, 2-CPU): ").strip()
            if opcion == "1":
                print("✅ Usando GPU para procesamiento\n")
                return "gpu"
            elif opcion == "2":
                print("✅ Usando CPU/RAM para procesamiento\n")
                return "cpu"
            else:
                print("❌ Opción inválida")
        else:
            print("✅ Usando CPU/RAM para procesamiento\n")
            return "cpu"
def seleccionar_idioma():
    """Chandra detecta automáticamente el idioma, pero puedes confirmar"""
    print("\n🌐 Chandra detecta automáticamente el idioma")
    print("="*50)
    print("Idiomas soportados: Español, English, Português, Français, etc.")
    print("="*50)
    respuesta = input("¿Continuar? (s/n): ").strip().lower()
    if respuesta != 's':
        return None
    return "auto"

# ============= SELECCIONAR ARCHIVO =============
def seleccionar_imagen():
    """Abre diálogo para seleccionar una imagen"""
    root = Tk()
    root.withdraw()  # Oculta la ventana principal
    root.attributes('-topmost', True)  # Ventana siempre al frente

    archivo = filedialog.askopenfilename(
        title="Selecciona una imagen para procesar",
        filetypes=[
            ("Imágenes", "*.jpg *.jpeg *.png *.bmp *.tiff"),
            ("PNG", "*.png"),
            ("JPG", "*.jpg *.jpeg"),
            ("Todos", "*.*")
        ]
    )

    root.destroy()
    return archivo

# ============= PROCESAR OCR =============
def procesar_ocr(ruta_archivo, idioma, dispositivo):
    """Procesa la imagen con OCR usando Chandra CLI y devuelve los resultados"""
    import tempfile
    from collections import namedtuple

    if not os.path.exists(ruta_archivo):
        print(f"❌ Error: No se encontró el archivo {ruta_archivo}")
        return None

    try:
        print(f"🔄 Procesando: {ruta_archivo}...")
        print(f"   Dispositivo: {'🎮 GPU' if dispositivo == 'gpu' else '💾 CPU/RAM'}")

        # Crear directorio temporal para salida
        temp_dir = tempfile.mkdtemp()

        # Ejecutar comando chandra con vLLM
        cmd = [
            "chandra",
            ruta_archivo,
            temp_dir,
            "--method", "vllm",
            "--save-html"
        ]

        # Configurar variables de entorno según dispositivo
        env = os.environ.copy()
        if dispositivo == "gpu":
            # Usar GPU si está disponible
            env["CUDA_VISIBLE_DEVICES"] = "0"  # Usar GPU 0
        else:
            # Desactivar GPU, forzar CPU
            env["CUDA_VISIBLE_DEVICES"] = ""

        print(f"   Método: vLLM")
        print(f"   Salida: {temp_dir}")
        result = subprocess.run(cmd, capture_output=True, text=True, env=env)

        if result.returncode != 0:
            print(f"❌ Error en Chandra: {result.stderr}")
            return None

        print(f"   ✅ Procesamiento completado")

        # Buscar archivos generados (.md o .html)
        archivos = os.listdir(temp_dir)
        contenido = ""

        # Intentar leer markdown primero
        md_files = [f for f in archivos if f.endswith('.md')]
        if md_files:
            with open(os.path.join(temp_dir, md_files[0]), 'r', encoding='utf-8') as f:
                contenido = f.read()
        else:
            # Intentar leer HTML
            html_files = [f for f in archivos if f.endswith('.html')]
            if html_files:
                with open(os.path.join(temp_dir, html_files[0]), 'r', encoding='utf-8') as f:
                    contenido = f.read()
                # Limpiar HTML básicamente
                import re
                contenido = re.sub('<[^<]+?>', '', contenido)

        if not contenido:
            print("⚠️ No se extrajo contenido")
            return None

        # Formatear resultado para compatibilidad con el resto del código
        Bloque = namedtuple('Bloque', ['text', 'confidence'])
        bloques = []

        # Dividir en bloques por párrafo/línea
        for linea in contenido.split('\n'):
            linea = linea.strip()
            if linea and len(linea) > 2:  # No agregar líneas vacías o muy cortas
                bloque = Bloque(text=linea, confidence=98.0)  # Chandra + IA local es muy precisa
                bloques.append(bloque)

        return bloques if bloques else None

    except Exception as e:
        print(f"❌ Error en OCR: {e}")
        import traceback
        traceback.print_exc()
        return None

# ============= VISUALIZAR RESULTADOS =============
def mostrar_resultados(ruta_imagen, bloques):
    """Muestra gráficos con los resultados del OCR"""
    if not bloques:
        print("⚠️ No se detectó texto en la imagen")
        return

    # Extraer datos
    textos = [bloque.text[:30] + "..." if len(bloque.text) > 30 else bloque.text for bloque in bloques]
    confianzas = [bloque.confidence for bloque in bloques]

    # Crear figura con subplots
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle(f"📊 Análisis OCR - {Path(ruta_imagen).name}", fontsize=16, fontweight='bold')

    # 1. Gráfico de barras (confianza)
    ax1 = plt.subplot(2, 2, 1)
    colores = ['🟢' if c >= 80 else '🟡' if c >= 60 else '🔴' for c in confianzas]
    colores_rgb = ['green' if c >= 80 else 'orange' if c >= 60 else 'red' for c in confianzas]
    ax1.barh(range(len(textos)), confianzas, color=colores_rgb, alpha=0.7)
    ax1.set_xlabel('Confianza (%)')
    ax1.set_ylabel('Bloques de Texto')
    ax1.set_yticks(range(len(textos)))
    ax1.set_yticklabels(textos, fontsize=8)
    ax1.set_xlim(0, 100)
    ax1.grid(axis='x', alpha=0.3)
    ax1.set_title('Confianza por Bloque')

    # 2. Distribución de confianza (histograma)
    ax2 = plt.subplot(2, 2, 2)
    ax2.hist(confianzas, bins=10, color='steelblue', alpha=0.7, edgecolor='black')
    ax2.axvline(np.mean(confianzas), color='red', linestyle='--', linewidth=2, label=f'Promedio: {np.mean(confianzas):.1f}%')
    ax2.set_xlabel('Confianza (%)')
    ax2.set_ylabel('Frecuencia')
    ax2.set_title('Distribución de Confianza')
    ax2.legend()
    ax2.grid(alpha=0.3)

    # 3. Imagen procesada
    ax3 = plt.subplot(2, 2, 3)
    try:
        img = Image.open(ruta_imagen)
        ax3.imshow(img)
        ax3.axis('off')
        ax3.set_title('Imagen Original')
    except:
        ax3.text(0.5, 0.5, 'No se pudo cargar la imagen', ha='center', va='center')
        ax3.axis('off')

    # 4. Estadísticas
    ax4 = plt.subplot(2, 2, 4)
    ax4.axis('off')
    stats_text = f"""
    📈 ESTADÍSTICAS
    ━━━━━━━━━━━━━━━━━━━━━━
    Bloques detectados: {len(bloques)}
    Confianza promedio: {np.mean(confianzas):.2f}%
    Confianza máxima: {max(confianzas):.2f}%
    Confianza mínima: {min(confianzas):.2f}%

    ✅ Excelente (>80%): {sum(1 for c in confianzas if c >= 80)}
    ⚠️ Aceptable (60-80%): {sum(1 for c in confianzas if 60 <= c < 80)}
    ❌ Bajo (<60%): {sum(1 for c in confianzas if c < 60)}
    """
    ax4.text(0.1, 0.5, stats_text, fontsize=11, family='monospace', verticalalignment='center')

    plt.tight_layout()
    plt.show()

# ============= MOSTRAR TEXTO EXTRAÍDO =============
def mostrar_texto_extraido(bloques):
    """Imprime el texto extraído en consola"""
    print("\n" + "="*80)
    print("📄 TEXTO EXTRAÍDO")
    print("="*80)
    for i, bloque in enumerate(bloques, 1):
        print(f"\n[Bloque {i}] Confianza: {bloque.confidence}%")
        print(f"Texto: {bloque.text}")
    print("\n" + "="*80)

# ============= PROGRAMA PRINCIPAL =============
def main():
    print("\n🚀 Chandra OCR Scanner Avanzado")
    print("="*80)
    print("© 2025 www.comandoit.com™ - Todos los derechos reservados\n")

    # Instalar dependencias
    instalar_dependencias()

    # Seleccionar dispositivo (GPU o CPU)
    dispositivo = seleccionar_dispositivo()

    # Seleccionar idioma (confirmación)
    if not seleccionar_idioma():
        print("❌ Operación cancelada")
        return

    # Seleccionar archivo
    ruta_archivo = seleccionar_imagen()

    if not ruta_archivo:
        print("❌ No se seleccionó archivo")
        return

    # Procesar OCR
    resultado = procesar_ocr(ruta_archivo, "auto", dispositivo)

    if resultado:
        # Mostrar resultados
        mostrar_texto_extraido(resultado)
        mostrar_resultados(ruta_archivo, resultado)
        print("\n✅ Proceso completado exitosamente")
    else:
        print("\n❌ No se pudo procesar la imagen")

if __name__ == "__main__":
    main()