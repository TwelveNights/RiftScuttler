# RiftScuttler

## Required Resources
[Slack](riftscuttler.slack.com)
[Riot Games API](https://developer.riotgames.com/api/methods)

Save your static files such as css and js files in /static/ folder. Run 
```
python manage.py collectstatic
```
This will migrate the files over to static_cdn for local use.

Run the following on the command line to create a superuser:
```
python manage.py createsuperuser
```
