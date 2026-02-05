# Proyecto Sihyora CanSat 🛰️

## Descripción General

Este proyecto documenta el desarrollo de un CanSat (Satélite Enlatado) - para participar en el Curso-Concurso Mundial de Satelites enlatados 2026 organizado por el Programa Espacial Universitario (PEU) de la Universidad Nacional Autónoma de México (UNAM). El objetivo es diseñar, construir y operar un CanSat que pueda recolectar y transmitir datos atmosféricos durante su descenso desde una altura determinada.

## Estructura del Proyecto

```
SihyoraCansat2026/
├── Hardware/
│   ├── firmware/
│   │   ├── src/              # Código fuente oficial del firmware (.c)
│   │   ├── include/          # Archivos de encabezado (.h)
│   │   └── tests/            # Scripts de prueba del firmware
│   ├── schematics/           # Esquemáticos electrónicos (KiCad, Eagle, etc.)
│   ├── pcb/                  # Archivos de diseño de PCB
│   ├── mechanical/           # Modelos 3D y diseños estructurales
│   └── bom/                  # Lista de materiales (BOM)
│
├── Software/
│   ├── ground_station/
│   │   ├── src/              # Código oficial de la estación terrena
│   │   └── tests/            # Pruebas de la estación terrena
│   ├── data_processing/
│   │   ├── src/              # Scripts de análisis y visualización de datos
│   │   └── tests/            # Pruebas de procesamiento de datos
│   └── utils/                # Módulos de utilidades compartidas
│
├── docs/                     # Documentación general del proyecto
├── .gitignore
└── README.md
```

## Objetivos del Proyecto

- Diseñar y construir un prototipo funcional de CanSat
- Implementar sistemas de telemetría y adquisición de datos
- Desarrollar comunicación confiable entre CanSat y estación terrena
- Analizar datos atmosféricos recolectados durante el vuelo
- Documentar el proceso completo de desarrollo

## Gestion de Proyecto (GitFlow)

Este proyecto utiliza GitFlow como modelo de ramificación para gestionar el desarrollo. Las ramas principales son:

- `main`: Contiene el código de producción estable.
- `develop`: Rama de desarrollo donde se integran nuevas características.
- `feature/`: Ramas para nuevas características específicas.
- `release/`: Ramas para preparar nuevas versiones.
- `hotfix/`: Ramas para correcciones urgentes en producción.
- `fix/`: Ramas para correcciones menores y ajustes.

## Hardware

El directorio `Hardware/` está organizado en:

- **firmware/src/**: Código fuente oficial del firmware embebido (C)
- **firmware/include/**: Archivos de encabezado del firmware
- **firmware/tests/**: Scripts de prueba para validar sensores, comunicación y funciones del firmware
- **schematics/**: Esquemáticos electrónicos del circuito
- **pcb/**: Diseños y archivos de PCB
- **mechanical/**: Diseños de estructura mecánica y modelos 3D
- **bom/**: Lista de materiales (BOM)

## Software

El directorio `Software/` está organizado en:

- **ground_station/src/**: Código oficial del software receptor de la estación terrena
- **ground_station/tests/**: Pruebas y scripts experimentales de la estación terrena
- **data_processing/src/**: Herramientas oficiales de procesamiento y visualización de datos
- **data_processing/tests/**: Pruebas de análisis y procesamiento de datos
- **utils/**: Módulos de utilidades compartidas entre componentes

## Estado de Desarrollo

🚧 **Proyecto en etapa inicial de desarrollo**

Actualmente estableciendo la estructura básica del proyecto. Los componentes de hardware y software se irán agregando progresivamente conforme avance el desarrollo.

## Tecnologías

- **Lenguajes de Programación**: Python, C
- **Microcontroladores**: [Por definir]
- **Sensores**: [Por definir]
- **Comunicación**: [Por definir]

## Contribuciones

Este es un proyecto activo de investigación y desarrollo. La documentación y componentes se actualizarán regularmente.

## Licencia

[Por definir]

---

_Última actualización: [27 de enero de 2026]_
