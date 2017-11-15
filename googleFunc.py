# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def sentiment_analysis_3args(target, num, str):
    mcontent = str
    
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    text = mcontent
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

    senti = ""
    if(sentiment.score > 0.5):
        senti = "pos"
    elif(sentiment.score < -0.5):
        senti = "neg"
    else:
        senti = "soso"
    target[num]["sentiment"] = senti


def sentiment_analysis_1arg(text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

    senti = ""
    if(sentiment.score > 0.5):
        senti = "pos"
    elif(sentiment.score < -0.5):
        senti = "neg"
    else:
        senti = "soso"

    return senti

### Unavailable for korean ###
#
# def entity_sentiment_text(text):
#     """Detects entity sentiment in the provided text."""
#     client = language.LanguageServiceClient()

#     if isinstance(text, six.binary_type):
#         text = text.decode('utf-8')

#     document = types.Document(
#         content=text.encode('utf-8'),
#         type=enums.Document.Type.PLAIN_TEXT)

#     # Detect and send native Python encoding to receive correct word offsets.
#     encoding = enums.EncodingType.UTF32
#     if sys.maxunicode == 65535:
#         encoding = enums.EncodingType.UTF16

#     result = client.analyze_entity_sentiment(document, encoding)

#     for entity in result.entities:
#         print('Mentions: ')
#         print(u'Name: "{}"'.format(entity.name))
#         for mention in entity.mentions:
#             print(u'  Begin Offset : {}'.format(mention.text.begin_offset))
#             print(u'  Content : {}'.format(mention.text.content))
#             print(u'  Magnitude : {}'.format(mention.sentiment.magnitude))
#             print(u'  Sentiment : {}'.format(mention.sentiment.score))
#             print(u'  Type : {}'.format(mention.type))
#         print(u'Salience: {}'.format(entity.salience))
#         print(u'Sentiment: {}\n'.format(entity.sentiment))