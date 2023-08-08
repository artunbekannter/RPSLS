from application import app, db

# Ensure that the application context is set up
if __name__ == "__main__":
    with app.app_context():
        # Create the database tables, including the match_history table
        db.create_all()
