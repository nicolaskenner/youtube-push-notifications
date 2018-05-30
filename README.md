# youtube-push-notifications
A callback server for YouTube Push Notifications using Bottle

#### A basic NGINX configuration
```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name example.com www.example.com;

    location / {
        proxy_pass http://localhost:8000;
    }
}
```

## Resources
[ElementTree](https://docs.python.org/3.6/library/xml.etree.elementtree.html) for parsing XML
[YouTube's Guide](https://developers.google.com/youtube/v3/guides/push_notifications)
[Bottle Docs](https://bottlepy.org/docs/dev/)
[PubSubHubbub Specification](https://pubsubhubbub.github.io/PubSubHubbub/pubsubhubbub-core-0.4.html)
