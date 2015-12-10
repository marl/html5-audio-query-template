HTML5 Audio Query Template
==========================

A skeleton website built with Flask and HTML5 Audio, that can be used for building any query-by-humming-like service.

![Screen Capture](http://i.imgur.com/S2k8VH5.png)

## Running

    python runserver.py

## Hacking

### Backend

The web UI will upload a WAV file to the server; you can then process the file using your Python code [here](https://github.com/marl/html5-audio-query-template/blob/master/voice/views.py#L18-L28), and return the result as JSON.

### Frontend

The JSON object will be retrieved back to the browser, and you can edit [here](https://github.com/marl/html5-audio-query-template/blob/master/voice/templates/index.html#L10-L13) to change what to do with the result. By default, it shows the JSON in a textarea.