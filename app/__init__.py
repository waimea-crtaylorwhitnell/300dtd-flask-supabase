from flask import Flask
from flask import render_template
from supabase import create_client
from dotenv import load_dotenv
import os

# Get environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

# Home route
@app.get("/")
def home():
    response = supabase.table("things").select().execute()
    records = response.data
    
    print(response)

    return render_template("pages/home.jinja", things=records)

# Error route
@app.errorhandler(404)
def notFound(error):
    return render_template("pages/404.jinja")