import json
import uuid
import flask
import calendar, time

from config import logic
from constructJson import body, healthCheck
from crypto import decrypt
from flask import Flask, jsonify, request

server = Flask(__name__)


@server.route('/parse', methods=['POST'])
def parse():    
    decryptMsg = decrypt(request.get_data().decode('utf-8'))
    getRequest = json.loads(decryptMsg)
    textQuery = getRequest['text']
    orgId = getRequest['context']['orgId']
    userId = getRequest['context']['userId']
    supportedDirectives = getRequest['context']['supportedDirectives']
    deviceId = getRequest['context']['deviceId']
    timezone = getRequest['params']['time_zone']
    timestamp = getRequest['params']['timestamp']
    language = getRequest['params']['language']
    locale = getRequest['params']['locale']
    challenge = getRequest['challenge']

    body = constructResponse(textQuery, orgId, userId, supportedDirectives, deviceId, timezone, timestamp, language, locale, challenge)
    return body


@server.route('/parse', methods=['GET'])
def health_check():
    encrypted_challenge: str = request.args.get('challenge')
    decryptMsg = decrypt(encrypted_challenge)
    msg = healthCheck(decryptMsg)
    return msg


def constructResponse(textQuery, orgId, userId, supportedDirectives, deviceId, timezone, timestamp, language, locale, challenge) -> str:
    epochtime = calendar.timegm(time.gmtime())
    id = str(uuid.uuid4())
    requestId = str(uuid.uuid4())
    responseTime = 0.01

    textResponse = logic(textQuery)

    msg = body(timezone, language, epochtime, locale, supportedDirectives, orgId, deviceId, userId, textQuery, textResponse, id, requestId, responseTime, challenge)

    return msg
