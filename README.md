

```
#Superheroes
This project is a Flask API for managing heroes, their powers, and the relationships between them. The API allows users to create, read, update, and delete heroes and powers, as well as manage the associations between them.

## Features

- **Hero Management**: Create, retrieve, update, and delete heroes.
- **Power Management**: Create, retrieve, update, and delete powers.
- **Hero-Power Associations**: Manage the relationship between heroes and powers, including strength classification.
- **Input Validation**: Ensure data integrity through validation rules.

## ER Diagram

The relationships between models are defined as follows:

- A `Hero` has many `Power`s through `HeroPower`.
- A `Power` has many `Hero`s through `HeroPower`.
- A `HeroPower` belongs to a `Hero` and a `Power`.

## Validations

- **HeroPower**: `strength` must be one of the following values: 'Strong', 'Weak', 'Average'.
- **Power**: `description` must be present and at least 20 characters long.

## API Routes

The following routes are available in the API:

### 1. Get All Heroes
**GET** `/heroes`  
Returns a list of all heroes.

Example response:
```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  ...
]
```

### 2. Get Hero by ID
**GET** `/heroes/:id`  
Returns a specific hero and their associated powers.

Example response:
```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "hero_id": 1,
      "id": 1,
      "power": {
        "description": "gives the wielder the ability to fly through the skies at supersonic speed",
        "id": 2,
        "name": "flight"
      },
      "power_id": 2,
      "strength": "Strong"
    }
  ]
}
```

### 3. Get All Powers
**GET** `/powers`  
Returns a list of all powers.

Example response:
```json
[
  {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  },
  ...
]
```

### 4. Get Power by ID
**GET** `/powers/:id`  
Returns a specific power.

Example response:
```json
{
  "description": "gives the wielder super-human strengths",
  "id": 1,
  "name": "super strength"
}
```

### 5. Update Power
**PATCH** `/powers/:id`  
Updates an existing power.

Request body:
```json
{
  "description": "Valid Updated Description"
}
```
Example response:
```json
{
  "description": "Valid Updated Description",
  "id": 1,
  "name": "super strength"
}
```

### 6. Create HeroPower
**POST** `/hero_powers`  
Creates a new HeroPower association.

Request body:
```json
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
```
Example response:
```json
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
  }
}
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mikemunene16/superheroes-api.git
cd hero-power-api
```

### 2. Install Dependencies

Use `pipenv` to install the required dependencies and enter the virtual environment:

```bash
pipenv install && pipenv shell
```

### 3. Install Requirements

Make sure to install any additional requirements listed in the `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Run the migrations and seed the database:

```bash
flask db upgrade
python seed.py
```

### 5. Run the Application

Start the Flask application:

```bash
python app.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements or bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
