class SpaceAge:
    SECONDS_PER_EARTH_YEAR = 31_557_600

    ORBITAL_PERIODS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds: int):
        self.seconds = seconds

    def _age_on(self, planet: str) -> float:
        earth_years = self.seconds / self.SECONDS_PER_EARTH_YEAR
        planet_years = earth_years / self.ORBITAL_PERIODS[planet]
        return round(planet_years, 2)

    def on_mercury(self) -> float:
        return self._age_on("mercury")

    def on_venus(self) -> float:
        return self._age_on("venus")

    def on_earth(self) -> float:
        return self._age_on("earth")

    def on_mars(self) -> float:
        return self._age_on("mars")

    def on_jupiter(self) -> float:
        return self._age_on("jupiter")

    def on_saturn(self) -> float:
        return self._age_on("saturn")

    def on_uranus(self) -> float:
        return self._age_on("uranus")

    def on_neptune(self) -> float:
        return self._age_on("neptune")
        pass