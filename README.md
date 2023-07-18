<table align="right">
 <tr><td><b><img src="https://github.com/ggwmwgg/ggwmwgg/blob/main/images/us_s.png" height="13" alt=""> English</b></td></tr>
 <tr><td><a href="README_ru.md"><img src="https://github.com/ggwmwgg/ggwmwgg/blob/main/images/ru.png" height="13" alt=""> Русский</a></td></tr>
</table>

## Insurance cost calculator (REST API)

### Description
Microservice for calculating insurance cost depending on cargo type and declared value (DV):
- Rate should load either from file or using JSON structure like below:
```
{
    "2020-06-01": [
        {
            "cargo_type": "Glass",
            "rate": "0.04"
        },
        {
            "cargo_type": "Other",
            "rate": "0.01"
        },
    ],
    "2020-07-01": [
        {
            "cargo_type": "Glass",
            "rate": "0.035"
        },
        {
            "cargo_type": "Other",
            "rate": "0.015"
        },
    ]
}
```
- Service should be able to calculate insurance cost for request using current rate.
- Service returns (DV * rate) depending on cargo type and date in request.
- Service should be deployed inside Docker.
- README.md contains detailed instruction for running service.
- Data should is stored in PostgreSQL.

#### Technologies used:
- *Python*
- *FastApi*
- *Tortoise ORM*
- *PostgreSQL*
- *Docker*
- *Docker-compose*

#### Configuration:
- Install ```requirements.txt```.
- Set your PostgreSQL connection data in ```db.env```.
- Set your healthcheck data in ```docker-compose.yml``` on line 23.
- Build containers with ```docker-compose build```.
- Run containers with ```docker-compose up```, you can add ```-d``` flag to run in background.
- Visit ```http://127.0.0.1:8000/```.
- To stop containers use ```docker-compose down```.

#### Usage:
- To load data from file use ```get``` request on ```/load_data```.
- To load data from json-object use ```post``` request on ```/load_data```.
- To calculate insurance use ```post``` request on ```/calculate_insurance```, pass ```date```, ```cargo_type``` and ```declared_value``` as parameters.

#### Contributing
Pull requests are welcome. For major changes please open an issue first.