# ddfuse

## What DDFuse is supposed to be

I would like DDFuse to exist as an open source project for people to learn with as well as a platform to share financial news with everyone

### Build instructions
* Requirements - Django, Channels, channels_redis, docker, redis (all dependencies can be viewed in req.txt)

1. Clone repository to location of your choice
2. Cd into the location of manage.py
3. Run the command `python manage.py runserver`
4. Browse to 127.0.0.1:8000/chats/general
5. Open another terminal and run `docker run -p 6379:6379 -d redis:5` to start the docker redis server
6. Open an incognito window at 127.0.0.1:8000/chats/general and send a message to your other window

I have put a temporary secret key in the settings file so that it could be shared. Production key will be regenerated when we actually put the thing in production.

### Contributing

Anybody and everybody can fork the repository and make a pull request. I'll review it and apply.

For places to start check out issues. If you'd like to make your own issue and solve it feel free.


### Production Timeline

- [x] Secure ddfuse domain
- [ ] Complete chat channels
- [ ] Complete a few blog posts
- [ ] Decide on hosting platform (Digital Ocean? Google Cloud?)
- [ ] Backend running
- [ ] Front end running
- [ ] Site live
