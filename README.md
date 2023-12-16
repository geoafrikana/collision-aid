# Collision-Aid

Collision-Aid is a web application designed to assist Canadians in easily locating collision repair centers in their area. With the prevalence of auto collisions, finding a trustworthy and affordable repair center can be challenging. This app streamlines the process by allowing users to input a Canadian postal code and search radius, returning all collision repair centers within that specified area. The results are displayed on a leaflet.js map, providing users with an interactive and visual representation of available repair centers.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone [repo_url]
   ```

2. **Create Virtual Environment:**
   ```bash
   virtualenv venv
   ```

3. **Activate Virtual Environment:**
   - CMD:
     ```bash
     venv\Scripts\activate
     ```
   - Bash:
     ```bash
     source venv/bin/activate
     ```

4. **Install Requirements:**  
   For Linux, run:
   ```bash
   pip install psycopg2-binary
   pip install -r requirements.txt
   ```
   
   For Windows, run:
   ```cmd
   pip install psycopg2==2.9.5
   pip install -r requirements.txt
   ```

5. **Setup PostgreSQL and PostGIS:**
   - Use a serverless service like neon.tech or set up locally with Docker.
   - Create a database named `collision_aid` and enable the PostGIS extension:
     ```sql
     CREATE EXTENSION postgis;
     ```

6. **Create .env File:**
   Create a `.env` file in the BASE_DIR (same folder as `manage.py`) with the following environment variables:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=collision_aid
   DB_USER=your_postgres_username
   DB_PASS=your_postgres_password
   DB_HOST=your_postgres_endpoint
   DB_PORT=5432
   STATIC_URL=static/
   ALLOWED_HOSTS=*
   ENGINE=django.contrib.gis.db.backends.postgis
   EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST=your_email_host
   EMAIL_USE_TLS=True
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_email
   EMAIL_HOST_PASSWORD=your_email_password
   ```

7. **Install GDAL:**
   - For Windows, download the appropriate wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal) and install using:
     ```bash
     pip install full_path_to_wheel_file
     ```
   - For Linux (Ubuntu), run:
     ```bash
     source gdal_install.sh
     ```

8. **Run System Check:**  
   From the BASE_DIR, run:
   ```bash
   python manage.py check
   ```

9. **Create Database Tables:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

10. **Load Dummy/Fake Data into Database:**
    ```bash
    python manage.py shell
    import os
    from django.conf import settings
    from shops.load import load_shop, load_postal_codes
    b = settings.BASE_DIR
    load_postal_codes(os.path.join(b, 'CanadianPostalCodes202208.csv'))
    load_shop(os.path.join(b, 'faker_shops_tilder.txt'))
    ```

## Usage

1. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application in your web browser at `http://localhost:8000`.

3. Enter a Canadian postal code and search radius to locate collision repair centers in the specified area.

## How Collision-Aid Works

Auto collisions are a common occurrence, and the app aims to simplify the process of finding trustworthy and affordable collision repair centers. Users can quickly locate repair centers within a specified radius, view their rates on an interactive map, and access aggregated repair rates in a table. The app also allows users to submit new collision repair centers and their rates, contributing to a comprehensive database.

## Contributing

We welcome contributions to improve Collision-Aid. If you find any issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to neon.tech for providing a generous free tier for serverless PostgreSQL services.
- The app utilizes the [Leaflet.js](https://leafletjs.com/) library for interactive maps.

Feel free to explore, use, and contribute to make Collision-Aid even better!