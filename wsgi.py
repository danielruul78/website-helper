def application(environ, start_response):
    status = '200 OK'
    output = b'Hello from Ubuntu Shell!'

    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [output]
