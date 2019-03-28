import logging
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

logger = logging.getLogger(__name__)

def create_user():
    user = PasswordUser(models.User())
    user.username = 'admin'
    user.email = 'admin@example.com'
    user.password = 'admin'
    session = settings.Session()
    session.add(user)
    session.commit()
    session.close()

if __name__ == '__main__':
    try:
        create_user()
    except Exception as e:
        logger.error(e)
