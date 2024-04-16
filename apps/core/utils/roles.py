from django.utils.translation import ugettext_lazy as _

ADMIN = "admin"
EDITOR = "edit"
SUPERVISOR = "super"
UNDEFINE = "undef"


ORGANIZER_ROLES = (
    (ADMIN, _("administrator")),
    (SUPERVISOR, _("supervisor")),
    (EDITOR, _("editor")),
    (UNDEFINE, _("undefine")),
)

LOGISTIC = "logistic"
CONTROL = "control"
AID = "aid"
GROUND = "ground"
SUPPLY = "supply"

VOLUNTEER_ROLES = (
    (LOGISTIC, _("logistic")),
    (CONTROL, _("control")),
    (AID, _("aid")),
    (SUPPLY, _("supply")),
    (GROUND, _("ground")),
    (UNDEFINE, _("undefine")),
)
