def body(timezone, language, time, locale, supportedDirectives, orgId, deviceId, userId, textQuery, textResponse, id, requestId, responseTime, challenge) -> str:
    msg = {
        "request":{
            "confidences":{},
            "nbest_aligned_entities":[],
            "domain":"unknown",
            "params":{
                "target_dialogue_state":"None",
                "time_zone":timezone,
                "language":language,
                "allowed_intents":[],
                "timestamp": time,
                "dynamic_resource":{},
                "locale":locale
            },
            "intent":"unknown",
            "frame":{},
            "nbest_transcripts_entities":[],
            "context":{
                "supportedDirectives":supportedDirectives,
                "orgId":orgId,
                "userType":"machine",
                "deviceId":deviceId,
                "userId":userId
            },
            "nbest_transcripts_text":[],
            "form":{},
            "entities":[],
            "text":textQuery,
            "history":[]
        },
        "slots":{},
        "params":{
            "target_dialogue_state":"None",
            "time_zone":"None",
            "language":"None",
            "allowed_intents":[],
            "timestamp":"None",
            "dynamic_resource":{},
            "locale":"None"
        },
        "frame":{},
        "dialogue_state":"unknown",
        "directives":[
            {
                "name":"reply",
                "type":"view",
                "payload":{
                    "text":textResponse,
                    "group":0
                },
                "id":id
            },
            {
                "name":"speak",
                "type":"action",
                "payload":{
                    "text":textResponse
                }
            },
            {
                "name":"sleep",
                "type":"action",
                "payload":{
                    "delay":0
                }
            }
        ],
        "form":{},
        "history":[
            {
                "request":{
                    "confidences":{},
                    "nbest_aligned_entities":[],
                    "domain":"unknown",
                    "params":{
                        "target_dialogue_state":"None",
                        "time_zone":timezone,
                        "language":language,
                        "allowed_intents":[],
                        "timestamp":time,
                        "dynamic_resource":{},
                        "locale":locale
                    },
                    "intent":"unknown",
                    "frame":{},
                    "nbest_transcripts_entities":[],
                    "context":{
                        "supportedDirectives":supportedDirectives,
                        "orgId":orgId,
                        "userType":"machine",
                        "deviceId":deviceId,
                        "userId":userId
                    },
                    "nbest_transcripts_text":[],
                    "form":{},
                    "entities":[],
                    "text":textQuery,
                    "history":[]
                },
                "slots":{},
                "params":{
                    "target_dialogue_state":"None",
                    "time_zone":"None",
                    "language":"None",
                    "allowed_intents":[],
                    "timestamp":"None",
                    "dynamic_resource":{},
                    "locale":"None"
                },
                "frame":{},
                "dialogue_state":"unknown",
                "directives":[
                    {
                        "name":"reply",
                        "type":"view",
                        "payload":{
                            "text":textResponse,
                            "group":0
                        },
                        "id":id
                    },
                    {
                        "name":"speak",
                        "type":"action",
                        "payload":{
                            "text":textResponse
                        }
                    },
                    {
                        "name":"sleep",
                        "type":"action",
                        "payload":{
                            "delay":0
                        }
                    }
                ],
                "form":{},
                "history":[]
            }
        ],
        "request_id":requestId,
        "response_time":responseTime,
        "challenge":challenge
    }

    return msg

