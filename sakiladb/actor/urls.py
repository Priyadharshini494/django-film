from django.urls import path, include
from django.conf import settings

APP_NAME = "actor"
url_patterns_data = {
    "android/v1/": {
        "prefix": "android/v1/",
        "urls_path": APP_NAME + ".android.v1.urls",
        "name": "ActorAndroidV1",
    },
    "web/v1/": {
        "prefix": "web/v1/",
        "urls_path": APP_NAME + ".web.v1.urls",
        "name": "ActorWebV1",
    },
}
urlpatterns = []

for url_prefix, url_pattern_data in url_patterns_data.items():
    if url_prefix in settings.ACTIVE_URL_PREFIX[APP_NAME]:
        urlpatterns.append(
            path(
                url_pattern_data["prefix"],
                include(url_pattern_data["urls_path"]),
                name=url_pattern_data["name"],
            )
        )
