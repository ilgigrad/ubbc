from datetime import date

from django.utils.translation import ugettext_lazy as _

BB = "BB"
EA = "EA"
PO = "PO"
BE = "BE"
MI = "MI"
CA = "CA"
JU = "JU"
ES = "ES"
SE = "SE"
M0 = "M0"
M1 = "M1"
M2 = "M2"
M3 = "M3"
M4 = "M4"
M5 = "M5"
M6 = "M6"
M7 = "M7"
M8 = "M8"
M9 = "M9"
M10 = "M10"


CATEGORIES = (
    (BB, _("baby athlé")),
    (EA, _("éveil athlétique")),
    (PO, _("poussin")),
    (BE, _("benjamin")),
    (MI, _("minnime")),
    (CA, _("cadet")),
    (JU, _("junior")),
    (ES, _("espoir")),
    (SE, _("Senior")),
    (M0, _("master 0")),
    (M1, _("master 1")),
    (M2, _("master 2")),
    (M3, _("master 3")),
    (M4, _("master 4")),
    (M5, _("master 5")),
    (M6, _("master 6")),
    (M7, _("master 7")),
    (M8, _("master 8")),
    (M9, _("master 9")),
    (M10, _("master 10")),
)

EURO_CATEGORIES = (
    (BB, _("baby athlé")),
    (EA, _("éveil athlétique")),
    (PO, _("U12")),
    (BE, _("U14")),
    (MI, _("U16")),
    (CA, _("U18")),
    (JU, _("U20")),
    (ES, _("U23")),
    (SE, _("Senior")),
    (M0, _("master 0")),
    (M1, _("master 1")),
    (M2, _("master 2")),
    (M3, _("master 3")),
    (M4, _("master 4")),
    (M5, _("master 5")),
    (M6, _("master 6")),
    (M7, _("master 7")),
    (M8, _("master 8")),
    (M9, _("master 9")),
    (M10, _("master 10")),
)

MAX_AGE_CATEGORIES = {
    BB: (0, 6),
    EA: (7, 9),
    PO: (10, 11),
    BE: (12, 13),
    MI: (14, 15),
    CA: (16, 17),
    JU: (18, 19),
    ES: (20, 22),
    SE: (23, 34),
    M0: (35, 39),
    M1: (40, 44),
    M2: (45, 49),
    M3: (50, 54),
    M4: (55, 59),
    M5: (60, 64),
    M6: (65, 69),
    M7: (70, 74),
    M8: (75, 79),
    M9: (80, 84),
    M10: (85, 99),
}


def get_category(*, birth: int, year: int = None):
    if year is None:
        year = date.today().year
    age = year - birth
    for category, age_interval in MAX_AGE_CATEGORIES.items():
        if age >= age_interval[0] and age <= age_interval[1]:
            return category


M = "M"
F = "F"
N = "N"
X = "X"

GENDERS = (
    (M, _("male")),
    (F, _("female")),
    (N, _("non binary")),
    (X, _("other")),
)
