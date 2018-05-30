from bottle import route, run, request, default_app, abort
import xml.etree.ElementTree as XML

secret = 'some_url_safe_secret'

namespaces = {
    'yt': 'http://www.youtube.com/xml/schemas/2015',
    'xmlns': 'http://www.w3.org/2005/Atom'
}


@route('/callback', method='get')
@route('/callback', method='post')
def index():
    if request.method == 'POST':
        response = request.body.read().decode('utf-8')
        root = XML.fromstring(response)

        for entry in root.findall('xmlns:entry', namespaces=namespaces):
            video_id = entry.find('yt:videoId', namespaces=namespaces).text
            title = entry.find('xmlns:title', namespaces=namespaces).text
            link = entry.find('xmlns:link', namespaces=namespaces).get('href')
            print(video_id, title, link)

        # Do Something Here

        return 'Goodly'

    try:
        mode = request.query['hub.mode']
        challenge = request.query['hub.challenge']
        verify_token = request.query['hub.verify_token']
    except KeyError:
        abort(404)

    if mode == 'subscribe' and verify_token == secret:
        return challenge
    abort(404)


if __name__ == '__main__':
    """For Development"""
    run(host='localhost', port=8080, debug=True)

# For Production
app = default_app()
