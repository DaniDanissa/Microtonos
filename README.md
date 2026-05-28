# 🎵 Simulador de Microtonos en Python

Este es un proyecto interactivo desarrollado en **Python** que simula un sistema de gestión y reproducción de frecuencias sonoras (microtonos) a través de la consola de comandos de Windows. 

El programa permite controlar un "banco" limitado de microtonos disponibles, activarlos para reproducir melodías secuenciales utilizando el hardware del equipo y recuperarlos posteriormente para liberar espacio en el sistema.

---

## 🚀 Características

* **Gestión de recursos:** Control dinámico de microtonos activos y libres (con un límite máximo de 25).
* **Reproducción de audio nativa:** Utiliza la librería integrada `winsound` para emitir pitidos reales (`Beep`) con frecuencias y duraciones controladas a través del hardware.
* **Validación de entradas:** Cuenta con estructuras `try-except` para capturar errores si el usuario introduce valores no numéricos.
* **Simulación de patrones melódicos:** Al activar los microtonos, el script recorre de forma cíclica una lista de frecuencias predefinidas generando variaciones en el sonido.

---

## 🛠️ Requisitos del Sistema

Para poder ejecutar este simulador y escuchar el audio correctamente, asegúrate de cumplir con lo siguiente:

* **Sistema Operativo:** Únicamente **Windows** (debido a que la librería `winsound` es nativa de esta plataforma).
* **Python:** Versión 3.x o superior instalada.

---

## 💻 Instrucciones de Uso

1. **Clona este repositorio** en tu máquina local o descarga el archivo `.py`:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
Navega a la carpeta del proyecto:Bashcd TU_REPOSITORIO
Ejecuta el script desde la consola o terminal de Windows:Bashpython simulador_microtonos.py
Interactúa con el menú interactivo ingresando las opciones del 1 al 5.🕹️ Funciones del PanelOpciónAcciónDescripción1Ver microtonos libresMuestra en pantalla cuántos microtonos tienes disponibles del total.2Activar microtonosPermite elegir cuántos microtonos encender para reproducir la secuencia de sonido.3Recuperar microtonosDesactiva los microtonos en uso para devolverlos al banco disponible.4Monitorear sonidoIndica cuántos microtonos se encuentran activos "vibrando en el ambiente".5SalirCierra de manera segura el bucle y finaliza el programa.💡 Nota de Corrección Técnica[!TIP]Si planeas realizar modificaciones en el código original, ten en cuenta que en la Opción 3, la llamada a la función de sonido debe escribirse como winsound.Beep(440, 150) (con B mayúscula), ya que Python distingue entre mayúsculas y minúsculas y winsound.beep provocará un error de ejecución en Windows.
***

### 📝 ¿Cómo agregarlo a GitHub?
1. Crea un nuevo archivo en la raíz de tu repositorio llamado exactamente `README.md`.
2. Copia todo el bloque de texto gris de arriba y pégalo dentro de ese archivo.
3. Recuerda cambiar `TU_USUARIO` y `TU_REPOSITORIO` por los datos reales de tu enlace de GitHub. ¡Y listo! Tu proyecto se verá muy profesional.
