def parse_record(line: str) -> dict:
    city, temperature, date = line.split(";")
    return {"city": city, "temperature": float(temperature), "date": date}
