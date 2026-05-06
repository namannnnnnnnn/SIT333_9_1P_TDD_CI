def submit_task(student_id, task_id, file_name):
    """
    This function checks a simple OnTrack task submission.
    It checks student ID, task ID and PDF file name.
    """

    if student_id == "":
        return "Student ID is required"

    if task_id == "":
        return "Task ID is required"

    if file_name == "":
        return "File name is required"

    if not file_name.endswith(".pdf"):
        return "Only PDF files are allowed"

    return "Wrong message"
