
# Zalando Aktien-WebApp

Diese Webanwendung zeigt den aktuellen Kurs und Verlauf der Zalando-Aktie. Bei einem Kurs von 136 € oder mehr wird ein Feuerwerk angezeigt.

## Dateien

- `app.py`: Flask-Webserver
- `index.html`: HTML-Seite mit Kursanzeige und Feuerwerk
- `kursverlauf.png`: Diagramm des Kursverlaufs
- `README.md`: Anleitung

## Kostenloses Hosting über Render.com

### Voraussetzungen

- GitHub-Konto
- Render.com-Konto

### Schritte

1. Lade alle Dateien in ein öffentliches GitHub-Repository hoch.
2. Gehe zu [render.com](https://render.com) und melde dich an.
3. Klicke auf **New → Web Service**.
4. Wähle dein GitHub-Repository aus.
5. Konfiguriere:
   - **Environment:** Python
   - **Build Command:** `pip install flask matplotlib`
   - **Start Command:** `python app.py`
   - **Region:** z. B. Frankfurt
6. Klicke auf **Create Web Service**.

Render stellt die App unter einer kostenlosen URL bereit.

## Vorschau

Die App zeigt:
- Kursverlauf als Diagramm
- Aktuellen Kurswert
- Feuerwerk bei Kurs ≥ 136 €

