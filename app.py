from ext import app
if __name__ =="__main__":
    from routes import index, regisration, login, post
    app.run(debug=True)
