import json
import uvicorn
from fastapi import FastAPI, HTTPException
from models import InsuranceRate
from db import load_db

# Создаем экземпляр приложения (create app instance)
app = FastAPI()


# Загрузка тарифов передачей json post запроса (load rates from json post request)
@app.post("/load_rates")
async def load_rates(rates: dict):
    for date, rate_list in rates.items():
        for rate in rate_list:
            await InsuranceRate.update_or_create(
                date=date,
                cargo_type=rate["cargo_type"],
                rate=rate["rate"]
            )
    return {"message": "Rates loaded/updated successfully"}


# Загрузка тарифов из файла (load rates from file)
@app.get("/load_rates")
async def load_rates():
    with open("test_rates.json", "r") as f:
        rates = json.load(f)
        for date, rate_list in rates.items():
            for rate in rate_list:
                await InsuranceRate.update_or_create(
                    date=date,
                    cargo_type=rate["cargo_type"],
                    rate=rate["rate"]
                )
    return {"message": "Rates loaded/updated successfully"}


# Расчет стоимости страховки (calculate insurance cost)
@app.get("/calculate_insurance")
async def calculate_insurance(date: str, cargo_type: str, declared_value: float):
    rate = await InsuranceRate.filter(date=date, cargo_type=cargo_type).first()
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    insurance_cost = declared_value * rate.rate
    return {"insurance_cost": insurance_cost}

# Загрузка БД (load db)
load_db(app)

if __name__ == "__main__":
    # Запуск сервера (run server)
    uvicorn.run(app, host="0.0.0.0", port=8000)
