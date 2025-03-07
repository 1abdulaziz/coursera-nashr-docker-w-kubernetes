from flask.cli import FlaskGroup # type: ignore #ignore
from project import server, db 

cli = FlaskGroup(server)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    
if __name__ == "__main__":
    cli() 