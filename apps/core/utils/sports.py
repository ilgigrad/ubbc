from django.utils.translation import ugettext_lazy as _

TENNIS = "tennis"
RUN = "running"
TRAIL = "trail"
ULTRA = "ultra"
ATHLE = "atle"
FOOT = "foot"
BIKE = "bike"
SWIM = "swim"
TRIATHLON = "triathlon"
SKIMO = "skimo"
SKI = "ski"
HIKE = "hike"
VERTICAL = "vertical"
WALK = "walk"
MB = "mb"
GRAVEL = "gravel"
CANOE = "canoe"
KAYAK = "kayak"
NORDIC = "nordic"
SKATE = "skate"
RUGBY = "rugby"
RUGBY14 = "rugby14"
RUGBY7 = "rugby7"
FOOT7 = "foot7"
FOOT5 = "foot5"

SPORTS = (
    (RUN, _("running")),
    (TRAIL, _("trail running")),
    (ULTRA, _("ultra trail")),
    (ATHLE, _("athletism")),
    (FOOT, _("football")),
    (TENNIS, _("tennis")),
    (BIKE, _("bicycling")),
    (SWIM, _("swimming")),
    (TRIATHLON, _("triathlon")),
    (SKIMO, _("ski mountaining")),
    (SKI, _("ski")),
    (HIKE, _("hiking")),
    (VERTICAL, _("vertical running")),
    (MB, _("mountain biking")),
    (GRAVEL, _("gravel biking")),
    (CANOE, _("canoe")),
    (KAYAK, _("kayak")),
    (NORDIC, _("nordic ski")),
    (SKATE, _("inline skate")),
    (RUGBY, _("rugby")),
    (RUGBY14, _("rugby 14")),
    (RUGBY7, _("rugby 7")),
    (FOOT7, _("fottball 7")),
    (FOOT5, _("football 5")),
)

_100K = "100k"
_100M = "100m"
_50K = "50k"
_50M = "50m"
_20K = "20k"
_20M = "20m"
_15K = "15k"
_10K = "10k"
_10M = "10m"
_5K = "5k"
SEMI = "semi"
MARATHON = "marathon"

DISTANCES = (
    (_100M, _("100M")),
    (_100K, _("100k")),
    (_50M, _("50M")),
    (_50K, _("50k")),
    (_20M, _("20M")),
    (_20K, _("20k")),
    (_10M, _("10M")),
    (_10K, _("10k")),
    (_5K, _("5k")),
    (MARATHON, _("marathon")),
    (SEMI, _("semi marathon")),
)
