

# YFCC15M_downloader
Un subconjunto de YFCC100M. Herramientas, scripts de verificación y enlaces de almacenamiento en la nube para descargar los conjuntos de datos.

---

Seguimos el proceso de preparación de conjuntos de datos de [DeCLIP](https://github.com/Sense-GVT/DeCLIP) *[aquí](https://github.com/Sense-GVT/DeCLIP/blob/main/docs/dataset_prepare.md#prepare-datasets)*.

1. Primero, descarga el archivo de etiquetas de YFCC15M de DeCLIP **'yfcc15m_clean_open_data.json'** desde [Google Drive](https://drive.google.com/file/d/1P-2_dHNc_c5XMY0A-89iNF5Cz_Y_Cfsy/view?usp=sharing).
2. Extrae las URLs del archivo JSON y divídelas en varios archivos de lista de URL para la descarga utilizando **split_download_task.py**.
3. Descarga las imágenes directamente desde las URLs utilizando **auto_download.bat** (Aquí utilizamos [Wget](https://eternallybored.org/misc/wget/), es posible que necesites instalarlo). El archivo `.bat` es para Windows, y es posible que debas crear un script de shell si usas Linux. O simplemente, ¡descarga desde los enlaces a continuación!
    - Puedes detener el proceso y reiniciarlo después si algo sale mal. Wget omitirá los archivos descargados y limpiará los archivos de registro.
    - Los errores se registrarán en los archivos de registro. Antes de reiniciar la descarga, se recomienda ejecutar **clean_err_file_from_logs.py** para filtrar y eliminar los archivos incorrectos.
    
4. Verifica las imágenes descargadas utilizando **check_images.py**.

---
Información del conjunto de datos:

- El conjunto de datos debería contener 15,388,848 imágenes.
- Logramos descargar 15,061,747 de ellas.
- Espacio total ocupado: 867.73G.

Enlaces de almacenamiento en la nube:

- [📂split_1](https://pan.baidu.com/s/1-vD-QpMkH0hVrApmXhnO3g?pwd=kn8w)✅
- [📂split_2](https://pan.baidu.com/s/1JMB6Vn2z3I2a38cAfqZ6lQ?pwd=1dim)✅
- [📂split_3](https://pan.baidu.com/s/1Ile-PpaatDrvDaNrdGMiHQ?pwd=xr69)✅
- [📂split_4](https://pan.baidu.com/s/1cAePRDhZ6QDny5dKjIeGVw?pwd=wkhh)✅
- [📂split_5](https://pan.baidu.com/s/1rWL4bX5svAClg6mQuy_YOw?pwd=fxp6)✅
- [📂split_6](https://pan.baidu.com/s/11qU_QMst5yrGEcSdhvbRPA?pwd=l7k8)✅
- [📂split_7](https://pan.baidu.com/s/1nIOsquJzZMUNTfFd4bsz9Q?pwd=ijvu)✅
- [📂split_8](https://pan.baidu.com/s/1RN95BgJ0DK7oZ3PlqDNyfg?pwd=a4qm)✅
- [📂split_9](https://pan.baidu.com/s/1leKjj_VqCewtq3IVc332VA?pwd=ubz1)✅
- [📂split_10](https://pan.baidu.com/s/1UtzDUvDops4lyfPc4i9AJg?pwd=hp6j)✅
- [📂split_11](https://pan.baidu.com/s/1KrkROY842NRr6dAmUTQ59g?pwd=ewi9)✅
- [📂split_12](https://pan.baidu.com/s/1ZbtiDuaGhBTWbEsPrkJr2g?pwd=2vn6)✅
- [📂split_13](https://pan.baidu.com/s/1aj2Uyy9dWGMwlx_mtVwQHg?pwd=0xgh)✅
- [📂split_14](https://pan.baidu.com/s/1H11kNWMUDy1TEhL2bTW9zA?pwd=2c4k)✅
- [📂split_15](https://pan.baidu.com/s/1lN4cb7gcwWDfEoxsueoRfg?pwd=n38e)✅
- [📂split_16](https://pan.baidu.com/s/1gq86juTG8pOc3ngWEcx6zQ?pwd=n8af)✅
---

Si algún enlace deja de funcionar, por favor deja un mensaje en las issues.

Actualización 2024-11-13: Puedes utilizar la herramienta [bypy](https://github.com/houtianze/bypy) para descargar los archivos desde Baidu Yun Web Drive.
