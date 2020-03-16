# python-hh-cv-updater

Your HeadHunter CV will be automatically updated every CV_REFRESH_INTERVAL minutes.

## docker:
docker run -d -e "HH_USERNAME=your_username" -e "HH_PASSWORD=your_password" -e CV_REFRESH_INTERVAL=300 lipunovms/cvupdater:1.0

## docker-compose
Create .env file and define HH_USERNAME, HH_PASSWORD and CV_REFRESH_INTERVAL
docker-compose up -d
