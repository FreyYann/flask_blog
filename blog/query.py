
if __name__=="__main__":
    import pymysql
    pymysql.install_as_MySQLdb()
    from blog import db
    from blog import User

    db.create_all()
    user1=User(username='Corey',email='c@gmail.com',password='1234')
    db.session.add(user1)
    db.session.commit()
    print(User.query.all())
