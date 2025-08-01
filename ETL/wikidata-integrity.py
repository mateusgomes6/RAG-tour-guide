from wikidata.client import Client

def get_wikidata_info(entity_id):
    client = Client()
    entity = client.get(entity_id, load=True)
    
    data = {
        'label': entity.label,
        'description': entity.description,
        'claims': {}
    }
    
    for prop, value in entity.attributes.get('claims', {}).items():
        prop_label = client.get(prop).label
        data['claims'][prop_label] = []
        for v in value:
            if isinstance(v.get('mainsnak', {}).get('datavalue', {}).get('value', {}), dict):
                if 'id' in v['mainsnak']['datavalue']['value']:
                    item = client.get(v['mainsnak']['datavalue']['value']['id'])
                    data['claims'][prop_label].append(item.label)
    
    return data