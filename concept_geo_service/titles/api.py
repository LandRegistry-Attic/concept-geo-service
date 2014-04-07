from restless.dj import DjangoResource
import models 

#/titles?partially_contained_by
class TitlesResource(DjangoResource):

    fields = {
        'extent': 'extent',
        'content': 'content'   
        }

    # GET /titles
    def list(self):
        return models.Title.objects.all()        