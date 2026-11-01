text = "My name is Nik and I work at Infobus in Prague."

entities = [
    {"entity_group": "PER", "score": 0.99, "start": 11, "end": 14},
    {"entity_group": "ORG", "score": 0.62, "start": 29, "end": 36},
    {"entity_group": "LOC", "score": 0.98, "start": 40, "end": 46},
]

def extract_words(text, entities):
    words = []
    for entity in entities:
        words.append(text[entity["start"]:entity["end"]])
    return words

def filter_by_score(entities, min_score):
    filtered_entities = []
    for entity in entities:
        if entity["score"] >= min_score:
            filtered_entities.append(entity)
    return filtered_entities

def group_by_type(text, entities):
    grouped_entities = {}
    for entity in entities:
        entity_type = entity["entity_group"]
        if entity_type not in grouped_entities:
            grouped_entities[entity_type] = []
            if entity_type in grouped_entities:
                grouped_entities[entity_type].append(entity)
            else:
                grouped_entities[entity_type] = entity
    return grouped_entities

a = group_by_type(text, entities)