from abidria.entities import Picture
from .models import ORMScene
from .entities import Scene


class SceneRepo(object):

    def _decode_db_scene(self, db_scene):
        if not db_scene.picture:
            picture = None
        else:
            picture = Picture(small_url=db_scene.picture.small.url,
                              medium_url=db_scene.picture.medium.url,
                              large_url=db_scene.picture.large.url)

        return Scene(id=db_scene.id,
                     title=db_scene.title,
                     description=db_scene.description,
                     picture=picture,
                     latitude=db_scene.latitude,
                     longitude=db_scene.longitude,
                     experience_id=db_scene.experience_id)

    def get_scenes(self, experience_id):
        db_scenes = ORMScene.objects.filter(experience_id=experience_id)
        scenes = []
        for db_scene in db_scenes:
            scenes.append(self._decode_db_scene(db_scene))
        return scenes
