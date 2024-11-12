from db import Club, Session


def add_post(ceo, club):
    with Session() as session:
        club = Club(ceo=ceo, club=club)
        session.add(club)
        session.commit()
        return True
    

def get_posts():
    with Session() as session:
        return session.query(Club).all()
    



def get_post(id):
    with Session() as session:
        return session.query(Club).where(Club.id == id).first()
    


def update_post(id, ceo, club):
    with Session() as session:
        post = session.query(Club).filter_by(id=id).first()
        post.ceo = ceo
        post.club = club
        session.commit()
        return "Інформацію про кліб успішно оновлено"
    

def del_post(id):
    with Session() as session:
      post = session.query(Club).filter_by(id=id).first
      session.delete(post)
      session.commit()
      return "Інформацію успішно видалено"