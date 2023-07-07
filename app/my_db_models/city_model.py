from app.extentions import db
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class City(db.Model):
    """
    A Mysql Table Wrote With Flask SQLAlchemy for Storing Citys
    in a Country
    """
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer)
    show_id = db.Column(db.String(250), nullable=False, unique=True, default=generate_uuid)
    city_name = db.Column(db.String(100), nullable=False)
    population = db.Column(db.Float)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    about = db.Column(db.Text)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"))
    cafe = db.relationship("Cafe", backref='city')

    def __repr__(self):
        """ Return City Name """
        return f'<city {self.city_name}>'

    def __init__(self, city_id, city_name, population, lat, lng, about, country_id):
        """
        Storing A City Data into the Mysql Database
        :param city_id: city_id is id of the city in https://openweathermap.org/ API
        :type city_id: int
        :param city_name: Name of City
        :type city_name: str
        :param population: Population of the city
        :type population: int
        :param lat: Latitude of the city
        :type lat: float
        :param lng: Longitude of the city
        :type lng: float
        :param about: useful Information About the city
        :type about: str
        :param country_id: Foreign Key for country of this city
        :type country_id: int
        """
        self.city_id = city_id
        self.city_name = city_name
        self.population = population
        self.lat = lat
        self.lng = lng
        self.about = about
        self.city_id = country_id
