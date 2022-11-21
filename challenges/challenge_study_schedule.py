def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None

    students_online = 0

    for period in permanence_period:
        login, logout = period
        if not isinstance(login, int) or not isinstance(logout, int):
            return None
        elif login <= target_time <= logout:
            students_online += 1
    return students_online


if __name__ == "__main__":
    students_time = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    time = 5
    print(study_schedule(students_time, time))
