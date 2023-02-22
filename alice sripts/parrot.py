import os
import pymongo
import datetime

from utils import replace_dotted_keys

MONGODB_URI = os.environ.get('MONGODB_URI')
db = None
logs_collection = None
if MONGODB_URI:
    # w=0 means fast non-blocking write
    client = pymongo.MongoClient(MONGODB_URI, w=0)
    db = client.get_default_database()
    logs_collection = db.get_collection('logs')

def handler(event, context):
    """
    Entry-point for Serverless Function.
    :param event: request payload.
    :param context: information about current execution context.
    :return: response to be serialized as JSON.
    """
    text = 'Hello! I\'ll repeat anything you say to me.'
    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        text = event['request']['original_utterance']

    response = {
        'version': event['version'],
        'session': event['session'],
        'response': {
            # Respond with the original request or welcome the user if this is the beginning of the dialog and the request has not yet been made.
            'text': text,
            # Don't finish the session after this response.
            'end_session': 'false'
        },

    }

    utterance = event.get('request', {}).get('original_utterance')
    if logs_collection and utterance != 'None':
        logs_collection.insert_one({
            'request': replace_dotted_keys(event),
            'response': response,
            'time': datetime.datetime.now(),
            'app_id': event['session'].get('application', {}).get('application_id'),
            'utterance': utterance,
            'response_text': response['response']['text'],
        })
    
    
    return response 