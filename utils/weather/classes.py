from dataclasses import field
from typing import ClassVar, Type

from marshmallow_dataclass import dataclass
from enum import Enum
from marshmallow import Schema, EXCLUDE


class WindDirection(Enum):
    North = 0, 'Северный'
    Northeast = 45, 'Северо-восточный'
    East = 90, 'Восточный'
    Southeast = 135, 'Юго-восточный'
    South = 180, 'Южный'
    Southwest = 225, 'Юго-западный'
    West = 270, 'Западный'
    Northwest = 315, 'Северо-западный'

    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.description = description
        return obj


@dataclass
class WeatherDescription:
    description: str

    class Meta:
        unknown = EXCLUDE


@dataclass
class Main:
    temp: int  # Температура
    feels_like: int  # температура по ощущениям
    humidity: int  # влажность воздуха
    pressure: int  # атмосферное давление

    @property
    def mmHG(self):
        """ Преобразуем hPa в мм ртутного столба"""
        return round(self.pressure / 1.333)

    class Meta:
        unknown = EXCLUDE


@dataclass
class Wind:
    speed: float
    deg: float
    gust: float

    @property
    def direction_wind(self):
        degrees = round(self.deg / 45) * 45
        if degrees == 360:
            degrees = 0
        return WindDirection(degrees).description

    class Meta:
        unknown = EXCLUDE


@dataclass
class Clouds:
    all: int  # %


@dataclass
class Weather:
    location: str = field(metadata={'data_key': 'name'})
    weather: list[WeatherDescription]
    main: Main
    wind: Wind
    clouds: Clouds

    @property
    def description(self):
        return ','.join(w.description for w in self.weather)

    Schema: ClassVar[Type[Schema]] = Schema

    class Meta:
        unknown = EXCLUDE
