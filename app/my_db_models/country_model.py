from app.extentions import db


class Country(db.Model):
    """ A Mysql Table Wrote With Flask SQLAlchemy for Storing an Country """
    __tablename__ = "country"
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(250), nullable=False, unique=True)
    about = db.Column(db.Text, nullable=True)
    iso2 = db.Column(db.String(100))
    phone_cod = db.Column(db.String(100))
    capital = db.Column(db.String(100))
    currency = db.Column(db.String(100))
    city = db.relationship("City", backref="country")

    def __repr__(self):
        """ Return Name of the Country """
        return f'<country {self.country_name}>'

    def __init__(self, country_name, about, iso2, phone_cod, capital, currency):
        """
        Storing A Country Data into the Mysql Database
        :param country_name: Name of the Country
        :type country_name: str
        :param about: Useful information about this country
        :type about: str
        :param iso2: Iso2(COD) of this Country
        :type iso2: str
        :param phone_cod: Phone Code of this Country
        :type phone_cod: str
        :param capital: Capital of this country
        :type capital: str
        :param currency: Currency symbol of this country
        :type currency: str
        """
        self.country_name = country_name
        self.about = about
        self.iso2 = iso2
        self.phone_cod = phone_cod
        self.capital = capital
        self.currency = currency
