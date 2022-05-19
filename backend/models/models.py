from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

_blood_types = {"A-", "A+", "B+", "B-", "O-", "O+", "AB+", "AB-"}


@dataclass
class Reporter:
    """
    Dataclass for information about the reporter of the incident

    :param first_name: First name of the reporter
    :param last_name: Last name of the reporter
    :param translated_name: Translated name of the reporter to English
    :param date_of_birth: Date of birth of the reporter
    :param nationality: Nationality of the Reporter
    :param country_residence: Current Residence of the Reporter
    :param phone_number: Phone number of the reporter
    :param phone_number_2: Second phone number of the reporter
    :param email: Email of the reporter
    :param relationship: Relationship of the reporter to the victim
    """
    first_name: str
    last_name: str
    date_of_birth: datetime
    nationality: str
    country_residence: str
    phone_number: str
    relationship: str
    translated_name: Optional[str] = None
    phone_number_2: Optional[str] = None
    email: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """
        Generate a Reporter class from a dictionary

        :param d: Dictionary with all of the infomration needed to populate reporter
        :return: a properly populated Reporter class
        """

        current_date = pytz.utc.localize(datetime.today())

        # Validating date of birth
        date_of_birth = pytz.utc.localize(datetime.strptime(d["date_of_birth"], "%Y/%m/%d"))
        if date_of_birth > current_date:
            raise ValueError("Birth date out of range")

        return Reporter(
            first_name=d["first_name"],
            last_name=d["last_name"],
            translated_name=d["translated_name"],
            date_of_birth=date_of_birth,
            nationality=d["nationality"],
            country_residence=d["country_residence"],
            phone_number=d["phone_number"],
            phone_number_2=d["phone_number_2"] if "phone_number_2" in d and d["phone_number_2"] else None,
            email=d["email"] if "email" in d and d["email"] else None,
            relationship=d["relationship"]
        )


@dataclass
class Child:
    """
    Dataclass for information about reported

    :param first_name: Child's first name
    :param last_name: Child's last name
    :param translated_name: Child's Tranaslated name to english
    :param date_birth:  Date of Birth of Child in python's datetime format
    :param gender: male or female only
    :param nationality: Nationality of the missing child
    :param blood _type:  blood type of child
    :param reported: If the loss had been reported to authorities
    :param last_seen: Dict of locations where the child was last seen
    :param comment: optional description of child (optional)
    :param picture: picture of child (Optional)
    """

    first_name: str
    last_name: str
    date_of_birth: datetime
    gender: str
    nationality: str
    reported: bool
    last_seen: Dict[str, Any]
    translated_name: Optional[str] = None
    blood_type: Optional[str] = None
    comment: Optional[str] = None
    picture: Optional[Any] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """
        Create a Child class from the specific dictionary

        :param d: the dictionary containing all of the information needed
        :return: a Child class with the information from the dictionary
        """

        global _blood_types

        current_date = pytz.utc.localize(datetime.today())

        # Validate birth date
        date_of_birth = pytz.utc.localize(datetime.strptime(d["date_of_birth"], "%Y/%m/%d"))
        if date_of_birth > current_date:
            raise ValueError("Birth date out of range")

        # Check valid gender
        if not (d["gender"] == "male" or d["gender"] == "female"):
            raise ValueError("No valid gender specified")

        # Check valid blood type
        if "blood_type" in d:
            if not d["blood_type"] in _blood_types:
                raise ValueError("Invalid blood type specified")

        # Check last_seen dictionary
        last_seen = {}
        if "date" in d["last_seen"] and "country" in d["last_seen"] and "city" in d["last_seen"]:
            lastseen_date = datetime.strptime(d["last_seen"]["date"], "%Y/%m/%d %H:%M:%S")

            # Verify location, get latitude and longitude and localize lastseen_date to the timezone in reported ares
            geolocator = Nominatim(user_agent="http")
            location = geolocator.geocode(f"{d['last_seen']['city']}, {d['last_seen']['country']}")
            obj = TimezoneFinder()
            local_timezone = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            local_timezone = pytz.timezone(local_timezone)
            lastseen_date = local_timezone.localize(lastseen_date)

            # Verify that the last seen date is within the correct range
            if lastseen_date <= date_of_birth or lastseen_date >= current_date:
                raise ValueError("Invalid last seen date")

            # After data has been verified and preprocessed save
            last_seen = {
                "date": lastseen_date,
                "country": d["last_seen"]["country"],
                "city": d["last_seen"]["city"]
            }

        return Child(
            first_name=d["first_name"],
            last_name=d["last_name"],
            translated_name=d["translated_name"] if "translated_name" in d and d["translated_name"] else None,
            date_of_birth=date_of_birth,
            gender=d["gender"],
            nationality=d["nationality"],
            blood_type=d["blood_type"] if "blood_type" in d and d["blood_type"] else None,
            reported=d["reported"],
            last_seen=last_seen,
            comment=d["comment"] if "comment" in d and d["comment"] else None,
            picture=d["picture"] if "picture" in d and d["picture"] else None
        )


@dataclass
class Event:
    """
    Dataclass for information about the event

    :param event_type: Type of event
    :param reporter: Reporter of the event
    :param children: Children involved in the event
    """

    event_type: int
    reporter: Reporter
    children: List[Child]

    @staticmethod
    def from_dict(d: Dict[str, Any]):
        """
        Creates an Event Class from input dictionary

        :param d: input dictionary with the information about the event
        :return: A properly populated Event class
        """
        return Event(
            event_type=d["event_type"],
            reporter=Reporter.from_dict(d["reporter"]),
            children=[Child.from_dict(c) for c in d["children"]],
        )
