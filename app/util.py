from passlib.hash import bcrypt

def hashpass(password):
  """returns hashed password using bcrypt"""
  return bcrypt.hash(password)

def verifypass(password, hashed_password):
  return bcrypt.verify(password, hashed_password)