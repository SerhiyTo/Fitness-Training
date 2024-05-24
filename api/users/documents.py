from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from api.users.models import CoachProfile


@registry.register_document
class CoachProfileDocument(Document):
    class Index:
        name = "coach_profile"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = CoachProfile
        fields = [
            "first_name",
            "last_name",
            "email",
            "experience",
            "rating",
            "price",
            "specialization",
        ]
