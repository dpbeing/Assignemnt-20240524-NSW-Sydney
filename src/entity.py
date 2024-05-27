from dataclasses import dataclass

@dataclass
class Address:
    street: str
    suburb: str
    state: str
    post_code: int

@dataclass
class Employee:
    full_name: str
    company: str
    birth_date: str
    age: int
    salary: str
    salary_bucket: str
    phone: int
    mobile: int
    email: str
    address: Address
