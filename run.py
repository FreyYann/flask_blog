from blog import create_app

if __name__ == '__main__':
    # app.run(debug=True)
    app=create_app()
    app.run(host="0.0.0.0", port=80,debug=True)