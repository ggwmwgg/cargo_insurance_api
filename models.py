from datetime import datetime
from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model


class InsuranceRate(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    cargo_type = fields.CharField(max_length=255)
    rate = fields.FloatField()

    class Meta:
        table = "cargo_insurance_rates"

    def __str__(self):
        return f"{self.date} {self.cargo_type} {self.rate}"

    def __repr__(self):
        return self.__str__()

