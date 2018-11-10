from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='d872db97834f46589ab9c6b70183b370')
#app = ClarifaiApp()
#CLARIFAI_API_KEY=d872db97834f46589ab9c6b70183b370

def get_relevant_tags(image_url):
    response_data = app.tag_urls([image_url])

    tag_urls = []
    for concept in response_data['outputs'][0]['data']['concepts']:
        tag_urls.append(concept['name'])

    return tag_urls

def get_models(image_url):
    model = app.models.get('general-v1.3')
    image = ClImage(url = image_url)
    response_data = model.predict([image])
    concepts = response_data['outputs'][0]['data']['concepts']
    concept_names = [concept['name'] for concept in concepts]
    longname = ' '.join(concept_names)
    return longname

def age_guesser(image_url):
    model = app.models.get("demographics")
    image = ClImage(url = image_url)
    data = model.predict([image])
    age = data['outputs'][0]['data']['regions'][0]['data']['face']['age_appearance']['concepts'][0]['name']
    # concept_names = [concept['name'] for concept in concepts]
    return age

def ethnicity_guesser(image_url):
    model = app.models.get("demographics")
    image = ClImage(url = image_url)
    data = model.predict([image])
    ethnicity = data['outputs'][0]['data']['regions'][0]['data']['face']['multicultural_appearance']['concepts'][0]['name']
    # concept_names = [concept['name'] for concept in concepts]
    return ethnicity

def isThisFood(image_url):
    model = app.models.get('food-items-v1.0')
    image = ClImage(url= image_url)
    response_data = model.predict([image])
    concepts = response_data['outputs'][0]['data']['concepts']
    concept_names = [concept['name'] for concept in concepts]
    return concept_names

def whichOneIsCuter(image_url1, image_url2):
    img1 = ClImage(url = image_url1, allow_dup_url=True)
    img2 = ClImage(url = image_url2, allow_dup_url=True)
    app.inputs.bulk_create_images([img1, img2])

    cute = app.inputs.search_by_predicted_concepts(concept='cute')
    for i in range(len(cute)): print (cute[i].url)


#print('\n'.join(get_relevant_tags('https://i.ytimg.com/vi/opKg3fyqWt4/hqdefault.jpg')))
