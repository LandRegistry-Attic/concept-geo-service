from restless.dj import DjangoResource
import models
import json

#/titles?partially_contained_by
class TitlesResource(DjangoResource):

    fields = {
        'extent': 'extent',
        'content': 'content'
        }

    def is_authenticated(self):
        return True

    def prepare(self, data):
        return json.loads(data.content)

    def create(self):

        #create a new entry
        title = models.Title()
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
        # elif near:
        #     return models.Title.objects.filter(extent__contains=partially_contained_by)
        else:
            result = models.Title.objects.all()
        return result

        # partially_contained_by = self.request.GET.get('partially_contained_by', None)
        # return partially_contained_by
        #
        # print partially_contained_by
        #
        # return models.Title.objects.all()
