from wikidata.client import Client

def get_wikidata_info(entity_id):
    client = Client()
    entity = client.get(entity_id, load=True)
    
    data = {
        'label': entity.label,
        'description': entity.description,
        'claims': {}
    }