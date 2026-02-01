# Proyecto Sihyora CanSat 🛰️

## Descripción General

Este proyecto documenta el desarrollo de un CanSat (Satélite Enlatado) - para participar en el Curso-Concurso Mundial de Satelites enlatados 2026 organizado por el Programa Espacial Universitario (PEU) de la Universidad Nacional Autónoma de México (UNAM). El objetivo es diseñar, construir y operar un CanSat que pueda recolectar y transmitir datos atmosféricos durante su descenso desde una altura determinada.

## Estructura del Proyecto

```
cansat-project/
├── hardware/          # Diseños de hardware, esquemáticos y archivos PCB
├── software/          # Firmware, código de estación terrena y procesamiento de datos
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

El directorio `hardware/` contendrá:

- Esquemáticos electrónicos
- Diseños de PCB
- Selección e integración de sensores
- Diseños de estructura mecánica
- Lista de materiales (BOM)
- Firmware embebido para microcontrolador
- Código de adquisición de datos de sensores
- Protocolos de transmisión de telemetría

## Software

El directorio `software/` contendrá:


- Software receptor de estación terrena
- Herramientas de procesamiento y visualización de datos

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
