# python-hh-cv-updater

Your HeadHunter CV will be automatically updated every CV_REFRESH_INTERVAL minutes.

Link to Github https://github.com/lipunovms/python-hh-cv-updater
## docker:

`docker build -t my-updater .`

`docker run -d -e "HH_USERNAME=your_username" -e "HH_PASSWORD=your_password" -e CV_REFRESH_INTERVAL=300 my-updater`

or you can use ready image

`docker run -d -e "HH_USERNAME=your_username" -e "HH_PASSWORD=your_password" -e CV_REFRESH_INTERVAL=300 lipunovms/cvupdater:1.0`

## docker-compose
You need to set in .env file  variables HH_USERNAME, HH_PASSWORD and CV_REFRESH_INTERVAL

`docker-compose up -d`
