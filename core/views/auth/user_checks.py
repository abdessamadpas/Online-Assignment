def staff_check(user):
    return user.is_staff

def student_check(user):
    return not user.is_staff
