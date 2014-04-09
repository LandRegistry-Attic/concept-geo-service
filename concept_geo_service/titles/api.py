from restless.dj import DjangoResource
from django.contrib.gis.measure import Distance, D
import models
import json

#/titles?partially_contained_by
class TitlesResource(DjangoResource):

    fields = {
        'content': 'content'
        }

    def is_authenticated(self):
        return True

    def prepare(self, data):
        if isinstance(data, models.Title):
            return json.loads(data.content)
        else:
            return data

    def create(self):
        if not self.data.get('content', {}).get('extent'):
            return {}

        #create a new entry
        title = models.Title()
        title.title_number = json.dumps(self.data['content']['title_number'])
        title.content = json.dumps(self.data['content'])
        title.extent = json.dumps(self.data['content']['extent']['geometry'])

        #check if already exists
        existing = models.Title.objects.filter(title_number=title.title_number).first()
        if existing:
            existing.delete()

        #save it
        title.save()
        return title

    # GET /titles
    def list(self):
        near = self.request.GET.get('near', None)
        partially_contained_by = self.request.GET.get('partially_contained_by', None)

        result = None
        if partially_contained_by:
            result =  models.Title.objects.filter(extent__intersects=partially_contained_by)
        elif near:
            return models.Title.objects.filter(extent__distance_lte=(near, D(km=50))).distance(near).order_by('distance')[:25]
        else:
            result = models.Title.objects.all()
        return result
