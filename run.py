from app import create_app

CONFIG_NAME = 'development'
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)