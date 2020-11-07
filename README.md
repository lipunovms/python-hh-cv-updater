# python-hh-cv-updater

Your HeadHunter CV will be automatically updated every `CV_REFRESH_INTERVAL` minutes.

Link to Github https://github.com/lipunovms/python-hh-cv-updater

## docker

```
docker build -t my-updater .
docker run -d -e "HH_USERNAME=your_username" -e "HH_PASSWORD=your_password" -e CV_REFRESH_INTERVAL=300 my-updater`
```
or you can use ready image:

```
docker run -d -e "HH_USERNAME=your_username" -e "HH_PASSWORD=your_password" -e HH_RESUMEID=your_cv_id lipunovms/cvupdater:1.0
```

## docker-compose

You have to fill values in the `.env` file:
```
HH_USERNAME=your_username
HH_PASSWORD=your_password
HH_RESUMEID=your_cv_id
CV_REFRESH_INTERVAL=300
```
and bring services up:
```
docker-compose up -d
```

You can take your CV ID in the URL of you CV page, e.g in `https://hh.ru/resume/87cb...4154` the last part `87cb...4154` is required CV ID.
