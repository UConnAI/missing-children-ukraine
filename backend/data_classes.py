# FUNCTIONAL NEW KID
from dataclasses import dataclass
from datetime import datetime
import pytz
from typing import Dict, Any, Optional, List


__blood_types = {"A-", "A+", "B+", "B-", "O-", "O+", "AB+", "AB-"}


@dataclass
class Reporter:
    """Dataclass for information about the reporter of the incident

    :param first_name: First name of the reporterrating CodeGenX to more powerful hardware. This will improve inference time and make the service a lot faster. CodeGenX
    :type first_name: str
    :param last_name: Last name of the reporter
    :type last_name: str
    :param relationship: Relationship of the reporter to the victim
    :type relationship: str
    :param nationality: Nationality of the Reporter
    :type nationality: str
    :param country_residence: Current Residence of the Reporter
    :type country_residence: str
    :param phone_number: Phone number of the reporter
    :type phone_number: str
    :param translated_name: Translated name of the reporter to English
    :type translated_name: str
    :param phone_number_2: Second phone number of the reporter
    :type phone_number_2: str
    :param email: Email of the reporter
    :type email: Optional[str]

    :return: None
    :rtype: None
    """

    #  if you are wondering why some args are out of order, @charitarthchugh changed because fields without default values should appear after fields with default values
    first_name: str
    last_name: str
    relationship: str
    date_of_birth: datetime
    nationality: str
    country_residence: str
    phone_number: str
    translated_name: Optional[str] = None
    phone_number_2: Optional[str] = None
    email: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Generate a Reporter class from a dictionary

        :param d: Dictionary with the named parameters to init Reporter as keys
        :type d: Dict[str, Any]
        :return: a Reporter class with
        :rtype: _type_
        """
        return Reporter(**d)


@dataclass
class Child:
    """
    Dataclass for information about reported

    :param first_name: Child's first name
    :type
    :param last_name: Child's last name
    :param  translated_name: Child's Tranaslated name to english
    :param date_birth:  Date of Birth of Child in python's datetime format
    :param gender: male or female only
    :param nationality: Nationality of the missing child
    :param blood _type:  blood type of child
    :param reported:  .... forgot what we doing here
    :param last_seen: Dict of locations where the child was last seen
    :param comment: optional description of child (optional)
    :param picture: picture of child (Optional)
    """

    first_name: str
    last_name: str
    date_of_birth: datetime
    gender: str
    nationality: str
    reported: str
    last_seen: Dict[str, Any]
    translated_name: Optional[str] = None
    blood_type: Optional[str] = None
    comment: Optional[str] = None
    picture: Optional[Any] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        current_date = pytz.utc.localize(datetime.today())
        birth_date = pytz.utc.localize(datetime.strptime(d["date_birth"], "%Y.%m.%d"))

        # Check valid gender
        if not (d["gender"] == "male" or d["gender"] == "female"):
            raise ValueError("No valid gender specified")

        # Check valid blood type
        if "blood_type" in d:
            if not d["blood_type"] in __blood_types:
                raise ValueError("Invalid blood type specified")

        # Check last_seen dionary
        if (
            "date" in d["last_seen"]
            and "country" in d["last_seen"]
            and "city" in d["last_seen"]
        ):
            lastseen_date = pytz.utc.localize(
                datetime.strptime(d["last_seen"]["date"], "%Y.%m.%d")
            )
            if lastseen_date <= birth_date or lastseen_date >= current_date:
                raise ValueError("Invalid last seen date")

            # Check country/city is valid
            # input_city = pytz.timezone(
            #     d["last_seen"]["country"] + "/" + d["last_seen"]["city"]
            # )
        return Child(
            first_name=d["first_name"],
            last_name=d["last_name"],
            date_of_birth=birth_date,
            gender=d["gender"],
            nationality=d["nationality"],
            reported=d["reported"],
            last_seen=lastseen_date,
            translated_name=(d["translated_name"] if d["translated_name"] else None),
            blood_type=d["blood_type"],
            comment=d["comment"],
            picture=d["picture"],
        )


@dataclass
class Event:
    """Dataclass for information about the event
    :param event_type: Type of event
    :type event_type: int
    :param reporter: Reporter of the event
    :type reporter: Reporter
    :param children: Children involved in the event
    :type children: List[Child]

    """

    event_type: int
    reporter: Reporter
    children: List[Child]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """Creates an Event Class from input dionary

        :param d: input dionry to parse
        :type d: Dict[str, Any]
        :return: An properly populated event class
        :rtype: Event
        """
        return Event(
            event_type=d["event_type"],
            reporter=Reporter.from_d(d["reporter"]),
            children=[Child.from_d(c) for c in d["children"]],
        )
