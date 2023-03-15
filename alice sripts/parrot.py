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
    move = 0
    text = 'Hello! I\'ll repeat anything you say to me.'
    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        text = event['request']['original_utterance']
        if text == "встань":
            text = "Вуф"
            move = 1
        elif text == "повернись":
            text = "Ваф"
            move = 2
        elif text == "проси":
            text = "Ваф ваф"
            move = 3
        elif text == "станцуй":
            text = "Ууууууу"
            move = 4
        elif text == "потанцуй":
            text = "Вуф вуф"
            move = 5
        else:
            text = "Я не знаю такой команды"


        



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
            'time': datetime.datetime.now(),
            "move": move,
        })
    
    
    return response 
