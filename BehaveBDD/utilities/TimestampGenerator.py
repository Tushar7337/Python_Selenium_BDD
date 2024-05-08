from datetime import datetime


def enter_unique_email():
    unq = datetime.now().time().strftime("%y_%m_%d_%H_%M_%S")
    return unq