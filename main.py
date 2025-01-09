from fastapi import FastAPI, HTTPException

app = FastAPI()

# Hàm kiểm tra số nguyên tố
def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Route trả về phiên bản
@app.get("/get_version")
def get_version():
    return {"version": "1.0.0"}

# Route kiểm tra số nguyên tố
@app.get("/check_prime/{number}")
def check_prime(number: int):
    if number < 0:
        raise HTTPException(status_code=400, detail="Number must be a non-negative integer")
    result = is_prime(number)
    return {"number": number, "is_prime": result}
