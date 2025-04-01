# Projekt Informatik - webserver

## Überblick

Das Projekt **PI_webserver** wurde im Rahmen eines Kurses entwickelt. 

## Anforderungen

Im "Projekt Informatik" soll eine verteilte Anwendung erstellt werden. Das können z.B. Spiele, mobile Anwendungen oder auch Datenbankanwendungen mit Client und Server sein

## Ziele der Entwicklung
Ziel des Projekts ist es, eine webbasierte Anwendung zu realisieren, die:
- Benutzer-Authentifizierung und -Verwaltung bietet
- Die Erstellung und Anzeige von Beiträgen (Posts) ermöglicht
- Eine PostgreSQL-Datenbank zur persistenten Speicherung nutzt
- Die Anwendung in einer containerisierten Umgebung (Docker) betreibt

## Verwendete Technologien

- **Entwickelt auf Windows**
- **Flask** – Web-Framework für Python
- **SQLAlchemy** – ORM für Datenbankzugriffe
- **PostgreSQL 14** – Datenbank zur persistenten Datenspeicherung
- **Docker & Docker Compose** – Containerisierung der Anwendung und Datenbank

## Installation und Setup

### Voraussetzungen
- **Entwickelt auf Python 3.13**
- **Docker / Docker Desktop**

### Instalations Anleitung

1. **Projekt herunterladen**  
   Entpacken des Projekt-Archiv (z.B. `PI_webserver.zip`) in einen gewünschten Ordner.

2. **Docker / Docker Desktop**
   - Herunterladen
   - PostgreSQL (ab Version 14) Docker-Image herunterladen 
   ``docker pull postgres:14.*`` 
   - ``docker-compose.yaml`` ausführen
3. **VEnv & Requirements**
    ```bash
   python -m venv venv
   pip install -r requirements.txt
4. Falls Flask-Debug mode gewünscht ist
   ```bash
   in webserver/webinterface/webinterface.py 
   run([...] debug=False) in debug=True ändern  

### Nutzung der Anwendung 
- **Dashboard:**
Nach erfolgreicher Anmeldung gelangst du zum Dashboard, wo du Beiträge erstellen, anzeigen und bearbeiten kannst.
- **Benutzer-Authentifizierung:**
Benutzer-Authentifizierung:
Die Anwendung unterstützt Registrierung, Login und Logout.
- **Posts**
Erstelle neue Beiträge, sieh dir deine eigenen Beiträge an und erkunde alle veröffentlichten Beiträge über die entsprechenden Routen.

### Struktur

- Anwendung läuft lokal und ist im Netzwerk zu erreichen unter 
   ```html
   http://127.0.0.1:5000
-  Datenbank läuft in einem Docker-Container
