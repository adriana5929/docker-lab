# Docker Lab con WSL2 y Ubuntu

## Este proyecto implementa un entorno de desarrollo basado en contenedores Docker utilizando WSL2 y Ubuntu sobre Windows.


## Tecnologías Utilizadas

- WSL2
- Ubuntu
- Docker
- Nginx
- Node.js
- PostgreSQL
- pgAdmin 4
- Jupyter Lab
- Git & GitHub


---

# Arquitectura del Proyecto

```text
Windows
│
├── WSL2
│   └── Ubuntu
│
└── Docker Compose
    ├── nginx
    ├── node-app
    ├── postgres
    ├── pgadmin
    └── jupyter
```

---


# Estructura del Proyecto

```text
docker-lab/
│
├── nginx/
├── node-app/
├── postgres/
├── jupyter/
├── .env
├── docker-compose.yml
└── README.md
```

---

# Instalación

## Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

## Entrar al proyecto

```bash
cd docker-lab
```

## Levantar contenedores

```bash
docker compose up -d
```



# Servicios

| Servicio | Puerto |
|---|---|
| Nginx | 8080 |
| Node.js | 3000 |
| PostgreSQL | 5432 |
| pgAdmin | 5050 |
| Jupyter | 8888 |

---

# Evidencias



## Nginx funcionando

<img width="932" height="488" alt="evidenciasdocker-ps png" src="https://github.com/user-attachments/assets/265853de-4769-4cee-8ce5-d5a987d1f478" />

## API Node.js

<img width="1064" height="266" alt="evidenciasnode-api png (2)" src="https://github.com/user-attachments/assets/582cc3a8-fbc9-40e8-b29d-8464d8778728" />


## pgAdmin

<img width="1802" height="858" alt="evidenciaspgadmin png" src="https://github.com/user-attachments/assets/9672dc46-6976-46fa-90d2-9398603cc131" />



## Jupyter Lab

<img width="1852" height="831" alt="evidenciasjupyter png" src="https://github.com/user-attachments/assets/f14fa524-349d-4469-ab53-084931062fe5" />

## contenedores activos

<img width="297" height="57" alt="image" src="https://github.com/user-attachments/assets/4b9405f2-f6d7-4097-b743-3ba27223d8c7" />

<img width="497" height="67" alt="image" src="https://github.com/user-attachments/assets/eebccb32-8da8-4205-86a4-e51d429b676c" />



---
---
# Laboratorio 2 - Gestión y Optimización de Procesos en Linux




## Objetivo

Monitorear, administrar y optimizar procesos en Linux utilizando herramientas como htop, stress, kill, nice, renice y cpulimit.

## Herramientas Utilizadas

* Docker
* Ubuntu
* htop
* stress
* stress-ng
* cpulimit
* Python 3

## Actividades Realizadas

### 1. Reconocimiento del entorno

Se analizaron los procesos del sistema mediante:

```bash
top
htop
ps aux
pstree
```

Se identificaron PID, usuario, prioridad, uso de CPU y memoria.

### 2. Generación de carga

#### Saturación de CPU

```bash
stress --cpu 4 --timeout 60s
```

#### Saturación de Memoria

```bash
stress --vm 2 --vm-bytes 256M --timeout 60s
```

#### Competencia de procesos

```bash
stress --cpu 2 &
python3 -c "while True: pass" &
dd if=/dev/zero of=/dev/null bs=1M &
```

### 3. Optimización e intervención

#### Finalización de procesos

```bash
kill PID
kill -9 PID
killall stress
```

#### Prioridades

```bash
nice -n 19 stress --cpu 2 &
renice -n 15 -p PID
```

#### Limitación de CPU

```bash
cpulimit -p PID -l 30
```

## Script Utilizado

Archivo:

```text
scripts/cpu_stress.py
```

Contenido:

<img width="578" height="295" alt="image" src="https://github.com/user-attachments/assets/954c989b-2703-4ee2-814e-b165a66d5bce" />


## Evidencias

Las capturas del laboratorio se encuentran en:

htop en reposo

<img width="921" height="480" alt="image" src="https://github.com/user-attachments/assets/3b943573-a4b8-4258-9966-286644329142" />


Arbol de procesos en el sistema

<img width="921" height="506" alt="image" src="https://github.com/user-attachments/assets/458459f2-1950-4229-97ba-597e2d9fb771" />


consumo artificial de memoria usando: stress --cpu 4 --timeout 60s  

<img width="921" height="501" alt="image" src="https://github.com/user-attachments/assets/39d9e144-0979-42a0-a0cf-7c09ce432efa" />


PID de mayor consumo

<img width="763" height="349" alt="image" src="https://github.com/user-attachments/assets/7182acc4-e2c7-431d-a390-e5dd2fbb865b" />

Procesos con carga artificial 

<img width="921" height="616" alt="image" src="https://github.com/user-attachments/assets/bad51c30-cda7-43f0-98b9-6b2a202cead9" />

Cambio de valores de NI = 19, NI =20

<img width="820" height="373" alt="image" src="https://github.com/user-attachments/assets/579785f0-fb0a-479d-bf2c-ea21008248fc" />



## Conclusiones

Las herramientas de administración de procesos permiten identificar cuellos de botella, controlar procesos problemáticos y optimizar el uso de recursos del sistema operativo Linux.

## Integrantes del grupo

| Nombre completo | Código | Correo institucional |
|-----------------|--------|----------------------|
| Adriana Milena Noscue Dagua  |     2477336  |         adriana.noscue@correounivalle.edu.co             |
| Sebastián Cucalon Astorquiza |     2477344  |           sebastian.cucalon@correounivalle.edu.co        |
