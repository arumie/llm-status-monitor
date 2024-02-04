from llmstatusmonitor.configuration import configuration


if configuration.env == 'mock':
    from mockfirestore import MockFirestore

    db = MockFirestore()
    db.reset()
else:
    from google.cloud import firestore
    db = firestore.Client()
